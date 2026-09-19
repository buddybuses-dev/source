# Module 4: Auth Done Right — Study Guide

## Authentication Security for AI Directed Engineers

This is the study guide. Everything for Auth Done Right is on this page — there's nothing to download.

## What This Module Covers

This module covers authentication security — how your application verifies user identity and how attackers try to bypass, steal, or brute-force their way through your login system. Authentication is the front door of your application. If it's weak, nothing behind it matters. You already understand auth from a functional perspective through the CADE program. This module covers the security perspective: how password hashing works and how it fails, why token storage location matters, how session fixation attacks steal sessions, how brute force attacks work against login endpoints, and how password reset flows are exploited. AI tools implement auth quickly. They add login forms, issue JWTs, and store sessions. But the defaults are often insecure — passwords hashed with weak algorithms, tokens stored in localStorage where XSS can steal them, reset flows that leak information about which email addresses exist, and no protection against automated login attempts.

## Why It Matters

Credential theft is the starting point for most data breaches. An attacker who gains a valid user session can do everything that user can do — access data, modify records, escalate privileges if the account has admin access. Auth isn't just a feature — it's the boundary between your application being used and your application being exploited. The OWASP Top 10 consistently lists authentication failures as one of the most critical web application security risks. Getting auth right is the highest-leverage security investment you can make.

## Module Certification Goal

You can evaluate the security of authentication implementations in AI-built applications — password hashing, token handling, session management, brute force protection, and password reset flows — direct your AI to implement secure patterns, and verify that the authentication system resists common attack techniques.

## What You Need to Know

- **Password hashing:** Passwords must never be stored in plain text or with reversible encryption. They should be hashed with a modern algorithm like bcrypt, scrypt, or Argon2 that includes salting and is deliberately slow to compute. AI tools sometimes use fast hashes like MD5 or SHA-256 which can be brute-forced at billions of attempts per second.
- **Token storage and security:** JWTs and session tokens must be stored securely. localStorage is accessible to any JavaScript on the page — if your app has an XSS vulnerability, tokens in localStorage are stolen. httpOnly cookies with Secure and SameSite flags are the safer storage mechanism because JavaScript cannot access them.
- **Session fixation and hijacking:** Session fixation occurs when an attacker sets a known session ID before the user logs in, then uses that same session ID to access the authenticated session. Session hijacking occurs when an attacker steals an active session token through XSS, network sniffing, or physical access. Regenerating session IDs on login prevents fixation.
- **Brute force protection:** Without rate limiting on your login endpoint, an attacker can try millions of password combinations. Account lockout after repeated failures, CAPTCHA challenges, and progressive delays between attempts make brute force impractical.
- **Password reset security:** Password reset flows are frequently exploited. Reset tokens that don't expire, reset emails that confirm whether an address exists in the system, and reset links that work more than once all create vulnerabilities. Reset tokens should be single-use, time-limited, and the response should not reveal whether the email exists.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to implement bcrypt hashing, httpOnly cookie storage, and rate limiting on auth endpoints.
- **Password hash verification:** Check your database to verify passwords are stored as bcrypt or Argon2 hashes, not plain text, MD5, or unsalted SHA hashes.
- **Auth testing checklist:** The OWASP Authentication Testing Guide provides a systematic checklist for evaluating every aspect of your auth implementation.
- **Rate limiting tester:** A script that sends 100 login attempts in rapid succession to verify your rate limiting activates and blocks further attempts.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **Password hashing algorithm:** Can you evaluate whether passwords are hashed with a secure modern algorithm like bcrypt or Argon2 rather than fast hashes like MD5 or SHA-256?
- **Token storage security:** Can you assess whether session tokens are stored in httpOnly cookies rather than localStorage where XSS can steal them?
- **Session management:** Can you identify whether session IDs are regenerated on login to prevent session fixation attacks?
- **Brute force protection:** Can you evaluate whether login endpoints have rate limiting, account lockout, or CAPTCHA to prevent automated password guessing?
- **Password reset flow:** Can you assess whether reset tokens are single-use, time-limited, and the flow doesn't reveal which email addresses exist?
- **Credential transmission:** Can you verify that login credentials are transmitted over HTTPS and never included in URL query parameters or server logs?
- **Multi-factor authentication:** Can you evaluate whether MFA is available and correctly implemented as a second authentication factor beyond just passwords?
- **Logout and session termination:** Can you verify that logging out actually invalidates the session server-side rather than just clearing the client-side token?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Hashing passwords with MD5 or SHA-256 because the AI used them by default. These are fast hashes designed for data integrity, not password storage. An attacker with a GPU can try billions of SHA-256 hashes per second. Use bcrypt or Argon2.
- Storing JWT tokens in localStorage. Any XSS vulnerability on your site lets an attacker's script read localStorage and steal every user's token. Use httpOnly cookies that JavaScript cannot access.
- Not regenerating session IDs after login. If the session ID stays the same before and after authentication, an attacker who knows the pre-login session ID can use it to access the post-login session.
- Building a login endpoint with no rate limiting. Without limits, an attacker can try every common password against every user account. Even 10 attempts per minute per account makes brute force impractical.
- Password reset flows that say 'no account found' for unknown emails. This confirms which email addresses have accounts, giving attackers a target list. Always say 'if an account exists, a reset email has been sent' regardless.
- Implementing logout by only deleting the client-side token. If the server still considers the session valid, a stolen token works even after the user logs out. Logout must invalidate the session on the server.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Are all passwords in your database hashed with bcrypt, scrypt, or Argon2?
- Are session tokens stored in httpOnly cookies with Secure and SameSite flags?
- Does your login endpoint regenerate the session ID after successful authentication?
- Is rate limiting active on your login, signup, and password reset endpoints?
- Does your password reset flow use single-use, time-limited tokens?
- Does your reset flow respond identically whether the email exists or not?
- Does logout invalidate the session on the server, not just clear the client token?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my authentication system and check the following. For each one, tell me pass or fail with a specific example: Password hashing: Are passwords stored with bcrypt or Argon2, not MD5 or SHA? Token storage: Are tokens in httpOnly cookies, not localStorage? Session management: Are session IDs regenerated on login? Brute force: Are login endpoints rate limited? Password reset: Are reset tokens single-use and time-limited? Logout: Does logout invalidate the session server-side? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 4 exam. The best way to prepare: check your database for how passwords are stored. Inspect your cookies in DevTools. Try logging in 50 times rapidly with wrong passwords. Request a password reset for a nonexistent email. Every weakness you find is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the Auth Done Right Exam →
