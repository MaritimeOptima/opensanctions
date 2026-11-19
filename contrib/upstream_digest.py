"""Digest of upstream (opensanctions/opensanctions) changes relevant to this fork.

Relevant means: commits touching a dataset in a tracked collection (children plus
transitive `inputs`), the collection file itself, or shared framework code.

The baseline is the last upstream commit already contained in the tracked ref
(`git merge-base <ref> upstream/main`), so the digest shrinks once you merge upstream.
Standard library only; the YAML fields we need are simple lists, parsed by hand.

Usage:
    python contrib/upstream_digest.py [--ref main] [--collection maritime]
        [--upstream upstream/main] [--shared zavod meta Dockerfile]
"""

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_SHARED = ["zavod", "meta", "Dockerfile", "contrib"]
# Shared-code paths that never affect crawl output.
SHARED_EXCLUDES = ["zavod/docs", "zavod/zavod/tests", "contrib/upstream_digest.py"]
SEP = "\x00"  # emitted by git via %x00 in --format


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True)


def yaml_list(path: Path, key: str) -> list[str]:
    """Read a top-level `key:` list of plain scalars from a dataset yml."""
    items: list[str] = []
    in_list = False
    for line in path.read_text().splitlines():
        if re.match(rf"^{key}:\s*$", line):
            in_list = True
            continue
        if not in_list:
            continue
        item = re.match(r"^\s+-\s+([\w\-]+)\s*(#.*)?$", line)
        if item is not None:
            items.append(item.group(1))
        elif line.strip() == "" or line.strip().startswith("#"):
            continue
        else:
            in_list = False
    return items


def resolve_scope(collection: str) -> dict[str, str]:
    """Map each tracked dataset name to the path prefix that holds its code.

    Datasets living in the shared `_collections`/`_externals` folders own just their yml.
    """
    ymls = {p.stem: p for p in Path("datasets").glob("**/*.yml")}
    scope: dict[str, str] = {}

    def visit(name: str) -> None:
        if name in scope:
            return
        path = ymls.get(name)
        if path is None:
            print(f"warning: no yml found for {name!r}", file=sys.stderr)
            return
        if path.parent.name in ("_collections", "_externals"):
            if path.parent.name == "_externals":
                scope[name] = str(path)
            return  # collections are expanded via their children, not tracked themselves
        scope[name] = str(path.parent) + "/"
        for dep in yaml_list(path, "inputs"):
            visit(dep)

    root = ymls[collection]
    scope[collection] = str(root)
    for child in yaml_list(root, "children"):
        visit(child)
    return scope


def owners(path: str, scope: dict[str, str]) -> list[str]:
    """All tracked datasets a file belongs to (datasets may share a folder)."""
    return [
        name
        for name, prefix in scope.items()
        if path == prefix or (prefix.endswith("/") and path.startswith(prefix))
    ]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="main", help="branch that tracks upstream merges")
    ap.add_argument("--collection", default="maritime")
    ap.add_argument("--upstream", default="upstream/main")
    ap.add_argument("--shared", nargs="*", default=DEFAULT_SHARED)
    args = ap.parse_args()

    base = git("merge-base", args.ref, args.upstream).strip()
    total = int(git("rev-list", "--count", f"{base}..{args.upstream}"))
    scope = resolve_scope(args.collection)

    pathspecs = list(scope.values())
    pathspecs += args.shared
    pathspecs += [f":(exclude){e}" for e in SHARED_EXCLUDES]
    out = git(
        "log", "--no-merges", "--name-only", "--date=short",
        "--format=%x00%h%x09%ad%x09%s", f"{base}..{args.upstream}", "--", *pathspecs,
    )

    by_dataset: dict[str, list[str]] = defaultdict(list)
    shared: list[str] = []
    for block in out.split(SEP):
        if not block.strip():
            continue
        header, *files = block.strip().split("\n")
        sha, date, subject = header.split("\t", 2)
        line = f"- `{sha}` {date} {subject}"
        names: set[str] = set()
        is_shared = False
        for f in filter(None, files):
            found = owners(f, scope)
            names.update(found)
            is_shared = is_shared or not found
        for name in sorted(names):
            by_dataset[name].append(line)
        if is_shared:
            shared.append(line)

    print(f"# Upstream changes relevant to `{args.collection}`\n")
    print(
        f"Baseline `{base[:9]}` (last upstream commit in `{args.ref}`). "
        f"Upstream is {total} commits ahead; "
        f"{len(set(shared) | {l for v in by_dataset.values() for l in v})} are relevant.\n"
    )
    if shared:
        print(f"## Shared code ({', '.join(args.shared)})\n")
        print("\n".join(shared) + "\n")
    for name in sorted(by_dataset, key=lambda n: -len(by_dataset[n])):
        print(f"## {name} ({len(by_dataset[name])})\n")
        print("\n".join(by_dataset[name]) + "\n")
    untouched = sorted(set(scope) - set(by_dataset) - {args.collection})
    if untouched:
        print("## No upstream changes\n")
        print(", ".join(f"`{n}`" for n in untouched))


if __name__ == "__main__":
    main()
