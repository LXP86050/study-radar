"""Morning email — today's blocks pulled verbatim from STUDY_PLAN.md.

Run at 6:30 AM ET via GH Actions cron (10:30 UTC EDT / 11:30 UTC EST, with hour gate).
"""
from __future__ import annotations

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import markdown

from src import email_sender, plan_parser

TARGET_HOUR_ET = 6  # 6:30 AM ET — hour check is on the hour, minute irrelevant
log = logging.getLogger("study_radar.morning")


def _is_target_hour() -> bool:
    if os.environ.get("FORCE_RUN") == "1":
        return True
    return datetime.now(ZoneInfo("America/New_York")).hour == TARGET_HOUR_ET


def build_html(day_n: int, heading: str, body_md: str, total_days: int) -> str:
    body_html = markdown.markdown(body_md, extensions=["extra"])
    et_now = datetime.now(ZoneInfo("America/New_York")).strftime("%a %b %d, %Y")
    progress_pct = int(day_n / total_days * 100)
    title = f"Study Plan — Day {day_n} of {total_days}"
    inner = f"""
        <div style="color:#666;font-size:12px;margin-bottom:14px;">
          {et_now} · {heading} · {progress_pct}% through the 30-day plan
        </div>
        {body_html}
    """
    footer = f"""
      <p style="margin-top:14px;color:#888;font-size:11px;line-height:1.5;">
        Tonight at 10pm you'll get a one-tap link to log your reflection.
        Phone in another room. App blockers on. 90 work / 10 break.
      </p>
    """
    return email_sender.base_html(title, inner, footer)


def run() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if not _is_target_hour():
        h = datetime.now(ZoneInfo("America/New_York")).hour
        log.info("skipping: ET hour is %d, target is %d", h, TARGET_HOUR_ET)
        return 0

    config = plan_parser.load_config()
    plan_text = Path(config["plan_path"]).read_text()
    found = plan_parser.todays_section(plan_text, config)

    if found is None:
        n = plan_parser.day_number(config["start_date"])
        if n < 1:
            log.info("plan hasn't started yet (day %d)", n)
            return 0
        if n > config["total_days"]:
            log.info("plan is complete (day %d)", n)
            email_sender.send_email(
                subject=f"Study Plan: complete — {config['total_days']} days done",
                html=email_sender.base_html(
                    "Study Plan complete",
                    "<p>You finished the 30-day plan. Real rest. Walk, no screens.</p>",
                ),
            )
            return 0
        log.warning("could not find Day %d section in plan", n)
        return 1

    day_n, heading, body_md = found
    et_short = datetime.now(ZoneInfo("America/New_York")).strftime("%b %d")
    subject = f"Study: Day {day_n} — {et_short}"
    html = build_html(day_n, heading, body_md, config["total_days"])
    email_sender.send_email(subject, html)
    log.info("sent Day %d email", day_n)
    return 0


if __name__ == "__main__":
    sys.exit(run())
