# Calebear Gate

**Execution governance layer for AI systems. Contract before execution. Fail-Closed by default.**

Calebear Gate is a public concept-demo project for governing execution before an AI system takes action.

**No contract = no execution.**

---

## Live Demo

| Demo | URL |
|---|---|
| Execution Governance Demo (v3.1) | https://calebjangcj-hash.github.io/calebear-gate/demo/jwt-auth/ |

This public demo shows an execution-governance flow, not just a generation result.

Current visible flow:

- **E5** — compress context
- **E6** — rewrite into neutral contract form
- **E7** — lock TASK + VERIFY
- **AUTO-CORRECT** — remove out-of-scope execution
- **RE-VERIFY** — check corrected contract again
- **E8** — close with visible execution result

Possible visible outcomes include:

- **PASS** — execution is allowed
- **CORRECT** — execution is adjusted and re-verified
- **ESCALATE** — execution requires higher review
- **DENY / CANCEL** — execution does not continue

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

If not, the system does not proceed as-is.

It may:

- stop,
- correct the scope,
- require re-verification,
- or escalate before execution.

---

## What the current demo is showing

The current public demo is intentionally simple.

It is designed to show:

- how execution can be governed before action
- how scope drift can be detected
- how auto-correction can remove out-of-scope steps
- how re-verification can happen before execution continues
- how execution results can be made visible in the UI
- how fail-closed behavior can be demonstrated clearly

This is a public concept demo, not a production security package.

---

## Current public scope

Current public path:

- `demo/jwt-auth/index.html`

Current demo direction includes:

- execution governance before action
- contract-first control
- visible UI decision flow
- scope lock patterns
- re-verification before continuation
- session-close awareness
- audit-friendly execution flow

---

## Architecture direction

Calebear Gate is moving toward a broader execution-boundary model, including ideas such as:

- contract before execution
- scope lock before action
- neutral rewrite before tool use
- verification before session close
- separation between research, build, and verify
- audit-friendly decision flow
- visual execution mapping

---

## Status

Current status:

- GitHub public repo created
- GitHub Pages live
- Execution Governance Demo v3.1 prepared for launch
- public concept-demo positioning aligned
- README updated to match current live direction

---

## Repository

GitHub Repo:  
https://github.com/calebjangcj-hash/calebear-gate

---

*Execution you can verify.*
