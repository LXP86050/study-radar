# Study Radar

Daily two-email pipeline driving my 30-day SWE-interview prep against [`STUDY_PLAN.md`](STUDY_PLAN.md). No LLM calls, no recurring AI cost — just deterministic markdown parsing + SendGrid.

```
                               ┌────────────────────┐
6:30 AM ET cron ──► extract ──►│ today's day in     │── SendGrid ──► inbox
                               │ STUDY_PLAN.md      │
                               └────────────────────┘

                               ┌────────────────────┐
10:00 PM ET cron ─► render ──►│ reflection prompt  │── SendGrid ──► inbox
                               │ + GH-edit deeplink │
                               └────────────────────┘
                                          │ tap
                                          ▼
                                    edit daily_log.md in GitHub mobile / web
```

## Files

| path | role |
| --- | --- |
| `STUDY_PLAN.md` | the 30-day plan, day-by-day, with chapter sections + LC numbers |
| `daily_log.md` | end-of-day reflection — appended via the evening email's edit link |
| `data/config.json` | start date, total days, repo slug for edit links |
| `src/plan_parser.py` | finds today's `#### Day N — …` section |
| `src/morning_email.py` | sends today's blocks at 6:30 AM ET |
| `src/evening_email.py` | sends reflection prompt at 10 PM ET |
| `src/email_sender.py` | shared SendGrid wrapper + email shell |
| `.github/workflows/morning.yml` | 10:30 / 11:30 UTC crons → morning_email.py |
| `.github/workflows/evening.yml` | 02:00 / 03:00 UTC crons → evening_email.py |

## DST handling

GitHub Actions cron runs in UTC. To keep the emails landing at exactly 6:30 AM and 10:00 PM Eastern year-round, each workflow has two cron entries (one per DST half-year), and the script gates on the actual ET hour so only the correct one sends.

## Tuning

- **Edit the plan:** open `STUDY_PLAN.md` directly. The next morning email will reflect the change.
- **Slip the schedule:** if you fall behind, change `start_date` in `data/config.json` to push everything forward.
- **Stop the morning emails for a day:** disable the workflow temporarily in *Actions → Morning Study Email → ⋯ → Disable workflow*.

## Manual trigger

```bash
gh -R LXP86050/study-radar workflow run "Morning Study Email" -f force=true
gh -R LXP86050/study-radar workflow run "Evening Reflection Email" -f force=true
```

`force=true` bypasses the hour gate so it sends immediately regardless of the time of day.
