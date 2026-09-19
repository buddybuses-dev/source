# Module 5: Versioning and Error Design — Study Guide

## API Product Build

### T4 The Mastery | Module 5 Study Guide

## Module 5: Versioning and Error Design

> Direct AI to version deliberately and make every error tell the developer what to do next.

## What This Module Covers

This module covers evolving an API without breaking the developers who depend on it: versioning strategies (URL path, headers, query params), breaking vs non-breaking changes, deprecation policies and sunset headers, migration guides, and error response design (consistent structure, machine-readable codes, human-readable messages, doc links, and the standard error categories).

## Why It Matters

An API is a promise you have to keep while still improving the product. Every developer who integrates is betting their own uptime on your stability, and the moment you break that promise, you break their production system, often silently, often at the worst time. Versioning and error design are the two disciplines that let you evolve without betrayal. Versioning lets you ship new behavior without forcing existing integrations to change on your schedule; error design lets developers handle failures gracefully instead of guessing. Together they are the difference between an API developers trust for years and one they abandon after the first surprise breakage.

## Certification Goal

Passing this exam proves you can choose and apply a versioning strategy, classify changes as breaking or non-breaking, run a humane deprecation process, and design error responses that are consistent, machine-readable, and actionable.

## What You Need to Know

**1. Versioning strategies and their tradeoffs.** The three common approaches: URL path versioning (/v1/, /v2/), which is explicit and easy to route and test; header versioning, which keeps URLs stable but hides the version from casual inspection; and query-parameter versioning, which is simple but clutters requests. URL path versioning is the most common product choice because it is visible and unambiguous: a developer can see exactly which version a request targets. Whatever you choose, consistency matters more than the specific mechanism, because the version is part of the contract every request carries.

**2. Breaking vs non-breaking changes.** The core competence: knowing which changes force consumers to update. Non-breaking (safe to ship anytime): adding a new endpoint, adding an optional field to a response, adding an optional request parameter. Breaking (require a new version): removing or renaming a field, changing a field's type, removing an endpoint, making an optional parameter required, changing default behavior, or tightening validation. The rule of thumb: adding is safe, changing and removing are not. Misjudging this is how APIs break integrations while the team believes they shipped a harmless update.

**3. Deprecation policies and sunset headers.** When you do need to retire something, you do it on a published timeline, not abruptly. A deprecation policy states how much notice developers get before a version or endpoint is removed. Sunset headers (and deprecation headers) communicate this in-band: the API itself tells the developer, in the response, that the endpoint they are calling is deprecated and when it will stop working. This turns removal from a surprise outage into a scheduled migration the developer can plan around.

**4. Migration guides that do not break integrations.** A new version needs a migration guide that walks developers through exactly what changed and how to adapt, field by field, endpoint by endpoint. The goal is that a developer can follow the guide and move to the new version without their integration breaking mid-migration. This means supporting both versions during the transition window, so developers migrate on their schedule rather than yours. A version cutover with no overlap and no guide is how you lose the developers who trusted you most.

**5. Consistent, structured error responses.** Every error your API returns should have the same shape, so a developer writes error handling once and it works everywhere. A good error structure carries: a machine-readable code (a stable string the developer's code can branch on), a human-readable message (what went wrong, in plain language), and often a link to the relevant documentation. Consistency is the point: an API where every endpoint returns errors in a different shape forces custom handling per endpoint and signals carelessness. You design the error envelope once and apply it universally.

**6. Error categories and correct signaling.** Errors fall into categories that map to how the developer should respond. Client errors (the request was wrong, 4xx): the developer can fix these, and the error should say how. Auth errors (401, 403): the key is missing, invalid, or lacks permission. Rate limit errors (429): the developer is over their limit and should back off, with headers saying when to retry. Server errors (5xx): the fault is yours, not the client's, and the developer should retry rather than change their request. Signaling the right category with the right status code tells the developer whether to fix their code, back off, or simply retry, which is exactly the information they need when something fails.

## Your Toolkit

- **Versioning strategy**: URL path, header, or query, chosen for visibility and applied consistently
- **Breaking-change classifier**: the add-safe, change-and-remove-breaking rule applied to every proposed change
- **Deprecation process**: published timelines plus in-band sunset and deprecation headers
- **Error envelope**: one consistent structure with machine code, human message, doc link, and correct category

## Exam Topics

1. Versioning strategies and their visibility tradeoffs
2. Classifying breaking vs non-breaking changes
3. Deprecation policies and sunset headers
4. Migration guides and dual-version support windows
5. Consistent, structured error responses
6. Machine-readable codes vs human-readable messages
7. Error categories: client, auth, rate limit, server
8. Signaling the right category so developers know how to respond

## Common Pitfalls

- Mixing versioning mechanisms so the version a request targets is ambiguous
- Shipping a breaking change believing it was harmless because the change felt small
- Removing an endpoint or version abruptly with no notice or sunset header
- Cutting over to a new version with no migration guide or overlap window
- Returning errors in a different shape on each endpoint, forcing custom handling
- Using a generic status code that hides whether the developer should fix, back off, or retry

## Self-Assessment Checklist

- Have I chosen one versioning strategy and applied it consistently?
- Can I correctly classify any proposed change as breaking or non-breaking?
- Do I retire endpoints on a published timeline with sunset headers?
- Do I provide migration guides and support both versions during transitions?
- Does every error share one consistent, machine-and-human-readable structure?
- Does each error's status code and category tell the developer how to respond?

## AI Audit Prompt Template

> You are auditing an API's versioning and error design. Check: (1) versioning: is one strategy chosen and applied consistently so every request's target version is unambiguous, (2) change safety: review recent changes and flag any breaking change (removed or renamed fields, type changes, newly required parameters) shipped without a version bump, (3) deprecation: are retirements announced on a timeline with sunset and deprecation headers, (4) migration: do new versions ship with migration guides and a dual-version overlap window, (5) error structure: do all errors share one envelope with a machine code, human message, and doc link, (6) categories: does each error use the correct status code and category so the developer knows whether to fix, back off, or retry. Report each finding with its developer-facing consequence.

## What's Next

Module 6 covers the operational promise behind the product: monitoring, uptime, SLAs, and incident communication.

## Certification Pathway

This is Module 5 of 7 in the API Product Build course, part of T4 The Mastery. Passing all seven module exams earns the API Product Specialist badge. This module is how the API evolves without losing trust.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
