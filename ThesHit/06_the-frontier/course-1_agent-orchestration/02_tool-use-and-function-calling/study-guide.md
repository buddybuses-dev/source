# Module 2: Tool Use and Function Calling — Study Guide

## How Agents Act on the World, and How You Keep That Safe

## What This Module Covers

This module covers how agents interact with external tools, APIs, and services: what tool use fundamentally adds, how agents select tools, the Model Context Protocol, and the discipline of access, validation, and logging that keeps a tool-wielding agent from becoming a liability.

Here's your real situation: tool use is the line between an agent that talks and an agent that acts. The ability to act beyond text: querying live systems, retrieving data, executing operations, is where the real value of agent systems lives. It's also where the real risk lives. An agent that can only write text can embarrass you. An agent with a delete tool and no confirmation gate can destroy something.

At this tier you're the architect of the contract between agents and the systems they touch. You decide which tools exist, how they're described, what access they carry, what gets validated, and what gets logged. The agent selects and calls. The boundaries are yours.

## Why It Matters

Every capability you wire into an agent is a capability that runs at machine speed, without fatigue, and without the instinct that makes a human pause before doing something irreversible. A tool architecture with sloppy access, no validation, and no logs works fine right up until the day it charges a card twice, deletes the wrong records, or follows instructions it found inside a fetched web page. By then the question isn't whether damage happened. It's whether you can even reconstruct what the agent did.

The discipline is well understood, and most builders skip it anyway: minimum access, defined contracts, validated results, gated destructive actions, and a complete audit trail. The builders who internalize it ship agent systems that enterprises trust with production access. The ones who don't ship demos. This module teaches you the difference.

## Module Certification Goal

You can architect an agent's toolset with minimum necessary access, clear contracts, and confirmation gates on consequential actions, diagnose tool selection failures through descriptions and scoping, and instrument every call so the system's behavior is verifiable after the fact.

## What You Need to Know

- **Tools turn talk into action:** Tool use adds the ability to act beyond text: querying live systems, retrieving data, executing operations. Even the most capable model needs them, because its knowledge is frozen and internal; tools connect it to live data and let it act on systems. Direct a dedicated tool into existence when a job needs precision, repetition, or real system access that reasoning can't guarantee. And when a step is mechanical, remember from Module 1 that plain automation may beat an agent entirely. Tools are power, and the rest of this module is about handling power.
- **Selection runs on descriptions, and bloat ruins it:** Agents choose tools by reading names and descriptions. When an agent ignores a perfect tool, the most common cause is that the name and description don't clearly convey when to use it. When it grabs the wrong tool, like web search instead of the internal database, look at how the tools are described and scoped: overlapping or vague descriptions ruin selection. And selection burden grows with the toolset: forty attached tools make choices worse, not better. When two tools could both do the job, the system should decide on task fit: scope, cost, and reliability against what the step needs. Curate the toolset like you'd curate the portfolio: few, sharp, unambiguous.
- **MCP standardizes the wiring:** The Model Context Protocol solves the connection problem: a standard way to connect agents to tools and data sources, instead of custom wiring per pair. It's why your toolset can be assembled from governed building blocks instead of hand-rolled integrations. Every tool, MCP or otherwise, should define exactly what inputs it accepts and in what form, so bad calls get rejected early and the tool stays predictable. And when a tool can return thousands of records, shape it at the tool layer: paginate, filter, or summarize, so the agent gets what it needs, not a flood.
- **Access is minimum, credentials stay out of context:** An agent reading customer records gets the minimum required: read access to the relevant records, nothing more, revocable anytime. Credentials live in the tool's infrastructure, not the agent's context, so conversations hold no secrets. Destructive actions, like permanent deletion, sit behind a confirmation gate: human approval or a strict check before the call executes. And the big one: money movement runs through an approval workflow: the agent prepares the action, a human authorizes it, then it runs. The agent proposes. Authority stays with you.
- **Results are data, never orders:** A well-built system validates every tool result before acting: is it sane, complete, and does it match what the task needs? When a call fails mid-task, the behavior is deliberate: retry if transient, try an alternative, or report the failure clearly. Never fabricate a result to keep moving. Design for the retry problem: if an action isn't safe to repeat, like charging a card, a network hiccup plus an automatic retry causes real damage, so consequential actions must be safe against duplication. And the sharpest edge: content returned by a tool that contains instructions, like "ignore your previous directions," is untrusted data, never commands. Fetched content must not steer the agent's behavior. That single principle blocks an entire class of attack.
- **Chains, limits, and the audit trail:** When one tool's output feeds another's input, verify between links: check each output fits the next input before continuing. Respect external services' limits: pace calls, batch where possible, back off when throttled. Test every tool directly and independently with known inputs before an agent depends on it, and run the whole toolset in a safe environment against test data before it touches production. Then log every call with inputs and results: the log is your audit trail, showing what the agent actually did when you must verify or debug. In production, monitor volume, cost, error rates, and unusual patterns: the signals that reveal drift or abuse before an invoice or an incident does.

## Your Toolkit

- **Claude Code:** Where you build, wire, and exercise toolsets, with subagents and structured workflows to test tool behavior under real conditions.
- **MCP servers:** The standard layer connecting agents to tools and data sources, with defined contracts instead of custom wiring per pair.
- **A staging environment:** The same tools running against test data, where behavior gets proven before production access exists.
- **Logging and monitoring (your platform's dashboards or a tool you direct AI to build):** The audit trail of every call, and the volume, cost, and error signals that catch drift early.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- Can you explain what tool use fundamentally adds, why capable models still need tools, and when a dedicated tool beats plain reasoning?
- Can you diagnose an agent ignoring the right tool or choosing the wrong one, and explain what toolset bloat does to selection?
- Can you identify what the Model Context Protocol solves, and why defined inputs make a tool predictable?
- Can you architect access correctly: minimum necessary, credentials in infrastructure, confirmation gates on destructive calls, and approval workflows for money?
- Can you handle results properly: validation before acting, deliberate failure handling, and treating embedded instructions in fetched content as untrusted data?
- Can you design against unsafe retries, verify between chain links, and respect external service limits?
- Can you specify what tool testing requires before an agent depends on it, and what must exist before tools touch production?
- Can you name what gets logged and monitored in production tool usage, and why the audit trail matters?

## Common Pitfalls

These are the mistakes vibecoders make most often at this stage. No judgment, they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- You grant broad access because scoping feels slow. Full database control, because restricting the agent felt like limiting its intelligence. Access isn't intelligence. Minimum required, revocable anytime, and the agent's capability comes from good tools, not wide keys.
- You attach every tool you have. Forty tools felt like forty capabilities, and selection quality fell off a cliff. Overlapping, vaguely described options degrade every choice. Curate hard: few tools, sharp descriptions, unambiguous scopes.
- You trust whatever comes back. The tool returned something, so the agent acted on it, and the something was incomplete. Validate every result before acting: sane, complete, matching the task. And when a fetched page says "ignore your previous instructions," that's data to be handled, never a command to be followed.
- You let the agent hold the keys. Credentials pasted into instructions travel with every conversation, into every log, past every boundary. Secrets live in the tool's infrastructure. Conversations hold none.
- You make destructive actions ordinary. Delete and pay sat next to read and search, called the same way. One retry after a network hiccup and a card gets charged twice. Gate the consequential calls: confirmation for destruction, approval workflows for money, and duplication safety on anything that can't safely repeat.
- You skip the logs until you need them. Everything worked, so logging felt like overhead, and then something went wrong with no record of what the agent actually did. The audit trail is not optional. It's the difference between debugging and guessing.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Does every tool in your system carry the minimum access its job requires, revocable anytime?
- Are credentials held in tool infrastructure, with zero secrets in any agent's context?
- Do destructive and financial actions sit behind confirmation gates or approval workflows?
- Does your system validate tool results before acting, and treat instructions inside fetched content as untrusted data?
- Have you tested every tool directly with known inputs, and the full toolset in a safe environment?
- Are consequential actions safe against accidental duplication from retries?
- Could you reconstruct everything your agent did last Tuesday from the logs?

## AI Audit Prompt Template

Copy this prompt into your AI assistant to get a quick health check on your agent's tool architecture. It checks the same things the certification exam covers.

> Review my agent's tool configuration and check the following. For each one, tell me pass or fail with a specific example: Access: Here are my tools and their permissions [list them]. Does each carry only the minimum access its job requires, and where do credentials live? Selection: Here are my tool names and descriptions [paste them]. Are any overlapping, vague, or likely to cause wrong-tool selection, and is the toolset small enough to choose from well? Gates: Which tools can destroy data or move money, and what confirmation or approval stands in front of each? Validation: Does the system check tool results for sanity and completeness before acting, and how does it treat instructions embedded in fetched content? Failure and retries: What happens when a call fails mid-task, and is every consequential action safe against duplication? Audit: Could I reconstruct the agent's actions from logs, and what monitoring would catch unusual volume, cost, or error patterns? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 2 exam. The best way to prepare: harden a real toolset. Take an agent you run today, strip its access to minimum, gate anything destructive, add result validation, and try to break it with a fetched page containing hostile instructions. Every hole you find and close is exactly what the exam tests.

## Certification Pathway

- **Frontier Specialist — Agent Orchestration:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush, take the time to build something real first.

---

Ready? Take the Tool Use and Function Calling Exam →
