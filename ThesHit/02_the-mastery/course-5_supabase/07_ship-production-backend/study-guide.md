# Module 7: Ship: Production Backend — Study Guide

## Supabase Backend Build

### T4 The Mastery | Module 7 Study Guide

## Module 7: Ship: Production Backend

> Direct AI to build production backends on Supabase with security policies that hold.

## What This Module Covers

This is the capstone. Everything from the first six modules, the schema from M2, the RLS policies from M3, the auth flows from M4, the storage and Edge Functions from M5, the environments from M6, comes together into one act: going live. You will direct your AI through a full production launch and verify every claim it makes before real users touch the system.

You will work the production checklist that separates a demo from infrastructure: RLS enabled on every table, auth locked to production domains, storage policies that deny by default, environment variables secured, and connection pooling configured. Then you go beyond the checklist into performance: indexes on the columns your queries actually filter on, connection limits that match your plan, and query optimization you supervise rather than assume.

Finally, you set up monitoring: dashboard metrics, Postgres logs, and error alerts that reach you before your users do. The goal is a backend that runs while you sleep. That is what shipping means at the Mastery tier.

## Why It Matters

The moment your 50-tenant SaaS app goes from staging to production, a single missing RLS policy becomes a data breach instead of a bug. Your marketplace opens file uploads, and a bucket without policies becomes a free CDN for strangers. Your client portal hands out role-based access, and a misconfigured auth redirect becomes an account takeover vector. Production does not grade on effort. It grades on what you actually shipped.

The builders who fail here are not the ones with bad code. They are the ones who let their AI say "done" without an audit. AI will happily scaffold a backend that works in the happy path and leaks data everywhere else, because nothing in a passing demo reveals a missing policy. Your job is to be the auditor: check the checklist, read the logs, and refuse to launch until the policies hold.

## Certification Goal

Passing this module's exam proves you can take a Supabase backend from working to production-ready: you can run a complete pre-launch audit, direct AI to close every gap in security, performance, and monitoring, and verify the fixes yourself instead of trusting the AI's word for it.

## What You Need to Know

### The Production Checklist Is Non-Negotiable

Before launch, five things must be true: RLS enabled on every table in the public schema, auth configured for production domains only, storage policies locked down, environment variables secured and never committed, and connection pooling configured. Direct your AI to verify each one with a query or settings check, not a summary. One unchecked item is one open door.

### RLS Coverage Means Every Table, Not Most Tables

A table with RLS disabled is fully readable and writable by anyone holding your anon key, which ships inside your frontend. Have your AI query pg_tables and pg_policies to list every table without RLS or without policies attached. In your 50-tenant SaaS, the forgotten "audit_logs" table is exactly where tenant data leaks.

### Auth Must Be Locked to Production Domains

Your Site URL and redirect allow-list control where auth tokens can be sent after login. Leaving localhost or wildcard redirects in production lets an attacker send a real user's session to a domain they control. Confirm the production domain is set, stale development URLs are removed, and email templates point at production links.

### Indexes Are Where Production Performance Lives

Queries that feel instant at 100 rows crawl at 100,000, and RLS makes it worse because policies execute on every row scanned. Direct your AI to index foreign keys, every column your RLS policies filter by (tenant_id, user_id), and columns in frequent WHERE clauses. Then have it prove the win with EXPLAIN ANALYZE, and read the output yourself.

### Connection Pooling Keeps the Backend Standing Under Load

Postgres allows a limited number of direct connections, and serverless frontends can exhaust them in one traffic spike. Supabase's pooler (Supavisor) multiplexes many client connections over few database connections. Make sure your app and Edge Functions connect through the pooler in production, and know when transaction mode applies versus a direct connection.

### Monitoring Is How the Backend Runs While You Sleep

The dashboard gives you database health: CPU, memory, disk IO, and connection counts. Postgres logs show slow queries, errors, and policy failures. Wire error alerts to a channel you actually check. A backend without monitoring is not infrastructure, it is a demo that has not failed yet.

## Your Toolkit

- **The Supabase Security Advisor**: Built into the dashboard under Advisors, it flags tables without RLS, permissive policies, and exposed functions. Run it before launch and after every schema change your AI ships.
- **EXPLAIN ANALYZE**: The Postgres command that shows how a query actually executes and how long it takes. Make your AI attach EXPLAIN output to any performance claim.
- **The Pre-Launch Audit Prompt**: A standing prompt (template below) you run before every launch and major release. Treat its output as a blocking gate, not a suggestion.
- **Dashboard Metrics and Log Explorer**: Your production eyes: resource graphs, API request metrics, and searchable Postgres logs. Check daily for the first week after launch, then set alerts and check weekly.

## Exam Topics

- The five items on the production launch checklist and how to verify each one directly
- Querying pg_tables and pg_policies to prove RLS coverage across every table
- Configuring Site URL and redirect allow-lists for production auth, and the risk of stale development URLs
- Which columns need indexes in an RLS-heavy schema, including foreign keys and policy filter columns
- When to route connections through the Supavisor pooler versus a direct connection, and why serverless traffic exhausts direct connections
- Securing environment variables: what the anon key can safely touch versus what the service role key must never touch
- Reading Supabase dashboard metrics and Postgres logs to spot slow queries and policy failures
- Setting up error alerts so production incidents reach you before users report them

## Common Pitfalls

- **Launching with one table missing RLS**: Your anon key is public by design, so a single unprotected table is fully exposed to anyone who opens your site's network tab.
- **Leaving localhost in the auth redirect list**: Stale development URLs in production config give attackers a landing spot for hijacked auth redirects.
- **Trusting the AI's "all policies are in place"**: AI summarizes intent, not state. Only a query against pg_policies or a Security Advisor run counts as verification.
- **Skipping indexes because staging felt fast**: Small tables hide missing indexes. At production row counts, unindexed RLS filter columns turn every request into a sequential scan.
- **Connecting serverless functions directly to Postgres**: Each invocation grabs a connection, and a modest spike hits your connection limit and takes the whole backend down.
- **Shipping with no alerts configured**: Without monitoring, your users become your monitoring, and you find out about outages from angry emails instead of dashboards.

## Self-Assessment Checklist

- I can run a complete production checklist and verify each item with evidence, not AI assurances
- I can direct AI to query the database and prove RLS is enabled with policies on every table
- I can configure production auth domains and strip stale redirect URLs before launch
- I can identify which columns need indexes and confirm the improvement with EXPLAIN ANALYZE
- I can explain when to use connection pooling and route my app through it correctly
- I can read Supabase dashboard metrics and Postgres logs to diagnose a production issue
- I can set up error alerts so my backend reports problems while I sleep

## AI Audit Prompt Template

Give your AI this prompt against your live project before launch, and treat any failed check as a launch blocker.

`Run a full production readiness audit on my Supabase project. For each section, show the exact queries or settings you checked and report PASS or FAIL with evidence. 1. RLS coverage: Query pg_tables and pg_policies. List every table in the public schema, whether RLS is enabled, and every policy attached (command, roles, USING and WITH CHECK expressions). Flag any table with RLS disabled, no policies, or USING (true) on writes. 2. Auth configuration: Verify Site URL and redirect allow-list contain only production domains. Flag localhost, wildcards, or staging URLs. Confirm email templates point at production links. 3. Storage policies: List every bucket, public or private, and every storage policy. Flag any bucket allowing public writes or missing owner-scoped policies for uploads, updates, and deletes. 4. Secrets and keys: Confirm the service role key appears nowhere in frontend code, client bundles, or committed files. List every environment variable the app expects and where it is stored. 5. Indexes and performance: List all foreign key columns and all columns used in RLS policy filters and frequent WHERE clauses. Flag any without an index. Run EXPLAIN ANALYZE on my five most common queries and flag sequential scans on large tables. 6. Connection pooling: Confirm the app and all Edge Functions connect through the pooler in production, and state the connection limits for my plan. 7. Monitoring: Report what metrics, log retention, and error alerting are in place. Recommend specific alerts I am missing. Output a numbered fix list ordered by severity. Do not mark anything PASS without showing the evidence.`

## What's Next

Pass this exam and you have completed all seven modules: claim your Supabase Specialist badge. You now own a production backend pattern that underpins most T4 Mastery builds. Nearly everything you ship from here, SaaS products, marketplaces, client portals, sits on a backend like this one. Carry it into your other Mastery courses and reuse the audit every time you launch.

## Certification Pathway

Pass this module's exam at 80 percent (20 of 25 questions) to earn the Module 7 badge. Pass all 7 module exams to earn the Supabase Specialist badge and complete Supabase Backend Build.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
