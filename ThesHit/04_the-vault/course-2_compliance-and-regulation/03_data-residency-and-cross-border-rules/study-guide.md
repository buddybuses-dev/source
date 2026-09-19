# Module 3: Data Residency and Cross-Border Rules — Study Guide

## Compliance Foundations for Builders

T6 The Vault | Module 3 Study Guide

Direct AI to map which regulations apply to any build before shipping it.

## What This Module Covers

Every piece of data your app collects lives somewhere physical. A row in your Supabase table sits on a server in a specific country, under that country's laws. Module 3 teaches you to answer a question most builders never ask: where does my data actually live, and what does that location legally obligate me to do?

You will learn the major data residency regimes by region: the EU, Canada, Australia, India, Brazil, and the Middle East. You will learn the three mechanisms that make cross-border transfers legal: adequacy decisions, Standard Contractual Clauses, and binding corporate rules. Then you will connect all of it to decisions you actually make. Picking an AWS region, spinning up a Supabase project, or deploying Vercel edge functions are not just technical choices. Each one creates or removes compliance obligations, and this module shows you how to direct AI to audit those choices before you ship.

## Why It Matters

In Module 2 you met the SaaS founder who launched in the EU without GDPR compliance. Here is the sequel: even a founder who knows GDPR exists can get burned by residency. She hosts everything in us-east-1 because that was the default, signs an EU customer, and now personal data flows from Europe to the United States with no transfer mechanism in place. The customer's legal team asks one question, "where is our data processed?", and the deal stalls. Data location questions kill B2B deals every week, and builders who can answer them cleanly win the contracts.

The stakes run the other direction too. If you build for clients, they inherit your hosting decisions without knowing it. You deploy their app on a global edge network, user data replicates across regions, and now they have obligations in countries they have never heard of. You do not need to become a lawyer to prevent this. You need to know the problem exists, where the tripwires are, and when to route the question to a professional. That is the boundary knowledge this module builds.

## Certification Goal

Passing the Module 3 exam proves you can identify where an application's data physically resides, name the residency expectations of major regions, recognize the legal mechanisms that permit cross-border transfers, and explain how hosting choices create compliance obligations. It proves you can build the residency portion of a compliance map, not that any build is compliant. That judgment belongs to professionals, and knowing when to bring them in is part of what you are certified on.

## What You Need to Know

### Data Residency vs. Data Sovereignty

Residency is where data is stored and processed. Sovereignty is whose laws govern it, which can follow the data after it leaves a country. A French user's data hosted in Virginia is physically resident in the US but still subject to EU rules because of who the user is.

### The Regional Landscape

The EU restricts transfers of personal data outside the European Economic Area unless a legal mechanism covers them. Canada's PIPEDA allows transfers with accountability, but some provinces and public-sector contracts expect Canadian hosting. Australia restricts offshore disclosure, with strict rules for health records. India's DPDP Act permits transfers except to blocklisted countries. Brazil's LGPD mirrors the GDPR transfer model. Middle East regimes vary sharply by country and sector, so check each market individually.

### Transfer Mechanisms

Three names to recognize on sight. Adequacy decisions: one government declares another country's protections good enough, so data flows freely, like the EU-US Data Privacy Framework. Standard Contractual Clauses (SCCs): pre-approved contract terms between sender and receiver, the workhorse most SaaS vendors rely on. Binding corporate rules: regulator-approved internal policies for transfers inside one multinational. A transfer leaving a regulated region with none of these is a flag for professional review.

### Your Hosting Choices Are Legal Choices

The AWS region dropdown, the Supabase project location picker, the Vercel deployment settings: each is a legal decision wearing a technical costume. Choosing eu-central-1 versus us-east-1 changes which transfer questions you must answer. Defaults are not neutral.

### Third Parties Move Your Data Too

Analytics, error tracking, email delivery, AI APIs, payment processors: every third-party service that touches user data processes it somewhere, usually the US. Your app can be perfectly hosted in Frankfurt while your logging tool ships personal data to California on every request. The full residency picture includes every service in the chain.

### Edge and Replication Complications

Edge functions, CDNs, and multi-region replicas execute and copy data in many countries at once. Caching personal data at 30 edge locations can mean 30 jurisdictions. Serve static assets from the edge freely, but know exactly which personal data, if any, follows them there.

## Your Toolkit

- **The Data Location Inventory.** A table listing every place your app stores or processes data: primary database, backups, file storage, logs, and each third party, with region and country. This is the core artifact of this module and a section of your Module 7 compliance map.
- **Provider Region Documentation.** AWS, Supabase, Vercel, and every serious vendor publish region lists and data processing terms. Bookmark them, and check where backups and support access happen, not just primary storage.
- **Sub-processor Lists.** Reputable vendors publish who they share data with and where. A vendor's sub-processor page tells you where your users' data really travels after it leaves your code.
- **The AI Residency Audit.** The prompt template in this guide, run against your actual stack, produces a draft data flow map in minutes. Verify it against provider docs, because the map is only as good as its accuracy.

## Exam Topics

- The difference between data residency and data sovereignty, with an example of each
- The general shape of each regional regime: EU, Canada, Australia, India, Brazil, Middle East
- The three transfer mechanisms and when each typically applies
- How choosing an AWS region or Supabase project location creates or avoids transfer obligations
- Why third-party services like analytics, email, and AI APIs are part of your residency picture
- How edge functions, CDNs, and replication complicate where data lives
- What belongs in a data location inventory and why backups and logs are included
- Which residency findings signal it is time to involve a professional

## Common Pitfalls

- **Accepting the default region.** us-east-1 is a decision, not a neutral starting point. Builders who never touch the region picker discover their obligations only when a customer asks.
- **Auditing the database and nothing else.** Your Postgres instance in Frankfurt means little if your error tracker, analytics, and email provider process the same personal data in the US with no transfer mechanism.
- **Assuming EU rules stop at storage.** Processing, support access, and backups count. An EU-hosted database administered from a US laptop still raises transfer questions.
- **Treating the Middle East as one jurisdiction.** Localization rules differ by country and sector. What is fine for the UAE may not be fine for Saudi Arabia.
- **Confusing a transfer mechanism with compliance.** Seeing "SCCs" in a vendor's terms means a mechanism exists, not that your specific use is covered. That distinction is where professionals earn their fee.
- **Deploying globally because the platform makes it easy.** Edge-first platforms default to worldwide distribution, which can create obligations in markets where you have zero users.

## Self-Assessment Checklist

- I can explain data residency versus data sovereignty in plain language.
- I can describe each covered region's general stance on cross-border transfers.
- I can define adequacy decisions, SCCs, and binding corporate rules and say when each shows up.
- I can explain how a hosting region choice creates or avoids compliance obligations.
- I can build a data location inventory covering my database, backups, logs, and third-party services.
- I can identify when edge functions or replication put personal data in additional jurisdictions.
- I can recognize residency findings that require a professional before I ship.

## AI Audit Prompt Template

Give your AI this prompt, filled in with your real stack, to draft the residency section of your compliance map.

> You are auditing the data residency of my application. Do not give legal advice. Your job is to map where data physically lives and flag cross-border flows for professional review. MY STACK: - App type and what it does: [describe] - Primary database and region: [e.g., Supabase project in us-east-1] - Hosting/deployment: [e.g., Vercel with edge functions, default regions] - File storage and region: [e.g., S3 us-east-1] - Third-party services touching user data: [analytics, email, error tracking, AI APIs, payments, auth, etc.] - Where my users are located: [countries/regions] - Types of personal data collected: [emails, names, payment info, health info, etc.] PRODUCE: 1. A data location inventory: every place data is stored or processed, with region and country, including backups and logs where known. 2. A cross-border flow list: every flow where data moves from a user's region to another country, especially out of the EU, Canada, Australia, India, Brazil, or Middle East markets I serve. 3. For each flow, note whether a transfer mechanism likely applies (adequacy decision, SCCs, binding corporate rules) based on the vendor's public terms, and mark anything uncertain as UNVERIFIED. 4. A list of architecture changes that would simplify my residency picture, such as region changes or EU-hosted alternatives. 5. A "professional review" list: every finding a qualified privacy professional should confirm before I ship or sign a customer. Ask me clarifying questions before answering if anything is ambiguous.

## What's Next

You now know where data lives and how it crosses borders. Module 4, Industry-Specific Trigger Points, adds the other axis of the map: what kind of data you handle and for whom. Residency told you where the dentist's scheduling data sits. Module 4 tells you why the word "dentist" changed everything the moment it entered the spec.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 3 badge. Pass all 7 module exams to earn the Compliance Foundations Specialist badge.

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
