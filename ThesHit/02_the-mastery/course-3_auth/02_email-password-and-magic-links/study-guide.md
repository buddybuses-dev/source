# Module 2: Email, Password and Magic Links — Study Guide

## T4 The Mastery | Authentication Systems Build

This is the study guide. Everything for Email, Password and Magic Links is on this page — there's nothing to download.

## What This Module Covers

This module covers the workhorse of authentication: the credential itself. How passwords must be stored and what makes a policy actually strong, how magic links work mechanically and where their security ceiling sits, why email verification and normalization matter, and the defensive layer around all of it: rate limiting, generic errors, breach-list checks, and the monitoring that catches credential stuffing while it is happening.

## Why It Matters

Credentials are where most real-world account takeovers happen, and almost none of them involve clever hacking. Attackers take a password leaked from some other site and try it on yours. They guess at scale. They read your error messages to learn which emails have accounts. They find the plaintext password your AI helpfully wrote into a debug log. Every one of these attacks is boring, automated, and defeated by decisions you make before launch, not heroics you perform after. This is also where AI direction gets dangerous, because your AI will produce a signup form that works perfectly while storing passwords wrong, capping their length "for safety," or emailing codes that never expire. The form looks identical either way. The difference lives in the layer you cannot see from the browser, which means it lives in the directions you give and the audits you run. A builder who knows what hashing, throttling, and enumeration resistance look like can direct and verify all of it in an afternoon. One who does not finds out from a breach notification.

## Certification Goal

Passing the Module 2 exam proves you can direct an AI to build email and password auth that stores credentials as strong one-way hashes, enforces policies that actually resist attackers, ships magic links that expire and burn on use, and wraps the whole flow in rate limiting, generic errors, and monitoring that spots an attack in progress.

## What You Need to Know

**Hashing, not encryption.** Passwords are stored as strong one-way hashes with a modern algorithm, so nobody, including you, can read them. Encryption is reversible by design; a hash can be checked but never turned back into text. A salt adds uniqueness per user, so identical passwords hash differently and precomputed rainbow tables go useless. When an algorithm ages out, you migrate by rehashing each user's password at their next login, the moment the plaintext is briefly present.

**What makes a policy strong.** Real length and a check against known breached passwords beat symbol theater every time. Attackers try leaked passwords first, so blocking them removes the likeliest successful guesses. Never let your AI cap password length at some low number "for safety": long passphrases are exactly what you want, and low caps forbid them.

**Magic links, mechanically.** A magic link is a single-use, expiring login link sent to the user's email, proving control of that inbox. The two non-negotiable properties: short expiry and single-use consumption, so an old or intercepted link buys nothing. The honest ceiling: a magic-link-only account is exactly as secure as the user's inbox, and inboxes get compromised often. The email itself must look trustworthy: clear sender identity, a stated expiry, and no request for anything beyond the click.

**Verification, normalization, and enumeration.** Verify emails at signup, because unverified addresses mean typos, fakes, and someone else's inbox holding the account keys. Normalize emails, trimming spaces and lowering case, so one person typing variants of their address lands on one account. Never confirm which accounts exist: login errors stay generic, and a signup with an already-registered email behaves identically to outsiders while alerting the real owner through their inbox.

**Rate limiting and the lockout trade.** Repeated failed logins get progressive slowing or a temporary hold, raising the cost of guessing without killing access. The trade is real: hard lockout lets an attacker deliberately lock real users out. A spike of failures across hundreds of accounts in an hour is credential stuffing from a breach elsewhere, and monitoring with alerts should surface it live, not in next month's review.

**Email infrastructure discipline.** Verification and reset emails send from a background queue, so a slow email provider never hangs the user-facing request. Development testing runs through a sandbox or capture tool so no real user ever receives a test email. Credentials never appear in logs: find plaintext passwords in debug output and you direct the fix, purge stored logs, and treat every exposed password as burned.

## Your Toolkit

- **Modern hashing via proven libraries.** Direct your AI to use the framework's or provider's standard password hashing, never a homemade scheme. The algorithm choice and salting come built in and battle-tested.
- **Breached-password checking.** Services and datasets that let signup reject passwords already circulating in dumps. One integration removes the attacker's best guesses.
- **A transactional email service with sandbox mode.** Background-queued sending for verification, magic links, and resets, plus a capture mode so development tests never touch a real inbox.
- **Login monitoring with alerts.** Dashboards and alerts on failed login volume per account and across accounts, so credential stuffing announces itself to you before your users do.

## Exam Topics

The Module 2 exam will test you on:

1. Hashing versus encryption, salts, and migrating old hashes at next login
2. Password policy: length and breach checks over symbol rules, and why caps are wrong
3. Magic link mechanics: single use, short expiry, and the inbox security ceiling
4. Email verification, normalization, and enumeration-resistant flows
5. Rate limiting: progressive slowing versus lockout, and the denial-of-service trade
6. Generic error messages and duplicate-signup handling that reveal nothing
7. Email infrastructure: background queues, sandbox testing, and log hygiene
8. Credential stuffing, SMS trade-offs, security questions, and session invalidation on password change

## Common Pitfalls

- **Symbol theater.** Requiring a capital, a number, and a symbol while allowing "P@ssw0rd1" is decoration. Length plus breach checks is the policy.
- **Helpful error messages.** "Wrong password" confirms the email exists. Every specific error feeds attackers a user list one guess at a time.
- **Magic links that live too long.** A link that works next week is a standing key in an unguarded inbox. Short expiry, single use, no exceptions.
- **Inline email sending.** Sending inside the web request means one slow provider hangs your signup. Queue it in the background.
- **Passwords in logs.** Debug logging that captures the login form captures credentials. Strip it now, purge old logs, treat exposed values as burned.
- **Surviving sessions after a password change.** When a user changes their password, other active sessions get invalidated. Otherwise the hijacker you were resetting away stays logged in.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I explain why hashing beats encryption for passwords, and what a salt adds?
- [ ] Can I define a password policy using length and breach checks, not symbol rules?
- [ ] Can I list the two properties every magic link must have?
- [ ] Can I explain enumeration and design signup, login, and errors so nothing leaks?
- [ ] Can I choose between throttling and lockout and defend the choice?
- [ ] Do I know how to migrate to a new hashing algorithm without a global reset?
- [ ] Could I spot credential stuffing in a monitoring dashboard and act on it?

## AI Audit Prompt Template

Use this prompt to audit your credential flows before launch:

> "You are a security reviewer examining the email, password, and magic link flows of my app: [paste flow descriptions]. Verify passwords are hashed with a modern salted algorithm and never logged, the policy favors length and breach checks over symbol rules with no low length cap, magic links are single-use with short expiry, emails are normalized and verified, all errors and duplicate signups resist enumeration, failed logins are throttled, and sends run in a background queue. List every gap in order of exploitability and tell me the exact direction to give my AI for each."

## What's Next

Module 3 hands the identity check to someone else: social login and enterprise SSO. You will learn what OAuth actually does, what your app receives and never receives, and how to borrow Google's or Microsoft's identity without betting your business on it.

## Certification Pathway

This module is the second step in the Authentication Systems Build course, a paid T4 The Mastery course inside Builder Access, alongside the SaaS Build and Database Design courses. Pass all seven module exams to earn the Auth Build Specialist badge, proof across The Faction that your credential handling holds under attack.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Email, Password and Magic Links Exam →
