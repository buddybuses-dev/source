# Module 7: Ship: Production Database — Study Guide

## T4 The Mastery | Database Design and Migration

This is the study guide. Everything for Ship: Production Database is on this page — there's nothing to download.

## What This Module Covers

This is the ship module. Everything from the first six modules converges into one act: taking a database live under real users and operating it like a professional. You will learn the pre-launch checklist, access discipline for humans and AI agents, the monitoring questions that must always have answers, incident readiness, and the goal state of every production database: boring.

## Why It Matters

What separates a production database from the same database in development is not the engine, the schema, or the pricing tier. It is real users and real consequences: mistakes now cost trust, money, and possibly the business. The production data's relationship to the business is blunt: it is the business, and losing it or leaking it is an existential event. Everything changes at that line. The AI agent that freely reshaped the schema during the build loses standing write access. The "quick fix" a senior builder wants to make by hand becomes a logged, reviewed change. And what turns a database incident into a company crisis is not the incident itself; it is silence and improvisation. This module is where you stop being someone who built a database and become someone who runs one, and that is the difference customers actually pay for.

## Certification Goal

Passing the Module 7 exam proves you can take a database to production and keep it there: a launch checklist verified by evidence, least-privilege access with guardrailed AI agents, monitoring that answers the four standing questions, tested runbooks, honest postmortems, and change only through process. It completes your Database Build Specialist badge.

## What You Need to Know

The launch checklist, verified by evidence. Before launch: backups verified by restore, monitoring live, access reviewed, migrations repeatable. Verified by restore means exactly that: "backups working" is proven by a restore into a separate environment with the app running against it, not by a green status icon. Launch traffic at ten times the estimate is survivable when you prepared known headroom and a tested plan for the next step up, decided before it was urgent. Dev and staging do not retire at launch; they remain the places where every future change proves itself first.

Access discipline for humans, agents, and secrets. The app connects through a least-privilege account with credentials in protected configuration, never as admin, never through a personal login. Direct query access belongs to a minimal, named set of people, logged and reviewed as roles change. The AI that built the schema keeps no standing write access once real users arrive: structural changes go through the migration pipeline with review. Secrets rotate on a schedule and after departures or incidents. Long-term, AI agents in production operations are powerful hands within guardrails: executing reviewed changes, never improvising on live data.

Monitoring answers four questions, always. Is it up, is it fast, is it filling, and is anything behaving unlike it did yesterday. Anomalies get investigated, not celebrated: disk growing four times faster than projected means find out what is growing and why, because surprise growth often means a bug, not success. Production's structure stays exactly what the applied migrations produce, nothing more or less; drift from the migration history is a standing alarm.

Change moves through process, even under pressure. Whether a schema change is safe to ship is decided by the process, staging test, migration review, and rollback plan, not by one person's confidence, one agent's authorship, or one customer's urgency. A new table plus a two million row backfill runs planned and batched at low traffic, tested on staging, with progress observable. Manual data fixes go through logged, reviewed channels. When the business wants a risky operation done today, name the risks, the safeguards, and the recovery path out loud, then decide together.

Incident readiness and the postmortem. A runbook is trustworthy when it has been walked through in a drill, so the steps are known to work under pressure. Whether a 2 AM alert is a crisis is decided by what already exists: runbook, on-call path, headroom decisions. Afterward, the postmortem records what happened, why, how it was caught and fixed, and what change prevents a repeat. Not who to blame: what to change.

The goal state is boring. Six months in, health comes from routine care: review slow queries, prune stale indexes, test restores, audit access. "The database is boring now" is the win condition: predictable, monitored, backed up, and changed only through process. Production is a promise: protect the data, rehearse the failures, and change only through process.

## Your Toolkit

- The launch checklist. Backups proven by restore, monitoring answering the four questions, access reviewed to least privilege, migrations repeatable, headroom decided. Every item verified by evidence.

- The access ledger. Who and what can touch production, at what privilege, logged and reviewed as roles change. The AI agent appears here too, inside guardrails, with no standing schema access.

- The incident kit. Drilled runbook, on-call path, communication plan, and pre-decided headroom moves. Built before the 2 AM alert, because that is the only time it can be built.

- The routine care calendar. The rhythm that keeps production boring: slow-query reviews, index pruning, restore tests, and access audits on a schedule instead of a memory.

## Exam Topics

- The Module 7 exam will test you on:

- What makes production different, and the data's existential relationship to the business

- The pre-launch checklist and proving backups by restore into a separate environment

- Least-privilege app connections, named human access, and secret rotation

- Removing standing AI write access, and agents as powerful hands within guardrails

- Monitoring's four questions, investigating anomalies, and schema matching migration history

- Change through process: staging tests, reviews, rollback plans, logged fixes, planned backfills

- Incident readiness: drilled runbooks, communication over silence, blameless postmortems

- Long-term health through routine care, and "boring" as the goal state

## Common Pitfalls

- Launching on a green icon. The backup job's status light is not evidence. Only a restore with the app running against it proves the checklist item.

- Leaving the builder's keys in the door. The AI that created the schema keeps write access nobody re-decided. Launch is when standing access ends.

- The quick manual fix. One unlogged production edit, however small, breaks the rule that keeps every other change reviewable.

- Celebrating anomalies. Disk growing four times faster than projected feels like traction and is often a bug. Investigate before you toast.

- Runbooks nobody has walked. A document that has never survived a drill is a guess wearing a checklist's clothes.

- Confusing boring with neglected. Boring is earned by routine care. Untouched is not the same as healthy.

## Self-Assessment Checklist

- Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I name what actually proves "backups working" on a launch checklist?

- [ ] Can I describe least-privilege access for the app, humans, and AI agents post-launch?

- [ ] Can I recite monitoring's four standing questions from memory?

- [ ] Do I know what decides whether a schema change is safe to ship after launch?

- [ ] Can I say what turns a database incident into a company crisis?

- [ ] Can I list what belongs in a postmortem, and what does not?

- [ ] Can I describe the routine care that keeps a production database healthy?

## AI Audit Prompt Template

Use this prompt before you flip the switch, and again at every quarterly review:

"You are a production database readiness auditor. Here is my setup: [describe backups and last tested restore, monitoring and alerts, access list including AI agent permissions, migration pipeline, runbooks and drill history]. Confirm backups are proven by an actual restore with the app verified against it, monitoring answers up, fast, filling, and behaving normally, the app connects with least privilege, human access is minimal, named, and logged, and no AI agent holds standing write access. Identify every change path that bypasses staging, review, or rollback planning. Then walk my runbook against a connection saturation alert at 2 AM and list every step that fails for lack of a specific person, credential, or decision."

## What's Next

Pass this exam and you have completed all seven modules of Database Design and Migration, earning the Database Build Specialist badge. Claim it in The Faction and put it to work: it tells clients and collaborators that the data layer of anything you direct is designed, migrated, backed up, and operated to a professional standard. Pair it with the SaaS Build course to ship complete products on databases you know how to run. The database under your app is boring now. That is the credential.

## Certification Pathway

This is the final module of Database Design and Migration, a T4 The Mastery course available with paid Builder Access, sitting alongside the SaaS Build course in the tier. Passing all seven module exams earns the Database Build Specialist badge. Modules 1 through 3 gave you design and performance, 4 through 6 gave you change, recovery, and scale, and this module proves you can carry it all into production.

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai

———

Ready? Take the Ship: Production Database Exam →
