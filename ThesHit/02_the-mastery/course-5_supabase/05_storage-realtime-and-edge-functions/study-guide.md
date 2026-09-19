# Module 5: Storage Realtime and Edge Functions — Study Guide

## Supabase Backend Build

### T4 The Mastery | Module 5 Study Guide

## Module 5: Storage, Realtime and Edge Functions

> Direct AI to build production backends on Supabase with security policies that hold.

## What This Module Covers

Modules 1 through 4 gave you a locked-down database with tables, relationships, RLS policies, and authenticated users. Module 5 adds the three features that make an app feel alive: Storage for files, Realtime for live updates, and Edge Functions for server-side logic. These are what your marketplace needs for product photos, your SaaS dashboard needs for live activity feeds, and your client portal needs for secure PDF delivery.

You will direct AI to create storage buckets with access policies that mirror your RLS rules, wire up realtime subscriptions that only deliver what each user may see, and write Deno-based Edge Functions that run trusted logic outside the browser. You will also learn the decision framework: when a feature belongs in an edge function, a database function, or an API route in your frontend framework. These features are where AI output most often looks correct and ships insecure, so the review skill is the whole game.

## Why It Matters

Storage is where data leaks get embarrassing fast. In your marketplace, sellers upload product photos and buyers upload dispute evidence. If your AI creates a public bucket because it was easier to get working, every file is one guessable URL from public. In your 50-tenant SaaS, a contract PDF from tenant 12 showing up for tenant 31 is not a bug ticket, it is a churn event and possibly a legal one. Bucket policies are RLS for files, and they deserve Module 3 levels of scrutiny.

Realtime and Edge Functions carry quieter risks. A realtime channel that ignores RLS will stream other tenants' rows to any subscribed client. An edge function that skips JWT verification is an open endpoint on the public internet, and one that leaks your service role key hands an attacker your entire database. These features demo beautifully on day one and fail loudly when real users show up. This module teaches you to catch that gap before launch.

## Certification Goal

Passing the Module 5 exam proves you can direct AI to implement storage, realtime, and edge functions, then audit the results: bucket policies enforce ownership, subscriptions respect RLS, functions verify auth, and each piece of logic lives in the right layer.

## What You Need to Know

### Storage Buckets and Access Policies

Every bucket is public or private, and access to private buckets is controlled by policies on the storage.objects table: ordinary RLS applied to file paths. The standard pattern stores files under a path prefix like the user's or tenant's ID, then writes policies checking that prefix against auth.uid(). A bucket with no policies is unusable from the client; a public bucket created to "fix" that is readable by everyone.

### Signed URLs and Image Transformations

Private files are served through signed URLs: short-lived, tamper-proof links generated for an authorized user. This is how your client portal delivers a contract PDF without making the bucket public. Supabase can also transform images on the fly via URL parameters, so your marketplace grid serves 200px thumbnails instead of 8MB originals.

### Realtime: Postgres Changes, Presence, and Broadcast

Realtime has three modes. Postgres Changes streams inserts, updates, and deletes from tables you explicitly enable. Presence tracks who is online in a channel, powering "3 teammates viewing" indicators. Broadcast sends ephemeral messages between clients without touching the database, ideal for typing indicators or cursor positions. AI often reaches for database changes when broadcast is cheaper and better, so know which mode fits which feature.

### Realtime Authorization

Realtime respects RLS when enabled properly, but this is the step AI skips most. Postgres Changes should only deliver rows the subscriber could SELECT under your policies, and private channels can require authorization before a client joins. In the 50-tenant SaaS, verify isolation is enforced by RLS on the server: client filters are a suggestion, RLS is a wall.

### Edge Functions with Deno

Edge Functions are TypeScript functions running on Deno, deployed with the Supabase CLI and invoked from your client. They house logic that cannot live in the browser: calling Stripe with a secret key, processing webhooks, sending emails, moderating uploads. By default they require a valid JWT, and inside the function you validate the user and authorize the action. Secrets live in environment variables, never in code AI writes into the repo.

### Choosing the Right Layer

Use a database function (Module 2 territory) when logic is pure data: totals, multi-table invariants, anything transactional. Use an edge function when you need secrets or third-party APIs. Use an API route in your frontend framework when logic is tightly coupled to that app and you already deploy a server. The wrong choice usually still works in the demo, so audit AI output for placement, not just correctness.

## Your Toolkit

- **Supabase Dashboard Storage and Realtime panels**: Create buckets, inspect policies, toggle realtime per table, and watch live events. Your first stop for verifying what AI actually configured versus what it claimed.
- **Supabase CLI**: Scaffold, serve, and deploy edge functions locally with `supabase functions new` and `supabase functions serve`, and manage secrets with `supabase secrets set`.
- **supabase-js client library**: The SDK your AI uses for uploads, signed URLs, channel subscriptions, and `functions.invoke()`. Knowing its shape lets you spot invented methods.
- **The AI Audit Prompt**: The template at the end of this guide. Run it after any AI session touching storage, realtime, or functions, just like the RLS audit from Module 3.

## Exam Topics

- Public versus private buckets, and when each is acceptable in production
- Reviewing storage policies on storage.objects that scope files by user or tenant path prefix
- Signed URLs, expiry windows, and image transformations for thumbnails
- The three realtime modes (Postgres Changes, presence, broadcast) and matching each to a use case
- How RLS interacts with realtime subscriptions and why client-side filters are not security
- When realtime is worth the connection overhead versus polling or refetch-on-focus
- Creating, deploying, and invoking edge functions, including JWT verification and secret management
- Choosing between edge functions, database functions, and frontend API routes

## Common Pitfalls

- **Public buckets holding private files**: AI defaults to public buckets because uploads just work. Every file becomes reachable by URL, and your client portal's contracts are one shared link from disaster.
- **Storage policies that check auth but not ownership**: A policy letting any authenticated user read a bucket means tenant 12 can pull tenant 31's files. Policies must check the path prefix against the user, not just require a login.
- **Trusting client-side realtime filters**: A `tenant_id=eq.12` filter in JavaScript can be edited in DevTools. Without RLS on the table, you are streaming cross-tenant data on request.
- **Edge functions with verification disabled**: AI ships `--no-verify-jwt` to ease testing and never turns it back on, leaving an anonymous endpoint that can email your users or charge cards.
- **Service role key in client code**: The service role key bypasses all RLS. In frontend code or an exposed env var, it voids every policy you wrote in Module 3.
- **Realtime for everything**: Subscribing to every table burns connections and complicates code. Data that changes daily needs a refetch, not a socket.

## Self-Assessment Checklist

- I can explain when a bucket should be private and direct AI to write path-based storage policies for it
- I can review a storage policy and confirm it checks ownership, not just authentication
- I can direct AI to serve private files through signed URLs with sensible expiry and thumbnail transformations
- I can choose between Postgres Changes, presence, and broadcast for a given live feature
- I can verify a realtime subscription is protected by RLS rather than client-side filters
- I can direct AI to deploy an edge function that verifies the caller's JWT and keeps secrets in environment variables
- I can justify whether a feature belongs in an edge function, a database function, or a frontend API route

## AI Audit Prompt Template

Paste this into your AI after any build session touching storage, realtime, or edge functions, and make it show receipts before you accept its answer.

`Audit this Supabase project's storage, realtime, and edge function security. Do not summarize; verify each claim against actual configuration and code. STORAGE 1. List every bucket and its public/private status. For each public bucket, justify why every file in it is safe to expose, or flag it. 2. Show every policy on storage.objects. Confirm each checks ownership or tenant scope via path prefix against auth.uid(), not merely authentication. 3. Flag any private file served without a signed URL, and report expiry times. REALTIME 4. List every table with realtime enabled and every channel subscription in the codebase. 5. For each Postgres Changes subscription, confirm RLS on the underlying table restricts what subscribers receive. Flag any subscription relying only on a client-side filter for isolation. 6. Flag realtime where polling would suffice, and any channel that should require authorization to join. EDGE FUNCTIONS 7. List every function and whether JWT verification is enabled. Flag any deployed with verification disabled. 8. Confirm each function validates the caller and authorizes the action, not just the token. Show the exact lines. 9. Search the codebase for the service role key or other secrets in client-reachable code or committed files. Report every hit. Output a table: item, risk level, exact file or setting, specific fix. Apply only the fixes I approve, one at a time.`

## What's Next

Module 6: Backups and Environments protects everything you have built: automated backups, point-in-time recovery, and separating development, staging, and production so an AI experiment never touches live customer data. Storage, realtime, and functions all behave differently across environments, so Module 6 picks up exactly where this one ends.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 5 badge. Pass all 7 module exams to earn the Supabase Specialist badge, certifying you can direct AI to build production backends on Supabase with security policies that hold.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
