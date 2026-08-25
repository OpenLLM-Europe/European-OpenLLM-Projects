# European Open Source LLM Projects :eu:

We're **OpenLLM Europe** :eu:, an Open Source community committed to empowering LLM projects in all European languages, with a specific focus on medium and low-resource languages. Our working language is English.

- Discord: <https://discord.gg/8cHZ6NVwxd>, shared with OpenLLM France, see the note below
- GitHub: <https://github.com/OpenLLM-Europe>
- Contact: <contact@openllm-europe.org>
- OpenLLM France, the community we grew out of: <https://openllm-france.fr/>

> **About that Discord invite.** OpenLLM Europe started inside OpenLLM France and still shares its Discord server, so the invite opens a server named *OpenLLM France* and many of its channels are in French. That is lineage, not policy. European discussions and this catalogue run in English, so open your thread in English wherever you land, and say so if a French-only conversation is in your way.

This repository maintains a **curated, living catalogue** of European open-source LLM projects, models, datasets, and initiatives. It is intentionally opinionated: projects are grouped by role in the ecosystem rather than by nationality alone, and inactive artefacts are archived rather than deleted, so the map stays honest.

> **Your project is missing?** Adding it takes two minutes and no git: open the [Add a project form](https://github.com/OpenLLM-Europe/European-OpenLLM-Projects/issues/new?template=add-project.yml) and we turn it into a catalogue row. Prefer a pull request? Copy the [row template](#row-templates) for the right section. Spotted a stale date or a dead link? [Tell us](https://github.com/OpenLLM-Europe/European-OpenLLM-Projects/issues/new?template=update-entry.yml).

---

## How to read this catalogue

The catalogue is organised in **four sections**, from the most strategic to the most historical:

1. **Foundation models, European frontier**: currently active, openly licensed foundation LLMs trained at scale in Europe.
2. **National and community LLMs (active)**: living projects with real 2025-2026 releases, typically focused on one or a few languages.
3. **Archives and historical models**: first-generation BERTs and early LLMs that appear less or no longer actively developed based on public evidence.
4. **Reoriented or acquired projects**: European labs and models that have changed hands or pivoted, kept here for lineage.

A **Latest release** column is included wherever public evidence exists. **Contributions welcome**, see [How to contribute](#how-to-contribute).

---

## 1. Foundation models, European frontier

Openly licensed foundation LLMs trained from scratch in Europe (or by European teams with a European mandate), currently active.

| Model / family | Sizes | Languages | License | Latest release | Origin | Links |
| --- | --- | --- | --- | --- | --- | --- |
| **Apertus / Swiss AI Initiative** (EPFL + ETH Zürich) | flagship LLM (trained on Alps supercomputer) | multilingual | open | 2025 | Switzerland | [Swiss AI Initiative](https://swiss-ai.org/) |
| **BgGPT 3.0** (INSAIT, Sofia) | 4B, 12B, 27B (vision + 131k ctx, based on Gemma 3) | bg, en | Gemma Terms of Use | 03/2026 | Bulgaria | [models.bggpt.ai](https://models.bggpt.ai/blog/), [HF](https://huggingface.co/INSAIT-Institute) |
| **Bielik v3** (SpeakLeash + ACK Cyfronet AGH) | 1.5B, 4.5B, 11B | pl + 20 EU languages (v3.0 11B) | Apache 2.0 | v3.0 11B: 12/2025, Minitron 7B v3: 04/2026 | Poland | [HF collection](https://huggingface.co/collections/speakleash/bielik-v3-family), [SpeakLeash](https://speakleash.org/) |
| **Devstral 2 / Magistral / Ministral** (Mistral AI) | 3B to 123B | multilingual + code | Apache 2.0 (Devstral 2: modified MIT) | 12/2025 | France | [Devstral](https://mistral.ai/news/devstral-2507/), [Magistral](https://mistral.ai/news/magistral/) |
| **Dragon LLM** (Lingua Custodia) | 3.8B demonstrator, 7B and 70B planned | fr, en + EU | open source (mixed with proprietary) | Demonstrator 2025 | France | [Company brief](https://emag.directindustry.com/2025/11/06/dragon-llm-ceo-olivier-debeugny-europe-frugal-ai-architecture-genai-airbus/) |
| **EuroLLM** (Unbabel + Instituto Superior Técnico + INESC-ID) | 1.7B, 9B, 22B | all 24 EU languages | Apache 2.0 | 22B: 12/2025 | Portugal / EU | [eurollm.io](https://eurollm.io/), [EuroLLM-22B blog](https://huggingface.co/blog/eurollm-team/eurollm-22b) |
| **HPLT models** (High Performance Language Technologies) | monolingual reference models, 2.15B x 38 languages | 38 EU + neighbouring languages | open | 2026 (co-release with OpenEuroLLM) | EU (Horizon Europe) | [hplt-project.org](https://hplt-project.org/) |
| **Luciole** (OpenLLM France / LINAGORA) | 1B, 8B (Mamba-Transformer hybrid), 23B | fr, en, de, es, it, pt, nl, ar | Apache 2.0 | Base 06/2026, Instruct 1.1 07/2026 | France | [HF collection](https://huggingface.co/collections/OpenLLM-France/luciole-llm), [Training dataset](https://huggingface.co/datasets/OpenLLM-France/Luciole-Training-Dataset), [Training code](https://github.com/OpenLLM-France/Luciole-Training) |
| **Mistral 3** (Mistral AI) | 3B, 8B, 14B, Large 3 (675B / 41B active) | multilingual | Apache 2.0 | 12/2025 | France | [mistral.ai](https://mistral.ai/news/mistral-3/), [HF](https://huggingface.co/mistralai) |
| **Occiglot** (DFKI, hessian.AI, TU Darmstadt) | 7B (EU5), incl. instruct variants | en, de, fr, es, it | Apache 2.0 | 2024 (community, slower cadence in 2025) | Germany / EU | [occiglot.eu](https://occiglot.eu/) |
| **OpenEuroLLM** (consortium, Charles University, ETH, Barcelona SC, etc.) | foundation models under construction | 24 EU languages | open | Consortium launched 02/2025, first co-releases 2026 | EU | [openeurollm.eu](https://openeurollm.eu/), [GitHub org](https://github.com/OpenEuroLLM) |
| **Pleias 1.0** (Pleias) | 350M, 1.2B, 3B | multilingual, trained on Common Corpus only | Apache 2.0 | 12/2024 | France | [pleias.ai](https://pleias.ai/research), [HF](https://huggingface.co/PleIAs), [Overview](https://simonwillison.net/2024/Dec/5/pleias-llms/) |
| **Salamandra / ALIA** (BSC, Projecte Aina) | 2B, 7B, 40B | ca, es, gl, eu + EU | Apache 2.0 | 2024-2025 | Spain | [Salamandra family](https://projecteaina.cat/tech/en/introducing-the-salamandra-family-of-models/), [HF](https://huggingface.co/projecte-aina) |
| **Soofi S** (Soofi Consortium, coordinated by KI Bundesverband) | 31.6B total, 3.2B active per token (hybrid Mamba-2 + MoE + attention) | de, en | permissive open release announced, not yet finalised | Pretraining report 07/2026, weights in beta preview | Germany | [soofi.info](https://www.soofi.info/soofi-s/), [HF](https://huggingface.co/Soofi-Project), [Pretraining report](https://arxiv.org/abs/2607.09424), [Training code](https://github.com/soofi-project/Soofi-Pretraining) |
| **Teuken-7B** (OpenGPT-X / Fraunhofer IAIS / Jülich) | 7B | 24 EU official languages | Apache 2.0 | v0.6, late 2025 | Germany / EU | [Press release](https://www.iais.fraunhofer.de/en/press-events/press-releases/press-release-241126.html), [HF](https://huggingface.co/openGPT-X) |
| **TildeOpen LLM** (Tilde) | 30B, plus a 64k-context variant | 34 European languages, Baltic and Eastern European focus | CC-BY-4.0 | 30B: 09/2025, integrated into Tilde MT 02/2026 | Latvia | [tilde.ai](https://tilde.ai/tildeopen-llm/), [HF](https://huggingface.co/TildeAI/TildeOpen-30b) |

### Speech, multimodal and agent foundation models

| Model | Modalities | License | Latest release | Origin | Links |
| --- | --- | --- | --- | --- | --- |
| **Alfred Sovereign v5** (LightOn) | text (RAG-oriented) | open weights + Paradigm platform | Alfred-sv5 (24B), 2025-2026 | :fr: France | [LightOn docs](https://docs.lighton.ai/en/developer-resources/lighton-models/alfred-sv5) |
| **Holo-1 / Surfer H** (H Company) | vision-language action model (web agents) | Apache 2.0 (open weights) | Holo-1 3B and 7B, 06/2025, Holo 3 in 2026 | :fr: France | [hcompany.ai](https://hcompany.ai/), [Surfer H CLI](https://github.com/hcompai/surfer-h-cli) |
| **Moshi / Moshika** (Kyutai) | full-duplex speech-to-speech | code MIT + Apache 2.0, weights CC-BY 4.0 | Public release 09/2024, TTS 1.6B and Unmute in 2026 | :fr: France | [kyutai.org](https://kyutai.org/), [GitHub](https://github.com/kyutai-labs/moshi) |
| **Voxtral** (Mistral AI) | speech understanding + TTS + transcription (3B, 4B, 24B), multilingual up to 13 languages | Apache 2.0 (understanding, Realtime), CC-BY-NC 4.0 (TTS) | Voxtral 07/2025, Transcribe 2 02/2026, TTS 03/2026 | :fr: France | [mistral.ai](https://mistral.ai/news/voxtral/), [Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2/), [TTS](https://mistral.ai/news/voxtral-tts/) |

---

## 2. National and community LLMs (active)

Living projects with real 2024-2026 releases, typically focused on one or a few languages.

| Project | Country / origin | Focus | License | Latest activity | Links |
| --- | --- | --- | --- | --- | --- |
| **AI Sweden** | :sweden: Sweden | GPT-SW3, Nordic models | mixed | Institutional programme, ongoing | [ai.se](https://www.ai.se/en) |
| **Beia Consult International** | :ro: Romania | Romanian speech and NLP, ASR, TTS and chatbots, inside EU research projects | mixed | R&D SME, active across FP7, H2020 and Horizon Europe projects | [beia.ro](https://beia.ro/), [EU projects](https://beiaro.eu/) |
| **Blip.solutions** | :slovakia: Slovakia | Open-source LLM tooling, langchain-decorators and prompt tracing | MIT | langchain-decorators still updated 04/2026 | [blip.solutions](https://www.blip.solutions/), [GitHub](https://github.com/ju-bezdek/langchain-decorators) |
| **Claire family** (OpenLLM France) | :fr: France | French conversational | Apache 2.0 | 2023-2024 (predecessor to Lucie/Luciole) | [HF](https://huggingface.co/OpenLLM-France) |
| **CroAI** | :croatia: Croatia | Croatian AI community | open | Active community | [croai.org](https://www.croai.org/) |
| **Croissant LLM** (CentraleSupélec + Illuin) | :fr: France | fr-en bilingual, small model | open | Reference 1.3B bilingual model | [HF](https://huggingface.co/croissantllm) |
| **Danish Foundation Models** (Munin family) | :denmark: Denmark | Danish | open | Munin 7B alpha 2024, continued in 2025 | [HF](https://huggingface.co/danish-foundation-models) |
| **DanskGPT** | :denmark: Denmark | Danish assistant | mixed | Public 2024-2025 | [danskgpt.dk](https://www.danskgpt.dk/) |
| **EMBEDDIA / SloBERTa** | :lithuania: Lithuania / :slovenia: Slovenia | Baltic and Slavic | open (research) | Historical family, still used | [embeddia.eu](http://embeddia.eu/) |
| **Expert AI** | :it: Italy | Hybrid neuro-symbolic NLP, knowledge graphs combined with LLMs | mixed | Active commercial + research | [expert.ai](https://www.expert.ai/) |
| **Fauno Italian LLM** (Sapienza) | :it: Italy | Italian | open | Reference release 2023-2024 | [GitHub](https://github.com/RSTLess-research/Fauno-Italian-LLM) |
| **Going Dutch, GEITje** | :netherlands: Netherlands | Dutch | open | Community-maintained | [Blog](https://goingdutch.ai/en/posts/introducing-geitje/) |
| **Hilanco** | :hungary: Hungary | Hungarian | open | Community project | [hilanco.github.io](https://hilanco.github.io/home.html) |
| **HUN-REN Linguistic Institute** | :hungary: Hungary | Hungarian | open (research) | Active in 2024-2025 | [nytud.hu](https://nytud.hu/en) |
| **KInit** | :slovakia: Slovakia | Slovak NLP | open (research) | Active on GitHub | [github.com/kinit-sk](https://github.com/kinit-sk) |
| **LAION** | :de: Germany / International | Open datasets and multimodal | open | Continuously active | [laion.ai](https://laion.ai/) |
| **Le Bon LLM** | :fr: France | French community | open | Community initiative | [lebonllm.fr](https://www.lebonllm.fr/) |
| **Llama-Krikri** (ILSP, Athena Research Center) | :greece: Greece | Greek LLMs and Greek evaluation suite | Llama 3.1 | Krikri 8B Instruct updated 12/2025, Greek evaluation datasets updated 2026 | [Krikri collection](https://huggingface.co/collections/ilsp/krikri-8b-68273283651ba864d44fc33a), [Greek evaluation suite](https://huggingface.co/collections/ilsp/ilsp-greek-evaluation-suite-6827304d5bf8b70d0346b02c), [ILSP on HF](https://huggingface.co/ilsp) |
| **LLM for Romanian (ILDS)** | :ro: Romania | Romanian | open (research) | Active 2024-2025 | [ilds.ro](https://ilds.ro/llm-for-romanian/) |
| **NLP Odyssey** | :it: Italy | NLP libs and models | open | Active OpenCollective | [OpenCollective](https://opencollective.com/nlpodyssey) |
| **Nordavind, nordic-ner** (Tollef Jørgensen, NTNU and Sikt) | :norway: Norway | Norwegian and Nordic fine-tunes, NER and evaluation datasets | open | Nordavind Llama 3.1 8B 02/2025, Nordic NER and Norwegian STS datasets | [HF](https://huggingface.co/tollefj), [Norwegian LLMs collection](https://huggingface.co/collections/tollefj/norwegian-llms) |
| **NOUS Research** | :gb: United Kingdom | Instruction & alignment | mixed open | Regular releases in 2025-2026 | [HF](https://huggingface.co/NousResearch) |
| **PORO / Viking / Europa** (ex-Silo AI, now AMD) | :fi: Finland / International | Nordic + multilingual | Apache 2.0 | Models still openly available, roadmap now under AMD | [Announcement](https://www.silo.ai/blog/poro-a-family-of-open-models-that-bring-european-languages-to-the-frontier) |
| **SiloGen platform** (AMD, ex-Silo AI) | :fi: Finland (AMD) | Enterprise LLM ops | mixed | Post-acquisition 2024+ | See section 4 |
| **TartuNLP** | :estonia: Estonia | Estonian NLP, translation | open | Continuously maintained | [tartunlp.ai](https://tartunlp.ai/) |
| **Tilde AI** | :latvia: Latvia | Baltic MT and LLM services, publisher of TildeOpen LLM (see section 1) | mixed | Active commercial + research | [tilde.com](https://www.tilde.com/) |

---

## 3. Archives and historical models

First-generation BERT-family models and early monolingual encoders. Based on public evidence they appear less or no longer actively developed, though most remain downloadable. Kept here for lineage and reproducibility, contributions to update their status are welcome.

| Model | Language | Origin | Links |
| --- | --- | --- | --- |
| **BERTu** | mt | :malta: Malta | [GitHub](https://github.com/MLRS/BERTu) |
| **Czech BERT** | cs | :czech_republic: Czech Republic | [Paper](https://aclanthology.org/2021.ranlp-1.149.pdf) |
| **Falcon 7B / 40B / 180B** (TII, adjacent) | en (multilingual) | :united_arab_emirates: UAE (adjacent to European ecosystem) | [HF](https://huggingface.co/tiiuae) |
| **gaBERT** | ga (Irish) | :ireland: Ireland | [Paper](https://aclanthology.org/2022.lrec-1.511.pdf) |
| **Insait, original BgGPT** (pre-Gemma 2) | bg | :bulgaria: Bulgaria | [Launch post](https://bggpt.ai/blog/2024-02-18-launching-the-first-free-and-open-bulgarian-llm/) |
| **Lucie-7B / Lucie-7B-Instruct** (OpenLLM France) | multilingual, fr-first | :fr: France | [Paper](https://arxiv.org/abs/2503.12294), succeeded by Luciole in 2026 |
| **LVBERT** | lv | :latvia: Latvia | [GitHub](https://github.com/LUMII-AILab/LVBERT) |
| **Meltemi-7B** (ILSP, Athena Research Center) | el | :greece: Greece | [Meltemi collection](https://huggingface.co/collections/ilsp/meltemi-7b-682731cced6c20f2dc1b725c), [Paper](https://arxiv.org/abs/2407.20743) - first open LLM for Greek (Mistral-based, 2024), succeeded by Llama-Krikri |
| **Polbert** | pl | :poland: Poland | [HF](https://huggingface.co/dkleczek) |
| **Sabia** | pt-br | :portugal: Portugal | [Paper](https://arxiv.org/abs/2304.07880) |
| **Serbian LLM eval** | sr | :serbia: Serbia | [GitHub](https://github.com/gordicaleksa/serbian-llm-eval) |
| **SloBERTa** | sl | :slovenia: Slovenia | [HF](https://huggingface.co/EMBEDDIA/sloberta) |
| **YugoGPT** | Serbo-Croatian family | :serbia: Serbia, :croatia: Croatia, :bosnia_herzegovina: Bosnia and Herzegovina, :macedonia: North Macedonia, :kosovo: Kosovo | [yugochat.com](https://www.yugochat.com/) |

> Adjacent, non-European projects (LangFuse, Sayhan and Sestek, AI Forever, Yandex YaLM, Evidently AI, EleutherAI) previously listed at repo level are no longer catalogued here. They are excellent references but out of scope for a European catalogue. Two further entries were dropped rather than archived: **Statisfied**, whose site no longer resolves, and **Sosnitskij**, a Hugging Face account republishing quantised Russian models with no activity since 02/2024.

---

## 4. Reoriented or acquired projects

Kept here for lineage. The teams and models are still relevant, but the governance or the mission has moved.

| Project | Status | What happened | Links |
| --- | --- | --- | --- |
| **BLOOM (BigScience)** | Historical milestone | Foundational 176B multilingual model, no active successor from BigScience itself, but a reference for every subsequent European effort | [HF](https://huggingface.co/bigscience/bloom) |
| **BSC, Aguila / Alpaca (Aina v1)** | Superseded | Rolled into the Salamandra / ALIA family (see section 1) | [projecteaina.cat](https://projecteaina.cat) |
| **LightOn Alfred-40B (Falcon-based)** | Superseded | Replaced by Alfred Sovereign v5 (24B, new architecture) | [Alfred v5](https://docs.lighton.ai/en/developer-resources/lighton-models/alfred-sv5) |
| **Silo AI (PORO, Viking, Europa)** | Acquired | Bought by **AMD** in 08/2024 for $665M, models remain open, roadmap now integrated into AMD's AI strategy | [AMD press release](https://www.amd.com/en/newsroom/press-releases/2024-8-12-amd-completes-acquisition-of-silo-ai-to-accelerate.html) |
| **Stability AI (UK)** | Reoriented | Refocused on image/video/audio generation, no longer a European frontier LLM effort | [stability.ai](https://stability.ai/) |

---

## Ecosystem organisations and infrastructures

The following organisations are **not models** but structure the European open-source AI ecosystem: funding, compute, licensing, governance. They are referenced here so contributors know where to look.

| Organisation | Role | Links |
| --- | --- | --- |
| **AI Factory France** | Sovereign AI infrastructure programme operated under GENCI | See GENCI |
| **ALT-EDIC, Alliance for Language Technologies EDIC** | European Digital Infrastructure Consortium for language technologies | [ALT-EDIC](https://language-data-space.ec.europa.eu/related-initiatives/alt-edic_en) |
| **BSC, Barcelona Supercomputing Center** | Host of MareNostrum 5, ALIA / Salamandra training | [bsc.es](https://www.bsc.es) |
| **Common Crawl Foundation** | Upstream open-web archive powering nearly every European pretraining corpus | [commoncrawl.org](https://commoncrawl.org/) |
| **Confiance.ai / European Trustworthy AI Association (ETAA)** | Trustworthy AI methodologies and open-source tooling | [confiance.ai](https://www.confiance.ai/) |
| **Current AI** | Global public-interest AI partnership launched at the Paris AI Action Summit (02/2025). $400M+ committed, $2.5B target over 5 years. Funds open datasets, open-source infrastructure and AI auditing. Country partners: France, Germany, Finland, Slovenia, Switzerland, Chile, India, Kenya, Morocco, Nigeria. CEO: Ayah Bdeir | [currentai.org](https://www.currentai.org/) |
| **Eclipse Foundation AISBL** | European open-source foundation, hosts AI working groups | [eclipse.org](https://www.eclipse.org/) |
| **EuroHPC JU** | European supercomputing joint undertaking (LUMI, Leonardo, JUWELS, MareNostrum 5, Jupiter, Alice Recoque) | [eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/) |
| **Fraunhofer IAIS** | Coordinator of OpenGPT-X, TrustLLM, Eurolingua | [iais.fraunhofer.de](https://www.iais.fraunhofer.de/en.html) |
| **GENCI + Jules Verne consortium** | French national HPC, hosting Jean Zay, leading the **Alice Recoque** Exascale system for EuroHPC | [genci.fr](https://www.genci.fr) |
| **GFOSS, Open Technologies Alliance** | Greek non-profit backed by 38 universities and research centres, runs GlossAPI to strengthen Greek in NLP | [gfoss.eu](https://gfoss.eu/), [GitHub](https://github.com/eellak) |
| **LLMs4EU** | Flagship ALT-EDIC project | [ALT-EDIC, LLMs4EU](https://www.alt-edic.eu/projects/llms4eu/) |
| **Luxembourg Institute of Science and Technology (LIST), Trustworthy AI group** | Research on trustworthy AI at EU level | [list.lu](https://www.list.lu/en/environment/research-groups/group/trustworthy-ai/) |
| **Open Source Initiative (OSI)** | Maintains the **Open Source AI Definition (OSAID)** | [opensource.org](https://opensource.org/) |
| **OpenForum Europe** | EU open-source policy advocacy | [openforumeurope.org](https://openforumeurope.org/) |
| **Paris Open Source AI Summit (POSAIS)** | Annual European gathering on open-source AI | [opensourceaisummit.eu](https://opensourceaisummit.eu/) |
| **TrustLLM** | Horizon Europe project on trustworthy multilingual LLMs | [trustllm.eu](https://trustllm.eu/) |

---

## How to contribute

Two ways in, pick whichever suits you.

**1. Open an issue, no git needed.** Fill the [Add a project form](https://github.com/OpenLLM-Europe/European-OpenLLM-Projects/issues/new?template=add-project.yml) and a maintainer turns it into a catalogue row. Use the [update form](https://github.com/OpenLLM-Europe/European-OpenLLM-Projects/issues/new?template=update-entry.yml) for a stale date, a dead link, or a project whose status has changed. This is the recommended path if pull requests are not your daily tool.

**2. Send a pull request.** Copy the [row template](#row-templates) for the right section, fill it in, open the pull request.

### What we accept

- Add a **missing European open-source project** with a public artefact (model card, dataset card, or repository).
- **Update the "Latest release" column** with an evidence link (Hugging Face, GitHub, arXiv, or an official press release).
- **Move a project** across sections when its status changes, for example from section 2 to section 3 when a project becomes inactive, or from section 1 to section 4 after an acquisition.
- Add or fix links.

### House rules

- **One project per pull request.** The whole catalogue lives in a single file, so small pull requests are what keeps contributors from conflicting with each other.
- **Rows are sorted alphabetically** inside each table. Insert yours in the right place rather than at the end.
- **Touch your row and nothing else.** No reformatting, no reflowing the rest of the table.
- **Match the column count of the section you are editing.** The six tables do not share the same columns, and a row copied from another section renders broken. A check runs on every pull request to catch this.
- Keep entries **short, evidence-based, and honest**. This catalogue is designed to help European teams find each other and build together, not to advertise vapourware. When in doubt, open an issue first.
- Every listed contact must be an **existing public contact** for the project (mailing list, contact form, LinkedIn). Please do not add personal emails without the person's consent.

### Row templates

Copy the block for your section, replace the placeholders, and paste your single row into the table. The header and separator lines are shown so you can see the shape, do not paste them.

<details>
<summary><b>1. Foundation models, European frontier</b> &mdash; 7 columns</summary>

```markdown
| Model / family | Sizes | Languages | License | Latest release | Origin | Links |
| --- | --- | --- | --- | --- | --- | --- |
| **Model name** (organisation) | 7B, 70B | fr, en + EU | Apache 2.0 | MM/YYYY | Country | [site](https://example.org), [HF](https://huggingface.co/example) |
```

</details>

<details>
<summary><b>Speech, multimodal and agent foundation models</b> &mdash; 6 columns</summary>

```markdown
| Model | Modalities | License | Latest release | Origin | Links |
| --- | --- | --- | --- | --- | --- |
| **Model name** (organisation) | speech-to-speech, 7B | Apache 2.0 | MM/YYYY | :eu: Country | [site](https://example.org), [HF](https://huggingface.co/example) |
```

</details>

<details>
<summary><b>2. National and community LLMs (active)</b> &mdash; 6 columns</summary>

```markdown
| Project | Country / origin | Focus | License | Latest activity | Links |
| --- | --- | --- | --- | --- | --- |
| **Project name** (organisation) | :eu: Country | What it works on | Apache 2.0 | What shipped and when | [site](https://example.org), [HF](https://huggingface.co/example) |
```

</details>

<details>
<summary><b>3. Archives and historical models</b> &mdash; 4 columns</summary>

```markdown
| Model | Language | Origin | Links |
| --- | --- | --- | --- |
| **Model name** (organisation) | xx | :eu: Country | [HF](https://huggingface.co/example) - one line of lineage, what superseded it |
```

</details>

<details>
<summary><b>4. Reoriented or acquired projects</b> &mdash; 4 columns</summary>

```markdown
| Project | Status | What happened | Links |
| --- | --- | --- | --- |
| **Project name** | Acquired / Superseded / Reoriented | One sentence, with the date | [announcement](https://example.org) |
```

</details>

<details>
<summary><b>Ecosystem organisations and infrastructures</b> &mdash; 3 columns</summary>

```markdown
| Organisation | Role | Links |
| --- | --- | --- |
| **Organisation name** | What it does for the ecosystem | [site](https://example.org) |
```

</details>

Before opening the pull request you can run the same check as CI:

```bash
python3 .github/scripts/check_tables.py README.md
```

## License

This catalogue is released under **CC-BY 4.0**. Individual projects retain their own licenses as indicated in each row.
