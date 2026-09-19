# Module 4: Auth and User Management — Study Guide

## Supabase Backend Build

### T4 The Mastery | Module 4 Study Guide

## Module 4: Auth and User Management

> Direct AI to build production backends on Supabase with security policies that hold.

## What This Module Covers

Authentication is the front door of your app, and this module teaches you to direct AI to build one that holds when real users show up. You will cover Supabase Auth end to end: email and password sign-up, magic links, and social providers like Google, GitHub, and Apple, plus why one bad redirect URL can lock every user out.

You will also learn the data side: auth.users versus your own profiles table, user metadata, and the trigger that gives every signup a profile row. Then come sessions and protected routes. The thread through it all is supervision: AI can scaffold an auth flow in minutes, but you demand the edge cases and refuse to ship until expired sessions, unverified emails, and broken reset links are all handled.

## Why It Matters

Auth failures are the most visible failures your app can have. An RLS gap leaks data quietly; broken auth is instant. Users cannot log in, or their reset email leads to a dead page. For your client portal, a broken login is a support ticket from a paying client. For your SaaS app with 50 tenants, it is churn.

There is also a security dimension. Every RLS policy from Module 3 keys off auth.uid(), and if your auth layer accepts unverified emails or lets signup skip profile creation, those policies stand on sand. AI-generated auth handles the happy path and ignores everything else; ship it unaudited and you find out at 2 a.m. that mobile signups cannot verify their email.

## Certification Goal

Passing the Module 4 exam proves you can direct AI to implement a complete Supabase Auth system: multiple sign-in methods, correct provider and redirect configuration, a profiles table linked to auth.users, protected routes with sound session handling, and coverage of the edge cases that break production apps.

## What You Need to Know

### Supabase Auth Methods

Supabase Auth supports email and password, passwordless magic links, and OAuth providers including Google, GitHub, and Apple. Every method issues the same thing on success: a session with a JWT that identifies the user to Postgres and your RLS policies. Magic links suit a client portal; email plus Google suits a marketplace.

### Configuring Auth Providers

Social providers need setup on both sides: register an OAuth app with the provider for a client ID and secret, enter those under Authentication, Providers, and register Supabase's callback URL on the provider's side. Apple adds a services ID and signed key.

### auth.users vs a Custom Profiles Table

The auth.users table is managed by Supabase and should never be modified or queried directly from your app. Instead, create a public profiles table whose id references auth.users, plus a trigger that inserts a profile row on every signup. Display names, avatars, roles, and tenant membership belong in profiles, governed by your Module 3 RLS policies.

### User Metadata

Each user carries two metadata blobs: user_metadata, which the user can update themselves, and app_metadata, which only the service role can change. That distinction is a security boundary: never store roles or tenant IDs in user_metadata, because a user could edit their own and escalate privileges.

### Sessions and Protected Routes

A session is a short-lived access token plus a refresh token that quietly obtains new ones. Protected routes must check the session server side, not just hide buttons, and must handle expiry by redirecting to login rather than crashing.

### Redirect URLs and Deep Links

Every magic link, verification email, OAuth callback, and password reset ends with a redirect, and Supabase only redirects to URLs on your allow list. The Site URL is the default destination; extra entries cover preview deploys, staging, and mobile deep links.

## Your Toolkit

- **Supabase Dashboard, Authentication Section**: Where you enable providers, set the Site URL and redirect allow list, customize email templates, and control confirmation and session expiry. Review these yourself; code changes do not touch them.
- **Supabase Client Libraries (supabase-js)**: The SDK your AI uses for signUp, signInWithPassword, signInWithOAuth, resetPasswordForEmail, and session handling. Knowing these names lets you spot invented methods.
- **The Profiles Trigger Pattern**: A Postgres function plus trigger on auth.users that auto-creates a profiles row on signup. Confirm it uses security definer so it can write to the public schema.
- **The Auth Edge Case Checklist**: A written list you reuse: expired session, unverified email, wrong password, duplicate signup, broken reset link, OAuth cancel, bad redirect. Run every AI-built flow against it.

## Exam Topics

- The three main Supabase auth methods and when each fits a given app
- Configuring a social provider, including the provider-side callback URL
- Why auth.users is never modified directly and how a profiles table with a signup trigger solves this
- user_metadata versus app_metadata, and why roles never live in user_metadata
- How access and refresh tokens work together, and a correct expired-session experience
- Server-side session checks versus client-only UI hiding
- The Site URL and redirect allow list, and the symptoms of a misconfigured redirect
- Password reset and email verification flows, including expired or reused links

## Common Pitfalls

- **Shipping with the Site URL set to localhost**: Every verification, magic link, and reset email in production points at your dev machine. The most common Supabase auth bug.
- **Storing roles in user_metadata**: Users can edit their own user_metadata, so a curious client portal user can promote themselves to admin.
- **Querying auth.users directly from the app**: The auth schema is not exposed to your API by design. Bypassing it breaks on upgrades and leaks fields you never meant to expose.
- **Skipping the profiles trigger**: Frontend profile creation means any interrupted signup leaves orphaned users, and your app crashes on the first lookup.
- **Testing only the happy path**: AI-built auth demos sign up and log in flawlessly. The failures live in expired sessions, unverified emails, OAuth cancellations, and reused reset links.
- **Protecting routes in the UI only**: Hiding a link is not access control. Without a server-side session check, anyone with the URL reaches the page.

## Self-Assessment Checklist

- I can direct AI to implement email and password, magic link, and one social login in the same app
- I can configure Google or GitHub OAuth end to end, including the provider-side callback URL
- I can set up a profiles table and the trigger that populates it on signup
- I can explain user_metadata versus app_metadata and where roles belong
- I can verify protected routes check the session server side and handle expiry gracefully
- I can configure the Site URL and redirect allow list for local, staging, and production
- I can test an auth flow against the full edge case list before calling it done

## AI Audit Prompt Template

Paste this prompt into your AI after it builds or modifies any auth flow.

`Audit this project's authentication against production edge cases. For each item, show the code that handles it or state that it is unhandled. 1. Expired sessions: does refresh work, and do protected routes redirect to login when it fails, never crashing or going blank? 2. Email verification: is confirmation required before login? Can any protected route or API path be reached unverified? 3. Password reset: what happens if the link is expired, already used, or opened in a different browser? 4. Redirect URLs: list every redirect used, including OAuth callbacks and email links. Flag anything on localhost or missing from the Supabase allow list. 5. OAuth failures: what happens if a user cancels the consent screen or the provider errors? 6. Duplicates and orphans: what happens on signup with an existing email? Confirm a trigger creates a profiles row for every signup path, including OAuth. 7. Session checks: confirm every protected route validates the session server side, not just in client components. Output a table: edge case, current behavior, file, severity, fix. Implement the high severity fixes and list what changed.`

## What's Next

With auth in place, your users can prove who they are. Module 5: Storage, Realtime and Edge Functions puts that identity to work: per-user file uploads for your marketplace, realtime subscriptions that respect RLS, and Edge Functions for server-side logic. Auth is the foundation for all three.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 4 badge. Pass all 7 module exams to earn the Supabase Specialist badge and certify you can direct AI to build production backends on Supabase.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
