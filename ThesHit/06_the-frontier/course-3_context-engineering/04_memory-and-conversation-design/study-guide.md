# Module 4: Memory and Conversation Design — Study Guide

## Context Engineering

### T8 The Frontier | Module 4 Study Guide

## Memory and Conversation Design

> "Direct AI to design what your system remembers, what it forgets, and how it recalls the difference."

## Why This Matters

Users experience memory as intelligence. An assistant that forgets the client's name by message thirty feels broken no matter how sharp its answers are, and one that remembers last month's project details feels like a colleague. Memory is also where windows quietly fill up, so designing it well solves retention and budget in one move.

## Core Concepts

**Memory is context management, not database design.** The model has no memory between calls; every call starts blank. "Memory" is whatever your system chooses to place back into the window. The design question is never "how do I store this?" Storage is trivial. The question is "what earns its way back into context, and when?"

**Short-term memory is conversation history.** The recent back-and-forth, replayed into the window each call. It is cheap to implement and expensive to keep: unbounded history is the most common window-killer in production systems.

**Long-term memory is stored and selective.** Summaries of past sessions, user profiles, project context, stated preferences: persisted outside the window and injected when relevant. Long-term memory is deliberate; nothing enters it unless your system decides to write it.

**Memory compression.** As history grows, summarize older messages into a compact digest and keep recent messages verbatim. The window then carries a summary of the distant past, full detail of the near past, and the current message. Compression is lossy by design; the craft is losing chatter while keeping decisions, facts, and commitments.

**What to remember, what to forget, how to recall.** A memory system answers three questions. Remember: durable facts, preferences, decisions, open tasks. Forget: greetings, dead ends, resolved clarifications. Recall: inject always (small profiles), inject when relevant (retrieval over memories), or inject on schedule (session summaries at session start).

**Session versus persistent architectures.** Session memory lives for one conversation and dies with it, which is right for one-off tools and privacy-sensitive flows. Persistent memory survives across sessions, which is right for ongoing client relationships. Choose per use case; persistent memory adds real obligations around accuracy and staleness.

## How It Works

A working memory loop looks like this. During the conversation, replay recent history verbatim. When history crosses a token threshold, direct the model itself to summarize the oldest portion, then replace those messages with the summary. At session end, extract durable facts and decisions into a persistent store keyed to the user or project. At session start, inject the relevant stored memories: small ones wholesale, large ones through retrieval. Log what memory entered each call, because stale memory bugs look exactly like model errors.

## Directing AI

1. "Design a memory policy for this assistant: what to remember, what to forget, and the recall rule for each memory type. Present it as a table before implementing."
2. "Direct the system to summarize conversation history older than 2,000 tokens into a digest that preserves decisions, facts, and open tasks, and drop the original messages."
3. "At session end, extract durable facts and preferences from this transcript into the user profile, and show me the diff before saving."
4. "At session start, inject the user profile and the last session summary above the conversation, clearly labeled as memory with dates."
5. "Add an expiry review: flag stored memories older than 90 days for confirmation instead of injecting them as current fact."

## Common Mistakes

1. Replaying entire history forever, until the window is all small talk and the system forgets its instructions.
2. Storing everything, which makes recall a search problem through noise instead of a lookup of signal.
3. Summarizing away the wrong things: keeping pleasantries, losing the budget figure the client committed to.
4. Injecting stale memory as current fact, so the system confidently references a plan that changed last month.
5. Building persistent memory for a tool that runs one-off tasks and needed none.
6. Never labeling injected memory, so the model cannot distinguish stored history from the live conversation.

## Real-World Application

A builder runs a project assistant for a marketing agency, and the team loves it until it starts confidently citing a campaign budget from three weeks earlier that the client has since cut in half. The stored summary was accurate when written and stale when recalled. The builder directs AI to add dates to every stored memory, inject them under a labeled "project memory, last updated" header, and instruct the model to treat dated memories as of that date rather than as current truth. The builder also adds a session-end diff so new decisions overwrite old ones instead of piling beside them. The assistant stops time-traveling, and the agency starts trusting it with client calls.

## Decision Framework

- Conversations short and self-contained? Session memory only; skip persistence entirely.
- Users returning across weeks? Persistent profile plus session summaries, injected at start.
- History eating the window? Compress: summarize old messages, keep recent ones verbatim.
- Facts contradicting current reality? Add dates and an update path; staleness is the bug.
- Many stored memories, few relevant per query? Recall through retrieval instead of injecting everything.
- Deciding what to store? Store decisions, durable facts, preferences, open tasks; drop the chatter.

## Tool and Platform Notes

You rarely need special infrastructure: history compression is a summarization call, profiles fit in Postgres or even JSON, and large memory stores can reuse the Module 3 retrieval stack with memories as chunks. Provider-side features like Claude Projects or ChatGPT memory show the pattern but are not a substitute when you need control over what your product remembers. Direct AI to build the loop; it is policy plus plumbing, not exotic tech.

## Key Takeaways

- Memory is choosing what re-enters the window, not choosing a database.
- Compress history: summarize the old, keep the recent verbatim, protect decisions and facts.
- Persistent memory needs dates and update paths, or it becomes confident staleness.
- Match architecture to relationship: session memory for one-offs, persistent for ongoing work.
- Label injected memory so the model knows stored context from live conversation.

## What's Next

Module 5 assembles everything dynamically: choosing per query what mix of memory, retrieval, and tool output the context should contain, decided at runtime by an orchestration layer.

## Exam Prep Notes

Expect scenarios on stale memory, runaway history, and choosing session versus persistent architectures. Know the three memory questions (remember, forget, recall), how compression works and what it must preserve, and why memory is framed as context management rather than storage.

———

*Matt Murphy AI | The Faction Group LLC | mattmurphy.ai*
