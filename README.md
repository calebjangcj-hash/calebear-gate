# Calebear Gate

**Execution governance layer for AI systems. Contract before execution. Fail-Closed by default.**

Calebear Gate is a public concept-demo project for governing execution before an AI system takes action.

**No contract = no execution.**

---

## Live Demo

| Demo | URL |
|---|---|
| Execution Governance Demo (v3.1) | https://calebjangcj-hash.github.io/calebear-gate/demo/jwt-auth/ |
| Irreversibility Guard Demo (Gate D) | https://calebjangcj-hash.github.io/calebear-gate/demo/gate-d/gate_d_demo.html |
| 30-Second Business Demo | https://calebjangcj-hash.github.io/calebear-gate/demo/gate-30s-business/ |

These public demos show execution governance before action, not just generation results.

### Demo 1 — Execution Governance Demo (v3.1)

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

### Demo 2 — Irreversibility Guard Demo (Gate D)

This public demo shows how agent actions can be classified by reversibility before execution.

Current visible idea:

- **REV-0** — fully reversible actions can pass instantly
- **REV-1** — partially reversible actions require confirmation
- **REV-2** — irreversible actions require double human sign-off or are blocked

Example REV-2 actions include:

- `delete_file`
- `open_ssh_tunnel`
- `api_payment`
- `deploy_to_prod`

This demo is designed to make one point visible:

**Irreversible execution should not proceed on a single unchecked step.**

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
- require human confirmation,
- or escalate before execution.

---

## What the current demos are showing

The current public demos are intentionally simple.

They are designed to show:

- how execution can be governed before action
- how scope drift can be detected
- how auto-correction can remove out-of-scope steps
- how re-verification can happen before execution continues
- how irreversible actions can be classified before execution
- how high-risk actions can require stronger human confirmation
- how execution results can be made visible in the UI
- how fail-closed behavior can be demonstrated clearly

These are public concept demos, not production security packages.

---

## Current public scope

Current public paths:

- `demo/jwt-auth/index.html`
- `demo/gate-d/gate_d_demo.html`

Current public direction includes:

- execution governance before action
- contract-first control
- visible UI decision flow
- scope lock patterns
- re-verification before continuation
- irreversibility-aware action control
- stronger confirmation for high-risk execution
- session-close awareness
- audit-friendly execution flow

---

## Architecture direction

Calebear Gate is moving toward a broader execution-boundary model, including ideas such as:

- contract before execution
- scope lock before action
- neutral rewrite before tool use
- reversibility classification before high-risk actions
- verification before session close
- separation between research, build, and verify
- audit-friendly decision flow
- visual execution mapping

---

## Status

Current status:

- GitHub public repo created
- GitHub Pages live
- Execution Governance Demo v3.1 live
- Irreversibility Guard Demo (Gate D) live
- public concept-demo positioning aligned
- README updated to match current live direction

---

## Repository

GitHub Repo:  
https://github.com/calebjangcj-hash/calebear-gate

---

*Execution you can verify.*
