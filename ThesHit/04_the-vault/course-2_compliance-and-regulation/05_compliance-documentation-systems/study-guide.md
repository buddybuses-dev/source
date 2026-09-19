# Module 5: Compliance Documentation Systems — Study Guide

## Compliance Foundations for Builders

T6 The Vault | Module 5 Study Guide

Direct AI to map which regulations apply to any build before shipping it.

## What This Module Covers

Modules 1 through 4 taught you which regulations touch your build. This module covers the paper trail: privacy policies, terms of service, cookie and tracking disclosures, Data Processing Agreements for B2B, and the records that let you prove what your product does when someone asks.

Any builder in The Faction can direct AI to generate a privacy policy in thirty seconds, and that is exactly the danger. A generic policy makes promises your app does not keep and misses disclosures it actually needs. The gap between "we have a privacy policy" and "our privacy policy matches our data practices" is where builders get hurt. You will learn what each document is for and how to direct AI to draft documentation that is accurate, not merely present. This is boundary knowledge, not legal advice: you build the map, and you bring in a professional when the stakes call for it.

## Why It Matters

Remember the builder who shipped a scheduling app for dentists without knowing HIPAA existed? The documentation version happens every week: a builder pastes a template policy saying "we do not share your data with third parties," while the app quietly sends events to three analytics SDKs and a session replay tool. That is a false statement to users, exactly what regulators like the FTC act on. Your app's behavior is the ground truth; the documents either match it or they are a liability.

The stakes go beyond regulators. The SaaS founder who launched in the EU without GDPR compliance watched an enterprise deal stall when the customer asked for a Data Processing Agreement before signing. Documentation is a sales asset, not just defense. Builders who can produce an accurate policy, a real DPA, and clean records close deals faster.

## Certification Goal

Passing this exam proves you can identify which compliance documents a build requires, explain what each must accurately reflect, describe baseline record-keeping, and direct AI to audit documentation against the app's real data practices. It proves you can build and verify the paper trail, not that any product is compliant.

## What You Need to Know

### The Accuracy Principle

Every compliance document is a claim about how your product behaves, and the product is the ground truth. A policy that overstates protections or omits real data flows is a misrepresentation, often a violation on its own. Make the documents match the build, and keep them matched as it changes.

### Privacy Policies That Match Reality

A real privacy policy answers: what data you collect (including automatically, via SDKs and logs), why, who you share it with, how long you keep it, and what rights users have. Templates answer these for someone else's app. Inventory your actual data flows first, then write the policy from the inventory.

### Terms of Service Basics

Terms of service define the deal with your users: what the service is, what users may not do, how accounts end, liability limits, and dispute handling. Builders lean hardest on acceptable use, disclaimers, and termination. Terms must be actually agreed to, so signup checkboxes and dated versions matter.

### Cookie Consent and Tracking Disclosures

If your app sets non-essential cookies or trackers, GDPR and EU ePrivacy rules, plus US state laws like CCPA, require disclosure and, in the EU, consent before trackers fire. A banner appearing after analytics scripts already loaded is theater. Know exactly what your app loads and when.

### Data Processing Agreements for B2B

When your product processes personal data for a business customer, you are the processor, they are the controller, and GDPR requires a written DPA. It specifies what you process, your security obligations, your subprocessors (hosting and AI API vendors count), and what happens on breach or termination.

### Record-Keeping and Producibility

Compliance is partly the ability to produce evidence on request: a data inventory, processing records if GDPR applies, timestamped consent logs, DPAs and vendor agreements, dated versions of every published policy, and logs of deletion or access requests. Keep records long enough to prove what you did, but do not hoard personal data past its stated retention.

## Your Toolkit

- **Data Flow Inventory:** A living list of every category of data your app touches, where it enters, where it is stored, which vendors receive it, and how long it lives. The source of truth every other document is written from.
- **Policy-to-Practice Audit Prompt:** A repeatable AI prompt (template below) comparing your published documents against your actual codebase and vendor list. Run it before every major release.
- **Document Version Log:** A dated archive of every published version of your policy, terms, and DPA, plus what changed and when users were notified.
- **Vendor and Subprocessor Register:** Every third-party service that touches user data, what each receives, and links to their DPAs. Feeds your policy, DPA annex, and security questionnaires.

## Exam Topics

- Why a privacy policy that does not match actual practices creates legal exposure.
- The core questions an accurate privacy policy must answer: what is collected, why, shared with whom, retention, and user rights.
- Why policies get written from a data flow inventory, not a template.
- The essential terms of service sections and why versioning and affirmative agreement matter.
- When cookie consent is required, what counts as non-essential, and why consent must precede trackers firing in the EU.
- What a DPA is, when B2B builders need one, and what a subprocessor is.
- Baseline record-keeping: consent logs, processing records, dated policy versions, deletion request logs, producibility on request.
- How to direct AI to audit documentation against the real app instead of generating generic documents.

## Common Pitfalls

- **Shipping a template policy untouched:** It describes someone else's app, so it makes false promises and misses your required disclosures. Regulators treat false statements as violations on their own.
- **Writing the policy before the inventory:** If you do not know your own data flows, your policy is fiction by construction.
- **Forgetting the SDKs:** Analytics, crash reporting, session replay, and AI APIs all receive user data. Leaving them out is the most common mismatch in vibecoded apps.
- **Consent banners that do nothing:** A banner appearing after trackers already fired is theater with no legal effect where consent is required.
- **No version history:** If you update policies silently, you cannot prove what any user agreed to.
- **Treating documentation as one-and-done:** New features, vendors, or data fields invalidate documents. They drift unless auditing is part of your release process.

## Self-Assessment Checklist

- I can build a data flow inventory including third-party SDKs and vendors.
- I can check my privacy policy against my inventory using the core disclosure questions.
- I can explain the essential terms of service sections and why versioned agreement matters.
- I can determine whether my app needs cookie consent and verify trackers respect it.
- I can explain what a DPA is, when I need one, and what belongs in a subprocessor list.
- I can name the records I should keep, how long, and what I must produce on request.
- I can direct AI to audit my documents against my app's actual behavior and act on the mismatches.

## AI Audit Prompt Template

Give your AI this prompt along with your published privacy policy, your cookie disclosure, and access to your codebase or a description of your stack and vendors.

> You are auditing my compliance documentation against my app's actual behavior. Do not flatter me. Find every mismatch. INPUTS: (1) my privacy policy, (2) my cookie disclosure and consent banner behavior, (3) my codebase or full stack list: SDKs, analytics, payment processors, hosting, AI services. DO THE FOLLOWING: 1. Build a data inventory from the app itself: every category of personal data collected, where it enters, where it is stored, and every third party that receives it. 2. Compare that inventory line by line against my policy. Flag: data the policy never mentions, claims the app does not honor, vendors omitted, retention statements with no matching deletion behavior. 3. List every tracker actually set, whether each is essential, and whether any fire before consent. 4. Flag statements a regulator could treat as false or misleading, ranked by severity. 5. Output a mismatch table: App Behavior | What My Documents Say | Gap | Suggested Fix. 6. List anything needing professional review rather than a wording fix, and why. Do not tell me I am compliant. Tell me where my documents and my product disagree.

## What's Next

Module 6, When To Bring In Professionals, picks up where this audit leaves off. Some mismatches are wording fixes; others, like a DPA for a big enterprise deal or a policy covering health data, are signals to bring in a lawyer or compliance specialist. Module 6 teaches you to tell the difference and scope the engagement.

## Certification Pathway

Pass this module's exam at 80 percent (20 of 25 questions) to earn the Module 5 badge. Pass all 7 module exams to earn the Compliance Foundations Specialist badge.

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
