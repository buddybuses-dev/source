# Module 5: Projects, Context, and CLAUDE.md

**Time:** about 45 minutes. **Hands-on:** yes. You'll set up a real project folder.

## Objectives

- Understand context: what Claude knows, when it knows it, and why it forgets
- Create a CLAUDE.md so every session starts already briefed
- Structure ongoing work as projects instead of one-off tasks

---

## 5.1 What Claude actually "knows"

In any session, Claude Code knows exactly three kinds of things. Three. Once you internalize this, half the confusing behavior stops being confusing:

1. **Training knowledge.** General knowledge of the world, languages, and tools. Fixed, with a cutoff date.
2. **What it reads this session.** Files it opens, commands it runs, web pages it fetches. This is called the context.
3. **What you tell it.** Your messages.

Two consequences surprise beginners, so hear them now instead of learning them the annoying way:

It doesn't automatically know your files. It discovers them by looking, which it does readily, but a brief that says where things are saves the scavenger hunt.

It forgets between sessions. Close the conversation and the context is gone. Tomorrow starts blank. (`claude --continue` resumes a past conversation, but the real fix for recurring context is the next section, and the next section is worth the price of this module.)

## 5.2 CLAUDE.md, your standing brief

Any folder can contain a file named `CLAUDE.md`. When you launch Claude Code in that folder, it reads that file automatically. Every session. Think about what that means: it's the briefing document a good manager hands a new contractor on day one, except you write it once and it briefs every session forever.

Here's what one looks like:

```markdown
# Hebb Consulting: Client Reports Project

## What this project is
Monthly performance reports for 12 clients. Raw exports land in /inbox,
finished PDFs go to /reports/<client>/<year>.

## Rules
- Never modify anything in /inbox. Treat it as read-only.
- All currency formatted as USD with commas: $12,345.67
- Client names must match the spelling in clients.csv exactly.
- Drafts are always reviewed by me before anything gets emailed or sent anywhere.

## How I like to work
- Show me a plan before touching more than 5 files.
- When in doubt about a judgment call, ask. Don't guess.
```

Notice what's in there: facts Claude can't discover on its own (where finished work goes), standing constraints (the inbox is read-only), your working style (plan first). Notice what's not: anything Claude can figure out by looking at the files. Don't document what's discoverable. Document what's decided.

And don't write it by hand. Delegate the delegation:

> "Look around this project and interview me briefly, then write a CLAUDE.md capturing what this project is, the rules I tell you, and how I like to work."

(For code projects, the built-in `/init` command does a version of this automatically.)

Maintain it conversationally. When you correct Claude on something that will always be true ("we never touch /inbox"), follow up with: "add that to CLAUDE.md." There's also a shortcut: start a message with `#` and Claude Code offers to store that note in memory for future sessions. Ten seconds now, and you never make that correction again. That's the trade. Take it every time.

## 5.3 Layered CLAUDE.md files

CLAUDE.md files stack:

- **`~/.claude/CLAUDE.md`** (in your home folder) is personal and applies everywhere: "I'm on Windows 11. I prefer plans before big changes. Explain things without assuming programming knowledge."
- **A project folder's `CLAUDE.md`** holds that project's facts and rules.
- **Subfolder `CLAUDE.md` files** exist too. You don't need them as a beginner. Ignore them guilt-free.

Set up the personal one today. Three sentences about you and your preferences, and every future session everywhere starts smarter. Three sentences. Highest leverage-per-word you'll write all week.

## 5.4 Structuring ongoing work

One-off tasks can live anywhere. Anything you'll touch weekly deserves a project folder:

```
my-project/
  CLAUDE.md        <- standing brief
  inbox/           <- raw inputs land here
  work/            <- intermediate files
  output/          <- finished products
```

The exact shape matters less than having a shape and recording it in CLAUDE.md. Here's the payoff: from then on, a session starts with "Two new client exports in inbox. Run the usual monthly report." One sentence. It works because CLAUDE.md is carrying the other 90% of the brief. You did the briefing work once. Now it's an asset, not a chore.

## 5.5 Managing context within a session

Long sessions degrade. Claude Code manages its own context as conversations grow, but running `/clear` at the start of each new task keeps quality high. Your CLAUDE.md files get re-read automatically after a clear. The standing brief survives, only the chat history is wiped.

`/compact` condenses a very long conversation you're not ready to leave, keeping the important parts.

Point, don't paste. Working with a big document? Don't paste it into the chat. Say the filename. Claude reads what it needs from disk.

---

## Exercises

1. **Personal CLAUDE.md.** Create `~/.claude/CLAUDE.md`. Ask Claude Code to do it: "create my personal CLAUDE.md, and interview me for it." Include your OS, your experience level, and two working-style preferences.
2. **Project setup.** Take your most likely recurring use (probably your Module 4 capstone). Create a project folder with the inbox/work/output shape and an interview-generated CLAUDE.md.
3. **Prove it works.** Exit, relaunch in the project folder, and give a deliberately lazy instruction ("process what's in inbox"). Watch how much the CLAUDE.md fills in. That gap between what you typed and what happened? That's your briefing asset paying dividends.
4. **Teach it one rule.** Mid-session, correct Claude about anything, then say "add that to CLAUDE.md." Confirm the file changed.

## Checkpoint

You're ready for Module 6 when a fresh session in your project folder already knows your rules without being told, and you can say what belongs in CLAUDE.md (standing facts, rules, preferences) versus what belongs in the brief (the specifics of today's task).
