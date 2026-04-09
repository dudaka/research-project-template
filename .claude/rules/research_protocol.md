# Research Protocol

## 1. Mathematical Rigor

- When fitting scaling laws or statistical models, always report **Standard Error**, **R-squared**, and model selection criteria (**AIC/BIC**).
- When implementing optimization algorithms, enforce convergence constraints and document any regularization choices.
- All mathematical claims in code must match the formulation in `FORMAL_FRAMEWORK.md`.

## 2. Formal Proofs (Mandatory)

Every core methodological claim requires a formal proof before implementation or submission. This is non-negotiable for A* venues (AAAI, IJCAI, ICML, NeurIPS, etc.) and Q1 journals. All formal content lives in `docs/research_log/FORMAL_FRAMEWORK.md`.

### 2.1 Problem Definition First

Before stating any theorem, the problem must be formally defined in `FORMAL_FRAMEWORK.md` Section 1:
- **Inputs and domains** explicitly specified
- **Output / solution** formally characterized
- **Objective function** written as a mathematical expression
- **Constraints** listed
- **Problem class** identified (convex optimization, online learning, combinatorial, etc.)

No proof is meaningful without a formal problem definition. This is the foundation.

### 2.2 Definitions and Notation

- All notation must be in the notation table (`FORMAL_FRAMEWORK.md` Section 2) before first use in any proof.
- All technical terms must have a numbered definition (`FORMAL_FRAMEWORK.md` Section 3) before use in assumptions or theorems.
- Notation must be consistent across `FORMAL_FRAMEWORK.md`, the paper draft, and the code.

### 2.3 Assumptions

- Every assumption must be numbered, precisely stated, and justified in `FORMAL_FRAMEWORK.md` Section 4.
- Each assumption must document: (a) why it is reasonable, (b) whether it is necessary or merely sufficient, (c) whether it holds in the experimental setup.
- No hidden assumptions in proofs. If a proof step requires a condition, it must trace back to a listed assumption.

### 2.4 Property Identification

Before writing any theorem, identify WHAT needs to be proven:
- List all claims from the paper. Classify each: needs proof, needs experiment, or both (`FORMAL_FRAMEWORK.md` Section 5.1).
- Map your contribution type to expected property families using the lookup table (`FORMAL_FRAMEWORK.md` Section 5.2).
- Novel properties MUST be proven. Inherited properties can be cited.
- Fill the Property Inventory (`FORMAL_FRAMEWORK.md` Section 5.4) -- this is the master checklist.

### 2.5 Proof Protocol

- **Scope:** Any theorem, lemma, proposition, or corollary supporting the contribution must be in `FORMAL_FRAMEWORK.md` Section 6.
- **Structure:** Statement (referencing D{{N}}, A{{N}}) -> Proof sketch (main body) -> Full proof (appendix) -> QED.
- **Proof techniques:** Name the technique (induction, contradiction, construction, reduction, direct, probabilistic, coupling, etc.).
- **Dependencies:** Maintained in the dependency graph (`FORMAL_FRAMEWORK.md` Section 7). Must be a DAG -- no cycles.
- **Theory-experiment link:** Each theorem's `Validates hypothesis` field must point to H{{N}} in `HYPOTHESES.md`, and each hypothesis's `Formal basis` field must point back.

### 2.6 Gates

- **Implementation gate:** No implementation proceeds until the relevant proof has status >= SKETCH ONLY.
- **Submission gate:** No submission until all core results have status PROVEN. Run the checklist in `FORMAL_FRAMEWORK.md` Section 8.

### 2.7 Code Consistency

- Implementations must match the proven formulation exactly.
- Any deviation (approximation, numerical trick, discretization) requires either a new proof or a documented equivalence argument logged in `DECISIONS.md`.

## 3. Evaluation Rubric

{{Define your project's primary evaluation metric and scoring rubric here.}}

- **Primary Metric:** {{Name}} [range: {{min}} to {{max}}]
  - {{min}}: {{What this means}}
  - {{max}}: {{What this means}}
- **Evaluation Protocol:** {{How evaluation is conducted (e.g., LLM-as-Judge with CoT, human annotation, automated metrics).}}

## 4. Literature Navigation (Progressive Disclosure)

Papers are stored in `docs/references/[paper]/` with a local `CLAUDE.md` navigation map.

- **Surgical Reading:** Do not read full markdown papers. Check the `CLAUDE.md` map first.
- **Navigation:** Identify the specific section (e.g., `02_methodology.md`) and read only that file or specific line ranges.
- **Asset Check:** If a paper mentions a diagram, refer to the `assets/` folder and ask the user for visual clarification if needed.

## 5. Reviewer Mode (A* Standards)

- **Proof Completeness:** Every core claim must have a formal proof with status PROVEN before submission. Flag any SKETCH ONLY or NOT STARTED entries in `FORMAL_FRAMEWORK.md`.
- **Proof Soundness:** Check each proof for: hidden assumptions, circular dependencies, unjustified steps, and edge cases not covered. Verify the dependency graph in `FORMAL_FRAMEWORK.md` Section 7 is acyclic.
- **Property Coverage:** Every row in the Property Inventory (`FORMAL_FRAMEWORK.md` Section 5.4) must have backing. No novel property without a theorem.
- **Assumption Audit:** Are all assumptions justified? Do they hold in the experimental setup? Could a reviewer argue any are unrealistic?
- **Theory-Experiment Alignment:** Every theorem links to a hypothesis; every hypothesis with a formal basis links to a theorem. Check both directions.
- **Baseline Fairness:** Every experiment must compare against a compute-matched or resource-matched baseline.
- **Failure Attribution:** Categorize failures systematically (define a taxonomy or adopt one from literature).
- **Novelty Audit:** Periodically check `LIT_REVIEW.md` gap matrix to ensure the contribution remains distinct from existing SOTA.
