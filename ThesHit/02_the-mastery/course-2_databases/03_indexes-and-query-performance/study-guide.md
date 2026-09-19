# Module 3: Indexes and Query Performance — Study Guide

## T4 The Mastery | Database Design and Migration

This is the study guide. Everything for Indexes and Query Performance is on this page — there's nothing to download.

## What This Module Covers

This module is about speed you can prove. You will learn what an index actually is, which columns deserve one, how to read what the database is really doing through execution plans, how to kill the N+1 query problem, and the discipline underneath all of it: measure before optimizing, and demand evidence after.

## Why It Matters

Every AI-built app is fast on day one. Dev has hundreds of rows; production grows to millions. A query that scans the whole table is invisible at three hundred rows and a customer-facing outage at three million, which is why search "got slower every week since launch" even though the query never changed. Performance problems in AI-built apps almost never come from insufficient hardware. They come from inefficient queries and missing indexes: a dashboard firing two hundred queries per page load, unindexed foreign keys forcing every join to scan, deep pagination paying for every row it skips. Your AI will happily generate all of these patterns, and it will also happily report "the query is optimized" without proof. The builder who knows what to measure and what evidence to demand keeps the app fast for the price of a few prompts. The builder who guesses buys bigger servers to run bad queries faster. This module makes you the first kind.

## Certification Goal

Passing the Module 3 exam proves you can direct evidence-based performance work: identify slow queries with data, read execution plans, index the columns queries actually use, fix N+1 patterns with set-based queries, and verify every fix with before-and-after proof instead of the agent's confidence.

## What You Need to Know

**What an index is and what it costs.** An index is a lookup structure that lets the database find matching rows without scanning the whole table. It is not free: every write must also update it, so inserts and updates get a little slower with each one, and unused indexes are pure overhead. That is why you never index every column, and why the strongest first candidates are the columns your queries actually filter, join, or sort on often. Foreign keys almost always deserve an index, because joins and lookups constantly filter by them, and an unindexed foreign key makes core queries scan.

**Full table scans and execution plans.** A full table scan means reading every row to answer a query, a red flag on large tables queried frequently. When a query is slow, do not rewrite it in a different style or guess: direct your AI to show the execution plan, which reveals whether indexes are used or rows are scanned. When an index exists but the query is still slow, check whether the query's pattern can even use it: leading wildcards and functions applied to the column defeat an index that is sitting right there.

**The N+1 problem.** N+1 is loading a list, then running one extra query per item, turning one fetch into hundreds. It is the signature performance bug of AI-generated code. The fix is not caching or upgrading the plan: it is combining per-item lookups into set-based queries that fetch the needed data in a few trips. A dashboard running two hundred queries per load is an N+1 storm, and set-based fetching is the first tool you reach for.

**Patterns that degrade with data.** Dev-versus-production speed differences are almost always data size: scans invisible at hundreds of rows hurt at millions. Offset-based pagination slows on deep pages because page 500 still walks past the 499 before it. Customers with long histories load slowly when queries fetch or sort everything without an index or paging. SELECT * everywhere moves wasted data, breaks when schemas change, and hides what the code actually needs. Learn these shapes; production will show you all of them.

**Where heavy work belongs.** A forty-second report query joining six tables does not belong on the database serving customers: it belongs on a replica or analytics copy, so heavy reporting stops competing with customer traffic. Composite indexes, one index over multiple columns, win when queries filter on those columns together. And when measured joins remain the bottleneck after indexing, denormalizing for read speed becomes legitimate, provided you accept the sync cost knowingly.

**Measure, fix, verify, watch.** Measure before optimizing means finding the actual slow queries with data first, so effort lands on real bottlenecks instead of guesses. Add indexes based on real query patterns, not up-front guessing that indexes the wrong things. Set up slow-query logging with thresholds and alerts so degradation shows up as signals rather than tickets, and watch query metrics after each release so a slow query introduced today is caught today. When your AI reports "optimized," ask for the before-and-after plan or timing that proves it. When it proposes caching, ask how stale the data can be and how the cache updates, because caching trades freshness for speed.

## Your Toolkit

- **The execution plan.** Your window into what the database really does with a query. Direct your AI to produce it for any slow query and explain whether it shows index use or a scan.
- **Slow-query logging and alerts.** Thresholds that turn quiet degradation into a signal you see the day it starts. Standing infrastructure, not a one-time investigation.
- **The set-based rewrite.** The standard N+1 cure: replace per-item lookups with queries that fetch what a whole screen needs in a few trips. Count queries per page load before and after.
- **The evidence demand.** A habit, not a tool: no performance claim is accepted without before-and-after timing or plans. "It should be faster now" is not a result.

## Exam Topics

The Module 3 exam will test you on:

1. What indexes are, what they cost on writes, and why you never index everything
2. Choosing index candidates: filtered, joined, and sorted columns, especially foreign keys
3. Full table scans, execution plans, and why growth makes unchanged queries slow
4. The N+1 problem and set-based query fixes for query-storm pages
5. Composite indexes and when they beat separate single-column indexes
6. Degradation patterns: production data size, deep pagination, SELECT *, index-defeating query shapes
7. Caching trade-offs, and moving heavy reporting onto replicas or analytics copies
8. Measurement discipline: slow-query logging, post-release metrics, before-and-after evidence

## Common Pitfalls

- **Optimizing by guess.** Effort lands on queries that feel slow instead of queries that are slow. Measurement first, always.
- **Indexing everything defensively.** Every index taxes every write, and unused indexes are dead weight. Index what real query patterns use.
- **Trusting "optimized" without proof.** An agent's confidence is not a benchmark. Demand the before-and-after plan or timing.
- **Fixing N+1 with capacity.** Upgrading the plan to absorb two hundred queries per page load pays monthly for a bug one rewrite would remove.
- **Caching without an invalidation answer.** A cache with no freshness story converts a speed problem into a correctness problem.
- **Letting reports fight customers.** Analytics on the primary means every heavy report degrades every live user. Separate the workloads.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I explain what an index does and what it costs on every write?
- [ ] Can I name the columns that deserve indexes first, and why foreign keys qualify?
- [ ] Can I describe the N+1 problem and the set-based fix in two sentences?
- [ ] Can I explain why a query got slower over months without changing?
- [ ] Do I know what to ask for when my AI says a query is optimized?
- [ ] Can I list two query shapes that defeat an existing index?
- [ ] Do I know where a forty-second reporting query should run, and why?

## AI Audit Prompt Template

Use this prompt to run a performance audit on any AI-built app:

> "You are a database performance auditor. Pull the slowest queries from our logs and, for each, show the execution plan and state whether it uses an index or scans. List every foreign key without an index. Count queries per page load on our three busiest screens, flag N+1 patterns, and propose set-based rewrites. Identify SELECT * and offset-based pagination on large tables. For every fix, give me the before measurement now and commit to an after measurement, and rank fixes by user impact, not ease. Do not propose caching without stating how stale the data may get and how the cache updates."

## What's Next

Module 4 is where schema work meets live traffic: migrations without downtime. You will learn the expand-contract pattern, batched backfills, rollback plans, and why locking a table for ten minutes is a choice you refuse.

## Certification Pathway

This is Module 3 of Database Design and Migration, a T4 The Mastery course available with paid Builder Access, sitting alongside the SaaS Build course in the tier. Pass all seven module exams to earn the Database Build Specialist badge. Performance is the bridge into the operational half of the course.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Indexes and Query Performance Exam →
