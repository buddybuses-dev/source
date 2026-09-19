# Module 1: Supabase Architecture and Project Setup — Study Guide

## Supabase Backend Build

### T4 The Mastery | Module 1 Study Guide

## Module 1: Supabase Architecture and Project Setup

> Direct AI to build production backends on Supabase with security policies that hold.

## What This Module Covers

You picked Supabase because it gets you to a working backend fast. This module makes sure that speed does not become the reason your app breaks later. You will learn what Supabase actually is under the hood: a full Postgres database with auth, storage, realtime, and edge functions layered on top, not a black-box backend service. Once you understand that architecture, everything your AI builds makes sense, and everything it gets wrong becomes obvious.

You will cover project creation and configuration, the dashboard vs direct Postgres access, local development with the Supabase CLI, and a real environment structure: development, staging, and production. Then you will practice the core skill of this course: directing AI to scaffold a project structured for growth. Not a demo. A foundation that can carry a SaaS app with 50 tenants, a marketplace with file uploads, or a role-based client portal without a rebuild.

## Why It Matters

Most Supabase horror stories start in the first week. A builder spins up a project, lets AI write everything against the production database, ships fast, then discovers there is no staging environment, no local setup, and no safe way to test a schema change. When the SaaS app with 50 tenants needs a fix, every change is a live-fire exercise. That is a setup problem, not a Supabase problem, and it is completely avoidable.

The other stake is comprehension. Your AI will happily generate tables, keys, and config, but if you cannot tell the anon key from the service role key, you cannot review what it produces. This module gives you the mental model to supervise the build instead of hoping it works. Every module after this one assumes this foundation.

## Certification Goal

Passing the Module 1 exam proves you can direct AI through a correct project setup: explain each layer of the platform, configure a project with proper key handling, run Supabase locally with the CLI, and structure development, staging, and production environments the way a production team would.

## What You Need to Know

### Supabase Is Postgres With Layers On Top

Supabase is not a proprietary database. It is standard Postgres with auth, storage, realtime, edge functions, and an auto-generated API built around it. Everything from Database Design and Migration applies directly, and your data stays portable.

### Project Anatomy: URL, Keys, and Roles

Every project gets a unique URL, an anon key for client-side use, and a service role key that bypasses all security rules. The anon key is safe in your frontend only because Row-Level Security guards the data behind it. The service role key belongs on servers only, never in browser code or a repo: there, it hands every visitor admin access.

### Dashboard vs Direct Postgres Access

The dashboard is a convenient admin view: table editor, SQL editor, auth settings, logs. But it operates with elevated privileges, so queries that work in the SQL editor can fail for real users once RLS is on. Direct Postgres access through a connection string is how migrations and serious tooling connect. Know which surface you are on.

### Local Development With the Supabase CLI

The CLI runs the entire stack on your machine in Docker. You develop locally with `supabase start`, capture schema changes as migration files with `supabase db diff`, and push to a hosted project with `supabase db push`. This makes database changes reviewable and repeatable.

### Environments: Development, Staging, Production

Never test schema changes on live data. The standard structure: local development via the CLI, a hosted staging project that mirrors production, and a production project that only receives migrations already proven in staging. Each environment has its own URL and keys, loaded from environment variables, never hardcoded.

### Migrations as the Source of Truth

Every schema change lives in a versioned migration file in your repo, not a one-off dashboard edit. Migrations let you rebuild any environment from scratch, review your AI's database changes like code, and roll forward safely. If a change is not in a migration, it does not really exist.

## Your Toolkit

- **Supabase Dashboard**: Your admin console for settings, table editor, auth configuration, and logs. Use it to inspect and verify, but treat it as read-mostly: schema changes belong in migrations.
- **Supabase CLI**: Runs the full stack locally, manages migrations, and links your local project to hosted environments. The backbone of a professional workflow.
- **Environment Variable Management**: A `.env` file per environment holding the URL and keys, gitignored. Your AI should never hardcode a key; catch it every time it tries.
- **AI Scaffolding Prompts**: Reusable prompts that tell your AI how to structure a new project: CLI-first, migrations in the repo, three environments, keys in env vars. You direct the structure; the AI does the typing.

## Exam Topics

- The layers of the Supabase platform and how each relates to the underlying Postgres database
- The anon key vs the service role key, and where each may safely be used
- Why dashboard SQL editor queries can behave differently than queries from your app
- Core CLI commands for local development, linking a project, and pushing migrations
- The purpose of each environment in a development, staging, production structure
- How environment variables keep credentials out of your codebase
- Why migration files, not dashboard edits, are the source of truth for your schema
- What to check when reviewing an AI-scaffolded Supabase project before building on it

## Common Pitfalls

- **Building directly against production from day one**: Every experiment risks live data, and once real users arrive there is no safe place to test anything.
- **Exposing the service role key in client code**: This key bypasses every security policy. In a browser, it gives any visitor full access to your database.
- **Treating the dashboard as your development environment**: Untracked edits cannot be reviewed, repeated, or rolled back, and environments silently drift apart.
- **Skipping the CLI**: Without local development and migration files, your AI's database changes are invisible until they hit a live environment.
- **One project for everything**: A single project serving as dev, staging, and production means a bad migration lands on your users with zero warning.
- **Assuming SQL editor success means app success**: The editor runs with elevated privileges; a query that works there may fail for a real user once RLS is on.

## Self-Assessment Checklist

- I can explain what Supabase is architecturally and how it relates to plain Postgres
- I can create and configure a new project and locate its URL and keys
- I can state where the anon key and service role key may each be used, and why
- I can run the full stack locally with the CLI and link it to a hosted project
- I can describe a development, staging, production structure and what flows between them
- I can explain why migrations in the repo beat dashboard edits
- I can review an AI-scaffolded project and spot missing structure before building on it

## AI Audit Prompt Template

Give your AI this prompt to audit your project setup and environment structure before you build on it.

`Audit my Supabase project setup and environment structure. Do not change anything yet: report findings first. Check and report on: 1. Keys: Search the codebase for any hardcoded Supabase URL or key. Confirm the service role key never appears in client-side code and .env files are gitignored. 2. Environments: List the environments (local, staging, production). Flag one project serving all purposes or a missing local setup. 3. CLI and migrations: Confirm supabase/config.toml exists, the project is linked, and all schema changes exist as versioned files in supabase/migrations. Flag any schema that exists only in the hosted dashboard. 4. Config hygiene: Confirm each environment loads its URL and keys from environment variables. 5. Growth readiness: Identify anything that would force a restructure once real users arrive. Output a numbered list of findings marked PASS, WARN, or FAIL, with a one-line fix for each issue. Wait for my approval before changing anything.`

## What's Next

With your project scaffolded and your environments separated, you are ready to build the data layer. Module 2: Postgres Tables and Relationships teaches you to direct AI to design tables, keys, and relationships that hold up under real load, using the migration workflow you just established.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the module badge. Pass all 7 module exams to earn the Supabase Specialist badge.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
