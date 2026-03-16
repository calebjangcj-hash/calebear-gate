# Calebear Gate

**Execution governance layer for AI systems. Contract before execution. Fail-Closed by default.**

Calebear Gate is a public concept-demo project for checking trust conditions before execution.

**No contract = no execution.**

---

## Live Demo

| Demo | URL |
|---|---|
| JWT Auth + ROME Gate | https://calebjangcj-hash.github.io/calebear-gate/demo/jwt-auth/ |
| Gate Flow (E5→E8) | https://calebjangcj-hash.github.io/calebear-gate/demo/gate-flow/ |
| 4CASE Interactive | Coming next |

These demos show simple **PASS / BLOCK** flows:

- **PASS** — required conditions are satisfied
- **BLOCK** — required conditions are missing, invalid, or out of scope

---

## Why this exists

Many AI systems are optimized to continue, answer, and act.

Calebear Gate explores a different default:

**Execution should not continue unless the required contract is satisfied first.**

The goal is not to make AI sound smarter.  
The goal is to make execution more controllable, inspectable, and fail-closed.

---

## Core idea

Before execution, the system checks whether the required conditions are met.

Instead of asking:
- "Can the system continue?"

It asks:
- "Has the system satisfied the contract to continue?"

If not, execution stops.

---

## PASS / BLOCK

### PASS
Execution is allowed because the required condition is satisfied.

### BLOCK
Execution is denied because the condition is missing, invalid, or out of scope.

This is the central rule of the project:

**No trust condition → no execution.**

---

## Current demo scope

Current public demos include:

- JWT-style execution gate example
- ROME-framed execution boundary example
- Gate Flow visual UX for E5→E8 understanding
- browser-based PASS / BLOCK decision flow
- visible execution decision in UI
- minimal concept demonstrations of fail-closed execution

Current public paths:
- `demo/jwt-auth/index.html`
- `demo/gate-flow/index.html`

These are public concept demos, not production security packages.

---

## What the demos are showing

The current demos are intentionally simple.

They are designed to show:

- how execution can be gated before action
- how PASS and BLOCK can be made visible
- how fail-closed behavior can be demonstrated clearly
- how execution flow can be understood visually before deeper implementation

---

## Architecture direction

Calebear Gate is moving toward a broader execution-boundary model, including ideas such as:

- scope lock before execution
- verification before session close
- separation between research, build, and verify
- audit-friendly decision flow
- visual execution mapping
- contract-first agent control

---

## What comes next

Planned next steps:

- JWT auth demo refinement
- Gate Flow refinement
- 4CASE Interactive demo
- finance-gate expansion
- broader execution-contract examples
- tool scope control patterns
- session separation patterns

---

## Status

Current status:

- GitHub public repo created
- GitHub Pages live
- JWT Auth + ROME Gate demo published
- Gate Flow demo being added
- README expanded for public viewing

---

## Repository

GitHub Repo:  
https://github.com/calebjangcj-hash/calebear-gate

---

*Execution you can verify.*
