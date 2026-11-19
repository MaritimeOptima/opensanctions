# Upstream changes relevant to `maritime`

Baseline `b9ada8fb5` (last upstream commit in `HEAD`). Upstream is 1329 commits ahead; 309 are relevant.

## Shared code (zavod, meta, Dockerfile, contrib)

- `ceef466c5` 2026-11-18 [zavod] Stage the statement dedupe in the parquet build
- `66ecc7b0e` 2026-11-18 [zavod] Also give pack and parquet write writable tmpdir
- `df7ddbc89` 2026-11-17 [zavod] More duckdb memory management for both small and big datasets
- `1e2a8db3e` 2026-11-17 [gb_fcdo_sanctions] Map 2026 human rights and IHL regime to GB-HR (#6335)
- `67d18c382` 2026-11-17 [zavod] upgrade nomenklatura to version with statements lake perf improvements
- `8ae1dc498` 2026-11-17 [zavod] Drop \r when reading statements for temp backward compatibiliy
- `86f6490da` 2026-11-16 Bump dspy from 3.4.1 to 3.5.0 in /contrib/tune
- `3918d8706` 2026-11-16 Update litellm requirement in /contrib/tune
- `b9dfd5119` 2026-11-15 Fill modifiedAt from the latest listing date in finalize_sanction
- `acc9bcef8` 2026-11-15 Add amendments_dated to h.finalize_sanction
- `aa1f839de` 2026-11-15 Note the plan to move sanction status into finalize_sanction
- `e0c6ba67e` 2026-11-15 Keep a status the crawler set in finalize_sanction
- `db75e3df9` 2026-11-15 Add h.finalize_sanction and document sanction dates
- `7a556736d` 2026-11-15 Register the international organisations seated in EU member states
- `d0a40c72e` 2026-11-15 Register the Union's agencies, authorities and joint undertakings
- `510110811` 2026-10-17 [wd_soe] Read state links in one query and follow government bodies
- `90f45261f` 2026-10-17 [wd_soe] Add Wikidata state-owned enterprise leadership crawler
- `ef0b8d831` 2026-11-13 [us_ori_admin_actions] Add US ORI PHS Administrative Actions crawler (#5545)
- `ec24c1a0d` 2026-11-13 Document dataset deprecation and add a deprecate-dataset skill
- `c4fc8bf11` 2026-11-12 Spell out some comments further; bump default export to 7000Mi
- `c8e9c873b` 2026-11-12 Remove memory warning stuff until it's less of a mess
- `a80c95f52` 2026-11-12 Copy on consoldate instead of mutating entities during export
- `9041ab1e6` 2026-11-04 Warn when a DuckDB instance holds most of its memory limit
- `64b96987e` 2026-11-04 Drop the delta's id index before looking for deletions
- `ec7b56e98` 2026-11-04 Spill the delta hash lookup to the dataset's state directory
- `91b9c72f1` 2026-11-04 Set the store's and the delta's DuckDB memory limits separately
- `8c2d9ca3d` 2026-10-08 Serve all stores from the LakeStore and drop plyvel
- `4ee5e6907` 2026-08-24 Order statement artifacts by a full sort key for reproducible output
- `f9598b77f` 2026-08-24 Crawl into statements.raw, derive pack and parquet, never publish raw
- `883ea66e4` 2026-08-23 Generate the delta export during the traversal, on DuckDB
- `d349ed43e` 2026-08-23 Add the LakeStore: a DuckDB statement store over a manifest's artifacts
- `c318c8ba4` 2026-08-23 Preinstall the duckdb httpfs extension in the ETL image
- `3dc2968ee` 2026-08-23 Read the previous parquet in place via an archive object URI
- `619d82b54` 2026-08-23 Build a parquet statement artifact per run, replacing the timestamp index
- `dc51c3019` 2026-11-12 [ph_amlc_sanctions] Catch News notices, add TF-118/119, move data into the repo (#6260)
- `42eeb1620` 2026-11-10 When we have to pick one, pick consistently
- `d89f5c9c7` 2026-09-13 zavod: pass request headers through zyte_api.fetch_text
- `ca14032aa` 2026-11-09 [lt_fiu_freezes] Parse UNSCR 1373 list and add LT-UNSC1373 program (#6217)
- `72536ab9b` 2026-11-09 [zavod] Derive occupancy retention from declaration dates (#6169)
- `0d2f62b9b` 2026-11-07 senzing: retired Wikidata QIDs are not identities; INN country is always ru
- `5f7f894a9` 2026-11-07 [us_sec_edgar] Bump followthemoney to 4.11.3 and rigour to 2.6.2
- `244732b63` 2026-11-06 senzing: assert OpenSanctions id features only for canonical ids
- `a4ac99fe1` 2026-11-06 [zavod] Derive on load so dedupe can see all datasets
- `550b45a62` 2026-11-06 [zavod] Bump nomenklatura to 4.17.6 and followthemoney to 4.11.2
- `1236cf353` 2026-11-06 senzing: figiCode maps to OTHER_ID FIGI
- `15911bc40` 2026-11-06 Bump pyicu from 2.16.2 to 2.17 in /zavod
- `49618422a` 2026-11-06 [zavod] Move country groups for publisher blocs to zavod.constants
- `df457404e` 2026-11-06 Bump python-calamine from 0.9.0 to 0.9.1 in /zavod
- `e2bfe6817` 2026-11-05 [zavod] Replace member-state publisher.eu with a publisher.europe bloc
- `01b0076d1` 2026-11-05 revert
- `8ca162b66` 2026-11-05 revert removal
- `5cec6a1b0` 2026-11-03 senzing: REF_OPENSANCTIONS_ID for the issuer's own id; cited ids are F1E
- `4defb2ba5` 2026-11-03 senzing: compare BQ_ID exactly (EXACT_COMP)
- `584c118f6` 2026-11-03 senzing: compare OPENSANCTIONS_ID exactly (EXACT_COMP)
- `3edf8ace5` 2026-11-03 senzing: compare OFAC_ID exactly (EXACT_COMP)
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `9d527908f` 2026-11-03 [zavod] Stop deriving target.* dataset tags
- `26f6e0094` 2026-11-02 senzing exporter: FEATURES holds only Senzing features
- `39072d2e8` 2026-11-02 [zavod] Select datasets using query instead of paths for xref and dedupe"
- `53d065565` 2026-11-02 [programs] target_territories are the territories a regime concerns
- `0599b4907` 2026-11-02 Bump dspy from 3.4.0 to 3.4.1 in /contrib/tune
- `2cc266c64` 2026-10-31 senzing exporter: put a held wallet's address on its holder's record
- `7046a2ca5` 2026-10-31 senzing exporter: one crypto asset code per asset
- `d3e1eefb4` 2026-10-31 senzing exporter: make the DATA_SOURCE overrides match
- `08109187b` 2026-10-31 senzing exporter: emit wikidataId only as TRUSTED_ID WIKIDATA
- `3f4a82b39` 2026-10-30 senzing exporter: map the remaining FtM ids to crosswalk schemes; split TAX_ID_TYPE config
- `f4277b5b9` 2026-10-30 senzing exporter: canonical identifier features and types per the crosswalk
- `eb91cb2b3` 2026-10-30 Switch to pydantic_ai's LLM SDK (via Agent)
- `b2240dc0c` 2026-10-30 [zavod] Derive publisher.us_ofac for datasets published by OFAC
- `679765960` 2026-10-30 [zavod] Derive publisher.eu for member-state sanctions lists
- `9fecd9bbb` 2026-10-29 [docs] Extend merge checklist, add topics page, run crawler in review skill
- `8b52671e0` 2026-10-19 Drop data: URI src attributes from funes outlines
- `fa5737cc4` 2026-10-19 Make typographic elements transparent in funes outlines
- `41a13909b` 2026-10-19 Keep table cell markers in funes page outlines
- `207820ecd` 2026-10-19 Drop structural validation from HAR media types
- `f5017aafb` 2026-10-19 Omit absent funes page fields instead of placeholder text
- `e99bd1e4b` 2026-10-15 Reduce snapshot inspectability to rendered_html presence
- `5abcc3ed4` 2026-10-15 Trim funes comments that restate the code
- `9211706f0` 2026-10-12 Assemble funes page metadata and prompts
- `e3f2674d3` 2026-10-12 Build model-facing page outlines on lxml
- `449c0c516` 2026-10-12 Port the funes snapshot inspectability checks
- `75a1851b9` 2026-10-29 Spell out a bit what it's doing
- `c49b35393` 2026-10-28 Drop the references to the module we copied the pattern from
- `c5887a8b0` 2026-10-28 Trim the last catalogue comments that rehash the code
- `69b111b22` 2026-10-28 Drop the funes Dataset model until a read path exists
- `375d7cefe` 2026-10-28 [zavod] Simplify target tag derivation and test derived tags in exports
- `5d368501d` 2026-10-28 Trim the catalogue comments to the non-derivable facts
- `129ce6932` 2026-10-28 [zavod] Add publisher bloc tags with a placeholder eu_efta bloc
- `d38748bd1` 2026-10-28 Model the catalogue rows and due selection as classmethods
- `75064fe17` 2026-10-28 [zavod] Derive publisher.* and target.* dataset tags at metadata export
- `f8c71639d` 2026-10-28 [tune] Remove uv.lock, document dev upgrades
- `9b9a2cf35` 2026-10-27 [zavod] Expose node hashing as h.xml_node_hash
- `db1639d5c` 2026-10-27 update programs, mostly their target_territories
- `0671e61e9` 2026-10-27 [docs] Move sanctions crawler rules from the skill into zavod/docs/sanctions
- `4004e3bb6` 2026-10-27 [zavod] Add headers argument to parse_xlsx_sheet
- `7402c1471` 2026-10-26 [docs] Define the skills layout once and enforce it from CLAUDE.md
- `ad773a548` 2026-10-26 [docs] Read run artifacts from _artifacts/ and lint with lint_dataset.sh
- `78afaae10` 2026-10-26 [docs] Move PEP rules and examples out of the crawler-pep skill
- `9bc73b30e` 2026-10-26 [zavod] Add python-calamine based parse_xlsx_sheet
- `8195a39a7` 2026-10-26 [zavod] Rename parse_xlsx_sheet to parse_xlsx_sheet_openpyxl
- `396906639` 2026-10-26 Bump alembic from 1.20.0 to 1.20.1 in /zavod
- `6ebeefbc9` 2026-10-26 Bump nomenklatura from 4.17.3 to 4.17.4 in /zavod
- `0cb9e1ad5` 2026-10-23 [il_mod_terrorists, il_mod_crypto] Allow items without an Arabic variant
- `a2c4e3923` 2026-10-22 [ps_national_terrorism_list] Simplify crawler and tidy metadata
- `61d704869` 2026-10-22 Bump certifi from 2026.7.22 to 2026.10.19 in /contrib/tune
- `7999bfbf0` 2026-10-21 Bump pillow from 12.3.0 to 13.0.0 in /contrib/tune
- `40b66b220` 2026-10-21 Fix typos in READMEs
- `c118e0550` 2026-10-21 Pin nomenklatura 4.17.3
- `d44299cd3` 2026-10-21 Pin rigour 2.6.1
- `0053e2f71` 2026-10-21 Import MULTI_LANG from rigour and pin rigour 2.6.0 / FtM 4.11.1
- `632e3b39c` 2026-10-21 ps terrorism crawler
- `68c4d76d1` 2026-10-21 [meta] Map OFAC PAIPA designations to US-CYB
- `a833ce3bf` 2026-10-21 [th_house_representatives] Strip titles attached to names in unspaced scripts
- `2c1d434af` 2026-10-21 Use gpt-6.1-sol for position name translations
- `36b8c7d4e` 2026-10-21 Use gpt-6-luna for Chinese and gpt-6.1-sol for other name transliterations
- `8413f7b84` 2026-10-20 Bump aiohttp from 3.14.3 to 3.14.4 in /contrib/tune
- `50998f130` 2026-10-19 [bs_tokyo_mou_psc] Sleep between retries
- `2b21ada63` 2026-10-19 add sanctions program ID
- `5e514c096` 2026-10-17 [wd_peps] Shorten docstrings and comments
- `9314d7d20` 2026-10-17 [wd_peps] Skip historical predecessor states among territory QIDs
- `f09564b7b` 2026-10-14 [contrib/load-tables] check if gcloud auth login is needed before cryptic error
- `ed078d4d0` 2026-10-14 Rebase the pravda snapshot migration onto position.last_seen
- `e7e2f88a5` 2026-10-12 Bump orjson from 3.12.0 to 3.13.0 in /zavod
- `e1fcf1799` 2026-10-12 Make the revisit interval a const in attempts, not a brief field
- `09e357521` 2026-10-12 [wd_peps] no need to drop holders now wikidata client will retry
- `f4a5ec89a` 2026-10-09 Select due funes candidates from the attempt history
- `e60a0b7b2` 2026-10-09 Trim the funes package docstring to the non-derivable fact
- `31a1d858c` 2026-10-08 [meta] Delete the retired US-DDTC-SD and US-DDTC-AD program files
- `010b5ceec` 2026-10-07 [openfigi] bump nomenklatura to skip external-only securities
- `71fbb64a0` 2026-10-06 Validate funes brief labels as plain strings
- `0c715d6ff` 2026-10-06 Sync the funes catalogue through the context's database session
- `e16f59a77` 2026-10-06 Read funes dataset briefs from metadata into the catalogue
- `5577308a4` 2026-10-06 Handle more placeholders
- `cdad7fec4` 2026-10-06 Clarify some stuff
- `a6a8a9b75` 2026-10-06 [il_mod_crypto] initial rewrite for new site
- `d48e41077` 2026-10-06 Drop nullword placeholder values in several crawlers
- `88e702d8e` 2026-10-05 [zavod] Track last_seen on positions in categorise
- `e40dbb710` 2026-10-02 Add mac docs
- `945878470` 2026-10-01 Serialise concurrent migration runs with an advisory lock
- `bae2352b9` 2026-10-02 Use nk's db engine with zavod's db url setting
- `8ec842b08` 2026-10-02 Bump duckdb from 1.5.5 to 1.5.6 in /zavod
- `48f4b70e9` 2026-10-01 Remove the zavod.db engine wrapper
- `2c30fe46b` 2026-10-01 Format the funes catalogue migration
- `b207e2e56` 2026-10-01 Name the funes attempt check constraints
- `f8252eed6` 2026-10-01 Give funes its own metadata in the Alembic target
- `887342ed9` 2026-10-01 Collapse funes verdict tables into the attempt row
- `8fbfcd98f` 2026-10-01 Add funes pipeline catalogue tables referencing pravda snapshots
- `801f081e7` 2026-10-01 Own pravda's snapshot table through the Alembic chain
- `5836c83f5` 2026-10-01 Drop manual index creation for the statement table
- `ffa32e842` 2026-10-01 Simplify tuning artifact note in contrib/tune README
- `381d5e700` 2026-10-01 Move DSPy tuning tooling out of zavod into contrib/tune
- `957af0dc8` 2026-09-30 Leave the statement table to nomenklatura; create it in load_db
- `a3217b7e1` 2026-09-30 Add database documentation covering the Alembic workflow
- `a490ad592` 2026-09-30 Move migrations to the default alembic/ layout
- `b8f6c376f` 2026-09-30 Drop create_db(); schema bootstrap is Alembic's job
- `edfc4c3f2` 2026-09-30 Add statement table migration; zavod owns its MetaData
- `fe193c254` 2026-09-30 Format migration revisions with ruff
- `0ed4de3c5` 2026-09-29 Drop the ix_position_created_at index from the model
- `f52851b24` 2026-09-28 Remove hand-applied SQL migrations, superseded by the alembic baseline
- `2747f546b` 2026-09-28 Add autogenerated baseline for the four stateful tables
- `4bd5dc06a` 2026-09-28 Take the migration URL from the alembic config first; named zavod env
- `80175262c` 2026-09-28 Add packaged Alembic migration environment to zavod
- `8ba69ed2e` 2026-09-28 Track SQL files in git; ignore zavod local venv
- `1cf152f66` 2026-10-01 Update litellm requirement in /zavod
- `1d3c33471` 2026-09-30 Configure logging in contrib scripts that use the zavod logger
- `0ad0885fc` 2026-09-30 Send ci_datasets.py logs to stderr
- `8e1846b65` 2026-09-28 Switch black_sea_mou_psc CAPTCHA solving to gpt-6-sol
- `4dd2a8ec9` 2026-09-21 style(zavod): ruff format senzing exporter and its test
- `16fcb4b3e` 2026-09-20 senzing exporter: assert the OpenSanctions id as an A1ES feature
- `3f1e2d099` 2026-08-28 senzing exporter: canonicalize Identification adjacency id TYPE
- `da0a2ce14` 2026-08-19 senzing exporter: single FEATURES list, canonical id TYPE/SUBTYPE, DISSOLUTION_DATE
- `18b0a6eb0` 2026-08-17 senzing exporter: document TAX_ID_TYPE sz_configtool config update
- `19edf6a78` 2026-08-13 senzing exporter: carry Identification document type into NATIONAL_ID_TYPE
- `a9d3f96aa` 2026-08-13 senzing exporter: qualify exclusive ids by country (NATIONAL_ID/TAX_ID/PASSPORT)
- `0499ff02a` 2026-08-13 senzing exporter: preserve identifier type for NATIONAL_ID and TAX_ID

## fr_tresor_gels_avoir (45)

- `eae7338f4` 2026-11-19 [fr_tresor_gels_avoir] Map KPP identification of JSCB Agropromcredit
- `6b7dfb2c2` 2026-11-19 [fr_tresor_gels_avoir] Map new identification fields and registration places
- `b73fd905c` 2026-11-18 [fr_tresor_gels_avoir] Map generic identification labels and remaining fields
- `ef327b868` 2026-11-17 [fr_tresor_gels_avoir] Map unparsed identification fields
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `679765960` 2026-10-30 [zavod] Derive publisher.eu for member-state sanctions lists
- `836c18555` 2026-10-28 [fr_tresor_gels_avoir] Link OMM-operated vessels from the identification field
- `1bbcd6f82` 2026-10-27 [fr_tresor_gels_avoir] Emit IdRegistre as authorityId, drop the EU reference
- `6668cd733` 2026-10-27 [fr_tresor_gels_avoir] assertion change post-dedupe
- `02ae351f2` 2026-10-27 tighten max assertion
- `40d37113d` 2026-10-27 [fr_tresor_gels_avoir] Map unparsed identification fields, raise Organization max
- `b9fe206e7` 2026-10-23 [fr_tresor_gels_avoir] Override Vessel schema for 11705, map undelimited identification fields
- `9de3ecc5d` 2026-10-22 [fr_tresor_gels_avoir] Map two malformed identification fields
- `d03dd0890` 2026-10-21 [fr_tresor_gels_avoir] Parse labelled identification fields
- `2dd6824f0` 2026-10-20 [fr_tresor_gels_avoir] Add lookups for unparsed identification and address fields
- `9cf9d2b1a` 2026-10-19 [fr_tresor_gels_avoir] Map RPDC place of activity to country
- `cbd583f09` 2026-10-19 [fr_tresor_gels_avoir] Map KEPCO and AOGC to abbreviation
- `441460cc4` 2026-10-19 [fr_tresor_gels_avoir] Drop dead code, unread aliases keys and stale comments
- `e42262594` 2026-10-19 [fr_tresor_gels_avoir] Remove identification segment splitter, map every field via identification_full
- `2e69bb8fa` 2026-10-19 [fr_tresor_gels_avoir] Move last identification segment to identification_full
- `3348a48b0` 2026-10-19 [fr_tresor_gels_avoir] Move 21 identification segments to identification_full
- `b0e258ebc` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `75a77bda2` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `8495ebee4` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `3da97ddf8` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `321c72be4` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `5531e7679` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `8c7ed519d` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `046088b54` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `2e7025d9b` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `50593661e` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `fd979fe00` 2026-10-19 [fr_tresor_gels_avoir] Move 20 identification segments to identification_full
- `915758ab7` 2026-10-19 [fr_tresor_gels_avoir] Move 10 identification segments to identification_full
- `7051f1eb4` 2026-10-19 [fr_tresor_gels_avoir] Move 10 identification segments to identification_full
- `f327c0971` 2026-10-19 [fr_tresor_gels_avoir] Move 10 identification segments to identification_full
- `e6f2d8682` 2026-10-19 [fr_tresor_gels_avoir] Move 10 identification segments to identification_full
- `9db53ae76` 2026-10-19 [fr_tresor_gels_avoir] Move 10 identification segments to identification_full
- `1fecb7580` 2026-10-19 [fr_tresor_gels_avoir] Map unparsed identification fields via identification_full
- `e1b9b86c1` 2026-10-19 [fr_tresor_gels_avoir] Warn once per identification field, fix via identification_full
- `cff07591c` 2026-10-15 [fr_tresor_gels_avoir] datapatches to unpack new entries
- `1bd02562e` 2026-10-15 [fr_tresor_gels_avoir] Remove unused lookups
- `1d3a0e69e` 2026-10-15 [fr_tresor_gels_avoir] handle some ogrn splits
- `df9397a7a` 2026-10-14 [fr_tresor_gels_avoid] datapatch
- `c55a965f7` 2026-10-13 [fr_tresor_gels_avoir] datapatches, add vessel support
- `ee7a0a3ba` 2026-09-30 [fr_tresor_gels_avoir] Map BIN/OGRN, INN, legal-form and split-address identification values

## eu_journal_sanctions (43)

- `333a42711` 2026-11-19 [eu_journal_sanctions] Pin 2010/573/CFSP consolidation 02010D0573-20261028
- `58ea1dd31` 2026-11-16 [eu_journal_sanctions] Transcribe Implementing Regulation (EU) 2026/2574
- `d190aaa98` 2026-11-16 [eu_journal_sanctions] Drop bare VKontakte usernames from website
- `c701e4806` 2026-11-16 [eu_journal_sanctions] Transcribe amending acts 32026R2558 and 32026R2569
- `7c78b0494` 2026-11-16 [eu_journal_sanctions] Transcribe amending acts 2026/2550 and 2026/2568 (#6307)
- `56da37ddb` 2026-11-13 [eu_journal_sanctions] Re-point earlier 881/2002 amendments to the new pin
- `ff3af2588` 2026-11-12 [eu_journal_sanctions] Update 881/2002 consolidation to 02002R0881-20261105
- `5f7aa5364` 2026-11-11 [eu_journal_sanctions] Update Iraq and Sudan consolidation pins (#6240)
- `670bbf079` 2026-11-06 [eu_journal_sanctions] Update Guinea 1284/2009 snapshot to 02009R1284-20261015 (#6178)
- `6e2d0fc05` 2026-11-05 [eu_journal_sanctions] Update 2017/1509 (DPRK) consolidation pin to 02017R1509-20261012 (#6161)
- `78338217f` 2026-11-04 [eu_journal_sanctions] Clean Konig identifiers from amendment 32026R2490 (#6153)
- `e39cf54f8` 2026-11-04 [eu_journal_sanctions] Transcribe ISIL/Al-Qaida amendment 2026/2490 (#6151)
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `25c95d81a` 2026-10-28 [eu_journal_sanctions] Bump 2016/44 consolidation to 20261013, parse Annex V
- `2f8fdf312` 2026-10-28 [eu_journal_sanctions] Keep the Libya pin; make the empty-annex guard see Annex V
- `6416bb5e2` 2026-10-28 [eu_journal_sanctions] Bump four consolidation pins
- `c6a45b78d` 2026-10-27 [eu_journal_sanctions] Close two amending acts with no designations (#6061)
- `3f02c50e8` 2026-10-23 [eu_journal_sanctions] Close 32026R2388 as a delisting-only act
- `9fa3b5db4` 2026-10-23 [eu_journal_sanctions] Bump 765/2006 and 2642/2024 consolidation pins
- `b2b9709e8` 2026-10-22 [eu_journal_sanctions] Transcribe Regulation (EU) 2026/2384
- `e24a3dab3` 2026-10-18 [eu_journal_sanctions] Keep entry 1207's address whole across the handoff
- `5a02b8c61` 2026-10-17 [eu_journal_sanctions] Bump 32014R0269 to consolidation 02014R0269-20261012
- `bf490fc49` 2026-10-15 [eu_journal_sanctions] Transcribe Implementing Regulation (EU) 2026/2333
- `df0dc4f3e` 2026-10-14 [eu_journal_sanctions] Close two delisting-only acts as reviewed
- `ad915680b` 2026-10-13 [eu_journal_sanctions] Bump 881/2002 consolidation pin to 02002R0881-20260922
- `36ae0f9c9` 2026-10-12 Fix address with ; in original
- `b038750ad` 2026-10-12 Classify country-only business places in EU sanctions
- `89ec0fec1` 2026-10-12 Classify EU registration places and map INN label
- `d50b01569` 2026-10-12 [eu_journal_sanctions] Fix 2026/2281 wording against the published act
- `f1e651058` 2026-10-12 [eu_journal_sanctions] Transcribe Implementing Regulation (EU) 2026/2281
- `7efc35ade` 2026-10-12 [eu_journal_sanctions] Transcribe amending acts 2026/2278 and 2026/2292
- `e38b69e31` 2026-10-12 [eu_journal_sanctions] Transcribe 32026R2271, close 32026R2259
- `9ede29dcf` 2026-10-09 [eu_journal_sanctions] transcribe Sudan amendment 32026R2262 (#5887)
- `c393ef6d5` 2026-10-09 [eu_journal_sanctions] Strip nested BIN/OGRN label from 269/2014 registration numbers
- `db7780220` 2026-10-09 [eu_journal_sanctions] Transcribe 2026/2287, bump 269/2014 to 02014R0269-20260928 (#5879)
- `c606580ec` 2026-10-08 [eu_journal_sanctions] Transcribe Council Implementing Regulation (EU) 2026/2257
- `3eb210c36` 2026-10-08 [eu_journal_sanctions] Transcribe Council Implementing Regulation (EU) 2026/2263
- `a7c2326da` 2026-10-06 Tag cleanup: merge medical tags into sector.health, drop list.sanction.eu (#5823)
- `567e9c03f` 2026-10-06 [eu_journal_sanctions] Bump 2024/1485 and 2024/2642 consolidation pins
- `e693e0c8a` 2026-09-30 [eu_journal_sanctions] Type-check parser scripts with mypy-datasets
- `0cfb526fb` 2026-09-29 [eu_journal_sanctions] Normalise two DRC passport numbers via type.identifier (#5763)
- `c5ef1f645` 2026-09-29 [eu_journal_sanctions] Transcribe Implementing Regulation (EU) 2026/2191 (#5759)
- `54fc3eae5` 2026-09-28 [eu_journal_sanctions] Transcribe amending acts 2026/2184 and 2026/2193 (#5752)

## gb_fcdo_sanctions (12)

- `1e2a8db3e` 2026-11-17 [gb_fcdo_sanctions] Map 2026 human rights and IHL regime to GB-HR (#6335)
- `cb508c331` 2026-11-13 [gb_fcdo_sanctions] Add lookups for new company names and registration numbers (#6268)
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `67d25de12` 2026-10-27 [gb_fcdo_sanctions] Copy the designation date to listingDate
- `309b92f93` 2026-10-27 [gb_fcdo_sanctions] Take person positions from the CSV only
- `da118b0b1` 2026-10-27 [gb_fcdo_sanctions] Emit the CSV birthplace as "Town, Country" too
- `302996b19` 2026-10-27 [gb_fcdo_sanctions] Parse XML person details, skip empty passports, use rigour for languages
- `d29b2ebe6` 2026-10-09 [gb_fcdo_sanctions] also extract crypto wallets from the CSV
- `d20425286` 2026-10-09 [gb_fcdo_sanctions] emit CryptoWallet entities from Other Information
- `57b9aad96` 2026-10-08 [gb_fcdo_sanctions] datapatches
- `7860233fa` 2026-10-08 Split multi-value fields in gb_fcdo_sanctions
- `f92acec2a` 2026-10-02 [gb_fcdo_sanctions] Add companies lookups for new vessel owner/operators

## us_ofac_cons (12)

- `378ecd2a4` 2026-11-13 [tags] Apply risk.misconduct to debarment and enforcement lists
- `ab73af892` 2026-11-06 Inline single-use XPath selectors and Zyte actions
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `eb91cb2b3` 2026-10-30 Switch to pydantic_ai's LLM SDK (via Agent)
- `b2240dc0c` 2026-10-30 [zavod] Derive publisher.us_ofac for datasets published by OFAC
- `6a07e4c42` 2026-10-30 Remove hand-set juris.us dataset tags
- `127c1ada5` 2026-10-22 Extract with gpt-6.1-sol instead of gpt-4o in five crawlers
- `68c4d76d1` 2026-10-21 [meta] Map OFAC PAIPA designations to US-CYB
- `27f6c3990` 2026-10-14 [us_ofac_sdn] Datapatch identifier type
- `f7f8df106` 2026-10-08 Tag cleanup: bring sector.crypto, academic, defense and energy to 5+ datasets (#5839)
- `f5d7147cb` 2026-10-08 Apply sector.securities to datasets that contain securities (#5838)
- `40a4c8b1d` 2026-09-30 [us] Fix mypy --strict type errors

## us_ofac_sdn (12)

- `378ecd2a4` 2026-11-13 [tags] Apply risk.misconduct to debarment and enforcement lists
- `ab73af892` 2026-11-06 Inline single-use XPath selectors and Zyte actions
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `eb91cb2b3` 2026-10-30 Switch to pydantic_ai's LLM SDK (via Agent)
- `b2240dc0c` 2026-10-30 [zavod] Derive publisher.us_ofac for datasets published by OFAC
- `6a07e4c42` 2026-10-30 Remove hand-set juris.us dataset tags
- `127c1ada5` 2026-10-22 Extract with gpt-6.1-sol instead of gpt-4o in five crawlers
- `68c4d76d1` 2026-10-21 [meta] Map OFAC PAIPA designations to US-CYB
- `27f6c3990` 2026-10-14 [us_ofac_sdn] Datapatch identifier type
- `f7f8df106` 2026-10-08 Tag cleanup: bring sector.crypto, academic, defense and energy to 5+ datasets (#5839)
- `f5d7147cb` 2026-10-08 Apply sector.securities to datasets that contain securities (#5838)
- `40a4c8b1d` 2026-09-30 [us] Fix mypy --strict type errors

## ch_seco_sanctions (9)

- `c247112cb` 2026-11-17 [ch_seco_sanctions] Match renamed DRC sanctions program
- `40f9ee316` 2026-11-16 [ch_seco_sanctions] Fill missing modifiedAt via h.finalize_sanction
- `3f6fbee09` 2026-10-27 [ch_seco_sanctions] Keep assert_all_accepted disabled as on main
- `9fc10536a` 2026-10-27 [ch_seco_sanctions] Move listing dates and reasons to the Sanction
- `8b3127852` 2026-11-04 Daily issues 2026 11 04 (#6155)
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `eb91cb2b3` 2026-10-30 Switch to pydantic_ai's LLM SDK (via Agent)
- `272928f35` 2026-10-27 [ch_seco_sanctions] Set modifiedAt on the Sanction
- `5cb6d8aea` 2026-10-27 [ch_seco_sanctions] Take listing and start dates from the "listed" modification only

## ua_war_sanctions (6)

- `fd65284ad` 2026-11-16 [ua_war_sanctions] Skip new Weapons row on company pages
- `9d7a8f21f` 2026-11-11 Daily issues 2026-11-11 (#6241)
- `9f099b935` 2026-10-14 [ua_war_sanctions] datapatch
- `f7f8df106` 2026-10-08 Tag cleanup: bring sector.crypto, academic, defense and energy to 5+ datasets (#5839)
- `8d610a87f` 2026-10-08 [ua_war_sanctions] datapatch
- `2aef1860d` 2026-09-28 ua_war_sanctions: match comma-separated Sberbank SWIFT codes

## ca_dfatd_sema_sanctions (6)

- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `39856e43d` 2026-10-27 [ca_dfatd_sema_sanctions] Copy the listing date to startDate
- `8879a9021` 2026-10-08 Split ca_dfatd_sema title and vessel type into English and French
- `a04c1795b` 2026-10-06 [ca_dfatd_sema] Stop warning about unaccepted reviews
- `8d99afbd6` 2026-10-02 [ca_dfatd_sema_sanctions] Suggest weakAlias and abbreviation for single-token names
- `b78cadaed` 2026-09-28 [ca_dfatd_sema_sanctions] Fix closing parentheses and post names for review (#5751)

## eu_sanctions_map (5)

- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `c382b788f` 2026-10-26 [eu_sanctions_map] Read XLSX with python-calamine
- `8195a39a7` 2026-10-26 [zavod] Rename parse_xlsx_sheet to parse_xlsx_sheet_openpyxl
- `a7c2326da` 2026-10-06 Tag cleanup: merge medical tags into sector.health, drop list.sanction.eu (#5823)
- `bc60fb4c6` 2026-10-02 chore: update last_checked dates in the metadata files (#5800)

## us_trade_csl (5)

- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `6a07e4c42` 2026-10-30 Remove hand-set juris.us dataset tags
- `85323b8dc` 2026-10-09 [us_trade_csl] Fix related-entity names, programId and link IDs
- `e62586ce5` 2026-10-07 [us_trade_csl] Replace ISN program label with renamed ACN label
- `6af24a1f5` 2026-10-07 [us_trade_csl] Map renamed ACN nonproliferation program label

## eu_fsf (4)

- `df7ddbc89` 2026-11-17 [zavod] More duckdb memory management for both small and big datasets
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `679765960` 2026-10-30 [zavod] Derive publisher.eu for member-state sanctions lists
- `5dd21653b` 2026-10-26 [eu_fsf] Split VK's crammed website value into vk.com and vk.company

## us_cbp_forced_labor (3)

- `09ef31a9f` 2026-11-16 [us_cbp_forced_labor] Add name lookup for Mitra Aneka Rezeki with location
- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `71ee91a4f` 2026-09-30 [us_cbp_forced_labor] Add name lookups for two new Indonesian palm oil WROs

## ae_local_terrorists (3)

- `73f5835d4` 2026-11-10 Fix lint in touched dataset YAMLs
- `d0c4c8bd8` 2026-11-10 Tag terror lists with risk.terror, retire list.terror
- `d5e339ff4` 2026-10-27 [ae_local_terrorists] Read XLS with python-calamine

## mc_fund_freezes (3)

- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `3f00d4df5` 2026-11-02 [mc_fund_freezes] Add alias lookup for reworded Khairkhwa birth note (#6128)
- `df1ad4b17` 2026-10-28 [mc_fund_freezes] Add date lookup for 'Environ 1971'

## be_fod_sanctions (2)

- `3089a62d1` 2026-11-03 Rename issuer.west to publisher.west and drop the eu_efta placeholder bloc
- `679765960` 2026-10-30 [zavod] Derive publisher.eu for member-state sanctions lists

## tokyo_mou_detention (1)

- `60deb32c7` 2026-11-02 Daily issues 2026 11 02 (#6131)

## No upstream changes

`abuja_mou_detention`, `black_sea_mou_detention`, `ext_abuja_mou_psc`, `ext_tokyo_mou_psc`, `kp_rusi_reports`, `paris_mou_banned`, `un_1718_vessels`
