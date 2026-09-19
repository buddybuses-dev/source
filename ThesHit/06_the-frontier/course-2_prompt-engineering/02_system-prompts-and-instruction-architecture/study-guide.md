# Module 2: System Prompts and Instruction Architecture — Study Guide

## "Direct AI with the precision, structure, and repeatability that separates professionals from hobbyists."

## What This Module Covers

Module 1 gave you the maturity model. Module 2 is where you start climbing it. This module teaches you to design system prompts, the persistent instruction layer that controls how a model behaves across every conversation it handles. A system prompt is not a message. It is architecture: it defines who the model is, what it must always do, what it must never do, and exactly what its output looks like.

You will learn the instruction hierarchy professionals use to structure that architecture: role, constraints, output format, examples, edge cases. You will learn why ambiguity is the number one killer of reliability, and the discipline that separates a prompt that works once from one that works ten thousand times: versioning and iteration tracking. In The Faction, you direct AI to build. The system prompt is the steering wheel.

## Why It Matters

Consider a customer support bot handling 10,000 conversations a day. One ambiguous instruction does not produce one bad answer. It produces hundreds of bad answers, every day, each landing in front of a real customer. The same math applies to a brand-voice content pipeline or a data extraction system feeding a database: a vague instruction is a defect deployed ten thousand times. Hobbyists judge a prompt by its best output. Professionals judge it by its worst, because at volume the worst case is guaranteed to happen.

The system prompt is also your leverage point. You cannot review every response your AI generates, but you can control the instruction layer that shapes all of them. A well-architected system prompt is the difference between a system you babysit and a system you trust, and when something breaks at 2 a.m., a versioned prompt lets you roll back in minutes instead of guessing what changed. That reliability is what clients pay for.

## Certification Goal

Passing the Module 2 exam proves you can architect a system prompt using the full instruction hierarchy, eliminate ambiguity that causes inconsistent behavior at scale, and manage prompt changes with versioning discipline. Your prompts are engineered artifacts, not lucky drafts.

## What You Need to Know

### The System Prompt as a Control Layer

The system prompt is the persistent instruction set that governs every interaction, separate from the user messages that flow through it. It sets behavior once and enforces it thousands of times. Everything the model must always do belongs here, not sprinkled into individual requests.

### The Instruction Hierarchy

Professional system prompts follow a deliberate structure: role, constraints, output format, examples, edge cases. Role establishes identity and scope, constraints define hard boundaries, output format specifies structure exactly, examples demonstrate the standard, and edge cases define behavior when inputs get weird. The ordering moves from broad identity to specific behavior and makes prompts scannable, testable, and maintainable.

### Unambiguous Instruction Design

Any instruction that can be read two ways will eventually be read both ways. "Keep responses short" is a guess. "Respond in 2 to 4 sentences, maximum 80 words" is a specification. Replace vague qualifiers with numbers, state implied behavior explicitly, and define every term the model could interpret loosely.

### Constraints: Positive and Negative

Constraints cover what the model must always do and what it must never do. Negative constraints need explicit fallbacks: do not just say "never invent a field value," say "if a field is not present in the source text, output null." A data extraction system that never hallucinates values pairs every prohibition with a defined alternative.

### Edge Case Coverage

Production inputs are hostile: empty messages, off-topic questions, attempts to pull the bot out of scope, malformed data. Your system prompt must define behavior for the inputs you do not want, not just the ones you expect. Unhandled edge cases become improvised behavior, and improvised behavior at scale becomes an incident.

### Prompt Versioning and Iteration Tracking

A prompt that works a thousand times got there through tracked iteration, not luck. Version every system prompt like code: numbered versions, what changed, why, and what improved or regressed. When behavior shifts in production, version history is the difference between a five minute rollback and a rebuild from memory.

## Your Toolkit

- **The Instruction Hierarchy Template:** A reusable skeleton with labeled sections for role, constraints, output format, examples, and edge cases. Start every system prompt here so nothing critical gets omitted.
- **The Ambiguity Audit:** A review pass where you ask of each instruction, "could this be read more than one way?" Any yes gets rewritten with numbers, definitions, or explicit conditions.
- **A Prompt Version Log:** A changelog, whether a markdown file, git repo, or spreadsheet, recording version number, date, what changed, and observed effect. It turns iteration from guesswork into engineering.
- **The Regression Spot-Check:** A fixed set of 5 to 10 test inputs, including known edge cases, run after every prompt change to confirm nothing broke. Module 5 expands this into full evaluation suites.

## Exam Topics

- The five layers of the instruction hierarchy in order: role, constraints, output format, examples, edge cases
- The difference between the system prompt layer and user messages, and what belongs in each
- Rewriting ambiguous instructions into single-interpretation specifications
- Pairing negative constraints with explicit fallback behavior, such as null outputs for missing extraction fields
- Defining handling rules for out-of-scope, empty, and adversarial inputs
- Why a prompt that works once can still fail at production volume, and how worst-case thinking changes design
- The elements of a prompt version log: version number, change description, rationale, observed effect
- When and how to roll back a prompt version after a production regression

## Common Pitfalls

- Stuffing behavior rules into user messages. Rules in individual messages get forgotten, contradicted, or dropped. Persistent behavior belongs in the persistent layer.
- Relying on model judgment for things you could specify. "Use a professional tone" means ten different things. Every open judgment call is a coin flip you run thousands of times a day.
- Prohibitions without fallbacks. "Never make up an answer" with no defined alternative forces the model to improvise, which is exactly what you were trying to prevent.
- Testing only the happy path. A prompt validated on five friendly inputs will meet its first hostile input in production, in front of a customer, with no handling rule.
- Editing prompts in place with no version history. When quality drops, you cannot compare, roll back, or prove what changed. You are debugging blind.
- Letting the system prompt sprawl. Contradictory instructions accumulate across untracked edits until the model starts choosing which rules to follow.

## Self-Assessment Checklist

- I can explain what a system prompt controls and why it is separate from user messages
- I can structure a system prompt using the full instruction hierarchy in order
- I can rewrite an ambiguous instruction so only one interpretation is possible
- I can write negative constraints with explicit fallback behavior
- I can enumerate likely edge cases for a production use case and define handling rules
- I can maintain a version log that lets me trace and roll back any prompt change
- I can explain why worst-case output is the professional standard for prompt quality

## AI Audit Prompt Template

Paste your system prompt into your AI along with this audit prompt to stress-test your instruction architecture before it goes to production.

> You are a senior prompt architecture reviewer. Audit the system prompt below and produce this report: 1. HIERARCHY CHECK: Which of the five layers are present: role, constraints, output format, examples, edge cases? List any missing or out of order. 2. AMBIGUITY SCAN: Quote every instruction that could be read more than one way and propose a single-interpretation rewrite with concrete numbers or conditions. 3. CONSTRAINT AUDIT: Flag every negative constraint that lacks an explicit fallback and propose one. 4. EDGE CASE GAPS: List realistic inputs this prompt does not handle (empty, off-topic, malformed, adversarial) and propose a handling rule for each. 5. SCALE FAILURE FORECAST: Predict the three most likely failure modes across 10,000 real-world runs. 6. VERDICT: Ready, Needs Revision, or Not Production Safe, with one paragraph of justification. Then output a revised system prompt implementing every fix, structured in the five-layer hierarchy. Here is my system prompt: [PASTE YOUR SYSTEM PROMPT HERE]

## What's Next

You now have the architecture layer: a structured, unambiguous, versioned system prompt. Module 3, Few-Shot, Chain-of-Thought, and Structured Reasoning, teaches you what to put inside it: worked examples that lock in format and tone, and reasoning patterns that make complex outputs reliable instead of lucky. Your hierarchy has an examples layer. Module 3 shows you how to fill it.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 2 badge. Pass all 7 module exams to earn the Advanced Prompting Specialist badge and certify at the T8 Frontier tier.
