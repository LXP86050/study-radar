"""Shared SendGrid client. Reads SENDGRID_API_KEY / SENDER_EMAIL / RECIPIENT_EMAIL from env."""
from __future__ import annotations

import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(subject: str, html: str) -> None:
    api_key = os.environ.get("SENDGRID_API_KEY")
    sender = os.environ.get("SENDER_EMAIL")
    recipient = os.environ.get("RECIPIENT_EMAIL")
    if not (api_key and sender and recipient):
        raise RuntimeError("Missing SENDGRID_API_KEY / SENDER_EMAIL / RECIPIENT_EMAIL env vars")

    msg = Mail(from_email=sender, to_emails=recipient, subject=subject, html_content=html)
    resp = SendGridAPIClient(api_key).send(msg)
    if resp.status_code >= 300:
        raise RuntimeError(f"SendGrid send failed: HTTP {resp.status_code} {resp.body}")


def base_html(title: str, body_html: str, footer_html: str = "") -> str:
    """Wrap content in a clean, mobile-friendly email shell."""
    return f"""<!doctype html>
<html><body style="margin:0;padding:0;background:#f6f8fa;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#111;">
  <div style="max-width:680px;margin:0 auto;padding:24px;">
    <h2 style="margin:0 0 12px 0;font-size:20px;">{title}</h2>
    <div style="background:#fff;border-radius:8px;padding:18px 20px;box-shadow:0 1px 2px rgba(0,0,0,0.05);font-size:14px;line-height:1.6;">
      {body_html}
    </div>
    {footer_html}
  </div>
</body></html>"""
