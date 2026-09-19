# Module 2: One-Time Checkout Flows — Study Guide

## Stripe Payments Build

### T4 The Mastery | Module 2 Study Guide

## Module 2: One-Time Checkout Flows

> Direct AI to build a one-time checkout flow that takes money and never trusts the redirect.

## What This Module Covers

This module covers directing AI to build one-time purchase flows with Stripe Checkout. You will learn hosted vs embedded checkout, how products, prices, and line items structure your catalog, how success and cancel URLs actually behave, and how to handle post-payment confirmation without losing orders.

## Why It Matters

Checkout is where money enters the business, and it is also where the most silent revenue leaks live. A builder who trusts the success redirect as proof of payment will ship a store that occasionally gives away product for free or fails to deliver what was paid for. A catalog modeled as loose amounts instead of prices becomes unauditable the first time finance asks "what did we actually sell in March?" Checkout done right is boring, reliable, and convertible. Checkout done wrong looks fine in demos and bleeds money quietly in production.

## Certification Goal

Passing this exam proves you can direct AI to build a complete one-time purchase flow: a correctly modeled catalog, a Checkout session with the right mode and configuration, sane success and cancel handling, and a confirmation path that treats the redirect as a UX event, not a source of truth.

## What You Need to Know

**1. Checkout Sessions are the unit of work.** A Checkout Session represents one customer's trip through payment. You direct AI to create it server-side with line items, a mode (payment for one-time), success and cancel URLs, and any metadata you need later. Stripe returns a URL or client secret, the customer pays, and the session completes. Sessions expire, default 24 hours, so they are disposable: never store one as if it were an order.

**2. Hosted vs embedded checkout.** Hosted Checkout redirects the customer to a Stripe-run page: fastest to ship, PCI burden minimized, conversion-optimized by Stripe, less brand control. Embedded Checkout renders the same engine inside your page: more control over surrounding experience, slightly more build surface. Fully custom flows with Payment Element give maximum control and maximum responsibility. The professional default for a first build is hosted; you direct AI toward embedded or custom only when a concrete business reason exists, not for aesthetics alone.

**3. Products and Prices are the catalog, not magic numbers.** A Product is the thing you sell. A Price is a specific amount, currency, and billing behavior attached to it. Directing AI to pass ad-hoc amounts into every session works until you need reporting, price changes, or multiple currencies. Model the catalog in Stripe: one product, potentially many prices. Line items in a session reference prices. This is also what makes the dashboard's revenue reporting mean something.

**4. Success and cancel URLs are UX, not truth.** After payment, Stripe redirects to your success URL, optionally with the session ID in the query string. The redirect can fail to happen: the customer closes the tab, the network drops, the phone dies. Payment still succeeded. So the success page is where you say thank you and show order status, ideally by retrieving the session server-side with the session ID. Fulfillment, granting access, sending the product, is triggered by the webhook in Module 4, never by the redirect alone. The cancel URL simply returns the customer to shopping; nothing was charged.

**5. Cart-to-checkout data flow.** Your cart lives in your app; Stripe sees only the line items you send when creating the session. The critical discipline: compute prices server-side from your catalog, never trust amounts sent from the browser. Attach your own order or user identifiers via client_reference_id or metadata so the completed session can be matched back to the right customer and cart when the webhook fires.

**6. Currency and locale handling.** Checkout can localize its interface and you can present prices in multiple currencies with per-currency price objects. Charging a customer in an unexpected currency creates confusion, conversion complaints, and disputes. Decide currency strategy at the catalog level, direct AI to build it there, and let Checkout's locale detection handle language.

## Your Toolkit

- **Stripe Checkout (hosted and embedded)**: the conversion-optimized payment engine you configure rather than rebuild
- **Products and Prices in the Stripe dashboard**: your auditable catalog and the source of truth for amounts
- **Payment Links**: zero-build checkout URLs for validating an offer before directing a full integration
- **Stripe test cards and the dashboard event feed**: how you verify every path: success, decline, and abandonment

## Exam Topics

1. Choosing hosted vs embedded vs custom checkout for a given business context
2. Checkout Session lifecycle: creation, expiration, completion
3. Modeling products, prices, and line items instead of ad-hoc amounts
4. Correct roles of success and cancel URLs and what they do not prove
5. Server-side price computation and why browser-supplied amounts are never trusted
6. Using client_reference_id and metadata to tie sessions to your own orders
7. Retrieving a session on the success page to display accurate confirmation
8. Currency and locale strategy at the catalog level

## Common Pitfalls

- Fulfilling orders from the success redirect and losing orders whenever the redirect never fires
- Passing cart totals from the browser into session creation, letting anyone edit their own price
- Skipping the catalog and hardcoding amounts, making revenue reporting and price changes painful
- Treating an expired or abandoned session as an error instead of a normal disposable object
- Building fully custom checkout for brand reasons and inheriting weeks of edge cases Stripe had solved
- Forgetting metadata on the session, then being unable to match a payment to an order when it matters

## Self-Assessment Checklist

- Can I explain why the success redirect is not proof of payment?
- Do I know what belongs in a Checkout Session vs what belongs in my own database?
- Could I direct AI to model a three-product catalog with prices in two currencies?
- Do I know where the amount a customer pays is computed in a safe build? (Server-side, from the catalog.)
- Can I describe what the customer experiences on cancel, and what Stripe recorded? (Return to shopping; nothing charged.)
- Have I tested a decline card and an abandoned session, not just the happy path?
- Can I explain when a Payment Link beats a coded integration?

## AI Audit Prompt Template

> You are auditing the one-time checkout flow of my project. Review it and report: (1) whether sessions are created server-side with prices drawn from a catalog, flagging any browser-supplied amounts, (2) how success and cancel URLs are handled and whether any fulfillment logic depends on the redirect, (3) whether client_reference_id or metadata ties each session to an internal order, (4) session expiration handling, (5) currency configuration and any mismatch risks. Output findings with severity, the exact revenue-loss scenario each finding enables, and a remediation plan I can direct you to execute.

## What's Next

Module 3 moves from one-time purchases to recurring revenue: subscriptions, price models, trials, and the Billing Portal that lets customers manage themselves.

## Certification Pathway

This is Module 2 of 7 in the Stripe Payments Build course, part of T4 The Mastery. Passing all seven module exams earns the Payments Build Specialist badge. This module delivers your first complete revenue flow.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
