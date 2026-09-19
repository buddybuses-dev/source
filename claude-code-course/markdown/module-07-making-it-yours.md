# Module 7: Making It Yours. Permissions, Commands, and Customization

**Time:** about 45 minutes. **Hands-on:** yes. You'll tune your setup and build a custom command.

## Objectives

- Tune permissions deliberately instead of clicking through prompts
- Use plan mode for look-before-you-leap work
- Create your first custom slash command
- Know what MCP, skills, and hooks are, and when you'll be ready for them

---

## 7.1 Permissions, deliberately

By now you've clicked through hundreds of permission prompts. Time to stop paying that tax on autopilot and start deciding. At each prompt your realistic options are:

- **Allow once**, for anything unusual.
- **Allow always**, the "stop asking about this" button, for actions you've decided you trust (like editing files inside this project). Remembered per project.

Your risk model as a beginner is one sentence: **loosen permissions in proportion to your ability to undo.** Inside a git-tracked project, file edits are cheap to undo (that was Module 6), so be generous there, it costs you almost nothing and removes most of the friction. Commands that reach outside the project or out to the internet? Those get a glance each time. Un-versioned folder of original files? Keep every prompt.

There are also two whole-session modes worth knowing. You can see the current mode in the interface, and Shift+Tab cycles through them.

**Plan mode.** Claude researches and proposes, and nothing gets changed until you approve the plan. Ideal for "I want to restructure this whole project," or any brief that's big or fuzzy. Get the reflex: big fuzzy brief → plan mode. It costs you one approval click and saves you entire wrong directions.

**Auto-accept mode.** No permission prompts for the session. Fine for low-stakes sandbox work. Think twice in folders that matter. (You'll also see `--dangerously-skip-permissions` in internet tutorials. The name is not being cute. It's telling you exactly what it does. Not while you're new, and never outside an isolated environment.)

## 7.2 Custom slash commands: your recurring briefs, canned

Here's a rule that will serve you forever: any brief you've typed three times is a product waiting to be built. A file at `.claude/commands/report.md` inside your project, containing a prompt template, becomes `/report` in your sessions. Weekly task, one command, zero re-explaining.

Don't write it by hand. Delegate the meta-task:

> "Create a custom slash command called /monthly-report that processes any new files in inbox/, follows the report rules in CLAUDE.md, and finishes by telling me what it produced and what looked unusual. Commands can take arguments, so let me pass a client name to run just that client."

Commands in `~/.claude/commands/` work in every project, your personal toolbox. Commands in a project's `.claude/commands/` folder travel with that project, and since Module 6 they're version-controlled and pushed to GitHub like everything else. Look at what just happened: you maintain software now. Nobody told the software industry it would be this easy to get in.

## 7.3 The extension landscape: a map, not the territory

You'll hear these terms. Here's what each one is and, more useful, the trigger that tells you it's your moment:

| Thing | What it is | Your trigger moment |
|-------|-----------|-------------------|
| **Skills** | Folders of instructions Claude loads for specific kinds of tasks (like "how we write proposals here"). Like CLAUDE.md, but per-capability instead of per-project. | A type of task, not a project, has rules worth teaching once |
| **MCP servers** | Plug-ins connecting Claude Code to outside services: Gmail, Notion, databases, your calendar | You catch yourself exporting data from a service just to hand it to Claude |
| **Hooks** | Automations that fire on events ("after every file edit, run X") | You have a rule you want enforced by the machine instead of remembered by the model |
| **Subagents** | Claude delegating pieces of work to parallel copies of itself | Mostly automatic. Ignore it. |

When a trigger fires, the play is always the same: ask Claude Code to set it up. "Connect to my Notion." "Add a hook that backs up the output folder after changes." The tool configures itself under your direction. You don't read configuration documentation. You recognize the moment and ask. That's the whole game.

## 7.4 A note on models

`/model` picks the brain. Flagship models (Opus-class) think deepest. Lighter ones (Sonnet and Haiku class) are faster and cheaper per task. The beginner policy that works: use the default, escalate to the biggest model when a task is high-stakes or has failed twice. The model lineup changes constantly. The policy doesn't. Learn policies, not lineups.

---

## Exercises

1. **Permissions audit.** In your project, deliberately set "always allow" for in-project file edits. Then ask Claude: "show me what permissions are currently saved for this project" and read the list.
2. **Plan mode rep.** Switch to plan mode (Shift+Tab) and give it a big fuzzy brief: "Propose a reorganization of this project for the next 6 months of use." Review the plan. Approve or revise, your call, and either way you've learned the mode. Notice that nothing was touched until you decided. That's the point.
3. **Build your command.** Turn your Module 4 capstone (that recurring weekly task) into a custom slash command. Test it. Commit it. Your hour-long weekly task is now a slash command. Do the annual math on that.
4. **One extension conversation.** Install nothing. Just ask: "Given how I work, which MCP servers or skills would actually help me? Interview me if needed." Keep the answer for the day a trigger fires.

## Checkpoint

You're ready for Module 8 when your recurring task is one slash command long, you've run one real task through plan mode, and permission prompts in your main project only show up for genuinely unusual actions.
