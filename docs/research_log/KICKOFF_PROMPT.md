# Kickoff Prompt

Use this prompt when starting a new research project with Claude Code. Copy-paste it into your first session after scaffolding the project.

---

## First Session Prompt

```
I'm starting a new research project using the Research OS template.

Here's the context:
- **Topic:** {{one sentence describing the research question}}
- **Target venue:** {{NeurIPS / EMNLP / ICML / ACL / workshop / etc.}} {{year}}
- **Deep research report:** saved in docs/deep-research/{{filename}}
- **Papers to ingest:** {{list arXiv IDs or filenames in incoming_papers/}}

Please help me fill in the project templates in this order:

1. `CLAUDE.md` -- objective, formal claim, core argument, code structure, infrastructure stack
2. `docs/research_log/HYPOTHESES.md` -- H1-HN with prior evidence from the deep research report
3. `docs/research_log/TIMELINE.md` -- phased roadmap with decision gates and cost estimates
4. `docs/research_log/LIT_REVIEW.md` -- SOTA gap matrix (pick the right column dimensions for my domain)
5. `.claude/rules/research_protocol.md` -- evaluation metric and scoring rubric
6. `.claude/rules/infra_standards.md` -- provider stack and experiment protocol
7. `docs/research_log/INFRA_STACKS.md` -- budget vs best-result cost analysis

Use Sequential Thinking for any complex design decisions. Log all decisions in DECISIONS.md.
```

---

## Intake Questions

Before filling templates, answer these (or have Claude ask you):

1. **What's the research question?** (one sentence)
2. **What's the formal claim?** (mathematical formulation if applicable)
3. **Why does this matter?** (core argument -- why your approach, why now)
4. **What's the primary dataset/benchmark?**
5. **What's the primary evaluation metric?**
6. **What compute do you have?** (local GPU, cloud budget, free tiers)
7. **Do you have the deep-search report saved?** (PDF, markdown, browser)
8. **Which papers are must-reads?** (Tier 1 = blocks everything)
9. **Target venue and deadline?**

---

## Kickoff Roadmap

### Phase 0: Scaffold (~5 min)

```bash
# 1. Copy template
cp -r ~/Workspace/phd/research-project-template ~/Workspace/phd/{{project-name}}
cd ~/Workspace/phd/{{project-name}}

# 2. Initialize
git init
uv init  # or edit pyproject.toml, then:
uv sync

# 3. Set up API keys
cp .env.example .env
# Edit .env with your keys
```

### Phase 1: Define the Project (~30 min, with Claude)

Work through the First Session Prompt above. Claude will help you fill in all 7 template files using your deep research report as source material.

Key outputs:
- `CLAUDE.md` fully populated (project brain)
- `HYPOTHESES.md` with H1-HN, each with prior evidence and test plan
- `TIMELINE.md` with 4-phase roadmap and decision gates
- `LIT_REVIEW.md` with gap matrix columns chosen for your domain
- `DECISIONS.md` with initial design decisions (D1-DN)
- Rules files customized for your evaluation metric and infrastructure

### Phase 2: Ingest Literature (~1-2 hours)

```bash
# 1. Archive deep research report
cp path/to/gemini-report.md docs/deep-research/

# 2. Convert papers (one at a time)
./convert_paper.sh path/to/paper1.pdf --use_llm
./convert_paper.sh path/to/paper2.pdf --use_llm

# 3. Organize into Tier 3 reference structure
uv run organize_papers.py

# 4. For each paper, ask Claude:
#    "Read docs/references/<slug>/CLAUDE.md, then the methodology section.
#     Update LIT_REVIEW.md and HYPOTHESES.md with this paper's findings."
```

Repeat step 4 for each paper. This is where the gap matrix and prior evidence sections get populated.

### Phase 3: Build Infrastructure (~1-2 days)

Start coding in `src/`. Typical module order:

1. **Provider/API abstraction** -- connect to your compute (LLM APIs, local models, etc.)
2. **Data loader** -- load and sample your dataset
3. **Core pipeline** -- the main experimental logic (orchestrator, runner, etc.)
4. **Evaluator** -- scoring/judging outputs
5. **Pilot runner** -- small-scale experiment with CLI interface
6. **Analysis + plotting** -- curve fitting, statistical tests, figures

Integration test after each module. Smoke-test the full pipeline before running the pilot.

### Phase 4: Run Experiments (Adaptive 3-Stage)

```
Stage 1: Discover  (~$1, ~1 day)
  Small pilot on subset. Decision gate: does the effect exist?

Stage 2: Establish  (~$8-30, ~1 week)
  Full sweep on primary dataset. Publication-quality results.

Stage 3: Differentiate  (~$30-100, ~1-2 weeks)
  Novel contribution experiments. Cross-dataset validation.
```

### Phase 5: Write Paper (~2-4 weeks)

1. Generate all tables and figures from `data/processed/`
2. Failure attribution (categorize what went wrong and why)
3. Draft in LaTeX: Intro, Related Work, Method, Results, Discussion, Limitations
4. "Reviewer 2" mode: Claude acts as hostile reviewer to find weaknesses
5. Novelty audit against `LIT_REVIEW.md`
6. Polish and submit

---

## Session Patterns

### Daily stand-up (start of every session)
```
Read CLAUDE.md, TIMELINE.md, and HYPOTHESES.md.
Where did we leave off and what's the immediate next step?
```

### End of session
```
Update DECISIONS.md with today's results and pivots.
Move completed items in TIMELINE.md.
```

### Context recovery (after /clear or new session)
```
Read CLAUDE.md and docs/research_log/DECISIONS.md.
Resume from where we left off.
```

### Reviewer 2 mode
```
Act as a hostile reviewer for {{venue}}.
Read HYPOTHESES.md and LIT_REVIEW.md.
What are the 3 biggest weaknesses in our experimental design?
```
