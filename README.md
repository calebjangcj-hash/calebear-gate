# Calebear Gate

**Execution governance layer for AI systems. Contract before execution. Fail-Closed by default.**

Calebear Gate is a concept demo for checking trust conditions before execution.

No contract = no execution.

---

## Live Demo

**JWT Auth Demo**  
https://calebjangcj-hash.github.io/calebear-gate/demo/jwt-auth/

This demo shows a simple PASS / BLOCK flow:

- **PASS** — required conditions are satisfied
- **BLOCK** — required conditions are missing or invalid

---

## Why this exists

Many AI systems are optimized to continue, answer, and act.

Calebear Gate explores a different default:

**execution should not continue unless the required contract is satisfied first.**

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

This is the central rule of the demo:

**No trust condition → no execution.**

---

## Current demo scope

Current public demo includes:

- JWT-style execution gate example
- browser-based PASS / BLOCK decision flow
- visible decision result in UI
- minimal concept demonstration of fail-closed execution

Current path:
- `demo/jwt-auth/index.html`

This is a public concept demo, not a production security package.

---

## What the demo is showing

The current demo is intentionally simple.

It is designed to show:

- how execution can be gated before action
- how PASS and BLOCK can be made visible
- how fail-closed behavior can be demonstrated clearly

---

## Architecture direction

Calebear Gate is moving toward a broader execution-boundary model, including ideas such as:

- scope lock before execution
- verification before session close
- separation between research, build, and verify
- audit-friendly decision flow

---

## What comes next

Planned next steps:

- JWT auth demo refinement
- finance-gate expansion
- broader execution-contract examples
- tool scope control patterns
- session separation patterns

---

## Status

Current status:

- GitHub public repo created
- GitHub Pages live
- JWT demo deployed
- README expanded for public viewing

---

## Repository

GitHub Repo:  
https://github.com/calebjangcj-hash/calebear-gate

---

*Execution you can verify.*
