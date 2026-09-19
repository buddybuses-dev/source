# Module 2: Auth Keys and Rate Limiting — Study Guide

## API Product Build

### T4 The Mastery | Module 2 Study Guide

## Module 2: Auth Keys and Rate Limiting

> Direct AI to build the auth and throttling layer before anyone gets a key.

## What This Module Covers

This module covers the access layer of your API product: API key generation, rotation, and revocation; the difference between API keys and OAuth tokens and when to use each; per-key rate limiting; usage tiers; IP allowlisting; key scoping; abuse detection; and making rate limits transparent to the developers who hit them.

## Why It Matters

Keys and rate limits are where your API becomes a business. A key identifies a paying customer, ties usage to billing, and gives you the control to cut off abuse without taking down the whole service. Rate limits are simultaneously a cost-protection mechanism, a product-tiering lever, and a developer-experience surface. Done well, they let you sell free, pro, and enterprise tiers off the same codebase and keep a runaway integration from bankrupting you. Done badly, they leak revenue, expose you to abuse, and frustrate the developers you most want to keep. This module is where access control becomes a product feature rather than an afterthought.

## Certification Goal

Passing this exam proves you can direct AI to build secure key lifecycle management, choose between API keys and OAuth appropriately, implement per-key rate limiting and usage tiers, scope keys to permissions, and surface limits transparently to developers.

## What You Need to Know

**1. Key lifecycle: generation, rotation, revocation.** An API key is a credential with a full life. Generation: keys are created with sufficient entropy, shown once, and stored hashed, never in plaintext, so a database breach does not hand over live keys. Rotation: developers can issue a new key and retire the old one without downtime, which means supporting multiple active keys during a transition. Revocation: a compromised or retired key can be killed instantly. You direct AI to build all three, because a key you cannot rotate or revoke is a security incident waiting to happen.

**2. API keys vs OAuth tokens.** These solve different problems. API keys identify an application or account and are ideal for server-to-server access where one party owns both ends. OAuth tokens represent a specific user's delegated permission and are the right choice when your API acts on behalf of end users who must consent, such as accessing their data in a third-party app. Using an API key where you need OAuth means you cannot represent per-user consent; using OAuth where a simple key suffices adds friction developers resent. You choose based on whose authority the call carries.

**3. Per-key rate limiting.** Every key gets a limit, enforced per key rather than globally, so one customer's traffic cannot starve another's. The common model is a request budget over a window (requests per second, per minute, or per month). You direct AI to enforce limits at the edge, before expensive work runs, and to make the limit a property of the key's tier rather than a hardcoded constant. This is what lets rate limits double as your pricing lever.

**4. Usage tiers as product.** Free, pro, and enterprise tiers are the same API with different key configurations: different rate limits, different scopes, different feature access. The tier lives on the key, so upgrading a customer is a configuration change, not a code change. This is the mechanism that turns your API into a product with a pricing page. You design the tiers so the free tier is genuinely useful (adoption) while the paid tiers unlock the volume and features that serious users need (revenue).

**5. Key scoping and IP allowlisting.** Scoping limits what a key can do: read-only vs read-write, or access to specific resources only. A read-only key handed to an analytics integration cannot be used to mutate data if it leaks, which contains the blast radius of a compromise. IP allowlisting restricts where a key can be used from, so a stolen key is useless outside the customer's known infrastructure. Both follow the principle of least privilege: a key should carry only the access its actual job requires.

**6. Abuse detection and transparent limits.** Abuse detection watches for the patterns that signal a problem: sudden spikes, credential stuffing, scraping, usage that does not match the customer's tier. But transparency is the other half. Rate limits must be visible to well-behaved developers through response headers (remaining quota, reset time), clear documentation, and error messages that say exactly what limit was hit and when it resets. A developer who hits an opaque 429 with no guidance churns; a developer who gets a clear header and a documented backoff path adapts. You make limits a communicated contract, not a silent wall.

## Your Toolkit

- **Key lifecycle system**: entropy-strong generation, hashed storage, multi-key rotation, instant revocation
- **Auth model decision**: API keys for server-to-server, OAuth for delegated user consent
- **Tiered rate limiter**: per-key limits driven by the key's tier, enforced at the edge
- **Transparency layer**: rate-limit headers, documented limits, and actionable 429 error messages

## Exam Topics

1. Key generation, hashed storage, rotation, and revocation
2. API keys vs OAuth tokens and when each applies
3. Per-key rate limiting enforced at the edge
4. Usage tiers as key configuration, not code changes
5. Key scoping and least privilege
6. IP allowlisting and containing a leaked key
7. Abuse detection patterns
8. Making rate limits transparent through headers, docs, and errors

## Common Pitfalls

- Storing API keys in plaintext so a database breach exposes every live credential
- Building keys that cannot be rotated without downtime or revoked instantly
- Using an API key where per-user OAuth consent is actually required
- Enforcing rate limits globally so one customer's spike degrades everyone else
- Hardcoding limits instead of tying them to the key's tier
- Returning an opaque 429 with no header or message telling the developer what to do

## Self-Assessment Checklist

- Are my keys stored hashed and shown to the user only once?
- Can a developer rotate a key with no downtime and can I revoke one instantly?
- Can I explain when to use an API key versus OAuth for a given integration?
- Are my rate limits enforced per key and driven by the key's tier?
- Do my keys carry only the scope their job requires?
- Does a rate-limited developer receive a header and message telling them when to retry?

## AI Audit Prompt Template

> You are auditing an API's access and rate-limiting layer. Check: (1) key storage: are keys hashed at rest and shown only once, (2) lifecycle: can keys be rotated without downtime and revoked instantly, (3) auth model: is the choice between API keys and OAuth appropriate for who authorizes each call, (4) rate limiting: are limits enforced per key at the edge and tied to the key's tier rather than hardcoded, (5) scoping: do keys follow least privilege with read-only and resource scoping available, (6) transparency: do rate-limited responses include remaining-quota and reset headers and actionable error messages. Report each finding with its security or developer-experience consequence.

## What's Next

Module 3 covers the surface developers judge you by most: documentation and developer experience, where the docs are the product.

## Certification Pathway

This is Module 2 of 7 in the API Product Build course, part of T4 The Mastery. Passing all seven module exams earns the API Product Specialist badge. This module turns access into a sellable, tiered product.

———

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai
