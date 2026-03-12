# Decision Log

Track architectural decisions, pivots, and rationale. Each decision gets a unique ID.

| ID | Date | Decision | Rationale | Alternatives Considered |
| :--- | :--- | :--- | :--- | :--- |

<!--
HOW TO USE:
- Log every non-trivial design choice (experimental, architectural, methodological).
- Include the rationale: why this choice over alternatives?
- Include alternatives considered and why they were rejected.
- Use Sequential Thinking MCP for complex decisions involving multiple trade-offs.
- Reference decisions by ID (e.g., "D7") in other documents and code comments.
- Decisions are immutable records. If you reverse a decision, add a new decision that supersedes it.

EXAMPLE:
| D1 | 2026-03-10 | Use 10-point strategic grid instead of 5x4 rectangular | 51% fewer calls, matched-C pair for N-vs-T decomposition, better scientific value per dollar | 5x4 rectangular (rejected: 51% more expensive, no matched-C), 3x3 grid (rejected: too few for AIC/BIC) |
| D2 | 2026-03-10 | Use last-round-only context in deliberation | Full history overflows 32K context at N=16; last-round-only is standard in debate papers | Full history (rejected: context overflow + 8x cost) |
-->
