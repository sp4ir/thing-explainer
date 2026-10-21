---
name: thing-explainer
description: Explain the current session's topic (or a named topic) using only the ten hundred (1,000) most common English words, in the style of Randall Munroe's "Thing Explainer". Use when the user runs /thing-explainer, or asks to explain something "like Thing Explainer", "in ten hundred words", "Up Goer Five style", or with only simple/common words.
argument-hint: "[topic — omit to explain what this session is about]"
---

# Thing Explainer

Explain a thing the way Randall Munroe does in *Thing Explainer*: every word
must be one of the ten hundred most common English words. No exceptions for
"just this one technical word" — the fun and the clarity both come from
finding a way around it.

## 1. Pick the topic

- If `$ARGUMENTS` is non-empty, that is the topic.
- Otherwise, use what this session has been about: the system, bug, code,
  service, or idea the conversation has centered on. If the session has no
  real topic yet (e.g. this is the first message), ask the user what to explain.
- Get the facts right first, in normal words, in your head. Simple words are
  not an excuse to be wrong. If the topic is code or a system in front of you,
  base the explanation on how it actually works here, not a generic version.

## 2. Write it

Style, taken from the book:

- **Name things by what they do or look like.** Rocket → "up-goer".
  Computer program → "set of orders for a computer". Server → "computer that
  answers other computers". Database → "big box of written-down facts".
  Password → "hidden word". Internet → "computers talking to each other
  all over the world".
- **Give each made-up name once, then reuse it** so the reader can follow.
  Capitalize the made-up names of the main parts if it helps
  (e.g. "the Answer Computer"), like the labeled parts in the book.
- **Numbers:** "thousand" and "million" are not on the list. Say "ten hundred",
  "a hundred hundred", "ten hundred hundred", or "a lot".
- **Short sentences. Dry, friendly humor.** Small asides are good
  ("This part is hard and people get it wrong a lot."). Keep it warm, never
  talk down to the reader.
- **Structure:** a title made of allowed words, the real name in backticks
  under it, then a few short sections. For things with parts, a labeled
  "picture" works well — a small ASCII drawing or a list where each part has
  its simple name and a line on what it does.
- **Length:** about 200–500 words unless the user asks otherwise.

Allowed outside the word rule (keep these few):
- The real name of the thing once, in backticks, at the top: `` `Kubernetes` ``.
- People's names and place names, sparingly.
- Nothing else — no "API", no "data", no "software" sneaking in.

## 3. Check every word

Run the checker on your draft before showing it. The word list is
`words.txt` next to this file (the Up Goer Five list: the ten hundred words
plus their normal forms like -s, -ed, -ing).

```bash
python3 ~/.claude/skills/thing-explainer/check.py <<'EOF'
...your draft...
EOF
```

Write the draft into the heredoc (not a file), so nothing lands in a repo.
For each word it flags, rewrite the sentence — don't just swap in a word
that is also off the list. Re-run until it prints `OK`. Text in backticks is
skipped, so keep backticks only for the real-name line.

Words that look common but are NOT on the list: thousand, million, rocket,
data, process, user, file, code, software, network, list, secret. Some that
ARE allowed: system, information, send, store, keep, answer, picture. When
unsure, run the checker — don't guess.

## 4. Show it

Output only the finished explanation in Markdown — no notes about the
process, no word-check log. If the user wants a short glossary mapping your
made-up names back to the real terms, add one at the end only when asked
(that part may use normal words).
