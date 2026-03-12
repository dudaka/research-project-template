# Workflow Guide: The Research OS

This is a Claude Code-native research workflow. It uses a 3-tier progressive disclosure architecture to keep the context window lean while giving Claude full access to your literature, decisions, and experimental state.

## Architecture: Progressive Disclosure (3-Tier)

```
Tier 1 (Global)    Root CLAUDE.md           Always loaded. Phase status, code map, must-read tracker.
                                             Keep under 150 lines.

Tier 2 (Rules)     .claude/rules/*.md       Auto-triggered when working in specific directories.
                                             Research protocol, infra standards, SDK workflow.

Tier 3 (Local)     docs/references/[paper]/ Raw paper data with local CLAUDE.md navigation maps.
                                             Zero tokens until explicitly read.
```

### Why This Architecture?

- **CLAUDE.md** is always in context -- it's your "project brain." Keep it current, keep it concise.
- **Rules** fire automatically -- research rigor, infrastructure conventions, and SDK patterns are enforced without you having to repeat them.
- **References** are lazy-loaded -- 9 papers = 0 extra tokens until Claude needs a specific section. The local `CLAUDE.md` in each paper folder is a table-of-contents that tells Claude exactly which file to read.

## Research Log Files

All research tracking lives in `docs/research_log/`:

| File | Purpose | Update Frequency |
| :--- | :--- | :--- |
| `TIMELINE.md` | Full roadmap with phases, weeks, deliverables, decision gates | Weekly |
| `HYPOTHESES.md` | Formal claims, prior evidence, test plans, status | When evidence changes |
| `DECISIONS.md` | Architectural choices with rationale and alternatives considered | Per decision |
| `LIT_REVIEW.md` | SOTA Gap Matrix -- what exists, what's missing, your contribution | Per paper ingested |
| `ABLATION_LOG.md` | Experiment comparisons (Config A vs B, metric, result) | Per experiment |
| `INFRA_STACKS.md` | Infrastructure options with cost breakdowns | When stack changes |
| `KICKOFF_PROMPT.md` | First-session prompt, intake questions, roadmap, session patterns | Once (at project start) |

## Starting a New Project

See `KICKOFF_PROMPT.md` for the full kickoff workflow: intake questions, first-session prompt to copy-paste, the 5-phase roadmap (Scaffold -> Define -> Ingest -> Build -> Run), and reusable session patterns (daily stand-up, context recovery, reviewer mode).

## Daily Workflow

### Stage A: Daily Stand-up (Start of Session)

Ask Claude to review `TIMELINE.md` and `HYPOTHESES.md`. Summarize where you left off and the immediate objective. Prevents context drift across sessions.

**Prompt:** "Read CLAUDE.md, TIMELINE.md, and HYPOTHESES.md. Where did we leave off and what's the immediate next step?"

### Stage B: Knowledge Ingestion (Adding Papers)

1. Convert PDF to markdown: `./convert_paper.sh path/to/paper.pdf` (add `--use_llm` for better quality)
2. Output lands in `incoming_papers/` automatically
3. Run `uv run organize_papers.py`
4. Verify local `CLAUDE.md` map and `references/` sub-folder were created
5. Ask Claude to update `LIT_REVIEW.md` with the new paper's gaps
6. Ask Claude to update `HYPOTHESES.md` with new prior evidence
7. Mark the paper as ingested in root `CLAUDE.md`

### Stage C: Surgical Implementation

1. Claude checks `docs/references/[paper]/CLAUDE.md` (the navigation map)
2. Claude reads only the specific section file (e.g., `02_methodology.md`)
3. Claude applies logic referencing `research_protocol.md` for rigor
4. For diagrams: "Visual Bridge" -- Claude identifies the image reference, asks user to describe the visual

### Stage D: Validation & Stress Testing

- Ablation checks against `ABLATION_LOG.md`
- "Reviewer 2" mode: Claude acts as hostile A* reviewer to find weaknesses
- Novelty audit against `LIT_REVIEW.md`

### Stage E: Scholar's Wrap-up (End of Session)

1. Update `DECISIONS.md` with results and pivots
2. Move completed items in `TIMELINE.md` to "Archive"
3. Run `/clear` to start fresh next session

## Troubleshooting

| Problem | Solution |
| :--- | :--- |
| Claude forgets the plan | Point to `TIMELINE.md` |
| Context gets heavy | `/clear` then ask Claude to resume by reading `DECISIONS.md` |
| Library API stale | Trigger Context7 MCP |
| Garbage collect | Every 3-4 days, summarize long discussion entries into concise notes |
| Long-running experiment | Use `nohup` or `tmux`, not Claude Code background tasks (killed on session clear) |
| Experiment interrupted | Build resume support (`--resume` flag) into all runner scripts |

## Decision Gates

Decision gates are checkpoints between phases where you evaluate whether to proceed, pivot, or stop. Define them in `TIMELINE.md` at the end of each phase.

**Template:**
```
**DECISION GATE:** {{What must be true?}} If yes -> {{next phase}}. If no -> {{pivot plan}}.
```

Decision gates prevent sunk-cost fallacy: if the pilot shows no signal, you pivot early instead of spending 3 more months.

## Adaptive Experimental Design (3-Stage Pattern)

A cost-efficient pattern for empirical research:

```
Stage 1: Discover  (~$1, ~1 day)
  Small pilot on subset of data. Confirms the effect exists before committing budget.

Stage 2: Establish  (~$8-30, ~1 week)
  Full sweep on primary dataset. Publication-quality results.

Stage 3: Differentiate  (~$30-100, ~1-2 weeks)
  Targeted experiments at points where Stage 2 showed strongest effects.
  Tests novel contribution (e.g., heterogeneity, ablations, cross-dataset).
```

Each stage has a decision gate. Total cost is 10-50x less than brute-force full grid.

## Paper Organization System

The `organize_papers.py` script converts PDF-to-markdown output into the Tier 3 reference structure:

```
docs/references/{{paper_slug}}/
  CLAUDE.md              Navigation map (section -> file)
  references/
    00_introduction.md
    01_abstract.md
    02_methods.md
    ...
  assets/
    figure1.png
    ...
```

This structure allows Claude to:
1. Read the `CLAUDE.md` map (tiny, fast)
2. Jump to exactly the section needed (e.g., `04_3_methods.md`)
3. Never load the full paper into context
