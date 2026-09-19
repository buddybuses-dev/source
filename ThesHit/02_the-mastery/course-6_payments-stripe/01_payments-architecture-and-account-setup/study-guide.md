# Module 1: Payments Architecture and Account Setup — Study Guide

## Stripe Payments Build

### T4 The Mastery | Module 1 Study Guide

## Module 1: Payments Architecture and Account Setup

> Direct AI to stand up a correctly architected Stripe account before a single payment moves.

## What This Module Covers

This module establishes how modern payment systems are structured before you direct AI to build one. You will learn Stripe's account types, the difference between test and live mode, how API keys are managed and protected, and the core payment object model that every other module builds on.

## Why It Matters

Payments are the one system in your product where a mistake costs real money in real time. A misconfigured account type locks you into the wrong platform model. Leaked API keys let attackers move funds or scrape customer data. A builder who does not understand the object model directs AI to bolt charges together with duct tape, and six months later nobody can answer "why did this customer get billed twice?" Get the architecture right on day one and every later module gets easier. Get it wrong and you will be unwinding it while revenue is on the line.

## Certification Goal

Passing this exam proves you can direct AI to stand up a correctly structured Stripe account, choose the right integration model for the business, protect keys like production credentials, and explain how customers, payment intents, payment methods, and charges relate to each other.

## What You Need to Know

**1. Stripe account types: Standard, Express, Custom.** Standard accounts are full Stripe accounts the user controls directly, right for a single business taking its own payments. Express and Custom exist for platforms and marketplaces that onboard other sellers. Express gives Stripe-hosted onboarding with your platform managing payouts. Custom gives you full white-label control and full liability for onboarding, compliance, and support. Most builds you direct will be a single Standard account. The moment your product moves money on behalf of other businesses, you are in Connect territory and the account type decision becomes a business model decision, not a technical one.

**2. Test mode vs live mode are parallel universes.** Every Stripe account has two complete environments with separate keys, separate data, and separate dashboards. Nothing crosses between them. Customers created in test mode do not exist in live mode. This is a feature: you direct AI to build and verify the entire system against test mode with test cards, then switch keys at go-live. The classic failure is mixed keys, a test publishable key with a live secret key, which produces confusing errors that waste hours.

**3. API key discipline.** The publishable key is safe in the browser. The secret key is the crown jewels: it can create charges, issue refunds, and read customer data. It lives in server-side environment variables only, never in frontend code, never in a repository, never in a screenshot you share for help. Restricted keys let you grant a service only the permissions it needs, which is what you direct AI to use for any third-party integration or internal tool that does not need full access.

**4. The payment object model.** Four objects carry the whole system. A Customer is the durable record of a person or business. A PaymentMethod is a stored way to pay, like a tokenized card. A PaymentIntent is the state machine for one attempt to collect money, tracking it from creation through authentication to success or failure. A Charge is the record of an actual money movement. Customers own payment methods; payment intents produce charges. When you direct AI to build any flow in later modules, you are really directing it to move these objects through their lifecycles.

**5. Platform vs direct integration decisions.** Direct integration means your product talks to Stripe with its own account: simplest, fastest, right for most SaaS and service businesses. Platform integration via Connect means you sit between Stripe and other sellers, taking on onboarding and compliance surface in exchange for controlling the money flow. Choosing platform when you only needed direct is the most expensive architecture mistake in this course because it multiplies every later module's complexity.

**6. Dashboard setup as a business act.** The Stripe dashboard is not just a dev console. Business name, statement descriptor, support email, and branding all show up on customer statements and receipts. A vague statement descriptor is a dispute machine: customers see a name they do not recognize and file chargebacks. Directing AI cannot do this part for you; account identity, banking, and verification are owner responsibilities you complete in the dashboard.

## Your Toolkit

- **Stripe Dashboard**: account configuration, test data inspection, logs, and the event feed you will live in while verifying builds
- **Stripe API keys and restricted keys**: the credential system your AI-built services authenticate with
- **Stripe test cards**: documented card numbers that simulate success, declines, disputes, and authentication challenges
- **Environment variable management** (your host's secret store): where secret keys actually live in a professional build

## Exam Topics

1. Choosing between Standard, Express, and Custom account types for a given business model
2. Test mode vs live mode boundaries and what does and does not transfer
3. Publishable vs secret vs restricted keys and where each is allowed to live
4. The Customer, PaymentMethod, PaymentIntent, and Charge object relationships
5. PaymentIntent as a state machine for a single collection attempt
6. Direct vs platform (Connect) integration decision criteria
7. Statement descriptors, branding, and dispute prevention at the account level
8. Key rotation and exposure response when a secret key leaks

## Common Pitfalls

- Building on a Connect platform architecture when a single Standard account was all the business needed
- Hardcoding secret keys in frontend code or committing them to a repository the AI can see and copy forward
- Mixing test and live keys in one environment and burning hours on the resulting errors
- Treating a Charge as the primary object and ignoring the PaymentIntent lifecycle that governs it
- Leaving the statement descriptor as a default or LLC name customers will not recognize
- Skipping restricted keys and giving every internal tool the full secret key

## Self-Assessment Checklist

- Can I explain when a business needs Standard vs Express vs Custom without looking it up?
- Can I state which key types are safe in a browser and which are not?
- Can I trace a payment from Customer to PaymentMethod to PaymentIntent to Charge?
- Do I know what happens to test mode data at go-live? (Nothing. It stays behind.)
- Could I direct AI to respond correctly if a secret key appeared in a public repository?
- Have I set a statement descriptor a customer would actually recognize?
- Can I name one business signal that says "this build needs Connect"?

## AI Audit Prompt Template

> You are auditing the Stripe account architecture of my project. Review the integration and report: (1) which account type is in use and whether it matches the business model, (2) every place API keys appear, flagging any secret key outside server-side environment variables, (3) whether restricted keys are used for services that do not need full access, (4) how Customer, PaymentMethod, PaymentIntent, and Charge objects are created and linked, flagging any flow that creates charges without a payment intent lifecycle, (5) test vs live mode configuration and any risk of mixed keys. Output a findings table with severity and a remediation plan I can direct you to execute.

## What's Next

Module 2 takes this foundation and builds your first revenue flow: one-time checkout. You will direct AI to stand up Stripe Checkout sessions, design the product catalog, and handle the success path without trusting the redirect.

## Certification Pathway

This is Module 1 of 7 in the Stripe Payments Build course, part of T4 The Mastery. Passing all seven module exams earns the Payments Build Specialist badge. This module is the architecture layer every later module assumes.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
