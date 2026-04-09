# Formal Framework

All formal theoretical content lives here. This file mirrors the Preliminaries + Theory sections of an A* conference paper or Q1 journal article.

**Rule:** No implementation proceeds without at least a proof sketch. No submission without all core results PROVEN.

---

## 1. Problem Definition

### 1.1 Informal Statement

{{One paragraph: what problem are you solving, in plain language?}}

### 1.2 Formal Problem Statement

{{State the problem as an optimization, decision, or learning problem. Be precise about inputs, outputs, and objective.}}

**Given:** {{Inputs and their domains, e.g., a dataset D = {(x_i, y_i)}_{i=1}^{n}, a model class F, ...}}

**Find:** {{What the solution looks like, e.g., f* in F that minimizes/maximizes...}}

**Subject to:** {{Constraints, e.g., computational budget, fairness constraints, ...}}

**Objective:**

$${{Mathematical objective function}}$$

### 1.3 Problem Class

{{Classification: convex/non-convex optimization, combinatorial, online learning, statistical estimation, etc.}}

**Known complexity:** {{If applicable: NP-hard, PSPACE-complete, polynomial, etc. Cite source.}}

---

## 2. Notation

Keep this table current. All symbols used in definitions, assumptions, and proofs must appear here.

| Symbol | Meaning | Domain / Type |
| :--- | :--- | :--- |
| {{x}} | {{Description}} | {{e.g., R^d}} |
| {{f}} | {{Description}} | {{e.g., F -> R}} |

<!--
Add notation as you develop the framework. Reviewers flag inconsistent notation.
Alphabetical or by-section ordering both work -- pick one and stick with it.
-->

---

## 3. Definitions

Numbered definitions that proofs and theorems rely on. Each definition should be precise enough that a reader can verify whether a concrete example satisfies it.

### Definition D1: {{Name}}

{{Precise mathematical definition.}}

**Intuition:** {{1-2 sentences: what does this mean informally?}}

---

### Definition D2: {{Name}}

{{Precise mathematical definition.}}

**Intuition:** {{Informal explanation.}}

---

<!--
TEMPLATE:

### Definition D{{N}}: {{Name}}

{{Precise mathematical definition.}}

**Intuition:** {{Informal explanation.}}
-->

---

## 4. Assumptions

Numbered assumptions your theoretical results rely on. Each must be justified.

### Assumption A1: {{Name}}

{{Precise mathematical statement.}}

**Justification:** {{Why is this reasonable? Is it standard in the field? Cite precedent if possible.}}

**Necessity:** {{Is this assumption necessary, or just sufficient? Can it be relaxed?}}

**Holds in experiments:** {{YES / NO / APPROXIMATELY -- explain.}}

---

### Assumption A2: {{Name}}

{{Precise mathematical statement.}}

**Justification:** {{Why reasonable.}}

**Necessity:** {{Necessary or sufficient.}}

**Holds in experiments:** {{YES / NO / APPROXIMATELY.}}

---

<!--
TEMPLATE:

### Assumption A{{N}}: {{Name}}

{{Precise mathematical statement.}}

**Justification:** {{Why reasonable. Cite precedent.}}

**Necessity:** {{Necessary or sufficient? Can it be relaxed?}}

**Holds in experiments:** {{YES / NO / APPROXIMATELY.}}
-->

---

## 5. Property Identification

Before writing any theorem, identify WHAT needs to be proven. The properties you prove depend on the type of contribution you are making.

### 5.1 Claim Inventory

List every claim from your abstract and introduction. Classify each as needing a formal proof, empirical validation, or both.

| # | Claim (from paper) | Needs Proof? | Needs Experiment? | Property Type | Backing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | {{e.g., "Our method converges at rate O(1/sqrt(T))"}} | YES | YES | Convergence rate | T{{N}} + H{{N}} |
| 2 | {{e.g., "Our method outperforms baseline X on dataset Y"}} | NO | YES | -- | H{{N}} |
| 3 | {{e.g., "The problem is NP-hard"}} | YES | NO | Complexity | T{{N}} |

### 5.2 Contribution Type to Property Map

Use this lookup table to identify which properties your contribution type typically requires.

| Contribution Type | Properties to Prove | Common Proof Techniques |
| :--- | :--- | :--- |
| **New algorithm** | Correctness, termination, time/space complexity | Loop invariants, induction, reduction |
| **New optimization method** | Convergence, convergence rate, (optimality) | Descent lemma, Lyapunov function, contraction mapping |
| **New learning algorithm** | Generalization bound, sample complexity | Rademacher complexity, VC dimension, PAC-Bayes, covering numbers |
| **New online/bandit algorithm** | Regret bound, (minimax optimality) | Potential function, confidence bounds, martingale |
| **New approximation algorithm** | Approximation ratio, (inapproximability) | Greedy analysis, LP relaxation, primal-dual, reduction |
| **Hardness / impossibility result** | Lower bound, NP-hardness, impossibility | Reduction from known hard problem, information-theoretic argument |
| **New framework / formalization** | Soundness, completeness, expressiveness | Structural induction, model theory, encoding |
| **Privacy mechanism** | Privacy guarantee (epsilon,delta)-DP | Composition theorems, sensitivity analysis, moments accountant |
| **Robustness method** | Certified radius, stability bound | Lipschitz analysis, randomized smoothing |
| **New loss / objective function** | Convexity, Fisher consistency, calibration | Hessian analysis, surrogate bounds |
| **Distributed / federated method** | Communication complexity, convergence under heterogeneity | Compression bounds, variance reduction |
| **New representation / embedding** | Expressiveness, distortion bounds, invariance | Covering dimension, algebraic arguments |
| **Game-theoretic method** | Equilibrium existence, price of anarchy, convergence to equilibrium | Fixed-point theorems, potential game arguments |

Most A* papers prove multiple property types. A new optimization method might prove convergence rate AND generalization bound.

### 5.3 Identification Process

Follow these steps to build your property inventory:

**Step 1: List all claims.** Extract every "we show...", "we prove...", "we achieve...", "we guarantee..." from the abstract and introduction. Fill in the Claim Inventory table (5.1).

**Step 2: Classify your contribution type.** Look up your type(s) in the map (5.2). This tells you which property families are expected.

**Step 3: Identify your novel properties.** What distinguishes your approach from prior work? The distinguishing property MUST be proven -- this is the core of your contribution and what reviewers scrutinize hardest.

**Step 4: Separate prove vs. cite.** If a property was already proven in prior work and you use it unchanged, cite it. Only prove properties that are new or that you modify.

**Step 5: Identify supporting results.** For each main theorem, ask: what intermediate facts (lemmas) are needed? Are there existing results to cite, or do you need new lemmas?

### 5.4 Property Inventory

The master checklist connecting claims to proofs and experiments. Every row must have backing before submission.

| ID | Property | Type | Novel? | Theorem | Hypothesis | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P1 | {{e.g., Convergence rate O(1/sqrt(T))}} | Convergence | YES | T1 | H1 | NOT STARTED |
| P2 | {{e.g., NP-hardness of general case}} | Complexity | YES | T2 | -- | NOT STARTED |
| P3 | {{e.g., Outperforms baseline on benchmark}} | Empirical | NO | -- | H2 | NOT STARTED |

<!--
Status: NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED / CITED (for inherited results)
Novel: YES = you prove it. NO = cite prior work. EXTENDED = you adapt a prior proof.
-->

---

## 6. Theoretical Results

Ordered by dependency: lemmas first, then theorems, then corollaries. Each result has a proof sketch (for the paper's main body) and a full proof (for the appendix).

### Lemma L1: {{Name}}

**Statement:** {{Precise statement, referencing definitions D{{N}} and assumptions A{{N}}.}}

**Uses:** D{{N}}, A{{N}}

**Proof technique:** {{induction / contradiction / construction / reduction / direct / probabilistic / coupling / etc.}}

**Proof sketch:**
{{2-5 sentences capturing the key insight. This goes in the main body of the paper.}}

**Full proof:**
{{Complete, rigorous, step-by-step proof. Every step follows from a named rule, definition, assumption, or prior result. This goes in the appendix.}}

*Proof.* {{Step-by-step...}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED

---

### Theorem T1: {{Main Result Name}}

**Statement:** {{Precise statement. This is the core theoretical contribution.}}

**Uses:** D{{N}}, A{{N}}, L{{N}}

**Proof technique:** {{Name the technique.}}

**Proof sketch:**
{{Key insight for main body.}}

**Full proof:**

*Proof.* {{Step-by-step...}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED

**Validates hypothesis:** H{{N}} in `HYPOTHESES.md`

---

### Corollary C1: {{Name}}

**Statement:** {{Follows directly from T{{N}}.}}

**Uses:** T{{N}}

**Proof:** {{Brief derivation.}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED

---

<!--
TEMPLATES:

### Lemma L{{N}}: {{Name}}

**Statement:** {{Precise statement.}}

**Uses:** {{D/A/L references}}

**Proof technique:** {{Name.}}

**Proof sketch:** {{Key insight.}}

**Full proof:**

*Proof.* {{Steps.}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED

---

### Theorem T{{N}}: {{Name}}

**Statement:** {{Precise statement.}}

**Uses:** {{D/A/L references}}

**Proof technique:** {{Name.}}

**Proof sketch:** {{Key insight.}}

**Full proof:**

*Proof.* {{Steps.}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED

**Validates hypothesis:** H{{N}}

---

### Corollary C{{N}}: {{Name}}

**Statement:** {{Follows from T{{N}}.}}

**Uses:** {{T references}}

**Proof:** {{Derivation.}} $\square$

**Status:** NOT STARTED / SKETCH ONLY / PROVEN / VERIFIED
-->

---

## 7. Dependency Graph

Text-based DAG showing the logical structure. Update as results are added.

```
D1, D2       (Definitions)
  |
A1, A2       (Assumptions)
  |
  v
L1           (Lemma: uses D1, A1)
  |
  v
T1           (Theorem: uses L1, A2)    --> validates H1
  |
  v
C1           (Corollary: uses T1)      --> validates H2
```

**Cycle check:** The graph above must be a DAG. If you find a cycle, one of the dependencies is wrong.

---

## 8. Pre-Submission Proof Checklist

Run this before submitting to any venue.

### Property Coverage
- [ ] Every claim in the Claim Inventory (Section 5.1) has backing: a theorem, a hypothesis, or both
- [ ] Every row in the Property Inventory (Section 5.4) has status PROVEN, VERIFIED, or CITED
- [ ] No property with Novel=YES is missing a theorem

### Completeness
- [ ] Every core claim in the paper has a corresponding result (L/T/C) in this file
- [ ] Every result has status PROVEN or VERIFIED
- [ ] No SKETCH ONLY or NOT STARTED results remain for core claims

### Soundness
- [ ] All variables and notation defined in Section 2 before first use in proofs
- [ ] Each proof step follows from a named rule, definition, assumption, or prior result
- [ ] No circular dependencies in the dependency graph (Section 7)
- [ ] Edge cases and boundary conditions addressed in each proof
- [ ] Proof techniques correctly named and applied

### Assumptions
- [ ] All assumptions listed in Section 4
- [ ] Each assumption has a justification (standard in field, or argued from problem structure)
- [ ] Each assumption marked as holding (or approximately holding) in the experimental setup
- [ ] No hidden assumptions in proofs that are not in Section 4

### Theory-Experiment Alignment
- [ ] Each theorem's "Validates hypothesis" field points to the correct H{{N}} in HYPOTHESES.md
- [ ] Each hypothesis in HYPOTHESES.md has a "Formal basis" pointing back to the correct T{{N}}
- [ ] Implementation in code matches the proven formulation exactly
- [ ] Any implementation deviation has a documented equivalence argument

### Paper Structure
- [ ] Proof sketches are suitable for the main body (concise, convey key insight)
- [ ] Full proofs are suitable for the appendix (complete, no gaps)
- [ ] Notation is consistent between this file, the paper draft, and the code
