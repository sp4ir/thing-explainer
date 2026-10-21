> **Source:** [PHP2Shell](https://www.php2shell.com/), a family of critical
> memory-safety bugs in core PHP (CVSS 9.2) that can allow unauthenticated
> remote code execution and memory disclosure.
>
> **Generated with:** `/thing-explainer https://www.php2shell.com/`
>
> Everything below the line uses only the ten hundred most common words.

---

# Big Hole in the Page Maker

`PHP2Shell`

## The Page Maker

When you look at a page on your computer, a computer far away has to build that page for you. For about seven out of every ten pages in the world, the thing doing the building is the same set of orders. Let's call it the Page Maker.

A lot of big, well known places are built on top of the Page Maker. One is the place where people write and share their thoughts every day. Another is the huge free book about everything that anyone can change.

## What went wrong

Some people (and a thinking computer helping them) found two bad holes in the Page Maker itself. The holes are not in the things built on top of it. They are in the Page Maker. So even a page that only says "Hello World" can be hurt.

```
   Visitor ---> [ Answer Computer ]
                  |
                  +-- Page Maker   <-- the holes are here
                  |     |
                  |     +-- Thinking Space (how much it can hold in its head)
                  |     +-- Left-Behind Stuff (things from the last visitor)
                  |
                  +-- Hidden words, keys, other people's stuff
```

**Hole one: Running out of Thinking Space.** The Page Maker is only allowed to hold so much in its head at once. If a bad person sends it a very large, strange question, it runs out of room. When that happens, it falls over in a bad way and leaves broken pieces lying around. A bad person who knows what they are doing can shape those pieces so the Page Maker starts following *their* orders. They don't need a hidden word first. Then they can do anything the Answer Computer can do.

**Hole two: Left-Behind Stuff.** The Page Maker answers one visitor, then the next, then the next. It is supposed to clean up between them. Sometimes it doesn't. A bad person can look through the stuff left behind and read things that belong to someone else, like hidden words and keys. This kind is extra quiet. It can steal without ever running strange orders, so the usual guards may not notice.

How bad is this? The people whose job is to say how bad these things are gave it a 9.2 out of 10. That is very bad.

## How to fix it

Get a newer Page Maker: 8.2.35, 8.3.36, 8.4.27, or 8.5.12 or later. Then turn the Answer Computer's Page Maker parts off and on again, or the old one keeps running.

Making the stuff on top newer does not help. The holes are under it. This part is easy to get wrong, so check twice.

If you can't change it today, there are a few settings you can change to make the holes smaller. None of them close the holes. Only the newer Page Maker does that.
