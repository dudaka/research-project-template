# Kickoff Prompt

Use this prompt when starting a new research project with Claude Code. Copy-paste it into your first session after scaffolding the project.

---

## First Session Prompt

```
I'm starting a new research project using the Research OS template.

- **Target venue:** {{NeurIPS / EMNLP / ICML / ACL / AAAI / IJCAI / workshop / Q1 journal / etc.}} {{year}}
- **Deadline:** {{date}}
- **Compute:** {{local GPU, cloud budget, free tiers}}

I have deep research files from Gemini (report + Q&A conversations). I will drop
them one by one. Do NOT fill any templates until I say "all files ingested."

---

PHASE 1: INGESTION (after each file I drop)

Use ultrathink to read the file thoroughly. Then produce a brief summary:
- **Key findings:** most important claims, methods, gaps, references
- **Relevant to:** which parts of the template this informs (problem definition,
  methodology, related work, experiments, evaluation)
- **Open questions:** anything unclear or needing my clarification
- **Contradictions:** any conflicts with previously ingested files

Wait for the next file.

---

PHASE 2: SYNTHESIS (after I say "all files ingested")

1. Cross-consistency check: verify all files agree on the core problem, approach,
   and claims. Flag contradictions — ask me to resolve before proceeding.
2. Present a synthesis for my confirmation:
   - The research question (one paragraph)
   - The proposed contribution (what is new)
   - Formal problem sketch (inputs, outputs, objective)
   - Key properties to prove (from FORMAL_FRAMEWORK.md Section 5.2)
   - Any remaining intake questions the files did not answer
3. Wait for my confirmation before proceeding to Phase 3.

---

PHASE 3: TEMPLATE FILLING (after I confirm the synthesis)

Fill templates in this order, using ultrathink and Sequential Thinking for every
complex decision. Log all decisions in DECISIONS.md.

1. `FORMAL_FRAMEWORK.md` Sections 1-5 -- problem definition, notation, definitions,
   assumptions, property identification (this is the foundation — everything else
   depends on it)
2. `CLAUDE.md` -- objective, formal claim, core argument, code structure, infra stack
3. `HYPOTHESES.md` -- H1-HN with prior evidence, each linked to theorems in
   FORMAL_FRAMEWORK.md via the "Formal basis" field
4. `LIT_REVIEW.md` -- SOTA gap matrix (pick column dimensions for my domain)
5. `TIMELINE.md` -- phased roadmap with theoretical development milestones, decision
   gates, and cost estimates
6. `research_protocol.md` -- evaluation metric and scoring rubric
7. `infra_standards.md` -- provider stack and experiment protocol
8. `INFRA_STACKS.md` -- budget vs best-result cost analysis

After all templates are filled:
- Run a final consistency check across ALL files (FORMAL_FRAMEWORK, CLAUDE.md,
  HYPOTHESES, LIT_REVIEW, TIMELINE, rules). Flag any mismatches.
- Verify bidirectional links: every theorem points to a hypothesis, every hypothesis
  with a formal basis points to a theorem.
- Present a summary of all decisions logged in DECISIONS.md.
```

---

## Intake Questions

Most of these will be answered by the ingested files. During Phase 2 synthesis, Claude should verify it can answer all of them. Any that remain unanswered become questions for the user.

1. **What's the research question?** (one sentence)
2. **What's the formal claim?** (mathematical formulation if applicable)
3. **What is the formal problem?** (optimization, decision, learning, estimation -- what are the inputs, outputs, and objective?)
4. **What type of theoretical guarantee do you aim for?** (convergence, regret bound, approximation ratio, generalization bound, complexity result, correctness, other)
5. **What are the key assumptions your approach relies on?** (convexity, smoothness, bounded domain, i.i.d. data, etc.)
6. **Why does this matter?** (core argument -- why your approach, why now)
7. **What's the primary dataset/benchmark?**
8. **What's the primary evaluation metric?**
9. **Which papers are must-reads?** (Tier 1 = blocks everything)

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

### Phase 1: Ingest Deep Research & Define Project (~1-2 hours, with Claude)

```bash
# 1. Archive deep research files
cp path/to/gemini-report.md docs/deep-research/
cp path/to/qa-session-*.md docs/deep-research/
```

1. Paste the First Session Prompt into Claude Code
2. Drop files one by one (report first, then Q&A files)
3. After each file, review Claude's ingestion summary — correct any misunderstandings
4. Say "all files ingested" when done
5. Review Claude's synthesis — confirm or adjust before template filling
6. Claude fills all templates, then runs the final consistency check

Key outputs:
- `FORMAL_FRAMEWORK.md` with problem definition, notation, definitions, assumptions, property identification
- `CLAUDE.md` fully populated (project brain)
- `HYPOTHESES.md` with H1-HN, each linked to theorems in FORMAL_FRAMEWORK.md
- `LIT_REVIEW.md` with gap matrix columns chosen for your domain
- `TIMELINE.md` with 4-phase roadmap, theoretical development milestones, and decision gates
- `DECISIONS.md` with initial design decisions (D1-DN)
- Rules files customized for your evaluation metric and infrastructure

### Phase 2: Ingest Literature (~1-2 hours)

```bash
# 1. Convert papers (one at a time)
./convert_paper.sh path/to/paper1.pdf --use_llm
./convert_paper.sh path/to/paper2.pdf --use_llm

# 2. Organize into Tier 3 reference structure
uv run organize_papers.py

# 3. For each paper, ask Claude:
#    "Read docs/references/<slug>/CLAUDE.md, then the methodology section.
#     Update LIT_REVIEW.md, HYPOTHESES.md, and FORMAL_FRAMEWORK.md with
#     this paper's findings."
```

Repeat step 3 for each paper. This populates the gap matrix, prior evidence, and may refine assumptions or properties.

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
Read HYPOTHESES.md, LIT_REVIEW.md, and FORMAL_FRAMEWORK.md.
Use the checklist in research_protocol.md Section 5.
What are the 3 biggest weaknesses in our theoretical claims and experimental design?
```

### Rebuttal preparation (after reviews arrive)
```
Read CLAUDE.md, FORMAL_FRAMEWORK.md, and HYPOTHESES.md.
I will paste the reviewer comments. For each concern:
1. Classify: theoretical gap, experimental gap, clarity issue, or misunderstanding
2. If theoretical gap: can we tighten the proof or add a lemma?
3. If experimental gap: what additional experiment would address it? Estimate cost and time.
4. If misunderstanding: draft a clear rebuttal paragraph.
Use ultrathink and Sequential Thinking for complex responses.
```

### Camera-ready (after acceptance)
```
Read CLAUDE.md and DECISIONS.md.
I will paste the final reviewer feedback. Help me:
1. Incorporate required changes into the paper
2. Update FORMAL_FRAMEWORK.md if any proofs were tightened during rebuttal
3. Verify notation consistency one final time
4. Prepare the code release (clean repo, README, license)
```
