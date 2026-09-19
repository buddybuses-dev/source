# Module 2: API Security Basics — Study Guide

## Backend Security for AI Directed Engineers

This is the study guide. Everything for API Security Basics is on this page — there's nothing to download.

## What This Module Covers

This module covers the security of your API endpoints — the backend routes that your frontend calls and that attackers will call directly. Your API is the real target. While Module 1 covered what attackers see from the frontend, this module covers what happens when they start making requests to your backend. Insecure API endpoints are the most exploited vulnerability in modern web applications. Missing authentication on routes, broken object-level authorization that lets users access other users' data, mass assignment that lets attackers modify fields they shouldn't, and rate limiting gaps that allow brute force attacks — these are the vulnerabilities that lead to data breaches. Your AI coding tool creates API routes quickly. It builds CRUD endpoints in minutes. But it often creates routes without authentication checks, returns more data than the client needs, accepts more fields than it should, and doesn't validate who is requesting what. Your job is to audit every route your AI creates and ensure it answers three questions: Who is making this request? Are they allowed to? Are they only getting what they should?

## Why It Matters

A single unprotected API endpoint can expose your entire database. If /api/users/123 returns user data and your API doesn't verify that the requesting user IS user 123, an attacker can iterate through every user ID and download your entire user table. This is called Broken Object-Level Authorization and it's the number one API vulnerability in the OWASP API Security Top 10. AI tools build APIs that work. They return the right data to the right frontend components. But working correctly for the intended user is not the same as being secure against an unintended user. Security means your API works correctly even when someone is actively trying to make it work incorrectly.

## Module Certification Goal

You can audit API endpoints built by your AI tool for authentication gaps, authorization failures, mass assignment vulnerabilities, and excessive data exposure — direct your AI to implement proper controls on every route — and verify that the API rejects unauthorized requests correctly.

## What You Need to Know

- **Authentication vs. authorization:** Authentication verifies who you are (login). Authorization verifies what you can access (permissions). An API that checks authentication but not authorization knows you're logged in but doesn't verify you're allowed to access the specific resource you're requesting. Both checks are required on every protected endpoint.
- **Broken Object-Level Authorization (BOLA):** BOLA occurs when your API lets a user access objects that belong to other users. If GET /api/invoices/456 returns invoice 456 without checking whether the requesting user owns that invoice, any authenticated user can access any invoice by changing the ID. Your AI builds the endpoint to return data — you must add the ownership check.
- **Mass assignment:** Mass assignment occurs when your API accepts more fields than intended. If your user update endpoint accepts any field sent in the request body, an attacker can send {role: 'admin'} and elevate their privileges. Your API should explicitly whitelist which fields each endpoint accepts.
- **Excessive data exposure:** AI-built APIs often return entire database records when the frontend only needs a few fields. An endpoint returning the full user object including password hash, internal notes, and billing details exposes data the client never displays. Return only the fields the frontend actually uses.
- **Rate limiting and brute force protection:** Without rate limiting, an attacker can send thousands of requests per second to your login endpoint trying password combinations, to your API trying different object IDs, or to your signup form creating spam accounts. Rate limiting restricts how many requests a single client can make in a time window.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to add authentication checks, authorization validation, and field whitelisting to every API endpoint.
- **API testing tool:** Postman or Insomnia to manually test your endpoints with different authentication states — no token, expired token, other user's token — to verify they reject properly.
- **OWASP API Security Top 10:** The reference checklist for API vulnerabilities. Review each item against your own API endpoints to identify gaps.
- **Request logging and monitoring:** Log every API request with user ID, endpoint, and response code. Unusual patterns (sequential ID enumeration, high request rates) indicate active attacks.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **Authentication enforcement:** Can you identify API endpoints that are missing authentication checks and should require a valid session or token?
- **Object-level authorization:** Can you detect when an API returns data that doesn't belong to the requesting user because ownership isn't verified?
- **Mass assignment prevention:** Can you evaluate whether an API endpoint restricts which fields can be modified by the client request?
- **Data exposure reduction:** Can you assess whether API responses include more data than the frontend needs and identify fields that should be excluded?
- **Rate limiting:** Can you evaluate whether critical endpoints like login and signup have rate limiting to prevent brute force attacks?
- **Input validation:** Can you identify when API endpoints accept and process input without validating data types, lengths, and formats?
- **Error handling security:** Can you assess whether API error messages reveal internal system details that help attackers understand your architecture?
- **HTTP method restriction:** Can you verify that API endpoints only respond to the HTTP methods they're designed for and reject unexpected methods?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Adding authentication to the frontend but not the API. If your React app checks login state before showing a page but the API endpoint returns data without checking the token, the frontend check is meaningless. Attackers call APIs directly.
- Using sequential integer IDs for resources without authorization checks. If your invoices are numbered 1, 2, 3... an attacker just increments the ID to access every invoice in your system. Always verify ownership before returning data.
- Accepting all fields from the request body because your AI built a generic update handler. If your endpoint runs UPDATE users SET ... with whatever the client sends, an attacker can modify any field including role and permissions.
- Returning full database records from every endpoint. Your user profile endpoint doesn't need to return the password hash, API keys, or internal admin notes. Select only the fields the client actually displays.
- Not rate limiting your login endpoint. Without rate limiting, an attacker can try millions of password combinations. Even basic rate limiting (10 attempts per minute) makes brute force attacks impractical.
- Exposing detailed error messages in production. An error like 'Column users.ssn does not exist' tells an attacker your table name and that you store SSNs. Production errors should be generic to the user and detailed only in server logs.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Does every API endpoint that returns user-specific data verify that the requesting user owns that data?
- Are all protected endpoints checking for a valid authentication token before processing the request?
- Does your API explicitly whitelist which fields each endpoint accepts for creation and updates?
- Do your API responses return only the fields the frontend needs, not full database records?
- Is rate limiting active on login, signup, and password reset endpoints?
- Have you tested your API with no token, an expired token, and another user's token to verify it rejects all three?
- Do production error responses hide internal details like table names, column names, and stack traces?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my API endpoints and check the following. For each one, tell me pass or fail with a specific example: Authentication: Do all protected endpoints verify a valid token? Authorization: Do endpoints that return user-specific data verify ownership? Mass assignment: Do update endpoints whitelist accepted fields? Data exposure: Do responses include only necessary fields? Rate limiting: Are login and signup endpoints rate limited? Error handling: Do production errors hide internal system details? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 2 exam. The best way to prepare: open Postman and call your own API endpoints. Try accessing another user's data by changing the ID. Send extra fields in an update request. Call endpoints without a token. Every gap you find is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the API Security Basics Exam →
