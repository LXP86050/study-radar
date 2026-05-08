# 30-Day SWE Interview Plan

**Start: Friday, May 8, 2026 · End: Saturday, June 6, 2026**

Source: *The SWE Interview Handbook* (your book). This plan converts Chapter 11's weekly skeleton into a day-by-day schedule fitted to your hours: **Mon–Thu 4.5h · Fri 8h · Sat–Sun 10h** (~46 hrs/week, ~202 hrs total).

## How to use this plan

- **One block = 90 minutes deep work + 10 min break.** Phone in another room. App blockers on. The 90/10 rhythm is non-negotiable — your brain doesn't get smarter past 90 min, it gets stupider.
- **Lunch** on long days = 45–60 min, away from a screen.
- **End-of-day reflection** (5 min in a notes file): *what clicked, what didn't, what tomorrow's #1 priority is.* This is the single highest-ROI 5 minutes of your day.
- **If you fall behind:** don't extend hours. Drop low-priority items in the current day (Linux drills, English Ch 10 work, second-pass review) before you cut DSA or the RAG project.
- **Code along.** The book says it; it's true. Re-type every code block in §1, §4, §6. Reading is not learning.

---

## Weekly milestones

| Week | Dates | Theme | DSA target | Other deliverables |
|------|-------|-------|---------:|---|
| 1 | Fri May 8 – Thu May 14 | Python · Code Readability · Linux · Hashing | ~22 LC | Resume v1, dev env set up |
| 2 | Fri May 15 – Thu May 21 | Two ptr · Sliding · Stack · BS · LL · Trees · Heap · System Design · STAR | ~30 LC | TinyURL + Newsfeed whiteboarded, all 8 STAR stories drafted |
| 3 | Fri May 22 – Thu May 28 | Backtracking · Graphs · 1D DP · Greedy · **AI/RAG project** · SRE · first mocks | ~25 LC | RAG project deployed + on resume |
| 4 | Fri May 29 – Sat Jun 6 | Mocks · weak-area · Resume v2 · apply | ~20 LC | Resume v2, 10 mocks, 50+ applications |

Cumulative LC: ~95–100 problems. One AI/RAG project shipped. ~10 mocks. ~50 applications.

---

## Day-by-day

> **Convention:** weekdays assume 18:30–23:00 (after Infosys), Fri 09:00–18:00, Sat–Sun 09:00–20:00. Shift to your actual rhythm — what matters is the duration, not the clock.

### Week 1 — Foundations (May 8–14)

#### Day 1 — Fri May 8 (8h)
- B1 — Read **Ch 1 Python §1.1–1.5** (data types, control flow, functions, comprehensions, classes). Re-type every example.
- B2 — Read **Ch 1 §1.6–1.8** (idioms, built-ins, generators). Solve **§1.10 #1** (frequency counter), **#2** (group anagrams), **#3** (two sum) cold.
- Lunch
- B3 — Read **Ch 2 §2.1–2.5** (naming, length, comments, guard clauses, three-reads). Refactor any old Python file of yours through this lens.
- B4 — Read **Ch 2 §2.6–2.8** (code-reading protocol + bug checklist + walkthroughs A, B, C). Do them out loud.
- B5 — LC **1 (Two Sum)**, **217 (Contains Duplicate)**, **242 (Valid Anagram)** — solve cold.
- B6 — Set up your study workspace: dev env, IDE, LeetCode account, `daily_log.md` notes file, app blockers installed. Reflection.

#### Day 2 — Sat May 9 (10h)
- B1 — **Ch 2 §2.9–2.10** + Drill 1 (have an LLM quiz you on a solution you wrote yesterday).
- B2 — **Ch 3 Linux §3.1–3.4** (FS, file ops, permissions, pipes/text). Type every command, don't just read.
- B3 — **Ch 3 §3.5–3.7** (processes, networking, shell scripting). Do **§3.9 practice tasks** both.
- Lunch
- B4 — LC **49 (Group Anagrams)**, **347 (Top K Frequent)**.
- B5 — LC **128 (Longest Consecutive)**, **219 (Contains Duplicate II)**.
- B6 — **Ch 8 (Resume) §8.1–8.4** read. Start Resume v1 draft using the bullet formula.
- B7 — Resume v1: write 3–5 quantified bullets per role. Use action verbs from §8.3.
- Reflection.

#### Day 3 — Sun May 10 (10h)
- B1 — **Ch 4 §4.1 (Big-O) + §4.2 (Hashing)**. Memorize the built-in complexity table.
- B2 — LC **1748 (Sum of Unique Elements)**, **1207 (Unique Number of Occurrences)**, **2225 (Find Players With Zero/One Losses)** — multi-counter pattern.
- B3 — **Ch 4 §4.3 (Two Pointers)**.
- Lunch
- B4 — LC **167 (Two Sum II)**, **125 (Valid Palindrome)**.
- B5 — LC **15 (3Sum)**, **11 (Container With Most Water)**.
- B6 — **Ch 4 §4.4 (Sliding Window)** read fully. LC **3 (Longest Substring Without Repeats)**.
- B7 — Resume v1 polish — sleep on it overnight.
- Reflection.

#### Day 4 — Mon May 11 (4.5h)
- B1 — LC **121 (Best Time to Buy/Sell Stock)**, **424 (Longest Repeating Char Replacement)**.
- B2 — LC **76 (Min Window Substring — hard, 45m timebox)**.
- B3 — **Ch 4 §4.5 (Stack)**. LC **20 (Valid Parens)**, **155 (Min Stack)**.
- Reflection.

#### Day 5 — Tue May 12 (4.5h)
- B1 — LC **150 (RPN)**, **739 (Daily Temperatures)** — monotonic stack, master this template.
- B2 — **Ch 4 §4.6 (Binary Search)**. Memorize *both* templates.
- B3 — LC **704 (Binary Search)**, **33 (Search Rotated Sorted)**.
- Reflection.

#### Day 6 — Wed May 13 (4.5h)
- B1 — LC **153 (Find Min in Rotated)**, **875 (Koko Eating Bananas)** — binary search on the answer.
- B2 — **Ch 4 §4.7 (Linked List)**. Re-type the templates.
- B3 — LC **206 (Reverse LL)**, **21 (Merge Two Sorted)**, **141 (Cycle Detect)**.
- Reflection.

#### Day 7 — Thu May 14 (4.5h)
- B1 — LC **19 (Remove Nth From End)**, **143 (Reorder List)**.
- B2 — **Ch 4 §4.8 (Trees)**. Memorize the 4 traversals — write each from scratch on paper.
- B3 — LC **226 (Invert Tree)**, **100 (Same Tree)**, **104 (Max Depth)**.
- Reflection.

---

### Week 2 — Patterns + System Design (May 15–21)

#### Day 8 — Fri May 15 (8h)
- B1 — LC **543 (Diameter)**, **110 (Balanced)**, **98 (Validate BST)** — the hidden-range pattern.
- B2 — LC **102 (Level Order)**, **199 (Right Side View)**.
- Lunch
- B3 — LC **235 (LCA in BST)**, **236 (LCA in Binary Tree)**.
- B4 — **Ch 4 §4.9 (Heap)**.
- B5 — LC **215 (Kth Largest)**, **295 (Median From Stream)** — two-heap, must master.
- B6 — LC **23 (Merge K Sorted Lists)**.
- Reflection.

#### Day 9 — Sat May 16 (10h)
- B1 — **Ch 5 §5.1–5.2** (interview framework + numbers). Memorize the latency table.
- B2 — **Ch 5 §5.3–5.4** (building blocks + CAP). Draw §5.3 diagrams from memory.
- B3 — **Ch 5 §5.5 (Scaling)** + **§5.6 (TinyURL walkthrough)**.
- Lunch
- B4 — Whiteboard TinyURL solo on paper, all 8 framework steps. Time yourself: 45 min.
- B5 — **Ch 5 §5.7 (Rate Limiter)** + **§5.8 (News Feed walkthrough)**.
- B6 — Whiteboard News Feed solo. Force yourself to articulate the fan-out tradeoff out loud.
- B7 — **Ch 5 §5.9–5.10** + LC review: pick 2 problems from W1 that felt hard, re-solve cold.
- Reflection.

#### Day 10 — Sun May 17 (10h)
- B1 — **Ch 9 §9.1–9.3** (STAR + 8 stories + sample failure answer).
- B2 — Draft **Stories 1–4** as 6-bullet index cards: Conflict, Failure, Leadership, Ambiguity. Real specifics, real numbers.
- B3 — Draft **Stories 5–6**: Tight Deadline, Learning Fast.
- Lunch
- B4 — Draft **Stories 7–8**: Disagreement w/ Manager, Proudest Achievement.
- B5 — **Ch 9 §9.4–9.7** (hard prompts, questions to ask, day-of mechanics). Practice "tell me about yourself" out loud, 5x.
- B6 — LC **230 (Kth Smallest BST)**, **297 (Serialize/Deserialize Tree — hard, 45m timebox)**.
- B7 — LC **124 (Max Path Sum — tree DP, hard, 45m timebox)**.
- Reflection.

#### Day 11 — Mon May 18 (4.5h)
- B1 — **Ch 4 §4.10 (Graphs)**. Memorize BFS + DFS templates.
- B2 — LC **200 (Number of Islands)**, **133 (Clone Graph)**.
- B3 — LC **207 (Course Schedule)** — topo sort.
- Reflection.

#### Day 12 — Tue May 19 (4.5h)
- B1 — LC **417 (Pacific Atlantic)**.
- B2 — LC **127 (Word Ladder — BFS shortest path, 45m timebox)**.
- B3 — LC **994 (Rotting Oranges)** — multi-source BFS. Recheck bug-spotting checklist.
- Reflection.

#### Day 13 — Wed May 20 (4.5h)
- B1 — **Ch 4 §4.11 (Backtracking)**. Memorize template.
- B2 — LC **78 (Subsets)**, **46 (Permutations)**.
- B3 — LC **39 (Combination Sum)**, **79 (Word Search)**.
- Reflection.

#### Day 14 — Thu May 21 (4.5h)
- B1 — **Ch 4 §4.12 (1D DP)**.
- B2 — LC **70 (Climbing Stairs)**, **198 (House Robber)**, **213 (House Robber II)**.
- B3 — LC **300 (Longest Increasing Subsequence)**.
- Reflection.

---

### Week 3 — AI/RAG Project + SRE + First Mocks (May 22–28)

#### Day 15 — Fri May 22 (8h)
- B1 — **Ch 6 §6.1–6.3** (LLM basics, prompting, RAG architecture).
- B2 — **Ch 6 §6.4** read carefully. Get an Anthropic API key. Set up project repo + venv. Install `chromadb`, `anthropic`.
- B3 — Implement chunking + indexing using your own markdown notes (the PDF, or 10–20 of your notes).
- Lunch
- B4 — Implement the `rag_answer` query loop. End-to-end test with one question.
- B5 — Build a **20-question eval set** against your dataset. Hand-label expected answers.
- B6 — Run the eval, log scores, identify failure modes (this is your baseline number).
- Reflection.

#### Day 16 — Sat May 23 (10h)
- B1 — **Ch 6 §6.5 (RAG failure modes)**. Map your eval failures to the table.
- B2 — Add **hybrid search** (BM25 + vector). Use `rank_bm25`, simple weighted score.
- B3 — Re-run eval. Confirm lift. Note the before/after numbers (resume bullet).
- Lunch
- B4 — Add a **reranker** (Cohere Rerank free tier or local cross-encoder).
- B5 — Re-run eval. Note new numbers.
- B6 — LC **322 (Coin Change)**, **139 (Word Break)**.
- B7 — LC review weak DP: re-solve LIS or Coin Change cold.
- Reflection.

#### Day 17 — Sun May 24 (10h)
- B1 — **Ch 6 §6.6–6.7** (agents + design principles).
- B2 — Add a tool-calling loop that decides "search docs vs general answer". Test 3 cases.
- B3 — Wrap as FastAPI endpoint `POST /ask`. Test 5 queries locally.
- Lunch
- B4 — **Ch 4 §4.13 (Greedy)**. LC **55 (Jump Game)**, **45 (Jump Game II)**.
- B5 — LC **435 (Non-overlapping Intervals)** — interval scheduling.
- B6 — **Ch 4 §4.14–4.15** (interview strategy, what to skip). Apply §4.14 script to 1 LC out loud.
- B7 — Project polish: README with usage, env-var config, error messages.
- Reflection.

#### Day 18 — Mon May 25 (4.5h)
- B1 — Deploy the RAG project on **Modal** or **Render**. Write the deploy doc as you go.
- B2 — Hit the live endpoint from a fresh browser/incognito; debug whatever breaks.
- B3 — Add the project to your resume (4 bullets per **§8.4** template). Use the actual numbers from your eval.
- Reflection.

#### Day 19 — Tue May 26 (4.5h)
- B1 — **Ch 7 §7.1–7.4** (SLI/SLO/SLA, error budgets, observability triad, four golden signals).
- B2 — **Ch 7 §7.5–7.7** (incidents, on-call, reliability patterns).
- B3 — **Ch 7 §7.8–7.9** (SRE agents, what to skip). LC review: 1 graph problem cold.
- Reflection.

#### Day 20 — Wed May 27 (4.5h)
- B1 — **Mock #1: DSA**. Pramp / Interviewing.io / a friend. Pick a problem you haven't seen.
- B2 — Postmortem the mock: what 3 things to improve. Start `MOCK_LOG.md`.
- B3 — LC review: re-solve 2 hard problems cold.
- Reflection.

#### Day 21 — Thu May 28 (4.5h)
- B1 — **Mock #2: System Design** (TinyURL or Rate Limiter variant).
- B2 — Postmortem + targeted re-read of weak Ch 5 sections.
- B3 — Apply to **5 companies** from your job-radar emails. Tailor each in 10 min.
- Reflection.

---

### Week 4 — Mocks · Polish · Apply (May 29 – Jun 6)

#### Day 22 — Fri May 29 (8h)
- B1 — **Mock #3: DSA** — medium tree problem.
- B2 — Postmortem.
- B3 — **Ch 8 §8.5–8.8** (ATS rules + tailor pass). Apply to your v1.
- Lunch
- B4 — Resume v2 polish: cut filler, quantify every bullet, ATS-test (paste into a free ATS scanner).
- B5 — LinkedIn polish: headline, About, Featured (link the RAG project).
- B6 — Application sprint #1: **10 companies**, tailored.
- Reflection.

#### Day 23 — Sat May 30 (10h)
- B1 — **Mock #4: Behavioral**, 5 prompts. Speak from memory; don't read the cards.
- B2 — Refine your 2 weakest stories. Re-record on video at 1.5x; note filler words.
- B3 — **Mock #5: DSA** — medium graph.
- Lunch
- B4 — Postmortems for both mocks.
- B5 — Application sprint #2: **15 more companies** from the IT Radar list.
- B6 — LC weak-area: 2 sliding-window or hashing problems you skipped earlier.
- B7 — Cheat-sheet review: read **Ch 11 §11.2–§11.5** aloud. Tape to wall.
- Reflection.

#### Day 24 — Sun May 31 (10h)
- B1 — **Mock #6: System Design** (News Feed variant).
- B2 — **Ch 10 (English & Communication)** full read. Pick 3 tactics to enforce next mock.
- B3 — LC: backtracking + heap mix (1 problem each), narrate aloud.
- Lunch
- B4 — **Mock #7: DSA** — random hard.
- B5 — Application sprint #3: **10 more companies**.
- B6 — Cheat-sheet drill: cold-recall §11.2–§11.5 — no peeking.
- B7 — Re-read Stories 1–8 quickly. Spot-check which ones still have weak numbers.
- Reflection.

#### Day 25 — Mon Jun 1 (4.5h)
- B1 — **Mock #8: System Design**.
- B2 — Cheat-sheet drill: §11.6 (behavioral one-liners) cold-recall.
- B3 — Apply to **5 more companies**.
- Reflection.

#### Day 26 — Tue Jun 2 (4.5h)
- B1 — **Mock #9: Behavioral**, 7 prompts.
- B2 — Address weakness #1 from `MOCK_LOG.md` head-on (e.g., off-by-one, naming, complexity articulation).
- B3 — LC 1 problem cold, talk through.
- Reflection.

#### Day 27 — Wed Jun 3 (4.5h)
- B1 — **Mock #10: DSA full 45-min loop**: medium → talk → code → trace → complexity. Clean end-to-end run.
- B2 — Re-read `MOCK_LOG.md`. Tabulate the top 3 recurring weaknesses across all mocks.
- B3 — One-day deep dive on weakness #1.
- Reflection.

#### Day 28 — Thu Jun 4 (4.5h)
- B1 — Final resume + LinkedIn pass. Confirm both link the RAG project.
- B2 — Re-rehearse "biggest weakness" + "why our company" 5x each, out loud.
- B3 — LC fluency: 2 easy/medium just to feel sharp. Apply to **10 more companies** (push to 50+ total).
- Reflection.

#### Day 29 — Fri Jun 5 (8h)
- B1 — **Full company-style 4-round simulation** in one block: DSA → Sys Design → Behavioral → wrap.
- B2 — Continuation: complete the 4-round.
- Lunch
- B3 — Postmortem honestly: am I ready? What's the one remaining gap?
- B4 — Address that gap (last weak chapter, last LC pattern, etc.).
- B5 — Cheat sheets review aloud.
- B6 — Light: organize notes, inbox, schedule pending interviews.
- Reflection.

#### Day 30 — Sat Jun 6 (10h)
- B1 — Cheat-sheet cold-recall: §11.2–§11.6, no peeking.
- B2 — One last mock with a friend or paid platform. Treat it as the real thing.
- Lunch
- B3 — Light DSA: 2 easy/medium fluency problems, just to feel sharp.
- B4 — Inbox triage: respond to recruiter pings, schedule any pending interviews.
- B5 — **Ch 11 §11.7 — re-read the seven mantras aloud.**
- B6 — Real rest. Walk, no screens. You're done with prep.

---

## Focus rules (the part that beats Instagram)

The book's Chapter 11 §11.7 mantra #7 is *Sleep.* Mantra #8 should be *Phone in another room.*

1. **Phone, in another room, charging, on Do Not Disturb.** Not face-down on the desk. Not in a drawer next to you. Different room. The mere visibility of a phone reduces working memory.
2. **One app blocker.** macOS: **Cold Turkey Blocker** ($) or **AppBlock**. iOS: Screen Time → App Limits → block Instagram/X/YouTube during your study window. Set it once, never disable mid-session.
3. **Tabs allowed during a block:** the chapter you're reading, the LeetCode problem, your editor, a notes doc. That's it. No email, no Slack, no Twitter.
4. **The "if-bored" rule.** If you feel boredom in minute 30 of a block, the urge to check your phone will spike. Pre-commit: when boredom hits, you stand up, drink water, walk 30 seconds, sit back down. You don't pick up the phone. This trains the boredom-tolerance muscle, which is the entire game.
5. **Anchor the start.** Same time, same place, same first action ("open the chapter, type the date in my notes file"). Decision fatigue kills more sessions than difficulty does.
6. **End-of-day reflection (5 min, non-negotiable).** Three sentences in `daily_log.md`:
   - What clicked today?
   - What didn't I understand?
   - What's tomorrow's #1 priority?

   This is the highest-leverage 5 minutes of the whole day. It compounds.
7. **Pomodoro: 90 work / 10 break.** During the 10: stand up, walk, water, no screen. Nothing trains focus like a hard bookend on the rest interval — if your "10-minute break" becomes 25 minutes of Reels, you've lost the war.
8. **One weekly review, Sunday night.** Look back: what % of blocks did I actually run cleanly? Adjust *systems*, not *willpower*.

> "You don't rise to the level of your goals; you fall to the level of your systems." — your book, page 1.

---

## Where this lives

This file: `~/Code/study-radar/STUDY_PLAN.md`. Version-controlled once we wire up the daily-email automation; for now you can edit it directly.

## Next step (optional)

Wire the plan into a daily 6:30 AM ET email — same SendGrid + GH Actions stack as job-radar — that pulls today's tasks from this file and adds an AI-generated 3-question quiz on yesterday's material. Asks me to scaffold `study-radar` when ready.
