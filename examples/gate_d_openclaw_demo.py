"""
gate_d_openclaw_demo.py
Calebear Gate — Gate D: Irreversibility Guard
Compatible with OpenClaw AgentSkill pattern

Fail-Closed by default.
REV-2 (irreversible) actions require double confirmation.
No confirmation = FAIL-IRREV = HARD STOP.

ROME incident type (SSH tunnel open) is handled as REV-2.

GitHub: https://github.com/calebjangcj-hash/calebear-gate
Demo:   https://calebjangcj-hash.github.io/calebear-gate/
"""

import time
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


# ─── REV LEVEL ───────────────────────────────────────────────────────────────

class RevLevel(Enum):
    REV_0 = "FULLY_REVERSIBLE"        # Read, view — no confirmation needed
    REV_1 = "PARTIALLY_REVERSIBLE"    # Move, rename — 1x confirmation
    REV_2 = "IRREVERSIBLE"            # Delete, deploy, SSH, payment — 2x confirmation


# ─── ACTION REGISTRY (OpenClaw context) ─────────────────────────────────────

ACTION_REGISTRY: dict[str, RevLevel] = {
    # REV-0: safe reads
    "read_file":         RevLevel.REV_0,
    "list_directory":    RevLevel.REV_0,
    "search_web":        RevLevel.REV_0,
    "get_status":        RevLevel.REV_0,

    # REV-1: reversible with effort
    "write_file":        RevLevel.REV_1,
    "move_file":         RevLevel.REV_1,
    "rename_file":       RevLevel.REV_1,
    "update_config":     RevLevel.REV_1,

    # REV-2: irreversible — ROME incident types included
    "delete_file":       RevLevel.REV_2,
    "open_ssh_tunnel":   RevLevel.REV_2,   # ROME incident type
    "send_email":        RevLevel.REV_2,
    "api_payment":       RevLevel.REV_2,
    "deploy_to_prod":    RevLevel.REV_2,
    "drop_table":        RevLevel.REV_2,
    "revoke_permission": RevLevel.REV_2,
    "submit_form":       RevLevel.REV_2,
    "git_force_push":    RevLevel.REV_2,
}


# ─── LEDGER ──────────────────────────────────────────────────────────────────

@dataclass
class LedgerEntry:
    action: str
    rev_level: str
    verdict: str
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ"))
    gate: str = "GATE-D-OPS19"

_ledger: list[LedgerEntry] = []

def _record(action: str, rev: RevLevel, verdict: str) -> None:
    entry = LedgerEntry(action=action, rev_level=rev.name, verdict=verdict)
    _ledger.append(entry)
    print(f"  [LEDGER] {entry.timestamp} | {action} | {rev.name} | {verdict}")


# ─── FAIL ────────────────────────────────────────────────────────────────────

class GateDFail(Exception):
    """FAIL-IRREV: irreversible action blocked by Gate D"""


# ─── GATE D CORE ─────────────────────────────────────────────────────────────

def gate_d(action: str, *, auto_confirm: bool = False) -> bool:
    """
    Gate D — Irreversibility Guard

    Args:
        action:       action name (must be in ACTION_REGISTRY or treated as REV-2)
        auto_confirm: if True, skip human prompts (only valid for REV-0/REV-1;
                      REV-2 always requires human confirmation — Fail-Closed)

    Returns:
        True if execution is authorized.

    Raises:
        GateDFail: if action is blocked.
    """
    # Classify — unknown = REV-2 (No-Guess / Fail-Closed)
    rev = ACTION_REGISTRY.get(action)
    if rev is None:
        print(f"  [GATE-D] ⚠  Unknown action '{action}' → REV-2 (Fail-Closed)")
        rev = RevLevel.REV_2

    # ── REV-0: pass immediately ──────────────────────────────────────────────
    if rev is RevLevel.REV_0:
        print(f"  [GATE-D] ✅  {action} → REV-0 → PASS")
        _record(action, rev, "PASS")
        return True

    # ── REV-1: single confirmation ───────────────────────────────────────────
    if rev is RevLevel.REV_1:
        print(f"  [GATE-D] ⚠   {action} → REV-1 (partially reversible)")
        if auto_confirm:
            print(f"  [GATE-D] ✅  REV-1 auto-confirmed → PASS")
            _record(action, rev, "PASS-AUTO")
            return True
        confirm = input(f"  Confirm '{action}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            _record(action, rev, "PASS-CONFIRMED")
            return True
        _record(action, rev, "FAIL-USER-CANCEL")
        raise GateDFail(f"[FAIL-IRREV] '{action}' cancelled")

    # ── REV-2: double confirmation mandatory ─────────────────────────────────
    if rev is RevLevel.REV_2:
        print(f"  [GATE-D] 🚨  {action} → REV-2 (IRREVERSIBLE)")

        # auto_confirm blocked for REV-2 — always requires human
        if auto_confirm:
            _record(action, rev, "FAIL-IRREV-AUTO-BLOCKED")
            raise GateDFail(
                f"[FAIL-IRREV] '{action}' BLOCKED — "
                "REV-2 requires human confirmation. auto_confirm not permitted."
            )

        print(f"  [GATE-D] Double-confirmation required.\n")
        print(f"    Action : {action}")
        print(f"    Grade  : REV-2 — this CANNOT be undone\n")

        # Step 1 — intent
        c1 = input("  [Step 1/2] Confirm intent to execute? (yes/no): ").strip().lower()
        if c1 != "yes":
            _record(action, rev, "FAIL-STEP1-CANCEL")
            raise GateDFail(f"[FAIL-IRREV] '{action}' cancelled at Step 1")

        # Step 2 — final execution
        c2 = input("  [Step 2/2] FINAL: execute (cannot undo)? (yes/no): ").strip().lower()
        if c2 != "yes":
            _record(action, rev, "FAIL-STEP2-CANCEL")
            raise GateDFail(f"[FAIL-IRREV] '{action}' cancelled at Step 2")

        _record(action, rev, "PASS-DOUBLE-CONFIRMED")
        print(f"  [GATE-D] ✅  REV-2 double-confirmed → PASS → Gate E")
        return True


# ─── OPENCLAW AGENT SKILL WRAPPER ────────────────────────────────────────────

def openclaw_skill(action: str, payload: dict, *, auto_confirm: bool = False) -> dict:
    """
    OpenClaw AgentSkill-compatible wrapper.
    Wrap any tool call with this before execution.

    Example:
        result = openclaw_skill("delete_file", {"path": "/data/users.db"})
    """
    print(f"\n{'─' * 56}")
    print(f"  Agent action request: {action}")
    print(f"  Payload : {payload}")

    try:
        gate_d(action, auto_confirm=auto_confirm)
        # ← Real execution would happen here
        return {"status": "executed", "action": action, "payload": payload}
    except GateDFail as e:
        return {"status": "blocked", "reason": str(e), "action": action}


# ─── DEMO ─────────────────────────────────────────────────────────────────────

def run_demo() -> None:
    print("=" * 56)
    print("  Calebear Gate — Gate D Demo")
    print("  OpenClaw Execution Governance")
    print("  Fail-Closed | REV-2 = Double Confirmation")
    print("=" * 56)

    scenarios = [
        # (label, action, payload, auto_confirm)
        ("Safe read",             "read_file",       {"path": "README.md"},       True),
        ("Config update",         "update_config",   {"key": "timeout", "v": 30}, True),
        ("⚠  File delete",         "delete_file",     {"path": "/data/users.db"},  False),
        ("🚨 ROME-type SSH tunnel","open_ssh_tunnel", {"host": "external.server"},  False),
        ("🚨 Payment API trigger", "api_payment",     {"amount": 4200, "to": "X"}, False),
        ("Unknown action",         "mine_crypto",     {"wallet": "0xABC"},         False),
    ]

    results = []
    for label, action, payload, auto in scenarios:
        print(f"\n  ▶ Scenario: {label}")
        r = openclaw_skill(action, payload, auto_confirm=auto)
        results.append((label, r["status"]))

    print("\n" + "=" * 56)
    print("  GATE D SUMMARY")
    print("=" * 56)
    for label, status in results:
        icon = "✅" if status == "executed" else "🚫"
        print(f"  {icon}  {label:40s} {status.upper()}")

    print("\n  LEDGER")
    print("  " + "-" * 52)
    for e in _ledger:
        print(f"  {e.timestamp}  {e.action:<25} {e.verdict}")

    print("\n  Fail-Closed: unknown/REV-2 blocked without human sign-off.")
    print("  ROME incident prevented. Gate D — Calebear Gate.")
    print("=" * 56)


if __name__ == "__main__":
    run_demo()
