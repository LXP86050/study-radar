"""Per-workflow once-per-day dedup so a delayed second cron firing doesn't double-send.

Stored as plain text files committed back by each workflow's "Commit updated state" step.
"""
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

STATE_DIR = Path(os.environ.get("STATE_DIR", "state/morning"))


def _today_et() -> str:
    return datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")


def already_sent_today() -> bool:
    p = STATE_DIR / "last_run_date.txt"
    if not p.exists():
        return False
    return p.read_text().strip() == _today_et()


def mark_sent_today() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    (STATE_DIR / "last_run_date.txt").write_text(_today_et())
