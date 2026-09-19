# Module 1: Why AI-Generated Code Fails Differently — Study Guide

## Vibecoder Security Audit Method

T6 The Vault | Module 1 Study Guide

Direct AI to find the failure patterns that only AI-generated code produces.

## What This Module Covers

This module establishes why AI-generated code has its own security failure patterns, distinct from what traditional code review was built to catch. You will learn pattern replication, insecure training data leakage, hallucinated security, missing defense-in-depth, inconsistent posture across sessions, and the false confidence effect.

## Why It Matters

The audit method you are learning exists because vibebuilt code fails differently. A human developer writes one vulnerable endpoint at a time; an AI replicates a vulnerable pattern across forty files in a single session. A human forgets to add auth to one route; an AI produces code that looks secured, reads as secured, and passes a casual review while the actual enforcement is missing. Builders who audit AI-generated code with human-era checklists find what those checklists were designed to find and miss the failure class that actually ships today. Understanding these patterns is what separates an auditor who runs tools from a Code Audit Specialist who knows where the bodies are buried.

## Certification Goal

Passing this exam proves you can name and recognize the distinct failure patterns of AI-generated code, explain why each one emerges from how AI produces code, and articulate why traditional review practices systematically miss them.

## What You Need to Know

1. Pattern replication multiplies single flaws into systemic ones. When AI generates code, it reuses the patterns it establishes. One insecure pattern, a raw SQL string, a missing permission check, an unvalidated input, gets stamped into every file that follows the same shape. In human code, a flaw is usually an incident; in vibebuilt code, it is usually a family. The audit consequence: when you find one instance, you direct AI to search the entire codebase for the pattern, because siblings almost certainly exist.

2. Training data leaks insecure patterns. Models learned from decades of public code, including its outdated tutorials, deprecated crypto, and copy-pasted Stack Overflow answers. AI can confidently produce authentication flows, hashing choices, and configuration patterns that were common in the training data and are known-bad today. The code is not random; it is yesterday's standard practice, which is precisely why it looks plausible to a casual reviewer.

3. Hallucinated security looks secure but is not. This is the signature failure. AI produces the shape of security: a middleware file named auth, a sanitize function that is imported but never called, a rate limiter configured but not attached to routes, comments describing protections the code does not implement. The presence of security-shaped code satisfies readers who skim structure instead of tracing execution. The audit discipline: verify enforcement, not existence. Trace whether the check actually runs on the path that matters.

4. Missing defense-in-depth. Prompted for a feature, AI builds the feature's happy path with a single layer of protection at best. Human security engineering assumes layers: validate at the edge, check at the API, enforce at the database. Vibebuilt systems commonly hang everything on one check, often client-side, so a single bypass opens the whole system. Auditors look for the second and third layer, and usually find air.

5. Inconsistent posture across sessions. AI has no memory of the standards it applied yesterday. Code generated across multiple sessions, prompts, or tools shows different auth patterns, different validation styles, and different error handling in different corners of one codebase. Attackers only need the weakest corner. The audit consequence: sampling a well-built module tells you nothing about its neighbors; posture must be verified per area, not inferred globally.

6. The false confidence effect. Clean, well-commented, professionally formatted code creates a trust response in reviewers. AI output maximizes exactly those signals regardless of underlying security. Founders read fluent code as competent code and skip the audit. The effect compounds: the better the model's style, the stronger the unearned trust. This is why the method insists on evidence over impressions, execution traces over code aesthetics, and RED/YELLOW/GREEN grades backed by findings rather than vibes.

## Your Toolkit

- **Pattern search across the codebase (grep and AI-directed search):** turning one finding into the full family of instances
- **Execution tracing:** following a request from entry to effect to verify checks actually run
- **Session archaeology:** commit history and file dating to map which areas came from which generation sessions
- **The CADE 13-layer stack (Module 2):** the framework that makes coverage systematic instead of impressionistic

## Exam Topics

- Pattern replication and why one finding implies a family
- Training data leakage of outdated and insecure practices
- Hallucinated security and verifying enforcement over existence
- Single-layer protection vs defense-in-depth expectations
- Cross-session inconsistency and per-area posture verification
- The false confidence effect on reviewers and founders
- Why traditional checklists miss AI-specific failure classes
- The auditor's evidence-over-impressions discipline

## Common Pitfalls

- Fixing the one instance you found and leaving the replicated siblings live
- Accepting a security-named file or imported library as proof the protection is active
- Auditing one module deeply and generalizing its quality to the whole codebase
- Trusting well-formatted, well-commented code because it reads professionally
- Reviewing code structure without tracing whether checks execute on real request paths
- Applying a human-era review checklist and reporting the codebase clean

## Self-Assessment Checklist

- Can I name the six failure patterns and give an example of each?
- When I find a flaw, is my next move a codebase-wide pattern search?
- Do I verify that security code is wired into the execution path, not just present?
- Can I explain why fluent code style says nothing about security posture?
- Do I check each area of a codebase independently rather than sampling?
- Could I explain to a founder why their AI-built app needs a different kind of review?

## AI Audit Prompt Template

> You are auditing an AI-generated codebase for the failure patterns specific to vibebuilt code. Report: (1) replicated patterns: find every instance of each insecure pattern you detect, not just the first, (2) hallucinated security: list every security-shaped construct (middleware, sanitizers, limiters, validators) and verify whether each is actually enforced on live execution paths, (3) defense-in-depth: for each sensitive operation, list the protection layers that exist and flag single-layer designs, (4) consistency: compare auth, validation, and error handling across modules and flag areas with weaker posture, (5) deprecated practices: flag crypto, auth flows, and configurations that reflect outdated standards. Output findings with file references and evidence, not impressions.

## What's Next

Module 2 delivers the framework that turns this understanding into systematic coverage: the complete CADE 13-layer audit stack, with RED/YELLOW/GREEN grading per layer.

## Certification Pathway

This is Module 1 of 7 in the Vibecoder Security Audit Method course, part of T6 The Vault. Passing all seven module exams earns the Code Audit Specialist badge. This module is the threat model the entire method answers.

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
