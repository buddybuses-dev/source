# Module 7: Ship: Professional Prompt Architecture — Study Guide

## Prompt Engineering at a Professional Level

### T8 The Frontier | Module 7 Study Guide

## Module 7: Ship: Professional Prompt Architecture

> "Direct AI with the precision, structure, and repeatability that separates professionals from hobbyists."

## What This Module Covers

This is the capstone. Everything from the first six modules converges into one deliverable: a complete, production-grade prompt system for a real application. You start with requirements, translate them into a layered architecture, wire in the reasoning patterns from M3, manage context using M4, prove correctness with the evaluation discipline from M5, and deploy with the production patterns from M6. Nothing here is theoretical. You ship.

The second half treats your prompt system as a product artifact: documentation another engineer can pick up cold, version control, changelogs, a test suite that runs before every change, and monitoring that tells you when quality drifts or a model update quietly changes behavior underneath you. You also learn the judgment call that defines senior prompt engineers: when a failing system needs a prompt refactor, and when it needs a different model. Get this wrong and you burn weeks polishing prompts no wording can save.

## Why It Matters

A customer support bot handling 10K conversations a day is not a clever prompt. It is a system with requirements, failure modes, and a budget. When it breaks at 2 AM, someone who is not you needs to read your docs, run your tests, find the regression, and ship a fix. If your architecture lives in your head, or in an untitled doc with seventeen unlabeled versions, you built a liability, not a product.

The Faction builds by directing AI, and the prompt layer is where that direction lives. In a content pipeline producing brand-voice output at scale, or an extraction system where one hallucinated field corrupts a database, the prompt is the most business-critical code in the stack. Professionals version it, test it, monitor it, and document it. Hobbyists paste it into a chat window and hope. This module is the line between the two.

## Certification Goal

Passing this exam proves you can take an application from requirements to a deployed, documented, monitored prompt system: one another engineer can maintain, with a test suite guarding every change, that you can debug in production with data instead of guesswork.

## What You Need to Know

### Requirements to Architecture Translation

Before writing a single instruction, extract requirements: what the system must do, what it must never do, format contracts, and failure tolerances. Those map onto architecture decisions: what belongs in the system prompt, what gets injected per request, and which tasks split into stages. A support bot's escalation rules are requirements first, prompt text second.

### Layered Prompt Architecture

Production prompt systems are layered, not monolithic. A stable system layer carries identity, rules, and format contracts. A dynamic context layer injects retrieved documents and user data. A task layer carries the specific request. You can change one layer, rerun the tests, and ship without touching the rest.

### The Prompt as a Product Artifact

Your prompt lives in version control with a semantic version, a changelog entry for every edit, and an owner. Every version ties to the eval results that justified shipping it. When someone asks why v2.3.1 phrases the refund policy that way, the answer is in the repo, not your memory.

### Documentation for Handoff

Maintenance docs answer four questions: what each section does, why it is written that way, what breaks if you change it, and how to run the tests. Document the failure modes you already fixed, or the next engineer will reintroduce them. The standard: an engineer who has never seen your system can ship a safe change in a day.

### Production Performance Measurement

In production you measure what your M5 evals measured offline: format compliance, accuracy on sampled outputs, escalation rates, latency, and cost per request. Sample real traffic continuously, because aggregates hide drift. A 2 percent rise in malformed JSON from your extractor is a fire alarm, not a rounding error.

### Refactor the Prompt or Change the Model

Refactor when failures are instruction-shaped: misread format rules, an edge case you never specified. Change the model when failures are capability-shaped: reasoning depth or consistency ceilings no prompt variant can cross. If your best three candidates all plateau below the quality bar on the same eval set, the prompt is not the problem.

## Your Toolkit

- **Prompt Repository with Versioning**: Every prompt in git with semantic versions, changelogs, and eval results per release. The source of truth that makes rollback and handoff possible.
- **Regression Test Suite**: A fixed set of representative and adversarial cases that runs before any change deploys. No green suite, no ship.
- **Production Monitoring Dashboard**: Live tracking of format compliance, sampled quality scores, latency, and cost, with alerts on drift thresholds.
- **Architecture Decision Record**: A short note per major design choice: what you decided, why, and what you rejected. The difference between documentation and archaeology.

## Exam Topics

- Translating requirements into a layered prompt architecture, and what belongs in each layer
- The full ship pipeline: requirements, architecture, drafting, evaluation, deployment, monitoring
- Semantic versioning for prompts and what belongs in a changelog entry
- The four questions maintenance docs must answer for a handoff to succeed
- Production metrics: format compliance, sampled quality scores, escalation rates, latency, cost per request
- Detecting and responding to output drift, including drift from upstream model updates
- The refactor-vs-model-change framework and the eval plateau signal that drives it
- How M5 evaluation suites become production regression gates

## Common Pitfalls

- **Shipping a monolith**: One giant prompt means every change risks everything, and no one can safely maintain it but you.
- **Documentation as an afterthought**: Docs written from memory weeks later lose the why behind every decision, so the next engineer reintroduces bugs you already fixed.
- **No regression gate**: Editing a live prompt without rerunning the tests is how a one-word tone tweak silently breaks JSON output for 10K conversations.
- **Monitoring launches, not operations**: Checking quality only at launch misses drift. Model updates and shifting traffic degrade systems that tested perfectly.
- **Refactoring past the plateau**: Rewording for weeks when evals show a capability ceiling wastes the one resource builders never have enough of: shipping time.
- **Versioning by vibes**: Files named final_v2_REAL mean you cannot roll back, diff, or tie an incident to the change that caused it.

## Self-Assessment Checklist

- I can translate application requirements into a layered prompt architecture.
- I can take a prompt system from draft through evaluation to deployment with a regression gate at every change.
- I can write maintenance docs that let another engineer ship a safe change without my help.
- I can define and instrument the production metrics that matter for my application.
- I can detect output drift and trace it to a prompt change, model update, or traffic shift.
- I can decide, with eval data, between a prompt refactor and a model change.
- I can manage a prompt repo with semantic versions, changelogs, and eval results per release.

## AI Audit Prompt Template

Before you ship, give your AI this prompt along with your complete architecture, docs, and test suite.

`You are a senior prompt architecture reviewer performing a pre-ship audit of my complete prompt system: layered prompts, requirements, maintenance docs, test suite, and monitoring plan. Report findings by severity (blocker, warning, suggestion) against these criteria: 1. Requirements coverage: Identify any requirement with no corresponding instruction, example, or test case. 2. Architecture: Flag anything in the system layer that should be dynamic, anything dynamic that should be stable, and any prompt doing work that should be split into stages. 3. Contract integrity: Verify format rules are unambiguous and each has a test asserting it. 4. Failure handling: Identify inputs (empty, adversarial, off-topic, oversized) with no defined behavior. 5. Documentation: Using only my docs, state what each section does, why it exists, what breaks if changed, and how to run the tests. Flag anything the docs cannot answer. 6. Test suite: Identify untested edge cases and any test that passes even if its target instruction were deleted. 7. Monitoring: Confirm each metric has a threshold and an alert owner. End with a ship or do-not-ship call and the three highest-impact fixes.`

## What's Next

Ship your capstone, pass the exam, and claim your Advanced Prompting Specialist badge. This course is the foundation of T8 The Frontier: every other Frontier course assumes this skill. The builders doing the most ambitious work in The Faction all stand on it. Now it is yours.

## Certification Pathway

Pass this module exam at 80 percent (20 of 25) to earn the Module 7 badge. Pass all 7 module exams to earn the Advanced Prompting Specialist badge.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
