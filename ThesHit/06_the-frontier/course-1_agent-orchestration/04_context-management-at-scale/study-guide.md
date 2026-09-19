# Module 4: Context Management at Scale — Study Guide

## Windows, Memory, State, and Knowing When to Summarize, Retrieve, or Reset

## What This Module Covers

This module covers the discipline that determines whether long-running AI work stays sharp or quietly rots: context windows, memory systems, conversation state, and the judgment calls between summarizing, retrieving, and resetting. It's the least visible skill in orchestration and the one that separates builders whose systems improve over weeks from builders whose sessions degrade by lunch.

Here's your real situation: the context window is the working memory an agent can attend to at once. Everything it acts on must fit inside it, and everything inside it competes for attention. Treat that space carelessly and you get the classic symptoms: forgotten early instructions, contradictions with prior decisions, and drifting quality. Treat it as the scarce, expensive workspace it is, and long-running efforts stay coherent across sessions, resets, and weeks.

You're the architect of what the agent knows at every moment. You decide what enters the window, what lives outside it, what gets compressed, and when a session's history stops earning its space. The model attends. You curate.

## Why It Matters

Context failures are the most expensive failures in agent work because they masquerade as model failures. The session that starts brilliant and turns sloppy, the agent that violates a rule stated hours ago, the fresh session that contradicts a locked decision: none of these are the model getting worse. They're context management getting neglected. Builders who don't understand that blame the model, restart randomly, and lose the same work twice.

The stakes compound in multi-session and multi-agent work. A summary that silently dropped a constraint becomes a wrong decision three sessions later. Small early errors that never got corrected become precedent the system keeps building on. Conflicting versions of a project detail across sessions become an argument nobody can settle. Every one of these has a design answer, and every design answer is cheaper than the failure. This module teaches you all of them.

## Module Certification Goal

You can budget and curate context so long-running sessions stay sharp, architect external state, retrieval, and memory so nothing critical lives only in a conversation, and make the summarize-retrieve-reset call correctly, including clean handoffs between sessions.

## What You Need to Know

- **The window is working memory, and degradation has symptoms:** The context window is the working memory an agent can attend to at once; everything it acts on must fit inside it. A degrading session shows itself: forgotten early instructions, contradictions with prior decisions, drifting quality. Noise accelerates it: pages of irrelevant tool output compete for attention, diluting what matters. Context budgeting is the answer at planning time: deciding up front what deserves space, instructions, state, materials, so the whole job fits. And discipline pays twice, because every token in context is billed on every call: lean context is better quality and lower cost and latency on every single turn.
- **Summarize, retrieve, or reset: three moves, three moments:** Summarization fits when history matters but detail doesn't: compress the past so the present stays sharp. Retrieval beats stuffing everything up front because pulling only what the current step needs keeps attention focused and capacity available; good retrieval is relevance and precision, surfacing the few pieces the step needs, not everything related. A searchable knowledge store holds the long tail of material, letting sessions pull relevant pieces on demand. And a fresh session is right when the current session's quality is visibly degrading and its accumulated history isn't earning its space. Reset without fear. The work survives resets when state lives outside, which is the next concept.
- **Authoritative state lives outside the conversation:** The state of a long project lives outside any session, in files or systems of record, with sessions reading from it. Sessions start empty: anything the agent should know must be provided or retrieved by design, and no provider courtesy changes that. Log permanently what you'll need when sessions are gone: decisions, outcomes, and key artifacts. When multiple sessions and documents disagree, the fix is structural: a designated source of truth that every session reads from and updates through one path. Memory design for a weeks-long job means deciding what gets written down, where, and how sessions load the right slice of it back.
- **Keep the record clean or it poisons the work:** Two failure patterns deserve names. First, stale decisions: when an early decision gets reversed hours later, the context holds both versions, and the agent may act on the dead one. Superseded decisions get explicitly retired. Second, context poisoning: small early errors that keep getting repeated and built upon, compounding as precedent. The fix is to correct the record explicitly or reset. And when critical rules stated at the start of a long session start being violated, re-anchor them: restate key rules periodically or put them somewhere the agent always re-reads. Rule decay is real, and design slows it.
- **Separate thinking from producing:** Run separate sessions for strategy and heavy production, because bulk production output floods the context, crowding out the judgment the strategy thread needs. This is the same separation you learned as a process standard in delivery work, now stated as architecture: the thread that decides and the thread that produces have different context needs, and mixing them degrades both.
- **Handoffs carry state, and strategies get tested:** A good handoff summary between sessions carries state, decisions, constraints, and next steps: what the next session needs to act correctly. Compression loses detail, so critical constraints need explicit carryover; the fresh session that violated a key constraint got a summary that silently dropped it. When context is nearly full and something must go, cut stale, low-value bulk: old raw outputs and resolved threads, never active constraints. And context strategy is empirical: test it by running the same long workload under different strategies and comparing output quality. Feel is not a measurement.

## Your Toolkit

- **Claude Code:** Long-running work with explicit context control: what loads, what persists in project files, and when a session resets.
- **An external state store (files, a database, or Notion):** The system of record for decisions, constraints, and project state that every session reads through one path.
- **A searchable knowledge store (retrieval over your documents):** The long tail of material, pulled piece by piece as steps need it instead of stuffed up front.
- **Claude or ChatGPT:** Drafts and maintains your handoff summaries, decision logs, and the re-anchoring blocks your long sessions re-read.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- Can you define the context window in practical terms and recognize the symptoms of a degraded session?
- Can you choose correctly between summarization, retrieval, and a fresh session for a given situation?
- Can you identify what belongs in persistent memory versus the conversation, and why sessions start empty by design?
- Can you architect authoritative state: external systems of record, permanent logging, and a designated source of truth across sessions?
- Can you diagnose stale-decision risk and context poisoning, and apply explicit retirement, correction, or reset?
- Can you apply context budgeting, re-anchor decaying rules, and explain why context discipline is also a cost discipline?
- Can you justify separating strategy sessions from production sessions, and identify what noise does to attention?
- Can you construct a handoff summary that carries constraints explicitly, choose what to cut when context fills, and test a context strategy empirically?

## Common Pitfalls

These are the mistakes vibecoders make most often at this stage. No judgment, they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- You push the marathon session past its death. Quality is visibly sliding, but the session "knows so much" that abandoning it feels like waste. The accumulated history stopped earning its space hours ago. Externalize the state, write the handoff, reset without fear.
- You stuff instead of retrieve. Every document goes in up front, just in case, and attention drowns in material the current step never needed. Retrieval exists so each step gets its few relevant pieces. The knowledge store holds the rest until asked.
- You let the conversation be the system of record. Decisions, constraints, and project state live only in a session's memory, and one reset erases the project's mind. State lives outside, in one governed place, and sessions load their slice of it. This is Module 1's single source of truth, applied to memory.
- You keep both versions of a reversed decision. The morning's choice and the afternoon's reversal sit side by side in context, and the agent builds on whichever it attends to. Retire superseded decisions explicitly. A record that contains its own contradictions isn't a record.
- You hand off with a summary that dropped the constraint. The compression read clean, the new session started fresh, and a locked rule vanished in transit. Critical constraints get explicit carryover, listed by name, never trusted to summarization.
- You evaluate context strategy by feel. The new approach "seems better," which is how expensive habits survive. Run the same workload under both strategies and compare the output. Context management is an engineering discipline. Measure it like one.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Can you name the degradation symptoms that would tell you a session needs a reset?
- Does your long-running work keep authoritative state in an external system of record with one update path?
- Do you budget context before big tasks: instructions, state, and materials sized to fit the whole job?
- Are superseded decisions explicitly retired, and do critical rules get re-anchored in long sessions?
- Do you run strategy and heavy production in separate sessions?
- Does your handoff template carry state, decisions, constraints, and next steps, with constraints listed explicitly?
- Have you ever tested two context strategies against the same workload and compared results?

## AI Audit Prompt Template

Copy this prompt into your AI assistant to get a quick health check on your context management. It checks the same things the certification exam covers.

> Review my context management for long-running AI work and check the following. For each one, tell me pass or fail with a specific example: State architecture: Here is where my project state lives [describe it]. Is authoritative state external to any conversation, with one governed update path, or would a session reset lose it? Budgeting: For my current long task [describe it], what deserves context space: instructions, state, materials, and what is bulk that belongs in retrieval? Record hygiene: Here are my recent decisions and reversals [paste them]. Are superseded decisions explicitly retired, and are there early errors being built on as precedent? Session discipline: Am I separating strategy from heavy production, and what symptoms would trigger a reset? Handoff: Here is my latest session handoff [paste it]. Does it carry state, decisions, constraints, and next steps, with critical constraints explicit rather than summarized away? Cost: Given my context sizes and call volume [estimate them], what is context bloat costing per week? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 4 exam. The best way to prepare: take your longest-running current project and rebuild its memory architecture: external state file, decision log with retirements, a handoff template, and a deliberate reset. If the fresh session picks up the work without missing a constraint, you've built it right. That continuity is exactly what the exam tests.

## Certification Pathway

- **Frontier Specialist — Agent Orchestration:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush, take the time to build something real first.

---

Ready? Take the Context Management at Scale Exam →
