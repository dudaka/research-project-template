# Project: {{PROJECT_TITLE}} ({{TARGET_VENUE}} {{YEAR}})

## Primary Objective

{{One paragraph describing the core research question and contribution.}}

**Formal:** {{Mathematical formulation of the main claim, if applicable.}} See `docs/research_log/FORMAL_FRAMEWORK.md` for full problem definition, assumptions, and proofs.

**Key hypotheses:** See `docs/research_log/HYPOTHESES.md` for H1-H{{N}}.

**Core argument:** {{Why this problem matters and why your approach is the right one.}}

## Current Status

**Phase {{N}}, Week {{N}}: {{Phase Name}}** -- {{IN PROGRESS / DONE}}

### In Progress (Week {{N}}: {{Phase Name}})

- [ ] {{Current task 1}}
- [ ] {{Current task 2}}
- [ ] **DECISION GATE**: {{What must be true to proceed?}}

### Completed (Previous Phases)

- [x] {{Completed milestone 1}}
- [x] {{Completed milestone 2}}

### Run Commands

```bash
# Step 1: {{Description}}
uv run python3 -m src.{{module}} {{args}}

# Step 2: {{Description}}
uv run python3 -m src.{{module}} {{args}}
```

### Infrastructure Stack

See `docs/research_log/INFRA_STACKS.md` for full details.

| Component | Provider | Cost |
| :--- | :--- | :--- |
| {{Component 1}} | {{Provider}} | {{Cost}} |
| {{Component 2}} | {{Provider}} | {{Cost}} |
| **Total** | | **~${{N}}** |

### Experimental Design

{{Brief summary of key experimental parameters: grid/sweep, dataset size, adaptive stages.}}

### Code Structure

| Module | Purpose |
| :--- | :--- |
| `src/provider.py` | {{Description}} |
| `src/{{module}}.py` | {{Description}} |

## Timeline & Milestones

1. **{{Phase 1 Name}} (Month 1):** {{Goals}}
2. **{{Phase 2 Name}} (Month 2):** {{Goals}}
3. **{{Phase 3 Name}} (Month 3):** {{Goals}}
4. **Writing (Month 4):** {{Goals}}

See `docs/research_log/TIMELINE.md` for the full roadmap.

## Reference Library

Located in `docs/references/`. Check the `CLAUDE.md` in each sub-folder for navigation.

### Ingested Papers

- {{Author et al. Year (Short Title)}}: `docs/references/{{slug}}/CLAUDE.md`

### Must-Read (To Ingest) -- Priority Order

**Tier 1 (Week 1 -- blocks everything):**
- [ ] {{Paper 1 -- why it blocks}}
- [ ] {{Paper 2 -- why it blocks}}

**Tier 2 (Week 2 -- methodology & frameworks):**
- [ ] {{Paper 3}}

**Tier 3 (Week 3-4 -- domain specifics):**
- [ ] {{Paper 4}}

**Tier 4 (as needed):**
- [ ] {{Paper 5 -- future work reference}}

## Research Log

- `docs/research_log/WORKFLOW_GUIDE.md` -- The Research OS manual
- `docs/research_log/TIMELINE.md` -- Full roadmap
- `docs/research_log/FORMAL_FRAMEWORK.md` -- Problem definition, notation, definitions, assumptions, property identification, theorems & proofs
- `docs/research_log/LIT_REVIEW.md` -- SOTA Gap Matrix
- `docs/research_log/HYPOTHESES.md` -- Empirical hypothesis tracking (links to theorems in FORMAL_FRAMEWORK.md)
- `docs/research_log/ABLATION_LOG.md` -- Experiment comparisons
- `docs/research_log/DECISIONS.md` -- Architectural pivots
- `docs/research_log/INFRA_STACKS.md` -- Infrastructure options & cost analysis

## Tools & MCP

- **Context7:** Check latest library docs before writing infrastructure code.
- **Sequential Thinking:** Always use for complex experimental design or architectural decisions.
