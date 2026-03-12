# Timeline: {{N}}-Week Roadmap ({{TARGET_VENUE}} {{YEAR}})

## Phase 1: Foundation & Infrastructure (Month 1)

### Week 1-2: Literature Intensive
- [ ] Ingest all Tier 1-3 papers through `marker` + `organize_papers.py`
- [ ] Populate `LIT_REVIEW.md` SOTA Gap Matrix
- [ ] Focus: {{Paper 1}} -- {{what to extract from it}}
- [ ] Focus: {{Paper 2}} -- {{what to extract from it}}
- [ ] Focus: {{Paper 3}} -- {{what to extract from it}}

### Week 3: Infrastructure
- [ ] Set up compute environment (local / cloud / hybrid)
- [ ] Build core abstractions: {{provider, orchestrator, evaluator, etc.}}
- [ ] Integration test on minimal configuration
- [ ] Dependencies added via `uv add`

### Week 4: Data Pipeline + Pilot (Stage 1: Discover)
- [ ] Download / prepare primary dataset
- [ ] Build data loader + pilot runner
- [ ] Smoke-test pipeline end-to-end
- [ ] Build evaluation script + analysis + plotting
- [ ] Run pilot on small subset
- [ ] **DECISION GATE:** Does the effect exist at all? If yes -> Phase 2. If no -> pivot early.
- [ ] Estimated cost: ~${{N}}

## Phase 2: {{Phase 2 Name}} (Month 2) -- Stage 2: Establish

### Week 5-6: Full Sweep
- [ ] Run full experimental grid on primary dataset
- [ ] {{Description of what is being swept}}
- [ ] Compute-matched baselines

### Week 7: Curve Fitting + Baselines
- [ ] Fit primary model (e.g., scaling law, regression)
- [ ] Compare alternative functional forms via AIC/BIC
- [ ] Report key statistics with confidence intervals

### Week 8: Expansion + Decision Gate
- [ ] If results hold: expand to secondary dataset / additional configurations for robustness
- [ ] **DECISION GATE:** Do results support the main claim? Proceed to Phase 3 or pivot.
- [ ] Estimated cost: ~${{N}}

## Phase 3: {{Phase 3 Name}} (Month 3) -- Stage 3: Differentiate

### Week 9-10: {{Novel Contribution Experiments}}
- [ ] Run targeted experiments at strongest effect points from Phase 2
- [ ] {{Description of what makes Phase 3 novel}}

### Week 11: Analysis
- [ ] {{Statistical tests for main claims}}
- [ ] {{Comparison analyses}}

### Week 12: Robustness & Final Fitting
- [ ] Cross-dataset validation
- [ ] Final model fit with all data
- [ ] Final evaluation calibration
- [ ] **DECISION GATE:** Story strong enough for {{venue}}? If not, target workshop paper.
- [ ] Estimated cost: ~${{N}}

## Phase 4: Analysis & Writing (Month 4)

### Week 13: Failure Attribution
- [ ] Categorize failures systematically
- [ ] Generate all experiment result tables

### Week 14: Figures
- [ ] {{Figure 1 description}}
- [ ] {{Figure 2 description}}
- [ ] {{Figure 3 description}}

### Week 15: Draft Writing
- [ ] Full paper draft in LaTeX
- [ ] Introduction, Related Work, Methodology, Results, Discussion, Limitations
- [ ] Ethics statement (if applicable)

### Week 16: Review & Submission
- [ ] Internal peer review ("Reviewer 2" mode)
- [ ] Address weaknesses
- [ ] Polish and submit

## Cost Summary (Adaptive 3-Stage Design)

| Stage | Phase | Data | Grid/Config | Cost | Compute |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Discover | Week 4 pilot | {{subset}} | {{small config}} | ~${{N}} | ~{{time}} |
| Establish | Phase 2 | {{primary dataset}} | {{full grid}} | ~${{N}} | ~{{time}} |
| Differentiate | Phase 3 | {{primary dataset}} | {{targeted configs}} | ~${{N}} | ~{{time}} |
| Validation | Cross-dataset | {{secondary dataset}} | selective | ~${{N}} | ~{{time}} |
| **Total** | | | | **~${{N}}** | **~{{time}}** |

## Scope Control: Explicitly Out of Scope

- {{Future work item 1}} -> future work
- {{Future work item 2}} -> future work
- {{Unrelated item}} -> different paper

## Archive
<!-- Move completed items here with dates -->
