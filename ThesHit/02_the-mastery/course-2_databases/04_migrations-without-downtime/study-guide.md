# Module 4: Migrations Without Downtime — Study Guide

## T4 The Mastery | Database Design and Migration

This is the study guide. Everything for Migrations Without Downtime is on this page — there's nothing to download.

## What This Module Covers

This module teaches you how to change a database that real users are standing on. You will learn what migrations are, why live schema changes risk downtime, the expand-contract pattern for zero-downtime change, how backfills run in batches, and the preparation that makes a risky change routine: staging tests, rollback plans, and verification after.

## Why It Matters

Your schema will change. Features will ship weekly, and the "final" design from Module 1 will need new columns, renamed fields, and restructured relationships while paying customers are using the app. This is where most AI-built apps get hurt, because the naive path looks so easy. But some changes lock tables while they run, and a locked table means requests pile up and fail. A dropped column is gone, and if anything still read it, you find out after it is unrecoverable. A hand-applied hotfix leaves production quietly different from the recorded schema, and the next migration breaks on the drift. Downtime during a schema change is not bad luck. It is a skipped pattern, and the choreography in this module is how professionals change structure under live traffic without users noticing.

## Certification Goal

Passing the Module 4 exam proves you can direct schema change like a professional: versioned migrations, expand-contract sequencing for breaking changes, batched backfills, staging tests on production-like data, rollback plans decided before anything runs, and verification of the app afterward, not just the migration.

## What You Need to Know

**Migrations are scripted, versioned, and tracked.** A migration is a scripted, versioned change to the database's structure that can be applied and tracked reliably. Migrations live in version control alongside the code, because schema state and code state must move together and be reproducible for any point in time. Track which migrations have run in each environment, so the same change never runs twice and every environment's state is knowable at a glance. Write the why into every migration's description, so a future reader understands the reason, not just the diff.

**Which changes are safe, and which are not.** Purely additive changes, a new nullable column or a new table nothing depends on yet, are generally safe without choreography. Renames, type changes, and drops are not. Dropping a column is more dangerous than adding one because dropped data is gone; before any drop, search the code, check query logs over time, and monitor access, then drop only with evidence of non-use. If a migration will lock a large table for minutes, do not schedule the outage: find a lock-avoiding approach, like online schema change tools or batched incremental steps.

**Expand-contract is the core pattern.** Add the new structure alongside the old, move code over gradually, then remove the old when unused. A safe live column rename follows this shape: add the new column, write to both, migrate readers, backfill, then drop the old one when nothing uses it. Ordering matters: expand first, code next, contract last, so each step keeps the system working. Through the middle phase, the app's code must work with both structures, since both exist while the change rolls out.

**Backfills run in batches.** Backfilling means populating a newly added column with correct values for the rows that already existed. A single huge update can lock the table and overwhelm resources; small batches keep the app responsive. A migration that alters ten tables at once gets the same treatment: smaller steps limit the blast radius and keep failures diagnosable and reversible.

**Rehearse, and be ready to retreat.** Every migration runs on staging with production-like data first, because production's volume and messy edge cases surface locks, timeouts, and failures that clean samples miss. Before the migration runs, two things already exist: a rollback plan and a healthy pre-change backup. Reversible means a defined way to undo the change exists, so when a deploy goes wrong you retreat instead of improvising. Never let anyone, human or AI, apply schema changes to production by hand: untracked drift means production no longer matches the recorded schema, and future migrations may break on the difference. Schema drift between environments is the same disease: what passed staging can fail in production.

**Verify the app, not the migration.** "It ran" is not success. After a migration completes, direct your AI to verify the app's critical paths work and data spot-checks match expectations. Treat every migration, however minor, as a small deployment with a plan, a test, a rollback, and verification. Change structure the way surgeons operate: prepared, incremental, reversible, and verified after.

## Your Toolkit

- **The migration pipeline.** Versioned migration files in the same repository as the code, with a tracked record of what has run where. The only road structural change travels.
- **The expand-contract playbook.** The reusable choreography for every breaking change: add alongside, dual-write, move readers, backfill, remove. Map any risky change onto these five steps before writing anything.
- **Staging with production-like data.** The rehearsal stage where locks and failures cost nothing. A migration that has not run against realistic volume has not been tested.
- **The rollback kit.** A healthy pre-change backup plus a written undo path, both in hand before the migration runs. If you cannot say how you would retreat, do not advance.

## Exam Topics

The Module 4 exam will test you on:

1. What migrations are and why they live versioned in source control with tracked history
2. Why live schema changes risk downtime, and which changes are safely additive
3. The expand-contract pattern and the safe sequence for renaming a live column
4. Backfills, why they run in small batches, and splitting oversized migrations
5. Code compatibility with both structures during rollout, and expand-code-contract ordering
6. Staging tests on production-like data, rollback plans, and pre-change backups
7. Drop discipline, evidence of non-use, hand-applied changes, and schema drift
8. Post-migration verification and the surgeon's mindset for structural change

## Common Pitfalls

- **The one-step rename at 3 AM.** Low traffic does not make a breaking change safe; it means fewer witnesses. The choreography is the safety, not the clock.
- **Testing on small clean samples.** Volume and messy edge cases are where locks and timeouts live, and only production-like data shows them.
- **The quick manual fix.** One hand-applied change and production no longer matches the record. The drift is invisible until the next migration fails on it.
- **Dropping on faith.** "It looks unused" is not evidence. Code search, query logs over time, and monitored access are.
- **Declaring victory when the script exits.** The migration ran; whether the app still works is a separate question you answer on purpose.
- **Improvising the retreat.** Deciding how to roll back while errors spike is how small incidents become long ones. The plan exists before the run, or the run waits.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I explain what a migration is and why it lives in version control with the code?
- [ ] Can I walk the expand-contract steps for renaming a column under live traffic?
- [ ] Can I explain why backfills run in batches and what a giant single update risks?
- [ ] Can I say what must be true of the app's code while both structures coexist?
- [ ] Do I know what must exist before any migration runs, and what to verify after?
- [ ] Can I explain schema drift and why hand-applied production changes cause it?
- [ ] Could I direct a multi-table restructure as a sequence of small reversible steps?

## AI Audit Prompt Template

Use this prompt before approving any migration your AI has written:

> "You are a database migration reviewer. Here is the proposed migration and its purpose: [paste migration and intent]. Classify every operation as additive-safe or breaking. Map each breaking operation onto expand-contract: what gets added alongside the old, how dual-writing works, when readers move, how the backfill runs in batches, and when the old structure is removed. Estimate lock behavior on production-sized tables and propose a lock-avoiding approach for anything holding a table more than seconds. Confirm the rollback path and pre-change backup. Then give me the staging test plan and the post-migration verification list for the app's critical paths."

## What's Next

Module 5 covers the safety net underneath every migration: seeding, backups, and restores. You will learn why a backup only counts once it has restored, how RTO and RPO set your schedule, and how restore drills keep the recovery path honest. The pre-change backup this module demanded becomes a discipline of its own there.

## Certification Pathway

This is Module 4 of Database Design and Migration, a T4 The Mastery course available with paid Builder Access, sitting alongside the SaaS Build course in the tier. Pass all seven module exams to earn the Database Build Specialist badge. Migration skill is the course's namesake: it lets everything you designed in Modules 1 through 3 evolve without breaking.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Migrations Without Downtime Exam →
