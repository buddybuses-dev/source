# Module 6: HTTPS, Headers & Transport Security — Study Guide

> ABG interim rewrite 2026-09-10 — curriculum card from module focus list. Original PDF/infographic still login-gated; replace/augment when T-009 browser scrape lands (browser-use stub ready).

## Transport Security for AI Directed Engineers

This is the study guide. Everything for HTTPS, Headers & Transport Security is on this page — there's nothing to download.

## What This Module Covers

This module covers how your application protects data in transit — the path between the user's browser (or another client) and your servers, and between your services themselves. Focus areas: SSL/TLS configuration, security headers, CSP and HSTS basics, X-Frame-Options and framing control, mixed content protection, certificate management, and secure app-to-internet transport. The guiding idea from the module focus list: **Secure the connection. Protect data in transit.**

AI-built apps often "work" over plain HTTP in local preview, ship with default headers, or embed `http://` asset URLs that break the HTTPS story the moment you deploy. Transport security is the layer that stops eavesdropping, downgrade attacks, clickjacking, and injected scripts on the wire — even when your auth and secrets management are otherwise solid.

## Why It Matters

Without TLS, credentials, tokens, and PII travel as readable bytes on shared networks. Without HSTS and careful cookie/header policy, a single HTTP visit can strip the "S" and open a downgrade path. Without CSP and framing controls, an attacker can inject scripts or nest your UI in a malicious frame. Certificate mistakes (expired, wrong hostname, self-signed in production, weak ciphers) turn "we have HTTPS" into a false sense of safety. Exam scenarios and real incidents both start from these gaps.

## Module Certification Goal

You can inspect an AI-built application's transport posture — TLS setup, response headers, mixed content, certificates, and framing/CSP policy — direct your AI to harden the connection, and verify that sensitive data cannot travel in the clear or under a weaker policy than you intended.

## What You Need to Know

- **SSL/TLS configuration:** TLS encrypts the connection. Prefer modern TLS (1.2+; ideally 1.3), disable obsolete protocols (SSL, TLS 1.0/1.1), and avoid weak ciphers. Termination often sits on a reverse proxy, CDN, or platform load balancer — know where TLS ends and whether traffic is still encrypted hop-to-hop behind it.
- **HTTPS everywhere:** Redirect HTTP → HTTPS. Serve cookies with `Secure` (and usually `HttpOnly` + appropriate `SameSite`). Do not assume "local HTTP is fine forever" — staging and production must match the HTTPS model you will certify against.
- **Security headers:** Response headers tell browsers how to treat your origin. Core set for this module: `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options` / `frame-ancestors`, plus related helpers such as `X-Content-Type-Options: nosniff` and referrer policy. Headers only help if they are present on the responses that matter (HTML documents especially).
- **CSP (Content-Security-Policy):** CSP limits which scripts, styles, images, and frames the browser will load. Start with a restrictive default (`default-src 'self'`), avoid `'unsafe-inline'` / `'unsafe-eval'` when you can, and use nonces or hashes for required inline scripts. Report-Only mode is useful while tightening. CSP is one of the strongest defenses against XSS payload execution after injection.
- **HSTS (Strict-Transport-Security):** Tells browsers to use HTTPS only for your host (and optionally subdomains) for a max-age window. Typical production pattern: long `max-age`, `includeSubDomains` when every subdomain is ready, and `preload` only when you meet preload list requirements. HSTS is sticky — misconfiguring it on a host that cannot serve HTTPS everywhere will lock users out.
- **X-Frame-Options / framing control:** Stop clickjacking by controlling who can embed your pages. Legacy header: `X-Frame-Options: DENY` or `SAMEORIGIN`. Modern CSP: `frame-ancestors 'none'` or an explicit allowlist. Prefer CSP `frame-ancestors` where supported; keep X-Frame-Options for older clients if needed.
- **Mixed content:** An HTTPS page that loads scripts, styles, or active content over HTTP is mixed content — browsers block or warn, and attackers can modify those HTTP resources. Fix by using HTTPS URLs (or protocol-relative carefully), upgrading asset hosts, and enabling upgrades where platforms offer them. Passive mixed content (images) is still a smell; active mixed content (scripts) is a hard fail.
- **Certificate management:** Certificates prove hostname identity and enable TLS. Track issuance, renewal, chain completeness, and hostname SANs. Automate renewal (e.g. ACME/Let's Encrypt or platform-managed certs). Watch for expiration, incomplete chains, hostname mismatch, and accidental trust of self-signed certs in production clients.
- **Data in transit (app → internet and service → service):** Encrypt every hop that carries secrets or personal data. Do not terminate TLS at the edge and then forward tokens in cleartext across untrusted networks without a deliberate, documented trust boundary. Prefer mTLS or private networking for sensitive internal APIs when the threat model requires it.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to enforce HTTPS redirects, set security headers, and purge `http://` asset URLs.
- **Browser DevTools:** Network + Security panels — confirm TLS, certificate details, and response headers on document responses.
- **Header scanners:** securityheaders.com, Mozilla Observatory, or `curl -I` against your deployed origin.
- **TLS checkers:** SSL Labs / platform TLS reports — protocol versions, cipher suites, chain issues.
- **CSP helpers:** browser console CSP reports; Report-Only policies while iterating.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **TLS posture:** Can you tell when an app still allows weak protocols, missing redirects, or cleartext hops behind the load balancer?
- **Security header gaps:** Can you spot missing or ineffective HSTS, CSP, framing, or nosniff headers on HTML responses?
- **CSP strength:** Can you recognize `'unsafe-inline'` / overly broad `*` sources as weak policy, and suggest a tighter default?
- **HSTS readiness:** Can you assess whether `includeSubDomains` / preload is safe for this host inventory?
- **Framing / clickjacking:** Can you choose `DENY` / `SAMEORIGIN` / `frame-ancestors` appropriately for an embed vs non-embed UI?
- **Mixed content:** Can you find HTTP script/style URLs on an HTTPS page and prescribe HTTPS upgrades?
- **Certificates:** Can you diagnose expired, mismatched, or incomplete-chain certificates and the operational fix (renew / correct SAN / fix chain)?
- **Transit boundaries:** Can you evaluate whether tokens or PII leave the trust boundary unencrypted?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Shipping "HTTPS" only on the marketing domain while the API or admin subdomain stays HTTP or has a broken cert.
- Setting security headers on the API JSON responses only, and forgetting the HTML document responses users actually load.
- Copy-pasting a CSP with `'unsafe-inline' 'unsafe-eval'` and `*` so the header exists but does almost nothing.
- Enabling HSTS preload before every subdomain serves valid HTTPS — users get hard failures that are painful to undo.
- Leaving `http://` CDN or font URLs in AI-generated HTML/CSS — classic mixed content after you flip the site to HTTPS.
- Ignoring certificate renewal until production expires on a Friday night.
- Assuming TLS at the CDN means the path from CDN to origin is automatically safe without checking.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Does every public hostname redirect HTTP → HTTPS and present a valid certificate chain?
- Are TLS 1.2+ (preferably 1.3) enforced and obsolete protocols disabled at the terminator you control?
- Do HTML responses include HSTS, a meaningful CSP, framing control (`X-Frame-Options` and/or `frame-ancestors`), and `X-Content-Type-Options: nosniff`?
- Is CSP free of unnecessary `'unsafe-inline'` / `'unsafe-eval'` and wildcard script sources?
- Have you loaded the app over HTTPS and confirmed zero active mixed content in DevTools?
- Is certificate renewal automated, with monitoring for expiry and hostname mismatch?
- Are cookies that carry session or auth material marked `Secure` (and appropriately `HttpOnly` / `SameSite`)?
- For service-to-service calls carrying secrets, is the path encrypted or otherwise inside a defined trust boundary?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my app's HTTPS and transport security. For each item, say pass or fail with a concrete example: HTTP→HTTPS redirects; TLS version/cipher posture at the edge; HSTS present and appropriate; CSP present and not trivially bypassable; framing controls (X-Frame-Options or CSP frame-ancestors); mixed content (any http:// assets on https pages); certificate validity and renewal plan; Secure cookie flags on auth cookies; cleartext hops for secrets behind the TLS terminator. Give me an overall score out of 9 and the top 3 fixes first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 6 exam. The best way to prepare: open your deployed (or staging) origin in DevTools, read the Security and Network panels, hit your URLs with `curl -I`, and fix every mixed-content and missing-header finding. Every weak redirect, missing HSTS, or `http://` script URL you catch is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

---

Ready? Take the HTTPS, Headers & Transport Security Exam →

<!-- speech/mp3 stale vs new guide — study-guide.mp3 / study-guide.speech.txt not regenerated this round -->
