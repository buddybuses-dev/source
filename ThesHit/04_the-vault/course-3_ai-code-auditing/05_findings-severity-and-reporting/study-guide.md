# Module 5: Findings, Severity and Reporting — Study Guide

## Vibecoder Security Audit Method

### T6 The Vault | Module 5 Study Guide

## Module 5: Findings, Severity and Reporting

> Direct AI to classify findings by real severity and write a report a client can act on.

## What This Module Covers

This module covers classifying and communicating findings: the five severity levels, how to write a finding a non-technical stakeholder can act on, and the report structure, executive summary, layer-by-layer findings, severity distribution, remediation priorities, and the RED/YELLOW/GREEN scorecard.

## Why It Matters

An audit that finds everything and communicates nothing is worthless. The deliverable is not the findings; it is the decisions the findings enable. Founders are not security engineers; a report written for engineers gets skimmed, misunderstood, and shelved, and the vulnerabilities stay live. The reporting skill is where the audit becomes valuable and where the audit business earns trust and referrals. A report that tells a founder exactly what is wrong, what could happen, what to do, and how hard the fix is turns a scary scan into a clear action plan, and turns a one-time audit into a recurring relationship.

## Certification Goal

Passing this exam proves you can assign severity consistently, write findings that non-technical stakeholders understand and act on, and structure a report that communicates posture and priorities clearly.

## What You Need to Know

**1. The five severity levels.** Critical: exploitable right now, with serious impact; an attacker needs no special conditions. High: exploitable with effort or a plausible precondition. Medium: exploitable only under specific conditions that are not currently met. Low: a best-practice gap with no direct exploit path. Informational: an observation worth noting that is not itself a weakness. Severity is impact times exploitability, not a measure of how alarming the finding sounds. A scary-sounding issue that cannot actually be exploited is Low; a boring-sounding missing auth check that exposes all data is Critical.

**2. Severity must be consistent and defensible.** The same class of finding earns the same severity across audits, or the scorecard means nothing. You anchor each rating to two questions: what is the impact if exploited, and how hard is it to exploit. Write the answer into the finding so the rating is auditable. Inflating severity to seem thorough destroys trust as fast as understating it destroys safety; the founder must be able to rely on Critical meaning drop-everything and Low meaning schedule-it.

**3. The four-part finding for non-technical readers.** Every finding answers, in plain language: what is wrong (the weakness, without jargon), what could happen (the business consequence, in terms of money, data, downtime, or reputation), what to do (the remediation direction), and how hard the fix is (effort, so the founder can plan). A finding that says "unparameterized query in the reports handler" fails; a finding that says "the reports page lets an attacker read your entire customer database, and here is the fix, which is about an hour of work" succeeds. The technical detail belongs in an appendix for whoever implements.

**4. The report structure.** Executive summary first: overall posture, the count and nature of the worst findings, and the single most important action, written for someone who reads only this section. Then the RED/YELLOW/GREEN scorecard: all thirteen layers on one page. Then layer-by-layer findings, each in the four-part format, ordered by severity within the layer. Then severity distribution: how many Critical, High, Medium, Low, so the shape of the risk is visible at a glance. Then remediation priorities: the ordered fix list that becomes Module 6's sprint plan.

**5. The scorecard as the centerpiece.** The RED/YELLOW/GREEN scorecard from Module 2 is what founders remember and share. It compresses the entire audit into thirteen grades they can grasp in seconds. It also creates the natural follow-up: RED layers demand immediate work, YELLOW layers become a roadmap, and the whole thing gives the next audit something to compare against. The scorecard is both the summary and the sales artifact for the ongoing relationship.

**6. Communicating without panic.** Findings are frightening to founders who conflate "vulnerable" with "already breached." The report's tone matters: state risks factually, frame them as fixable, and always pair a Critical with its remediation so the reader never sits with fear and no path. The auditor's job is to make the client safer and calmer, not more scared. Panic produces paralysis or rushed bad fixes; clarity produces action. This tone discipline is a professional skill, not a softness, and it is what makes clients come back.

## Your Toolkit

- **The five-level severity rubric**: impact times exploitability, anchored and written into each finding
- **The four-part finding template**: what is wrong, what could happen, what to do, how hard
- **The report skeleton**: executive summary, scorecard, layer findings, distribution, priorities
- **The RED/YELLOW/GREEN scorecard**: the one-page centerpiece and comparison baseline

## Exam Topics

1. The five severity levels and their definitions
2. Severity as impact times exploitability, not alarm level
3. Consistent, defensible, anchored severity ratings
4. The four-part finding written for non-technical readers
5. Report structure and the role of each section
6. The executive summary as a standalone artifact
7. The scorecard as summary and relationship driver
8. Communicating risk factually without inducing panic

## Common Pitfalls

- Rating severity by how scary a finding sounds rather than by real exploitability
- Inflating ratings to look thorough, until Critical stops meaning anything
- Writing findings in engineer language a founder cannot act on
- Presenting a Critical with no remediation, leaving the reader in fear
- Burying the most important action instead of leading the executive summary with it
- Handing over a findings list with no scorecard, so posture is invisible at a glance

## Self-Assessment Checklist

- Can I define all five severity levels and place a finding correctly?
- Is each of my ratings anchored to impact and exploitability in writing?
- Does every finding answer what is wrong, what could happen, what to do, and how hard?
- Could a non-technical founder read my executive summary and know the top action?
- Does my report lead with the scorecard and severity distribution?
- Do my Criticals always ship with their fixes so the reader is never left panicked?

## AI Audit Prompt Template

> You are turning raw audit findings into a client-ready report. For each finding: (1) assign severity (Critical, High, Medium, Low, Informational) and write one line anchoring it to impact and exploitability, (2) rewrite it in four parts for a non-technical reader: what is wrong, what could happen to the business, what to do, and how hard the fix is, keeping technical detail in an appendix. Then assemble the report: (3) an executive summary leading with overall posture and the single most important action, (4) the RED/YELLOW/GREEN scorecard across all thirteen layers, (5) findings grouped by layer and ordered by severity, (6) a severity distribution count, (7) an ordered remediation priority list. Keep the tone factual and non-alarming, and never present a Critical without its remediation.

## What's Next

Module 6 executes the priorities: remediation sprints that turn the report's fix list into verified, re-scanned, documented resolutions.

## Certification Pathway

This is Module 5 of 7 in the Vibecoder Security Audit Method course, part of T6 The Vault. Passing all seven module exams earns the Code Audit Specialist badge. This module is where findings become decisions.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
