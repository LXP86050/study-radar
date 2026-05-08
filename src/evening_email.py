"""Evening email — short reflection prompt + one-tap link to add a line to daily_log.md."""
from __future__ import annotations

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from src import email_sender, plan_parser, state

TARGET_HOUR_ET = 22  # 10:00 PM ET; gate allows target±1 to tolerate GH cron delay
FORCED = os.environ.get("FORCE_RUN") == "1"
log = logging.getLogger("study_radar.evening")


def _is_target_hour() -> bool:
    if FORCED:
        return True
    h = datetime.now(ZoneInfo("America/New_York")).hour
    return abs(h - TARGET_HOUR_ET) <= 1


def build_html(day_n: int, heading: str, repo: str, log_path: str, total_days: int) -> str:
    edit_url = f"https://github.com/{repo}/edit/main/{log_path}"
    et_now = datetime.now(ZoneInfo("America/New_York")).strftime("%a %b %d, %Y")
    title = f"End of Day {day_n} — Reflection"
    inner = f"""
        <div style="color:#666;font-size:12px;margin-bottom:14px;">
          {et_now} · {heading}
        </div>
        <p style="margin-top:0;">Three sentences before you close the laptop:</p>
        <ol style="padding-left:20px;margin:8px 0 16px 0;">
          <li>What <b>clicked</b> today?</li>
          <li>What <b>didn't</b> you understand?</li>
          <li>What's tomorrow's <b>#1 priority</b>?</li>
        </ol>
        <div style="text-align:center;margin:18px 0 4px 0;">
          <a href="{edit_url}"
             style="background:#1a73e8;color:#fff;text-decoration:none;padding:11px 22px;border-radius:6px;display:inline-block;font-weight:600;font-size:14px;">
             Open daily_log.md to add today's entry
          </a>
        </div>
        <p style="font-size:12px;color:#888;text-align:center;margin:6px 0 0 0;">
          Tap the button on your phone — opens directly in the GitHub app's editor.
        </p>
    """
    footer = f"""
      <p style="margin-top:14px;color:#888;font-size:11px;line-height:1.5;">
        Day {day_n} of {total_days}. Reflection is the highest-leverage 5 minutes of the day. It compounds.
      </p>
    """
    return email_sender.base_html(title, inner, footer)


def run() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if not _is_target_hour():
        h = datetime.now(ZoneInfo("America/New_York")).hour
        log.info("skipping: ET hour is %d, target is %d±1", h, TARGET_HOUR_ET)
        return 0
    if not FORCED and state.already_sent_today():
        log.info("skipping: already sent today")
        return 0

    config = plan_parser.load_config()
    plan_text = Path(config["plan_path"]).read_text()
    found = plan_parser.todays_section(plan_text, config)
    if found is None:
        log.info("today is outside the plan range — no reflection email")
        return 0

    day_n, heading, _ = found
    et_short = datetime.now(ZoneInfo("America/New_York")).strftime("%b %d")
    subject = f"Study: End of Day {day_n} reflection — {et_short}"
    html = build_html(day_n, heading, config["github_repo"], config["log_path"], config["total_days"])
    email_sender.send_email(subject, html)
    state.mark_sent_today()
    log.info("sent end-of-day %d email", day_n)
    return 0


if __name__ == "__main__":
    sys.exit(run())
