# Module 6: Git and GitHub Without Tears

**Time:** about 45 minutes. **Hands-on:** yes. Your project goes under version control.

## Objectives

- Understand what git does for you, in one paragraph, no diagrams
- Put a project under version control using only plain English
- Undo changes with confidence (this is the real payoff)
- Back up a project to GitHub

---

## 6.1 Git in one paragraph

Git is a save-point system for a folder. At any moment you can say "save everything as it is now" (that's called a commit) along with a note about what changed. Later you can see the history of every save, compare any two, or restore the folder, or a single file, to any past save-point. That's the whole idea. Git is famous for being complicated, but the complicated part is its command-line interface, and here's the good news: you will never learn it. Claude Code speaks fluent git. You speak English to Claude Code. Done.

Why am I making you do this before the fun capstone? Because Module 1 promised an undo button for everything, and this is it. Once a project is under git, no mistake, Claude's or yours, is permanent. And that changes the whole economics of delegation. "Try restructuring the whole site" is a terrifying request when a bad result is forever. It's a cheap experiment when the whole site is one sentence away from restored. Bold and safe at the same time. That's what you're buying with this module.

## 6.2 Putting a project under git

In your project folder from Module 5, say:

> "Put this project under version control. Some files shouldn't be tracked. Figure out which ones (temp files, huge files, anything sensitive like API keys) and set that up too. Then make the first commit."

Claude will run `git init`, create a `.gitignore` (the do-not-track list, notice it thought about your secrets without being asked), and commit. Verify with "show me the history." You should see one commit. That's it. The thing developers take whole workshops to learn, you just did with a paragraph.

## 6.3 The working rhythm

The new habit is one sentence long: **commit at every good state.**

- Finished a chunk of work that's correct? "Commit this with a sensible message."
- About to attempt something big or risky? "Commit first, then let's try it."

Claude writes the commit messages. You just decide when. The rule of thumb: commit whenever you'd be annoyed to lose what you just got working. In practice that's a few times per session. Claude Code won't commit on its own initiative. You say when, and that's by design. You're the one with skin in the game.

## 6.4 Undo, in all its flavors

All plain English. The only vocabulary that matters is being clear about what you want undone.

| You say | What happens |
|---------|--------------|
| "Undo the changes since the last commit" | Uncommitted work is reverted and the last save-point is restored |
| "Undo just the changes to pricing.md, keep the rest" | Single-file restore |
| "Roll the whole project back to how it was Tuesday" | Time travel. Claude finds Tuesday's commit and asks whether to revert or reset, in plain terms. When unsure, say "keep history." |
| "What changed between now and the last commit?" | You get the differences, explained in English. Great pre-commit review. |
| "I think we broke something in the last few commits. Find where." | Claude walks the history comparing versions to locate the break |

Practice this now, on purpose (see the exercises). Undo skills learned during a crisis are learned badly. Undo skills learned on a Tuesday afternoon with nothing at stake are learned for life.

## 6.5 GitHub: your project, off your machine

Git lives on your machine. GitHub hosts a synced copy online. Why you want it: backup (laptop dies, project doesn't), access from a second machine, sharing and collaboration, and later, deployment. The website in Module 8 publishes straight from GitHub.

One-time setup:

1. Create a free account at github.com.
2. Install the GitHub CLI (`gh`). Ask Claude Code to install and set it up. When the login step needs your browser, it hands you a link.
3. Then: "Create a private GitHub repository for this project and push it."

Default to private repositories. Public is for things you've deliberately decided to publish, not things you forgot to hide.

From then on, syncing is one sentence: "push my latest commits." Claude will also mention pushing when it's overdue.

## 6.6 What you can skip for now

Branches, pull requests, merge conflicts, rebasing. Real git topics. You need exactly none of them until you're collaborating with other people on the same files. When that day comes, ask Claude Code to teach you branches using your actual project, it's a much better tutor with a real example in front of it. Until then: one branch, commit often, push regularly. For a solo person, that's not a beginner's compromise. That's a complete, professional-grade workflow.

---

## Exercises

1. **Version your project** (section 6.2) and verify with "show me the history."
2. **The fire drill.** (a) Ask Claude to make some visible change to a file. (b) "Undo the changes since the last commit." (c) Confirm the file is restored. (d) Make two commits with distinct small changes, then roll back to the first, then return to the latest. Pass this and you're crisis-proof. Not crisis-resistant. Proof.
3. **The diff habit.** Before your next commit, ask "what changed since the last commit?" and read the explanation. Make this your default pre-commit move.
4. **Go remote.** GitHub account, `gh` set up, private repo, push. Then open github.com and see your files sitting there.
5. **Update CLAUDE.md.** Add: "Remind me to commit when we reach a good state, and to push at the end of a session."

## Checkpoint

You're ready for Module 7 when your project is on GitHub, you've completed the fire drill without help, and "commit first, then let's try it" has entered your vocabulary for risky changes.
