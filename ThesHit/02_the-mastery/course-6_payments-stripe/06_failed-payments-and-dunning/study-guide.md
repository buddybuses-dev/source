# Module 6: Failed Payments and Dunning — Study Guide

## Stripe Payments Build

### T4 The Mastery | Module 6 Study Guide

## Module 6: Failed Payments and Dunning

> Direct AI to recover the revenue a failed card would otherwise quietly take with it.

## What This Module Covers

This module covers the revenue nobody plans for: payments that fail. You will learn why payments fail, how Smart Retries and custom schedules work, how to direct AI to build dunning email sequences and grace periods, and how to run the recovery waterfall that separates involuntary churn from customers who actually left.

## Why It Matters

A meaningful slice of subscription payment attempts fail, and most of those customers did not choose to leave. Cards expire. Balances dip. Banks decline for reasons nobody can see. A build with no recovery system treats every failed renewal as a cancellation, silently converting recoverable revenue into churn. At scale this is one of the largest invisible line items in a subscription business. The recovery waterfall, retry, notify, escalate, suspend, cancel, is pure margin: infrastructure that wins back revenue you already earned. And because dunning is automated communication about money, tone matters; a respectful sequence recovers customers, an aggressive one finishes the churn the failed card started.

## Certification Goal

Passing this exam proves you can direct AI to build a complete recovery system: retry configuration matched to the business, a dunning sequence with the right tone and timing, grace periods that keep customers whole during recovery, and measurement that tells you what the system actually recovers.

## What You Need to Know

**1. Why payments fail.** Expired cards: predictable, preventable with pre-expiry outreach and card updater services. Insufficient funds: often temporary, which is why retry timing matters more than retry count. Fraud flags and bank declines: the issuer said no, sometimes with a reason code, often generically. Do-not-honor style generic declines are the bank declining to explain. Reading decline codes tells you whether retrying is promising, pointless, or harmful; hammering hard declines damages your standing with issuers.

**2. Involuntary vs voluntary churn are different problems.** Voluntary churn is a customer deciding to leave: a product and value problem. Involuntary churn is a payment mechanism failing under a customer who intended to stay: an infrastructure problem, and the one this module solves. Mixing them in metrics hides both. A rising churn number that is actually failed payments sends teams off fixing the product when the fix was retry timing and a card update email.

**3. Smart Retries vs custom schedules.** Stripe's Smart Retries use machine learning across the network to pick retry moments most likely to succeed for that card and failure type, and they outperform naive fixed schedules for most businesses. Custom schedules give you fixed control: retry on day 1, 3, 5, 7. The professional default you direct is Smart Retries, with the retry window and the end-of-retries action, cancel, mark unpaid, or leave past_due, chosen deliberately to match your grace period policy.

**4. Dunning sequences are lifecycle email about money.** The sequence: a soft notice at first failure, assume error, make fixing it one click via the Billing Portal, then escalating clarity as retries continue, then a final notice with the consequence and the date. Every message links directly to updating the payment method. The tone rule: the customer is not delinquent, their card had a problem; write like you are helping them stay, not chasing a debt. Stripe can send basic failure emails; a real sequence in your email system, triggered by invoice.payment_failed events, gives you tone, timing, and branding.

**5. Grace periods keep customers whole while recovery runs.** Revoking access at first failure punishes a customer whose bank hiccupped and converts a recoverable failure into an angry cancellation. The pattern: subscription enters past_due, access continues through a defined grace window while retries and emails run, then access suspends if recovery fails, then cancellation per your retry settings. Grace length is a business decision: long enough for the sequence to work, short enough that free riding stays negligible.

**6. Measure recovery or you are guessing.** The number that matters: of payments that failed, what percent were ultimately collected? Watch recovery rate, time-to-recovery, and where in the waterfall recoveries happen. If most recoveries come from retry two, your emails may be decoration. If recoveries spike after the final notice, your earlier messages are too soft. Dunning is a system you tune with data, not a set-and-forget checkbox.

## Your Toolkit

- **Stripe Smart Retries and Billing retry settings**: network-informed retry timing plus your end-of-retries policy
- **invoice.payment_failed and customer.subscription.updated webhooks**: the triggers your dunning sequence and access states hang off
- **Billing Portal payment method update flow**: the one-click fix every dunning email points to
- **Your email platform's automation triggered by payment events**: the branded, tone-controlled sequence Stripe's basic emails cannot deliver

## Exam Topics

1. Decline categories and what each implies about retrying
2. Involuntary vs voluntary churn and keeping the metrics separate
3. Smart Retries vs custom schedules and choosing the end-of-retries action
4. Dunning sequence structure: timing, escalation, and tone
5. Grace period design and the past_due access policy
6. The full recovery waterfall: retry, notify, escalate, suspend, cancel
7. Card expiration prevention and updater services
8. Recovery rate measurement and tuning the waterfall

## Common Pitfalls

- Revoking access on first failure and turning bank hiccups into cancellations
- Retrying hard declines aggressively and degrading issuer trust in your merchant account
- Counting involuntary churn as voluntary and misdiagnosing a retention problem
- Writing dunning emails that read like collections letters to customers who never chose to leave
- Running Smart Retries with no email sequence, or emails with no working payment update link
- Never measuring recovery rate, so the waterfall is never tuned and quietly underperforms

## Self-Assessment Checklist

- Can I explain what happens in my system at first failure, hour by hour?
- Do I know my end-of-retries action and why it was chosen?
- Does every dunning email link directly to a payment method update?
- Would I be comfortable receiving my own final-notice email?
- Do past_due customers keep access through a defined grace window?
- Can I state my current recovery rate, or am I guessing?
- Is card expiration handled before it fails, not after?

## AI Audit Prompt Template

> You are auditing the failed payment recovery system of my subscription business. Review it and report: (1) retry configuration: Smart Retries or custom, window length, end-of-retries action, (2) the dunning sequence: triggers, timing, escalation, tone, and whether every message links to a payment update, (3) grace period behavior: what access a past_due customer has and for how long, (4) the full waterfall from first failure to cancellation with any missing stage, (5) metrics: whether recovery rate is measured and what it shows, (6) churn reporting: whether involuntary and voluntary churn are separated. Output findings with severity, the revenue each gap forfeits, and a remediation plan I can direct you to execute.

## What's Next

Module 7 is the capstone: taking everything live. The go-live checklist, production webhooks, fraud basics with Radar, PCI scope, and the monitoring that ensures your payment system never breaks silently.

## Certification Pathway

This is Module 6 of 7 in the Stripe Payments Build course, part of T4 The Mastery. Passing all seven module exams earns the Payments Build Specialist badge. This module recovers the revenue you already earned.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
