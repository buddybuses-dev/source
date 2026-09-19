# Module 1: What Claude Code Is (and Isn't)

**Time:** about 30 minutes. **Hands-on:** thought exercises only. Setup comes in Module 2.

## Objectives

By the end of this module you can:
- Explain the difference between a chatbot and an agent
- Tell Claude, Claude Code, and Claude Cowork apart, and say why this course teaches Claude Code
- Describe what Claude Code can touch on your computer and what it can't
- Name the three habits that separate productive users from frustrated ones

---

## 1.1 Chatbot vs. agent

You've used a chatbot. You type a question, it types an answer. The conversation lives in a browser tab, and if you want to actually *do* anything with the answer (save a file, rename 200 photos, update a spreadsheet) you do it yourself. By hand. The chatbot talks about the work. You still do the work.

Claude Code is a different animal. It's an agent. It runs on your computer, in your terminal, and it takes actions:

- read and write files on your machine
- run programs and commands
- search the web
- use git, install software, call APIs

You describe an outcome, something like "organize my Downloads folder by file type and year," and it plans the steps, executes them, checks the results, and reports back. When something fails, it reads the error message and tries another approach, the way a competent assistant would.

Here's the mental model that works, and I want you to actually adopt it, not just nod at it: **Claude Code is a very fast, very literal contractor you just hired.** Skilled. Never tired. But it only knows what's in front of it: your instructions, your files, whatever it discovers along the way. Good outcomes come from a good brief: clear goal, relevant context, known constraints. That's true of every contractor you've ever hired, and it's true here.

The mental model that fails: mind reader. "Fix my website" gets you clarifying questions or a guess. "The contact form on my site returns an error after clicking submit. The project folder is right here. Find the cause and fix it" gets you a fix. Same tool. Same day. The variable was you.

## 1.2 Claude, Claude Code, and Cowork: which one is this?

Anthropic sells one subscription with three doors into the same brain, and the names confuse everyone. Thirty seconds to sort it out.

**Claude** (the app and website) is the chatbot from section 1.1. It talks. You do.

**Claude Cowork** lives in the Claude desktop app, and it's rolling out on the claude.ai website and phone apps too. It's an agent like Claude Code, but with buttons instead of a terminal: point it at a folder, and it can organize files, pull data out of PDFs, build reports, and run scheduled tasks. It launched in early 2026 and it's included in paid plans, same as Claude Code. If all you ever want is document and file chores, Cowork alone might cover you, and I'd rather tell you that now than have you find out after buying a course.

**Claude Code** is the full toolbox. Everything Cowork does, plus the things this course is actually about: building and publishing a real website, the git undo button that makes mistakes free (Module 6), automation you set up once and rerun forever, and a workspace you customize per project (Module 5 and 7). Cowork drives an automatic; Claude Code hands you the keys to the truck.

So why does this course teach the terminal version? Because the terminal is a one-week discomfort and the toolbox is permanent. Modules 2 and 3 get you through the discomfort. The rest of the course spends the payoff. And once you're comfortable in Claude Code, Cowork will feel obvious on the days you want the simpler door.

## 1.3 What it can and can't touch

Claude Code operates from a working directory, the folder you launch it in. Think of it as the job site.

It can read, edit, and create files, run terminal commands, use the internet, work with git repositories, and (with your permission) act outside the working directory.

It can't act without being run. It can't see your screen. It can't click around inside apps like Excel or Photoshop, because it works with files, not windows. And it can't do anything your user account can't do.

Permissions are your safety rail. Out of the box, Claude Code asks before doing anything with side effects: editing a file, running a command. You'll see a prompt: allow once, allow always, or deny. Early on, read these prompts. Every one. They're how you learn what the tool actually does, and that education is free. Later, in Module 7, you'll tune them so routine actions stop nagging you.

## 1.4 The three habits

Put a frustrated beginner and a productive user side by side and you'll see the same three differences every single time. Not ten. Three. Master these and you're ahead of almost everyone who installs this tool.

**Habit 1: Scope the work.** One coherent outcome at a time. "Clean up this folder, then build me a website, and also can you look at my taxes" produces mush. One brief, one outcome, next.

**Habit 2: Review before you build on top.** After Claude finishes, look at what changed. You don't need to read code line by line. Ask: "What did you change and why?" Then check the result itself: open the file, load the page, look at the report. Skipping this step is how a small problem two weeks ago becomes a big problem today.

**Habit 3: Correct course instead of starting over.** Result is 80% right? Say what's wrong with the other 20%: "Good, but the dates should be DD/MM/YYYY, and skip hidden files." Iterating in the same conversation keeps all the context Claude has built up. Restarting throws it away.

## 1.5 "But I can't read code. Isn't this dangerous?"

Fair question. Three straight answers.

First, most beginner tasks aren't code. Organizing files, summarizing documents, cleaning up CSVs. You verify the outcome with your own eyes, no code reading required.

Second, version control is your undo button. Module 6 sets it up, and after that, any change Claude makes to a project rolls back with one sentence: "undo the last change." When mistakes cost nothing, fear stops being useful.

Third, know where the boundary is. Anywhere a silent mistake is expensive (payroll data, legal documents, systems other people depend on), you verify the output independently or bring in someone who can. The course flags these moments explicitly when they come up. That's not an AI rule. That's a business rule.

## 1.6 What it costs

Claude Code is included in paid Claude plans. Pro, around $20 a month, covers this entire course comfortably. Heavy professional use can eventually hit plan limits, and the fix is a bigger plan or API billing, but that's a decision you won't face until long after this course. Twenty bucks a month against the hours you're about to reclaim. Run that math once and move on.

---

## Exercises

**1. Write your first three briefs.** Pick three real annoyances from your work or computer life: a messy folder, a repetitive weekly task, a document you keep meaning to make. For each one, write a two-to-four sentence brief as if handing it to a contractor: the outcome, where the materials are, the constraints. Keep these. You'll run one in Module 3. This is the ten-minute exercise that triples the value of everything after it. Do it.

**2. Sort these requests.** For each one, decide: good brief, needs scoping, or needs extra care in verification?
- "Make my resume better"
- "Rewrite my resume (resume.docx on my Desktop) to emphasize project management, and keep it to one page"
- "Update the pricing formulas in our client invoicing spreadsheet"

Answers: the first needs scoping (better how? for what job?). The second is a good brief. The third needs verification care: money math gets an independent check, always. One way: ask Claude to also produce a before-and-after comparison you can eyeball.

## Checkpoint

You're ready for Module 2 if you can answer these cold:
- What's the difference between an agent and a chatbot? (An agent takes actions on your machine. A chatbot produces text in a tab.)
- When would Cowork alone cover someone? (When all they need is file and document chores. Claude Code adds building, publishing, the git undo button, and per-project setup.)
- What's a working directory? (The folder Claude Code is launched in. Its job site.)
- What are the three habits? (Scope the work, review the results, correct course instead of restarting.)
