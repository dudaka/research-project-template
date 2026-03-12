# Research Project Template: Setup Guide

A Claude Code-native research workflow for empirical ML/NLP research papers. Designed for PhD students targeting top venues (NeurIPS, EMNLP, ICML, ACL, etc.).

## What This Template Provides

### 1. Progressive Disclosure Architecture (3-Tier)

Keeps Claude's context window lean while giving full access to literature, decisions, and experimental state.

| Tier | Location | Loaded When | Purpose |
| :--- | :--- | :--- | :--- |
| 1 (Global) | `CLAUDE.md` | Always | Project brain: status, code map, reading list |
| 2 (Rules) | `.claude/rules/*.md` | Auto-triggered by directory | Research protocol, infra standards |
| 3 (Local) | `docs/references/[paper]/` | On explicit read | Paper sections with navigation maps |

### 2. Research Log System (6 Files)

| File | Purpose |
| :--- | :--- |
| `WORKFLOW_GUIDE.md` | The Research OS manual (daily workflow, troubleshooting) |
| `TIMELINE.md` | Full roadmap with phases, decision gates, cost estimates |
| `HYPOTHESES.md` | Formal claims with prior evidence and test plans |
| `DECISIONS.md` | Architectural choices with rationale and rejected alternatives |
| `LIT_REVIEW.md` | SOTA Gap Matrix showing your unique contribution |
| `ABLATION_LOG.md` | Experiment comparison results |
| `INFRA_STACKS.md` | Infrastructure options with cost breakdowns |

### 3. Paper Ingestion Pipeline

PDF -> markdown (via `marker`) -> organized sections -> navigation map -> auto-updates to `CLAUDE.md` and `LIT_REVIEW.md`.

### 4. Adaptive Experimental Design Pattern

3-stage pattern: Discover (cheap pilot) -> Establish (full sweep) -> Differentiate (novel contribution). Decision gates between stages prevent wasted budget.

### 5. Daily Workflow

Stand-up -> Knowledge Ingestion -> Surgical Implementation -> Validation -> Wrap-up.

## Quick Start

### 1. Copy template to new project

```bash
cp -r research-project-template ~/Workspace/phd/my-new-project
cd ~/Workspace/phd/my-new-project
git init
```

### 2. Initialize Python environment

```bash
uv init  # or edit pyproject.toml directly
uv sync
```

### 3. Fill in the templates

Replace `{{placeholders}}` in these files (in this order):

1. **`CLAUDE.md`** -- Project title, objective, formal claim, hypotheses summary, target venue
2. **`docs/research_log/HYPOTHESES.md`** -- Your formal hypotheses with prior evidence
3. **`docs/research_log/TIMELINE.md`** -- Your phased roadmap with decision gates
4. **`docs/research_log/LIT_REVIEW.md`** -- Column headers for your SOTA dimensions
5. **`.claude/rules/research_protocol.md`** -- Your evaluation metric and rubric
6. **`.claude/rules/infra_standards.md`** -- Your provider stack and conventions
7. **`docs/research_log/INFRA_STACKS.md`** -- Detailed cost analysis

### 4. Set up API keys

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 5. Install marker for PDF conversion

```bash
uv tool install marker-pdf
```

This installs `marker_single` globally (no conda needed).

### 6. Ingest your first papers

```bash
# Basic conversion (no LLM, fast, free)
./convert_paper.sh path/to/paper.pdf

# With LLM assistance (better quality, requires ANTHROPIC_API_KEY in .env)
./convert_paper.sh path/to/paper.pdf --use_llm

# Then organize into Tier 3 reference structure
uv run organize_papers.py
```

The pipeline: PDF -> `incoming_papers/` (via `convert_paper.sh`) -> `docs/references/<slug>/` (via `organize_papers.py`).

### 7. Start your first session with Claude

See `docs/research_log/KICKOFF_PROMPT.md` for the full kickoff prompt, intake questions, roadmap, and session patterns. Copy-paste the First Session Prompt into Claude Code after filling in your topic details.

## Project Structure

```
my-research-project/
  CLAUDE.md                          # Tier 1: Always loaded, project brain
  README.md                          # Brief project description
  pyproject.toml                     # Python dependencies (uv)
  .env                               # API keys (gitignored)
  .env.example                       # API key template
  .gitignore
  convert_paper.sh                   # PDF -> incoming_papers/ (via marker)
  organize_papers.py                 # incoming_papers/ -> Tier 3 reference structure
  .claude/
    settings.local.json              # MCP permissions
    rules/
      research_protocol.md           # Tier 2: Math rigor, eval rubric, lit navigation
      infra_standards.md             # Tier 2: Provider stack, data standards
  docs/
    research_log/
      WORKFLOW_GUIDE.md              # The Research OS manual
      TIMELINE.md                    # Phased roadmap + decision gates
      HYPOTHESES.md                  # Formal claims + prior evidence
      DECISIONS.md                   # Architecture decision log
      LIT_REVIEW.md                  # SOTA Gap Matrix
      ABLATION_LOG.md                # Experiment comparisons
      INFRA_STACKS.md                # Infrastructure cost analysis
    references/                      # Tier 3: One folder per paper
      <paper_slug>/
        CLAUDE.md                    # Navigation map (section -> file)
        references/                  # Section markdown files
        assets/                      # Figures
    deep-research/                   # Archive for deep research reports
  src/                               # Source code modules
    __init__.py
  tests/                             # Integration and unit tests
    __init__.py
  data/
    raw/                             # Downloaded datasets
    processed/                       # Experiment outputs (JSONL)
  plots/                             # Generated figures
```

## Key Principles

1. **CLAUDE.md is the single source of truth.** Keep it under 150 lines. Update it every session.

2. **Hypotheses drive everything.** Every experiment, decision, and code module should trace back to an H1-HN hypothesis.

3. **Decision gates prevent sunk costs.** If the pilot shows no signal, pivot early. Don't spend 3 months on a dead end.

4. **Progressive disclosure saves context.** Never dump a full paper into Claude's context. Use the CLAUDE.md navigation maps.

5. **Decisions are immutable records.** Log the choice, the rationale, AND the alternatives you rejected. Future-you (and reviewers) will thank you.

6. **Cost-aware by default.** The INFRA_STACKS.md file forces you to think about cost before you start running experiments.

7. **Sequential Thinking for hard decisions.** Complex experimental design or architecture trade-offs get the Sequential Thinking MCP treatment, not ad-hoc reasoning.

## Recommended MCP Servers

| MCP Server | Purpose |
| :--- | :--- |
| **Sequential Thinking** | Complex experimental design, multi-factor trade-offs |
| **Context7** | Latest library/SDK documentation |
| **GitHub** | Experiment branches, PR workflow |

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- [uv](https://docs.astral.sh/uv/) Python package manager
- Python 3.13+

### One-time setup

```bash
# Install marker globally as a uv tool (no conda needed)
uv tool install marker-pdf
```

This makes `marker_single` available system-wide. The `convert_paper.sh` script wraps it with proper env var handling.
