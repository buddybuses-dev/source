# Module 1: Your App's Attack Surface — Study Guide

## Frontend Security for AI Directed Engineers

This is the study guide. Everything for Your App's Attack Surface is on this page — there's nothing to download.

## What This Module Covers

This module covers the attack surface of your AI-built application — every point where an attacker can interact with your product and try to break in. Your frontend is the most exposed part of your stack. It runs in the user's browser where anyone can inspect it, modify it, and probe it for weaknesses. Client-side secrets, unvalidated inputs, clickjackable iframes, cross-site scripting injection points, and exposed API endpoints are all visible to anyone who opens their browser's developer tools. Your AI coding tool builds fast. It ships features in hours. But speed creates blind spots. AI tools don't audit their own output for security vulnerabilities unless you explicitly tell them to. A login form that looks correct might accept script injection. A dashboard that works perfectly might expose admin API routes in the client-side JavaScript bundle. An image upload feature might accept executable files. Every feature your AI builds is a potential entry point for an attacker — and your job as the AI Directed Engineer is to know where to look.

## Why It Matters

Attackers don't start with your database. They start with what they can see: your frontend. They view your page source. They inspect your API calls in the network tab. They read your JavaScript bundle for hardcoded keys and hidden endpoints. They test your forms with malicious input. They try to iframe your pages. Every piece of information your frontend exposes — intentionally or accidentally — gives an attacker a map of how to get deeper into your system. The builders in this community ship AI-built applications to real users. Those users trust that the application protects their data. Understanding your attack surface is the first step in honoring that trust. You can't secure what you can't see, and this module teaches you to see what attackers see.

## Module Certification Goal

You can identify the attack surface of an AI-built web application — exposed endpoints, client-side secrets, injection points, and clickjacking risks — direct your AI tool to remediate each vulnerability, and verify that the fixes actually close the gaps without breaking functionality.

## What You Need to Know

- **What is an attack surface:** Your attack surface is every point where an unauthorized user can attempt to interact with your system. Forms, API endpoints, file upload handlers, URL parameters, cookies, and client-side storage are all part of it. The larger your attack surface, the more opportunities an attacker has. Reducing it means removing unnecessary exposure — endpoints that don't need to be public, features that don't need to accept user input, and data that doesn't need to be in the browser.
- **Client-side secrets exposure:** AI tools frequently hardcode API keys, database connection strings, and service credentials in frontend code. These are visible to anyone who views the page source or inspects the JavaScript bundle. Your AI built the feature — you need to audit where it stored the credentials. Secrets belong in server-side environment variables, never in client-side code.
- **Cross-Site Scripting (XSS):** XSS occurs when your application renders user-supplied content without sanitizing it. If a user can submit a comment containing a script tag and that script executes when other users view the page, the attacker can steal session tokens, redirect users, or modify what they see. AI-generated code often renders dynamic content without proper escaping — this is one of the most common vulnerabilities in AI-built applications.
- **Clickjacking and iframe protection:** Clickjacking tricks users into clicking something different from what they see by overlaying your application inside a transparent iframe on the attacker's page. The user thinks they're clicking a button on a legitimate site but they're actually interacting with your application. The X-Frame-Options header and Content Security Policy frame-ancestors directive prevent this.
- **Exposed API routes in client bundles:** When your AI builds a frontend, it often includes references to every API endpoint in the client-side JavaScript — including admin routes that should never be visible to regular users. An attacker reads your bundle and discovers endpoints like /api/admin/users or /api/internal/export that the UI doesn't show but the browser can still call.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to audit your frontend for exposed secrets, XSS vulnerabilities, and unnecessary API exposure.
- **Browser developer tools:** Chrome DevTools Network tab to see every API call your frontend makes, Sources tab to inspect your JavaScript bundle, and Application tab to check what's in cookies and local storage.
- **Security scanner:** OWASP ZAP or Burp Suite Community Edition to automatically probe your application for common vulnerabilities. Run these against your staging environment.
- **Content Security Policy evaluator:** CSP Evaluator (csp-evaluator.withgoogle.com) to check whether your Content Security Policy headers actually protect against XSS and clickjacking.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **Attack surface identification:** Can you identify every point where an attacker can interact with your application and evaluate which ones need to be locked down?
- **Client-side secret detection:** Can you find API keys and credentials exposed in frontend code and know where they should be stored instead?
- **XSS vulnerability recognition:** Can you identify when user input is rendered without sanitization and know what remediation to direct your AI to implement?
- **Clickjacking prevention:** Can you evaluate whether your application is protected against iframe-based clickjacking attacks through proper headers?
- **API route exposure:** Can you audit your client-side bundle for references to internal API endpoints that should not be discoverable by regular users?
- **Input validation:** Can you assess whether all user-facing forms properly validate and sanitize input before processing it on the server?
- **Security header configuration:** Can you evaluate whether your application serves the correct security headers to prevent common browser-based attacks?
- **Attack surface reduction:** Can you identify unnecessary features, endpoints, or data exposure that increase your attack surface without adding user value?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Assuming your AI tool wrote secure code by default. AI tools optimize for functionality not security. Every feature needs a security review before it ships to users.
- Storing API keys in frontend JavaScript because the AI put them there. Client-side secrets are visible to every user. Move them to server-side environment variables.
- Rendering user-submitted content without sanitization. If a user can submit HTML or JavaScript and it renders on the page, you have an XSS vulnerability.
- Not setting security headers because the application works without them. Security headers prevent entire categories of attacks. Working without them just means you haven't been attacked yet.
- Leaving debug endpoints active in production. Your AI may have created /api/debug or /api/test routes during development. If they're still accessible in production, they're part of your attack surface.
- Not inspecting your own JavaScript bundle. If you don't look at what your build process produces, you don't know what secrets and routes you're shipping to every browser that loads your application.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Have you opened your browser's DevTools and inspected every API call your frontend makes to understand your full attack surface?
- Have you searched your client-side JavaScript bundle for API keys, tokens, or credentials that should be server-side only?
- Does your application sanitize all user input before rendering it on any page?
- Are X-Frame-Options and Content Security Policy headers set to prevent clickjacking?
- Have you removed or locked down all debug and test endpoints in production?
- Can you list every form, API endpoint, and file upload handler that accepts external input in your application?
- Have you run a security scanner against your staging environment in the last 30 days?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my application's frontend attack surface and check the following. For each one, tell me pass or fail with a specific example: Client-side secrets: Are any API keys, tokens, or credentials visible in the frontend JavaScript bundle or page source? XSS protection: Is all user-submitted content sanitized before rendering? Clickjacking: Are X-Frame-Options and CSP frame-ancestors headers configured? API exposure: Are internal or admin API routes discoverable in the client bundle? Input validation: Do all forms validate and sanitize input server-side? Security headers: Are CSP, HSTS, X-Content-Type-Options, and Referrer-Policy set? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 1 exam. The best way to prepare: open your own application in Chrome DevTools. Inspect the Network tab. Read your JavaScript bundle. Search for hardcoded strings. Try submitting script tags in every form. Every vulnerability you find in your own app is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the Your App's Attack Surface Exam →
