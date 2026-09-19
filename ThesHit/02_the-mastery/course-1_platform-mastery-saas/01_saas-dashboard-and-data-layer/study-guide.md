# Module 01: SaaS Dashboard — Study Guide

## Module 1: Building the SaaS Dashboard

**Frontend Foundations for Subscription Products**

This is the study guide. Everything for SaaS Dashboard is on this page — there's nothing to download.

———

## What This Module Covers

This module covers frontend foundations as they apply specifically to SaaS applications—the dashboards, pricing pages, settings panels, and user-facing components that make a subscription product feel like a professional tool instead of a weekend project. You already know frontend basics from the CADE program. This goes deeper into the patterns that separate a SaaS product from a regular website: multi-step onboarding flows, plan-gated UI elements, usage dashboards that update in real time, and settings panels that manage billing, teams, and permissions all in one place. Your AI coding tool can build a beautiful dashboard in an afternoon. But if the pricing page doesn’t clearly show what each plan includes, if the settings panel forgets to hide admin controls from regular users, or if the dashboard doesn’t load fast enough when there’s a year’s worth of data—your customers will churn before their first renewal.

## Why It Matters

SaaS lives and dies on the dashboard. It’s where your customers spend 90% of their time. A SaaS dashboard isn’t just a frontend—it’s the product itself. If your dashboard is confusing, slow, or inconsistent, customers don’t complain. They cancel. The pricing page is the second most important screen in your entire application, right after the dashboard. It’s where the buying decision happens. If your pricing page doesn’t clearly communicate value at each tier, you lose revenue on every visit. AI coding tools are excellent at generating dashboard layouts. They’re terrible at understanding your business logic—which features are gated to which plan, what data a free user should see versus a paying user, and how to handle the moment someone downgrades. Those decisions are yours. This module teaches you what to ask for.

## Module Certification Goal

You can describe a SaaS dashboard, pricing page, and settings panel to an AI coding tool, evaluate the output for plan-gated visibility, responsive layout, and data loading performance, and ship a frontend that feels like a product customers will pay for monthly.

## What You Need to Know

**Dashboard layout architecture:** A SaaS dashboard isn’t one big page—it’s a shell with a sidebar navigation, a top bar (usually showing the user’s name and plan), and a content area that swaps based on what the user clicks. Your AI tool will build this, but you need to tell it the navigation structure upfront or you’ll rebuild it three times.

**Plan-gated UI components:** Some features in your app are only available to certain subscription plans. The frontend needs to know which plan the logged-in user is on and show or hide features accordingly. A free user might see a ‘Usage’ widget but not ‘Team Management.’ This gating happens in the frontend, but the source of truth is the backend—the frontend just reads the user’s plan and decides what to render.

**Pricing page design patterns:** SaaS pricing pages follow a well-established pattern: plan columns side by side, features listed with checkmarks, a highlighted ‘recommended’ plan, and clear CTAs. Your AI tool knows this pattern. What it doesn’t know is your specific plan logic—which features belong in which tier, what the upgrade path looks like, and whether you offer monthly vs annual billing with a discount.

**Real-time data loading for dashboards:** A SaaS dashboard often shows live data—usage metrics, recent activity, notifications. If you ask AI to build a dashboard and don’t specify how data loads, it might fetch everything on page load, which works fine with 10 records but chokes at 10,000. You need to tell your AI tool about pagination, lazy loading, and caching strategies.

**Onboarding flows:** The first experience a new user has with your SaaS product determines whether they stay or leave. Onboarding flows—step-by-step wizards that walk users through setup—are critical. Your AI can build the screens, but you need to define the steps, the data each step collects, and what happens when someone skips a step or drops off halfway through.

**Settings and billing panels:** Every SaaS app needs a settings section where users manage their account, team, and billing. This includes profile editing, plan management (upgrade/downgrade), payment method updates, and invoice history. These panels touch multiple backend services—auth, payments, database—so the frontend needs to handle loading states, error states, and confirmation dialogs gracefully.

## Your Toolkit

**AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code, Windsurf, or whatever AI-assisted builder you prefer. You’ll describe dashboard layouts, pricing pages, and settings panels to it.

**A component library or design system:** Shadcn/ui, Radix, Headless UI, or whatever your AI tool generates. SaaS dashboards benefit from consistent components—cards, tables, modals, dropdowns—that share the same design language across every screen.

**A charting library:** Recharts, Chart.js, or similar. SaaS dashboards almost always need charts—usage graphs, revenue trends, activity timelines. Your AI tool will pick one, but you need to know that chart rendering can be heavy and should be lazy-loaded.

**Browser DevTools:** Chrome DevTools for checking responsive layouts, inspecting network requests (are dashboard API calls fast enough?), and verifying that plan-gated components are actually hidden—not just visually concealed with CSS.

## Certification Exam Topics

Every exam question is scenario-based. You’ll see a situation and need to identify what’s right, what’s wrong, or what to do next. Here’s what gets tested:

**Dashboard architecture:** Can you evaluate whether an AI-built SaaS dashboard separates navigation, layout shell, and content areas into proper components—or dumps everything into one file?

**Plan-gated visibility:** Can you identify when a feature is hidden with CSS (still in the DOM, still accessible) versus properly gated by the user’s plan from the backend?

**Pricing page evaluation:** Can you spot when a pricing page is missing critical conversion elements—unclear plan differences, no annual/monthly toggle, hidden feature limits?

**Data loading performance:** Can you diagnose why a dashboard loads slowly as data grows and identify the right strategy—pagination, virtualization, or caching?

**Onboarding flow design:** Can you evaluate whether an onboarding flow collects the right data, handles drop-offs gracefully, and actually gets users to their first moment of value?

**Settings panel completeness:** Can you assess whether a settings panel handles all the edge cases—plan changes, payment failures, team removals, account deletion?

**Responsive SaaS layouts:** Can you verify that a SaaS dashboard works on mobile—not just the marketing site, but the actual product experience with sidebar, tables, and charts?

**Component consistency:** Can you catch when an AI tool generates inconsistent components across different dashboard sections—different button styles, card widths, or table layouts?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment—they’re easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Building the marketing site and the dashboard as separate projects with separate design systems. They should share the same brand tokens—or your product looks like two different companies made it. Hiding premium features with CSS instead of conditional rendering. A user who opens DevTools can see (and potentially use) features they haven’t paid for. Plan gating must be enforced by the backend—the frontend just decides what to show. Building the pricing page with hardcoded plan data instead of pulling it from a config or API. When you change pricing (and you will), you’ll forget to update the pricing page and your checkout page will show different numbers. Not testing what happens when a paying customer downgrades to the free plan. Do their premium features disappear immediately? Do they get a grace period? Does the UI handle the transition without errors? Loading the entire dashboard’s data on initial page load. A dashboard with usage charts, recent activity, team members, and billing data should load each section independently so the user sees something fast instead of a spinner for 8 seconds. Skipping empty states. What does your dashboard look like for a brand new user with zero data? If it’s a blank screen with no guidance, you’ve lost them. AI won’t add empty states unless you ask for them.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every “no” is something to work on. Can you describe your SaaS dashboard layout to AI clearly enough to get a usable shell with navigation, top bar, and content area on the first try? Does your pricing page clearly show what’s included in each plan, with a highlighted recommended tier and both monthly and annual options? Are premium features gated by the user’s subscription plan from the backend—not just hidden with CSS? Does your dashboard load data in sections (progressive loading) rather than all at once on page load? Have you tested what your dashboard looks like for a brand new user with no data? Does your settings panel handle plan upgrades, downgrades, payment method changes, and account deletion without errors? Does your SaaS product work on a phone—not just the landing page, but the actual dashboard with its sidebar and data tables?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my SaaS application’s frontend and check the following. For each one, tell me pass or fail with a specific example: Dashboard architecture: Is the dashboard built with a proper shell (sidebar + top bar + content area) using separate, reusable components? Plan gating: Are premium features conditionally rendered based on the user’s subscription plan from the backend—not just hidden with CSS? Pricing page: Does the pricing page clearly show plan differences, include a recommended tier highlight, and offer monthly/annual toggle? Data loading: Does the dashboard load data progressively (section by section) rather than fetching everything at once on page load? Empty states: Do all dashboard sections show helpful guidance when there’s no data yet, instead of a blank screen? Settings panel: Does the settings section handle profile editing, plan management, payment methods, and team management without broken states? Give me an overall score out of 6 and list the top 3 things to fix first.

## What’s Next

Once you’ve gone through this module and can answer “yes” to the self-assessment checklist, you’re ready for the Module 1 exam. The best way to prepare: build a real SaaS dashboard. Start with the shell—sidebar, top bar, content area. Add a pricing page. Build a settings panel. Connect plan data from your backend and test what happens when a user upgrades, downgrades, or hits their usage limit. Every gap you catch during building is exactly what the exam tests.

### Certification Pathway

**Platform Specialist — SaaS Build:** Pass all 7 module exams in this course

**CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges

**CADE Distinguished:** CADE Certified + 6 specialist badges Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush—take the time to build something real first.

———

Ready? Take the SaaS Dashboard Exam →
