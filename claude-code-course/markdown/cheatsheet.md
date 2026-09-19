# Claude Code: One-Page Cheat Sheet

Everything from the course, one page. Keep this open. Stop guessing, start looking it up.

## Launching
| | |
|---|---|
| `claude` | Start in the current folder (the "job site") |
| `claude --continue` | Resume the most recent conversation here |
| `cd <folder>` first | Good habit, not a rule. The permission prompt is the real safety net |

## In-session commands
| | |
|---|---|
| `/help` | The always-current manual |
| `/clear` | Fresh start. New task means new clear. CLAUDE.md survives. |
| `/compact` | Condense a long conversation you're not done with |
| `/model` | Switch brains. Escalate for hard or high-stakes tasks. |
| `/init` | Generate a CLAUDE.md for a code project |
| `Esc` | Interrupt mid-action. Always allowed. |
| `Shift+Tab` | Cycle modes: normal, auto-accept, plan mode |
| `/exit` or `Ctrl+C` twice | Exit (your files stay) |
| `#` prefix | Save a note to memory for future sessions |

## The brief (4 parts)
1. **Outcome:** what exists when the work is done
2. **Materials:** where the inputs are
3. **Constraints:** what must and must not happen
4. **Done:** how you'll both know it worked

For anything touching many files, add: "show me a plan and a small sample first."

## Phrases that earn their keep
- "Show me a plan before touching anything."
- "What did you change and why?"
- "What could go wrong with this approach?"
- "Write a check that verifies this a different way, and run it."
- "Good, but..." (a targeted correction beats a restart)
- "Stop fixing. Diagnose first, then propose, then wait."
- "Add that to CLAUDE.md."
- "Commit this." / "Commit first, then let's try it."
- "Undo the changes since the last commit."
- "Turn this into a script / slash command I can reuse."

## Git in English
| Say | Get |
|---|---|
| "Put this project under version control" | git, .gitignore, first commit |
| "Commit this with a sensible message" | Save-point |
| "What changed since the last commit?" | Plain-English diff |
| "Undo changes to X, keep the rest" | Single-file restore |
| "Roll back to how it was Tuesday" | Time travel |
| "Create a private GitHub repo and push" | Off-machine backup |

## Safety defaults (non-negotiable)
- New tool or new territory: sandbox folder first
- Many files: sample before the full run
- Say "don't delete anything" and "never overwrite originals" explicitly
- Money, legal, or outbound email: independent verification, every time
- Loosen permissions in proportion to your undo ability. Git-tracked folder, relax. Unversioned originals, keep the prompts.

## When stuck
1. Say specifically what's wrong, with an example
2. Separate diagnosis from action ("explain first, don't fix yet")
3. Undo, then `/clear`, then re-brief with what you learned
4. Escalate the model (`/model`) for genuinely hard problems

## Is this a Claude Code task?
Repetitive across many items. Format-shifting. Rule-based tedium. Many sources into one document. Anything you'd do if it took 5 minutes but skip because it takes an hour. If you nodded at any of those, stop reading and go delegate it.
