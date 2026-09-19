# Module 6: Vercel Deployment and Environments — Study Guide

## Next.js Application Build

### T4 The Mastery | Module 6 Study Guide

## Module 6: Vercel Deployment and Environments

> Direct AI to build fast, SEO-ready web applications on Next.js and Vercel.

## What This Module Covers

Everything before this module happens on your machine. This module is where your app meets the real world: you direct AI to deploy a Next.js project to Vercel, wire up environment variables across preview, staging, and production, connect a custom domain with proper DNS, and choose between edge and serverless functions for each route.

You will also learn the operational side that separates a hobby deploy from a production pipeline: build configuration, deployment monitoring, and rollback strategies that recover from a bad ship in under a minute. Vercel makes deployment look like magic, and that is exactly why builders get burned: when every push to main goes live automatically, a careless merge is a production incident. Your job is to direct AI to set up the pipeline, then audit it yourself, because AI will happily configure something that works on the happy path and fails the first time something goes wrong.

## Why It Matters

Picture your SaaS dashboard serving 10K daily users. Your AI ships a feature, the build passes, and twenty minutes later payments are failing because production is reading a test Stripe key. That is not a code bug. That is an environment management failure, and it is the single most common way vibecoded apps break in production.

The same stakes apply to your content site that needs to rank: a botched DNS cutover can take your domain dark for hours while search engines are crawling, and a bad redirect setup splits your authority between www and apex. When a bad deploy goes out, the builders who thrive roll back in sixty seconds instead of debugging live while users churn. Deployment competence is what makes everything from Modules 1 through 5 actually reachable, fast, and trustworthy.

## Certification Goal

Passing the Module 6 exam proves you can direct AI to deploy a Next.js application to Vercel with correctly scoped environment variables, a working custom domain, sensible edge versus serverless choices, and a rollback plan, and that you can audit that pipeline for the misconfigurations that break production.

## What You Need to Know

### Vercel Project Setup and Git Integration

Vercel connects to your Git repository and deploys automatically: pushes to your production branch trigger production deploys, and every other branch or pull request generates a preview deployment. Your branch strategy is your deployment strategy. Direct your AI to keep main deployable at all times, because on Vercel, merged means live.

### Environment Variables Across Environments

Vercel scopes variables to three environments: Production, Preview, and Development. The same variable name holds different values in each, which is how preview deploys use a test database while production uses the real one. Anything prefixed NEXT_PUBLIC_ is bundled into client JavaScript and visible to anyone, so secrets must never carry that prefix, and changed variables do not take effect until you redeploy.

### Preview Deployments as Your Staging Layer

Every pull request gets its own live URL running the Preview environment's variables. This is where you review your AI's work in a real deployed context before it touches production: click through the feature, check the data it connects to, share the link for feedback. Teams wanting a formal staging layer pin a staging branch with its own domain and variable values.

### Custom Domains and DNS

Connecting yourdomain.com to Vercel means adding an A record for the apex domain and a CNAME for www, or moving nameservers to Vercel entirely. SSL certificates provision automatically once DNS resolves. Pick www or apex as canonical and let Vercel redirect the other, because serving both without a redirect splits your SEO signals.

### Edge vs Serverless Functions

Serverless functions run in a single region with full Node.js support: use them for heavy work, database logic, and packages that need Node APIs. Edge functions run close to the user worldwide with near-zero cold starts but a restricted runtime: use them for middleware, auth checks, redirects, and personalization. The trap to catch in review: an edge function calling a database in a distant region adds a slow round trip per request, erasing the edge benefit.

### Build Configuration and Output Optimization

The build step turns your code into the deployed output, and it is where size and speed are won. Direct your AI to keep builds clean: no ignored TypeScript or ESLint errors just to force a deploy, correct root directory settings in a monorepo, no heavy dependencies bloating the client bundle. A build time or bundle size that suddenly doubles means something was added that should not be there.

## Your Toolkit

- **Vercel Dashboard**: Mission control for deployments, environment variables, domains, logs, and instant rollback. Every incident response starts here, so know where these panels live before you need them under pressure.
- **Vercel CLI**: Run `vercel` for preview deploys, `vercel env pull` to sync variables into a local .env file, and `vercel logs` to inspect a deployment. This is how you verify the pipeline without clicking through the dashboard.
- **Preview URL Review Habit**: Treat every pull request's preview link as a mandatory checkpoint. You are the QA gate for your AI's output, and the preview deployment is where you do that job against real infrastructure.
- **Instant Rollback**: Vercel keeps every previous deployment immutable and ready, so promoting a known-good deploy back to production takes seconds with no rebuild. Know this flow cold before you need it.

## Exam Topics

- The Git-to-deploy flow: which pushes create preview deployments and which create production deployments
- The three Vercel environment scopes and how one variable name holds different values in each
- Why NEXT_PUBLIC_ variables are exposed to the browser and which values must never use that prefix
- Why an updated environment variable requires a redeploy to take effect
- DNS for custom domains: A record for apex, CNAME for www, one canonical version redirecting to the other
- Choosing edge versus serverless functions, including the database-latency trap for edge
- How instant rollback to a previous immutable deployment works and when to use it
- What to check in build logs and deployment monitoring before and after promoting a deploy

## Common Pitfalls

- **Test keys in production, or live keys in preview**: Misscoped variables are the number one production failure for vibecoded apps. One wrong scope means broken payments in production or real charges from a preview branch.
- **Secrets in NEXT_PUBLIC_ variables**: The prefix ships the value to every visitor's browser. Anyone with dev tools now has your API key, and rotating it after exposure is painful.
- **Merging without checking the preview URL**: A passing build does not mean the feature works. Skip the preview click-through and production becomes the first place you see your AI's mistakes.
- **DNS cutover with no plan**: Changing records on a live domain without accounting for propagation and TTL can take your site dark for hours during peak crawl time.
- **Edge functions doing serverless work**: An edge function hitting a single-region database makes every request slower than plain serverless would have been. Faster runtime, worse architecture.
- **No rollback rehearsal**: If the first time you look for the rollback button is during an outage, you are debugging live while users churn. Practice the flow before you need it.

## Self-Assessment Checklist

- I can direct AI to connect a repository to Vercel and explain which branches produce preview versus production deploys
- I can scope environment variables correctly to Production, Preview, and Development, and explain why changes require a redeploy
- I can spot a secret wrongly exposed through a NEXT_PUBLIC_ prefix during review
- I can configure a custom domain with correct A and CNAME records and one canonical redirect
- I can decide, route by route, whether edge or serverless is the right runtime and defend the choice
- I can read build logs and deployment status to catch a bad deploy before promoting it
- I can execute an instant rollback to a previous deployment in under a minute

## AI Audit Prompt Template

Give your AI this prompt to audit your deployment pipeline before you trust it with production traffic.

`Audit the Vercel deployment pipeline for this Next.js project. Report findings by severity (critical, warning, suggestion). 1. Environment variables: List every variable the code reads. Confirm each exists in the correct scopes (Production, Preview, Development), flag any secret using the NEXT_PUBLIC_ prefix, and flag anywhere preview could touch production data or live payment keys. 2. Preview flow: Confirm every pull request generates a preview deployment using non-production credentials, and that nothing reaches the production branch without review. 3. Domains and DNS: Verify domain configuration and SSL, confirm one canonical domain (www or apex) with a redirect from the other, and flag wrong or missing DNS records. 4. Runtime choices: List every route using the edge runtime and confirm each has a reason. Flag any edge function calling a single-region database. 5. Build health: Check for ignored TypeScript or ESLint errors, and report build time and bundle size with anything unusually large flagged. 6. Rollback readiness: Confirm previous deployments are available for instant rollback, then write a runbook: exact steps to roll production back to the last known-good deploy in under one minute. Do not change anything yet. Report first, then propose fixes for my approval one at a time.`

## What's Next

Module 7 is the capstone: Ship: Production Next.js App. You will combine routing, server components, data fetching, server actions, SEO, and this module's deployment pipeline to direct AI through shipping a complete production application end to end. Everything you validated here becomes the launch checklist you run for real.

## Certification Pathway

Pass this module's exam at 80% (20 of 25 questions) to earn the Module 6 badge. Pass all 7 module exams to earn the Next.js Specialist badge, certifying that you can direct AI to build fast, SEO-ready web applications on Next.js and Vercel.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
