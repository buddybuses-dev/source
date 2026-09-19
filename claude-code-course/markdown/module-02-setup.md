# Module 2: Setup, Install, and First Launch

**Time:** about 30 minutes. **Hands-on:** yes. You'll finish with Claude Code running.

## Objectives

- Open a terminal on your operating system without dread
- Install Claude Code and log in
- Launch it in a safe practice folder and run your first commands

---

## 2.1 Meet your terminal

The terminal is the thing that stops most people from ever starting. So let's kill the fear with a fact: you need exactly three ideas from it. Three. Not thirty.

1. You type commands, press Enter, they run.
2. You're always "in" a folder (the current directory). `cd foldername` moves you into a folder. `cd ..` moves you up one level.
3. Copy and paste work. Windows: Ctrl+Shift+V or right-click. Mac: Cmd+V.

To open it:
- **Windows:** press Start, type `PowerShell`, press Enter.
- **Mac:** press Cmd+Space, type `Terminal`, press Enter.
- **Linux:** you already know.

Try it right now. Type `cd Desktop` and press Enter. Done? Congratulations, that's most of the terminal skill this entire course requires. The scary black window took you eleven seconds. Claude Code handles the rest.

## 2.2 Install Claude Code

You need a paid Claude account first (Pro or higher). Sign up at claude.ai if you haven't.

For the install itself, check https://docs.anthropic.com/claude-code for the current command for your operating system. Install methods change over time and the docs are always right. As of this writing:

- **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`
- **Mac/Linux:** `curl -fsSL https://claude.ai/install.sh | bash`

Close and reopen your terminal after installing, then verify:

```
claude --version
```

Version number? You're in. "Command not found"? Reopen the terminal and try again, that fixes it nine times out of ten. Still stuck? The docs page has troubleshooting per OS. The usual culprit is something called PATH, and here's the fun part: once you're running, diagnosing PATH problems is exactly the kind of thing you'll hand to Claude Code.

## 2.3 First launch

Rule one of new tools: don't test them where you keep things you love. Make a sandbox:

```
mkdir claude-practice
cd claude-practice
claude
```

The first run walks you through login (it opens a browser to authenticate with your Claude account) and a couple of preference questions. Defaults are fine.

You land at a prompt. This is a conversation. Type in plain English:

> Create a file called hello.txt containing a haiku about terminals.

Two things happen. First, Claude Code asks permission to write the file, the permission prompt from Module 1, live and in person. Approve it. Second, the file appears. Now verify it: type "Read hello.txt back to me," or open the folder in your file explorer and look with your own eyes.

Stop and notice what you just did, because it's the whole course in miniature: **instruct, permission, action, verify.** Everything from here is that loop with bigger stakes.

## 2.4 Five things worth knowing on day one

Inside a Claude Code session, lines starting with `/` are commands to the tool itself rather than messages to Claude:

| Command | What it does |
|---------|-------------|
| `/help` | Lists everything Claude Code can do. The always-current manual. |
| `/clear` | Wipes the conversation and starts fresh. New task, new clear. |
| `/model` | Shows or changes which Claude model you're using |
| `/config` | Settings: theme, notifications, and so on |
| `Esc` (the key) | Interrupts Claude mid-action. Your brake pedal. |

To leave, type `/exit`, or press `Ctrl+C` twice (the first one just cancels whatever you're typing; you'll see "Press Ctrl-C again to exit"). Your files stay. Only the conversation ends. Relaunching with `claude --continue` picks up your most recent conversation in that folder.

## 2.5 Where to work from

You don't have to `cd` into the right folder every time. Claude Code will launch from wherever your terminal already is, and reach outside that folder when a task calls for it. The permission prompt is the real safety net here, not the folder you happened to launch from: anything outside the working directory, or anything destructive, stops and asks first.

That said, `cd`-ing into the project folder before you start is still a good habit when it's easy. It keeps you oriented, and "everything below here" becomes obvious shared context for both of you. Cleaning up Downloads? `cd Downloads` first. Working on a website project? `cd my-website`. In a hurry, or bouncing between a few things? Just launch and let the permission prompt do its job.

---

## Exercises

1. **Install and verify.** `claude --version` shows a number.
2. **The full loop, three times.** In your sandbox, ask for: (a) a file listing 5 dinner ideas, (b) a second file translating them into another language, (c) both files combined into one nicely formatted `menu.md`. Approve the permissions and verify each result yourself in your file explorer. Reps build the habit. The habit builds the trust.
3. **Use the brake.** Ask Claude to "count from 1 to 1,000,000 in a file" and press `Esc` once it starts. Nothing breaks. Interrupting is allowed, learn that now, while the stakes are a joke file. Then ask it to delete that file.
4. **Ask the tool about itself.** Run `/help`, then ask in plain English: "What can you do with images?" Interrogating the tool is a skill that pays forever, because the tool keeps changing and the skill doesn't.

## Common snags

- "command not found" right after installing: close and reopen the terminal.
- Login loop, or the browser doesn't open: copy the printed URL into your browser manually.
- Nervous about permission prompts: for this whole course, when in doubt, read what it's asking. If the action is inside your sandbox or project folder, approve it. Module 7 covers loosening and tightening this deliberately.

## Checkpoint

You're ready for Module 3 when Claude Code launches, you've created and verified real files with it, and you know how to interrupt (`Esc`) and exit (`/exit`, or `Ctrl+C` twice).
