# Module 2: Server and Client Components — Study Guide

## Next.js Application Build

### T4 The Mastery | Module 2 Study Guide

## Module 2: Server and Client Components

> Direct AI to build fast, SEO-ready web applications on Next.js and Vercel.

## What This Module Covers

Module 2 tackles the most important architectural decision in every Next.js app your AI builds: which components render on the server and which render in the browser. Module 1 covered how the App Router organizes pages and layouts. Now you learn what happens inside those files. Next.js defaults to Server Components: your code runs on Vercel's infrastructure, produces finished HTML, and ships almost no JavaScript to the visitor. Client Components are the exception you opt into with the "use client" directive when you genuinely need interactivity.

This module gives you the server-first mental model, shows how data flows from server components into client components through props, and covers the mistakes that wreck AI-generated Next.js apps: marking everything as client, leaking secrets into browser code, and breaking the server component tree. You will not write these components yourself. You tell your AI where the client boundary belongs, then audit its output to confirm it obeyed.

## Why It Matters

Component boundaries are where AI-built Next.js apps quietly go wrong. Under vague direction, AI will slap "use client" on every file because it silences errors fast. The app works in a demo, so you ship it. Then your content site sends crawlers a near-empty HTML shell, your SaaS dashboard ships 800KB of JavaScript to every phone, and your Lighthouse scores crater. At 10K daily users, visitors feel every wasted kilobyte, and Google ranks you accordingly.

The security stakes are worse. A server component can safely hold a database query or a Stripe secret key because that code never leaves the server. The moment the same logic lands in a client component, your secrets sit in the browser bundle where anyone can read them with View Source. Builders who cannot audit the server and client split are one lazy AI suggestion away from a leaked API key and a very bad week.

## Certification Goal

Passing the Module 2 exam proves you can classify any component as server or client, direct AI to place the "use client" boundary correctly, and catch secret leaks and performance regressions in AI-generated component trees before they ship.

## What You Need to Know

### The Server-First Mental Model

Every App Router component is a Server Component until you say otherwise. It runs on the server, can talk directly to databases and APIs, and sends finished HTML to the browser with zero component JavaScript. Your default instruction to AI: keep it on the server unless there is a specific reason not to.

### What Client Components Are Actually For

Client Components exist for interactivity: click handlers, form state, useState and useEffect hooks, browser APIs like localStorage, and widgets that need the DOM. If a component only displays data, it has no business being a client component. A dashboard page can be 90 percent server-rendered with a few small interactive islands.

### The "use client" Directive

The string "use client" at the top of a file marks where server rendering ends and browser JavaScript begins. Critically, everything that file imports also joins the client bundle. One directive placed too high in the tree drags dozens of components to the client with it, which is why boundary placement is the decision you supervise most closely.

### Passing Data Across the Boundary

Server components fetch data and pass it to client components as props. The catch: props crossing the boundary must be serializable. Plain objects, arrays, and strings travel fine; functions, class instances, and database connections do not. Direct your AI to fetch on the server and pass plain data down.

### Composition: Server Children Inside Client Parents

A client component cannot import a server component, but it can receive one as children. This is how a server-rendered article lives inside an interactive tab wrapper without becoming client code. When your AI claims something "has to be a client component," the children pattern usually proves it wrong.

### Why This Decides SEO, Performance, and Security

Server components give crawlers complete HTML on the first response, which is why a server-first content site ranks. Less client JavaScript means faster loads for your 10K daily users. And server-only code is the only safe home for secrets. Every boundary decision moves all three needles at once.

## Your Toolkit

- **The Boundary Question**: Before approving any component, ask: does this need to respond to user interaction in the browser? If no, it stays on the server. This single filter catches most AI boundary mistakes.
- **Leaf-Node Placement Rule**: Direct your AI to push "use client" as far down the tree as possible, wrapping only the button, form, or toggle that needs it, never the whole page. Small client islands, big server ocean.
- **Bundle Inspection**: Run the build and read the route-by-route JavaScript sizes Next.js prints, or use @next/bundle-analyzer. A route whose bundle balloons after an AI change means the boundary moved somewhere it should not have.
- **Env Var Naming Discipline**: Only variables prefixed NEXT_PUBLIC_ are exposed to the browser. Keep secrets unprefixed, and treat any AI suggestion to add NEXT_PUBLIC_ to a key as a red flag to investigate.

## Exam Topics

- The default rendering location of an App Router component and why Next.js chose it
- What "use client" does, where it goes, and what happens to that file's imports
- Which features require a client component: useState, useEffect, event handlers, browser APIs
- What server components can do that client components cannot: direct data access, secret usage, zero-JS rendering
- Serialization rules for props passed from server to client components
- The children composition pattern for nesting server components inside client components
- How component boundaries affect SEO crawlability, bundle size, and Core Web Vitals
- Identifying secret exposure risk in a component tree, including NEXT_PUBLIC_ misuse

## Common Pitfalls

- **Marking everything "use client"**: It makes build errors disappear, so AI reaches for it constantly. You lose server rendering, ship a bloated bundle, and hand crawlers an empty shell.
- **Secrets in client components**: An API key referenced in a client file gets compiled into public JavaScript. Anyone can extract it, and you find out when your bill spikes.
- **Placing the boundary at the page level**: One "use client" on a page file converts the entire subtree. Your whole dashboard becomes browser JavaScript because one dropdown needed state.
- **Importing server components into client files**: This silently converts the server component to client code or throws confusing errors. The fix is the children pattern, not more directives.
- **Passing non-serializable props across the boundary**: Functions and class instances cannot cross from server to client. AI sometimes tries it, and the runtime errors will not name the real cause.
- **Fetching data inside client components by default**: It works, but it trades a fast server-side fetch for loading spinners, layout shift, and an extra round trip your users pay for.

## Self-Assessment Checklist

- I can explain why Next.js renders components on the server by default
- I can read a component's code and decide whether it needs "use client"
- I can direct AI to place the client boundary at the smallest possible leaf component
- I can explain how data passes from server to client and what serialization allows
- I can use the children pattern to keep server components inside client wrappers
- I can spot a secret or private env var about to ship in a client bundle
- I can connect a boundary decision to its impact on SEO, bundle size, and load speed

## AI Audit Prompt Template

Paste this prompt into your AI assistant after any build session to audit the component boundaries it created.

`Audit the component boundaries in this Next.js App Router project. 1. List every file containing the "use client" directive. For each one, state the specific interactive feature (hook, event handler, or browser API) that justifies it. Flag any client component with no such justification and propose converting it back to a server component. 2. For each "use client" file, list what it imports and estimate how much of the tree it pulls into the client bundle. Flag any boundary placed at the page or layout level and propose a smaller leaf-level boundary instead. 3. Scan all client components and their imports for secrets: API keys, database URLs, tokens, or any process.env variable without the NEXT_PUBLIC_ prefix. Flag every instance as a critical security issue. 4. Check props passed from server to client components for non-serializable values such as functions or class instances. 5. Identify data fetching happening in client components that could move to a server component parent. Output a table: file path, current type (server/client), verdict (correct / should be server / security risk), and the one-line fix. Do not change any code until I approve the plan.`

## What's Next

With boundaries under control, Module 3: Data Fetching and Caching shows you where the data itself comes from. You will direct AI to fetch inside server components, control caching and revalidation, and decide what renders fresh per request versus serving instantly from cache. The server-first model you built here is the foundation that module stands on.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 2 badge. Pass all 7 module exams to earn the Next.js Specialist badge and prove you can direct AI to ship production Next.js applications end to end.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
