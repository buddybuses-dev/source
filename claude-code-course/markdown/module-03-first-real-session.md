# Module 3: Your First Real Session

**Time:** about 45 minutes. **Hands-on:** yes. You'll run one of your own briefs from Module 1.

## Objectives

- Run the instruct, review, refine loop on a real task
- Write briefs that get good results on the first try
- Recover confidently when a result is wrong

---

## 3.1 Anatomy of a good brief

A brief that works has four parts. You won't always need all four, but when a result disappoints you, come back to this list, because one of these is what was missing. Every time.

1. **Outcome.** What exists when the work is done. "A single PDF combining these three reports."
2. **Materials.** Where the inputs are. "The reports are the three .docx files in this folder."
3. **Constraints.** What must or must not happen. "Keep the original files untouched. Order: Q1, Q2, Q3."
4. **Definition of done.** How you'll both know it worked. "Tell me the final page count so I can sanity-check it."

Compare:

> "combine my reports"

> "Combine the three quarterly .docx reports in this folder into one PDF named `2026-annual.pdf`, in Q1 to Q3 order, leaving the originals untouched. Tell me the final page count."

The second version costs you 20 extra seconds of typing. It saves you three rounds of back and forth. That trade, seconds of clarity for minutes of correction, is the highest-ROI trade in this entire course, and you get to make it on every single task forever.

One more thing. Notice the brief says nothing about HOW to convert docx files to PDF. Not your job. If a tool needs installing, Claude proposes it. **You own the what. Claude owns the how.** Write that somewhere.

## 3.2 What you're looking at while Claude works

During a task, Claude narrates: reading files, running commands, making edits. You don't need to follow every line. Watch for three things:

- **Permission prompts.** Read them. They tell you what's about to happen before it happens.
- **Questions.** Claude asks when your brief left a real decision open. Answering well beats letting it guess.
- **The wrap-up summary.** Claude's account of what it did. Your review starts here.

Heading somewhere you don't like? Press `Esc` and redirect. Interrupting is normal usage, not an emergency measure. You're the boss. Act like it.

## 3.3 Reviewing without expertise

Three review moves, cheapest first:

1. **Check the artifact.** Open the file. Load the page. Look at the folder. Most beginner tasks verify with your eyes in under a minute.
2. **Interrogate.** "Summarize every file you changed and why." "What could go wrong with this approach?" "Did anything fail that you worked around?" Claude answers honestly about its own work, including its doubts. Free information. Take it.
3. **Ask for a self-check.** "Write a quick check that verifies the totals in the output match the input files, and run it." A second method catching the first is how silent errors die.

Money, legal language, anything sent to other people: do move 3, then add your own independent look on top. Every single time. No exceptions. No matter how good the last ten results were.

## 3.4 Refining: the 80% pattern

First results are commonly 80% right. Beginners see the 20% and start over. That's the expensive move. The winning move is a targeted correction:

> "Good. Two fixes. First, the dates should read like 'July 2, 2026', not '02/07/26'. Second, you missed the files in the subfolder, so include those too."

Why not restart? Because the session has context: everything Claude has read and learned so far. A restart sets that on fire. Two rules:

- Same task? Keep going in one conversation.
- New unrelated task? `/clear` first. Stale context from an old task confuses a new one, and very long conversations lose quality. New job, fresh slate.

## 3.5 When it's really wrong

Sometimes iteration isn't converging. Don't flail. Climb the ladder:

1. Say what's wrong specifically, with an example of the wrong output next to what you expected.
2. Separate diagnosis from action: "Stop fixing. First explain why the totals are off, then propose a fix and wait for my okay." This is the single most useful sentence for stuck situations. Steal it.
3. Undo and re-brief: "Restore everything to how it was before this task." Then `/clear`, and write a better brief using what you learned. Before Module 6, Claude can usually reverse its own file changes. After Module 6, undo becomes trivial and guaranteed.

A failed task that teaches you what the brief was missing isn't a failure. It's tuition, and it's a lot cheaper than mine was.

## 3.6 A worked example

A brief given in a folder of 340 vacation photos:

> "Rename all photos in this folder to `YYYY-MM-DD_HHMM_original-name.jpg` using each photo's taken-date from its metadata. Photos with no metadata date go untouched into a subfolder called `no-date`. Show me a plan and a 5-file sample first."

Why it's strong: outcome, materials (this folder), constraints (how to handle photos without dates). And a staged rollout: "plan and sample first." For any task touching a lot of files, a small sample before the full run turns a potential 340-file mistake into a 5-file one. Same insurance a smart contractor sells you, except this one's free.

---

## Exercises

1. **Run one of your Module 1 briefs.** Pick the safest of the three. Before running it, upgrade it with the four parts (outcome, materials, constraints, done), and if it touches many files, add a sample-first stage. Work in a copy of the real folder this first time.
2. **Practice the interrogation.** After it finishes, ask all three review questions from 3.3 and actually read the answers.
3. **Force a refinement.** Find something imperfect in the result (there's usually something) and fix it with a targeted correction, not a restart.
4. **Practice the undo.** Ask: "Restore this folder to exactly how it was before we started." Then verify it did. Undo skills learned in a crisis are learned badly. Learn them now, while nothing's on fire.

## Checkpoint

You're ready for Module 4 when you've completed a real task of your own end to end, refined it at least once without restarting, and undone at least one change on purpose.
