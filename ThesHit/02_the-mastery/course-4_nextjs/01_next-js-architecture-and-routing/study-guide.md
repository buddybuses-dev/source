# Module 1: Next.js Architecture and Routing — Study Guide

## Next.js Application Build

### T4 The Mastery | Module 1 Study Guide

## Module 1: Next.js Architecture and Routing

> Direct AI to build fast, SEO-ready web applications on Next.js and Vercel.

## What This Module Covers

This module gives you the architectural foundation for everything that follows. You will learn how the Next.js App Router works: how folders become routes, how layouts wrap pages, how loading states and error boundaries are wired directly into the file system, and why this structure is the most important thing to get right before your AI writes a line of feature code. You will also learn when Next.js is the right call versus a plain React app or a static site generator.

Just as important, you will learn the difference between the App Router and the older Pages Router. Your AI has seen millions of lines of both, and if you do not direct it explicitly, it will happily mix the two and hand you a project that half works. By the end of this module you will know how to scaffold a project with the right foundation, review the structure your AI produces, and catch architectural mistakes before they calcify into technical debt, including structure decisions that scale: where routes and shared components live, and how route groups keep a marketing site and a SaaS dashboard separated inside one codebase.

## Why It Matters

Architecture is the one thing you cannot easily fix later. If your AI scaffolds a content site with the wrong routing structure, every page, layout, and SEO decision inherits that mistake. A content site that needs to rank cannot afford a structure that fights the framework, and a SaaS dashboard serving 10K daily users cannot afford routes bolted on instead of designed. Refactoring routing in a live app touches every URL, link, and layout at once. Getting it right on day one costs an hour. Getting it wrong costs weeks.

There is also an AI supervision stake. The App Router is convention driven: file names like `page.tsx` and `layout.tsx` carry real behavior. An AI that names a file wrong, nests a layout wrong, or drops Pages Router patterns into an App Router project produces bugs invisible in review unless you know the conventions. This module makes you the reviewer who catches those mistakes in seconds.

## Certification Goal

Passing this exam proves you can direct AI to scaffold an App Router project with a route structure, layout hierarchy, and error handling strategy that will scale, and that you can audit an existing structure and catch architectural mistakes before they ship.

## What You Need to Know

### The App Router Is the Modern Standard

The App Router, stable since Next.js 13.4, lives in the `app` directory and is the architecture this course is built on. It supports Server Components, nested layouts, streaming, and colocated loading and error states. Say "App Router" explicitly in every prompt, because vague prompts invite legacy patterns.

### File-Based Routing

Folders define routes and special files define behavior. The folder `app/dashboard/settings` becomes the URL `/dashboard/settings`, and its `page.tsx` is what renders there. Dynamic segments use square brackets, so `app/blog/[slug]/page.tsx` handles every blog post URL. The file tree is the routing table, so you can audit routing by reading a folder listing.

### Layouts and Nesting

A `layout.tsx` file wraps every page beneath it in the tree, and layouts nest automatically. The root layout holds your HTML shell, fonts, and global navigation; a dashboard layout adds the sidebar only for dashboard routes. Layouts preserve state and do not re-render on navigation between their child pages, which makes an app feel fast for free.

### Loading States and Error Boundaries

A `loading.tsx` file gives a route an instant loading UI backed by React Suspense, and an `error.tsx` file gives it an error boundary that catches failures without crashing the app. Both are per-route and inherited down the tree. A project missing them shows blank screens on slow data and white screens on errors.

### Route Groups and Project Organization

Folders wrapped in parentheses, like `(marketing)` and `(app)`, group routes and assign them different layouts without affecting the URL. This is how one codebase cleanly serves a public content site and an authenticated SaaS dashboard. Shared components and utilities belong outside the route folders, in top-level directories like `components` and `lib`, so the `app` directory stays a clean map of your URLs.

### When to Use Next.js at All

Choose Next.js when SEO matters, first-load performance matters, or you want frontend and backend in one deployable unit: content sites that need to rank, SaaS products, e-commerce. A purely internal tool behind a login can be a plain React SPA, and a five-page brochure site can be a static generator. Knowing when the framework earns its complexity is part of the certification.

## Your Toolkit

- **create-next-app**: The official scaffolding command. Direct your AI to start every project with it, with TypeScript and the App Router agreed up front, so you begin from a known-good baseline.
- **The Next.js documentation (nextjs.org/docs)**: Your source of truth when AI output looks suspicious. Training data lags releases; the docs do not. Verify conventions there before accepting an unfamiliar pattern.
- **The file tree audit**: Before reviewing any code, read the `app` directory listing top to bottom and confirm every route, layout, loading state, and error boundary is where it should be. Five minutes here catches most architectural drift.
- **A project structure spec in your prompt**: Give your AI the intended route map and folder rules in writing before it scaffolds anything. AI fills unspecified decisions with training-data habits; a written spec replaces its defaults with yours.

## Exam Topics

- Mapping an `app` directory tree to the URLs it produces, including dynamic segments like `[slug]` and catch-all segments
- The role of each special file: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`, and `route.ts`
- How nested layouts compose, what state they preserve, and what belongs in the root layout
- Route groups with parentheses: what they change, what they do not, and when to use them
- Key App Router versus Pages Router differences, and recognizing Pages Router patterns in AI-generated code
- Deciding when Next.js is the right framework versus a React SPA or static site generator, given a scenario
- Project structure decisions that scale: where routes, shared components, and utilities live
- Writing a scaffolding prompt that locks your AI to the App Router, TypeScript, and a specified route map

## Common Pitfalls

- **Letting AI choose the router**: An unspecified prompt often yields Pages Router code or a mix of both, which breaks in subtle ways and confuses every future prompt you write.
- **A `pages` directory appearing in an App Router project**: The clearest sign of architectural drift in AI output. Next.js will try to honor both, and routing behavior becomes unpredictable.
- **Skipping `loading.tsx` and `error.tsx`**: The app works in a demo, then shows blank screens and crashes in production when data is slow or a fetch fails. Users at 10K daily volume will find every missing boundary.
- **Duplicating navigation in every page instead of a layout**: You lose state preservation, re-render the shell on every navigation, and every design change touches dozens of files.
- **Dumping shared components inside route folders**: The `app` directory stops being a readable map of your URLs and imports tangle across routes. Separate routes and shared code from day one.
- **Choosing Next.js reflexively for every project**: An internal admin tool behind a login gains nothing from server rendering and SEO tooling. Framework overhead you do not need is complexity you still maintain.

## Self-Assessment Checklist

- I can read an `app` directory tree and state exactly which URLs it produces
- I can explain what `page.tsx`, `layout.tsx`, `loading.tsx`, and `error.tsx` each do
- I can describe how nested layouts compose and why shared UI belongs in a layout
- I can use route groups to separate a marketing site from an app dashboard in one codebase
- I can spot Pages Router patterns in AI-generated code and direct the AI to correct them
- I can justify choosing Next.js, a React SPA, or a static generator for a given scenario
- I can write a scaffolding prompt that produces an App Router project matching my route map

## AI Audit Prompt Template

Paste this prompt into your AI assistant inside your Next.js project to audit its structure and routing decisions.

`Audit this Next.js project's architecture and routing. Do not change any code yet. 1. Confirm the project uses the App Router exclusively. Flag any pages directory, getServerSideProps, getStaticProps, or other Pages Router patterns. 2. Print the app directory tree and map every route folder to the URL it produces, including dynamic and catch-all segments. 3. List every layout.tsx and what it wraps. Flag shared UI (navigation, headers, sidebars) duplicated in pages instead of a layout. 4. List every route missing a loading.tsx or error.tsx and rate how badly each gap would show in production. 5. Flag shared components, utilities, or config living inside route folders that should move to top-level directories like components or lib. 6. Evaluate whether route groups correctly separate distinct areas of the app, and recommend groupings if missing. 7. Confirm there is a root layout with the HTML shell and a not-found handler. Output a numbered list of issues ordered by severity, each with the file path, why it matters at production scale, and the fix. End with a one-paragraph verdict: is this structure ready to build on, or does it need restructuring first?`

## What's Next

Module 2: Server and Client Components takes you inside the rendering model that makes the App Router fast. You will learn where code actually runs, why "use client" is a boundary and not a preference, and how to direct AI to put interactivity only where users need it. The route structure you mastered here is the map; Module 2 teaches you what runs at each destination.

## Certification Pathway

Pass this module's exam at 80% (20 of 25 questions) to earn the Module 1 badge. Pass all 7 module exams to earn the Next.js Specialist badge and certify that you can direct AI to build, optimize, and ship production Next.js applications on Vercel.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
