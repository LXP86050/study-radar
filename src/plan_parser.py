"""Parse STUDY_PLAN.md and find today's day section.

The plan uses headings like:
    #### Day 1 — Fri May 8 (8h)
    - B1 — ...
    - B2 — ...

We extract from one such heading up to the next `#### ` (or the next `## `, end of file).
"""
from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

CONFIG_PATH = Path("data/config.json")
DAY_HEADING_RE = re.compile(r"^####\s+Day\s+(\d+)\s+—\s+(.+?)\s*$", re.MULTILINE)


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def today_et() -> date:
    """Today's date in Eastern Time — the schedule's frame of reference."""
    return datetime.now(ZoneInfo("America/New_York")).date()


def day_number(start_date_iso: str, on: date | None = None) -> int:
    start = date.fromisoformat(start_date_iso)
    on = on or today_et()
    return (on - start).days + 1


def find_day_section(plan_text: str, day_n: int) -> tuple[str, str] | None:
    """Return (heading, body_markdown) for `#### Day {day_n} —` or None if not found.

    Body is the lines from after the heading up to the next `#### ` or `## ` heading.
    """
    matches = list(DAY_HEADING_RE.finditer(plan_text))
    target = next((m for m in matches if int(m.group(1)) == day_n), None)
    if target is None:
        return None
    start = target.end()
    # End is next #### heading or next ## heading
    end = len(plan_text)
    for m in matches:
        if m.start() > target.end():
            end = m.start()
            break
    # Also clamp at next "## " section
    section_end_re = re.compile(r"^##\s", re.MULTILINE)
    sec = section_end_re.search(plan_text, start)
    if sec and sec.start() < end:
        end = sec.start()
    body = plan_text[start:end].strip()
    heading = target.group(0).lstrip("# ").strip()  # "Day 1 — Fri May 8 (8h)"
    return heading, body


def todays_section(plan_text: str, config: dict) -> tuple[int, str, str] | None:
    """Returns (day_n, heading, body) for today's section, or None if out of range."""
    n = day_number(config["start_date"])
    if n < 1 or n > config["total_days"]:
        return None
    found = find_day_section(plan_text, n)
    if found is None:
        return None
    return n, found[0], found[1]
