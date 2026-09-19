# Glossary: Plain-English Definitions

No jargon you can't use. If a term shows up in the course and you're not sure what it means, it's here.

**Agent:** An AI that takes actions (files, commands, web) rather than just answering in text. Claude Code is an agent.

**Auto-accept mode:** A session mode where Claude acts without permission prompts. For low-stakes sandbox work.

**Brief:** Your instruction to Claude. Outcome, materials, constraints, and definition of done.

**CLAUDE.md:** A file Claude Code automatically reads at launch. Your standing brief: project facts, rules, and working-style preferences. The personal version lives at `~/.claude/CLAUDE.md`.

**CLI (command-line interface):** A program you use by typing commands in a terminal.

**Commit:** A named save-point of your whole project in git. "Commit this" means save the current state permanently.

**Context:** Everything Claude knows in the current session: your messages plus whatever it has read and run. It's gone when the session ends, which is what CLAUDE.md and memory are for.

**Diff:** The precise list of what changed between two versions. Ask for it in English: "what changed since the last commit?"

**Git:** A save-point system for a folder. History, comparison, and restore for every file. You use it through Claude in plain English.

**GitHub:** A website that hosts a synced online copy of your git project. Backup, sharing, and the launch pad for free website deployment.

**Hook:** An automation that fires on an event ("after every edit, do X"). Rules enforced by the machine.

**localhost:** Your own computer acting as a website host. An address like `http://localhost:8080` is a preview only you can see.

**MCP (Model Context Protocol):** The plug-in standard that connects Claude Code to outside services like Gmail, Notion, and databases.

**Model:** The AI brain currently in use. Bigger models (Opus-class) think deeper. Smaller ones (Haiku-class) are faster and cheaper. `/model` switches between them.

**Permission prompt:** Claude asking before it takes an action with side effects. Your safety rail, and your window into what it's doing.

**Plan mode:** Claude researches and proposes but changes nothing until you approve. For big or fuzzy work.

**Push:** Send your local commits to GitHub. "Push my latest commits."

**Repository (repo):** A folder under git version control. On GitHub, the online copy of one.

**Sandbox:** A throwaway folder for practice and experiments, where nothing can be harmed.

**Skill:** A folder of instructions Claude loads for a specific kind of task (how we write proposals, how we review data).

**Slash command:** Anything starting with `/` typed in a session. There are built-ins like `/help` and `/clear`, plus your own canned briefs stored in `.claude/commands/`.

**Subagent:** A parallel copy of Claude that the main session delegates a piece of work to. Mostly automatic.

**Terminal:** The text window where you run commands and where Claude Code lives. PowerShell on Windows, Terminal on Mac.

**Version control:** The general practice git implements: a tracked history of changes with the ability to restore any of them.

**Working directory:** The folder you launched Claude Code in. Its job site. Easy access inside it, extra checks outside it.
