# thing-explainer

A [Claude Code](https://claude.com/claude-code) skill that explains things
using only the ten hundred most common English words, in the style of
Randall Munroe's *[Thing Explainer](https://xkcd.com/thing-explainer/)*
(and the [Up Goer Five](https://xkcd.com/1133/) comic that started it).

```
/thing-explainer                     # explain what this session is about
/thing-explainer how DNS works       # explain a named topic
/thing-explainer https://example.com # explain what a page is about
```

Claude writes the explanation, then runs every word through a checker and
rewrites until nothing off the list is left. Here's
[an example](examples/php2shell.md) explaining a PHP security bug.

## Install

Copy the `thing-explainer/` folder into your personal skills directory so it
works in every project:

```bash
git clone https://github.com/sp4ir/thing-explainer.git
cp -r thing-explainer/thing-explainer ~/.claude/skills/
```

Or drop it in a repo's `.claude/skills/` to share it with a project.

## What's inside

| File | What it does |
| --- | --- |
| `thing-explainer/SKILL.md` | The instructions: picking the topic, the writing style, the check step |
| `thing-explainer/words.txt` | The allowed words: the ten hundred plus their normal forms (-s, -ed, -ing), 3,634 entries |
| `thing-explainer/check.py` | Flags every word not on the list. Text in `` `backticks` `` is skipped |
| `thing-explainer/words.txt.LICENSE` | The GPL-3.0 license for `words.txt` |

You can use the checker on its own:

```bash
python3 thing-explainer/check.py my-draft.md
echo "The rocket goes up" | python3 thing-explainer/check.py
# 1 word(s) not on the list:
#   rocket
```

## Credits and license

- *Thing Explainer* and *Up Goer Five* are by Randall Munroe. This project
  isn't affiliated with him or xkcd.
- `words.txt` is the Up Goer Five word list from Theo Sanderson's original
  editor, taken from [Cleartext](https://github.com/mortenjust/cleartext-mac)
  by Morten Just. It stays under the GPL-3.0; see
  [`thing-explainer/words.txt.LICENSE`](thing-explainer/words.txt.LICENSE).
- Everything else in this repo is under the [MIT License](LICENSE).
