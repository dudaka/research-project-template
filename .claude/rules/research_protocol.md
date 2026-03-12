# Research Protocol

## 1. Mathematical Rigor

- When fitting scaling laws or statistical models, always report **Standard Error**, **R-squared**, and model selection criteria (**AIC/BIC**).
- When implementing optimization algorithms, enforce convergence constraints and document any regularization choices.
- All mathematical claims in code must match the formulation in `HYPOTHESES.md`.

## 2. Evaluation Rubric

{{Define your project's primary evaluation metric and scoring rubric here.}}

- **Primary Metric:** {{Name}} [range: {{min}} to {{max}}]
  - {{min}}: {{What this means}}
  - {{max}}: {{What this means}}
- **Evaluation Protocol:** {{How evaluation is conducted (e.g., LLM-as-Judge with CoT, human annotation, automated metrics).}}

## 3. Literature Navigation (Progressive Disclosure)

Papers are stored in `docs/references/[paper]/` with a local `CLAUDE.md` navigation map.

- **Surgical Reading:** Do not read full markdown papers. Check the `CLAUDE.md` map first.
- **Navigation:** Identify the specific section (e.g., `02_methodology.md`) and read only that file or specific line ranges.
- **Asset Check:** If a paper mentions a diagram, refer to the `assets/` folder and ask the user for visual clarification if needed.

## 4. Reviewer Mode (A* Standards)

- **Baseline Fairness:** Every experiment must compare against a compute-matched or resource-matched baseline.
- **Failure Attribution:** Categorize failures systematically (define a taxonomy or adopt one from literature).
- **Novelty Audit:** Periodically check `LIT_REVIEW.md` gap matrix to ensure the contribution remains distinct from existing SOTA.
