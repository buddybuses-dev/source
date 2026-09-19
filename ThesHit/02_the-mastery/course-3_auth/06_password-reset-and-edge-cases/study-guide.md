# Module 6: Password Reset and Edge Cases — Study Guide

## T4 The Mastery | Authentication Systems Build

This is the study guide. Everything for Password Reset and Edge Cases is on this page — there's nothing to download.

## What This Module Covers

This module covers the flow that decides whether your auth system is actually secure: password reset and the edge cases around it. You will learn the anatomy of a safe reset, the properties every reset token must have, how to resist enumeration and reset floods, what email scanners do to single-use links, and how email changes, deletion, dormancy, and lost-email recovery are handled without opening a back door.

## Why It Matters

Recovery is the back door to every account, and attackers know it. They do not brute-force a strong password protected by 2FA; they request a reset, probe the flow for a weakness, and walk in through the door you built for forgetful users. That is why the governing principle of this module is blunt: build recovery as carefully as login, because attackers walk through it. This module is also where builder discipline gets tested hardest. Your AI will ship a reset flow whose happy path works beautifully and call the feature complete. But auth quality lives in the edges: the expired token, the double-clicked email, the corporate scanner that opens every link, the flood of scripted requests, the user whose inbox is gone, the dormant account that wakes up and drains itself. Every one is a real scenario from real products, and every one has a known correct answer. The builder who knows those answers can direct and audit a reset flow in one session. The builder who does not is shipping a demo with a breach schedule.

## Certification Goal

Passing the Module 6 exam proves you can direct an AI to build a reset flow with hashed, expiring, single-use tokens, responses that never reveal which accounts exist, session invalidation on completion, scanner-proof token consumption, rate-limited endpoints, and safe handling of email changes, deletion, dormancy, and lost-email recovery.

## What You Need to Know

**The anatomy of a safe reset.** A time-limited, single-use token sent to the verified email, exchanged for a new password on a real form. The token is random, expiring, single-use, and stored hashed, so a database leak does not leak live reset keys. The app never emails an existing password: being able to send it means you stored it readably, the deeper failure the email reveals. Completing a reset invalidates the account's active sessions, because if an intruder is the reason for the reset, this is the moment their access ends. The completed change triggers a notification to the account's email, so an unauthorized change is discovered fast.

**Token lifecycle rules.** Issuing a new token kills the earlier one, so only one live reset path exists at a time. When a double-click creates two, only the newest works. The token is consumed on the form's submission, not the link's opening, because corporate email scanners open every link and would burn single-use tokens before the user sees the form. Never let a click alone change anything: clicks happen without intent, and the change needs a real form. When a token expires mid-form, good handling gives a clear message and a one-click path to a fresh link, not a dead-end error page.

**Enumeration and flood resistance.** A reset request for a nonexistent email gets the same message as a real account, so the endpoint never confirms who is registered. The endpoint also responds in roughly constant time either way, because timing differences leak the same secret the identical text protects. Scripted floods are throttled by rate limits per account and per source. Requests against deactivated accounts behave outwardly like any reset while internally following the account's state rules.

**Identity change flows.** An email change verifies control of the new address, notifies the old one, and requires re-authentication before the swap. When email is the login identity, a change ripples through everything that treated it as permanent: login, invites, history. Account deletion includes re-authentication, a clear grace window, and honest communication about what is removed.

**The hard recovery cases.** A user who has lost their email entirely gets a slower manual path with real identity verification, because instant alternatives are how takeovers happen. Long-dormant accounts are prime targets: high-risk actions on them get extra verification, because the silent account that resets its password and drains its stored value was a designed-in failure. Manual reset requests to support are governed by the verification procedure, followed exactly, because urgency is the attacker's main tool.

**Evidence and testing.** The audit log records requests, sends, completions, and failures, with time and source, because patterns tell the story a single event hides. A real test pass attempts expired, reused, and tampered tokens, wrong accounts, and flood behavior. The reset email contains the link, a clear expiry, and a note to ignore it if unrequested, nothing more.

## Your Toolkit

**Hashed token storage.** Reset tokens stored like passwords: hashed at rest, so a leaked table holds no live reset keys. Direct your AI to treat tokens as credentials, because they are.

**Rate limiting on the reset endpoint.** Per-account and per-source throttles that blunt floods before inboxes fill and before your email sender reputation burns.

**A scanner-safe consumption design.** Token burned on form submission, not link open. This one direction saves you the mystery tickets where "the link never works" for every corporate user.

**A reset event log.** Requests, sends, completions, and failures with time and source. This is where reset floods, targeted attacks, and support disputes become visible.

## Exam Topics

The Module 6 exam will test you on:

**The anatomy of a safe reset** and why existing passwords can never be emailed

**Token properties:** random, expiring, single-use, stored hashed, newest-token-wins

**Enumeration resistance:** identical responses and constant-time behavior

**Session invalidation** on completion and change notifications to the account

**Scanner-proof consumption** and handling expiry mid-form

**Rate limiting** reset floods and handling deactivated accounts

**Email change, account deletion, lost-email recovery,** and dormant account risk

**Support procedures under pressure,** audit logging, and edge-case test passes

## Common Pitfalls

**Happy-path completion.** The clicked link that works proves the demo, not the feature. The edges: expired tokens, scanners, floods, and lost access, are the feature.

**Change-on-click resets.** A link that sets a new password the moment it is opened gets triggered by scanners and previews. Intent requires a form.

**Honest error messages.** "No account exists for this address" hands attackers a verified user list. Same message, same timing, either way.

**Surviving sessions.** A reset that leaves the intruder's session alive changed the lock while the burglar was inside. Invalidate active sessions on completion.

**Sympathy-driven support.** The convincing, urgent caller is the attack. The procedure, followed exactly, is the defense.

**Forgetting dormant accounts.** Long-dead accounts with stored value are prime takeover targets. High-risk actions on them get extra verification.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I list the four properties every reset token must have?
- [ ] Can I explain why the reset endpoint gives the same response and timing for any email?
- [ ] Can I explain what happens to sessions and notifications when a reset completes?
- [ ] Can I describe the corporate scanner problem and the consumption fix?
- [ ] Can I design a safe email change and a safe account deletion flow?
- [ ] Can I explain how lost-email recovery and dormant accounts must be handled?
- [ ] Could I run a full edge-case test pass on a reset flow my AI calls done?

## AI Audit Prompt Template

Use this prompt to audit your reset flow before believing it is finished:

> "You are a security reviewer attacking my password reset flow: [paste flow description]. Verify tokens are random, expiring, single-use, and stored hashed, a new token kills the old one, consumption happens on form submission rather than link open, responses and timing are identical whether or not the account exists, completion invalidates sessions and notifies the account, endpoints are rate limited per account and per source, and all events are logged. Then walk the edges: expired token mid-form, double-clicked emails, deactivated accounts, lost email, dormant accounts, and a convincing urgent support request. Tell me exactly where my flow breaks first."

## What's Next

Module 7 is the ship module: taking everything from Modules 1 through 6 into production. Launch checklists, secret rotation, monitoring, incident response, staged rollouts, and the operational rhythm that keeps auth boring for years.

## Certification Pathway

This module is the sixth step in the Authentication Systems Build course, a paid T4 The Mastery course inside Builder Access, alongside the SaaS Build and Database Design courses. Pass all seven module exams to earn the Auth Build Specialist badge, proof to The Faction that the back door of your apps is built as well as the front.

Matt Murphy AI | The Faction Group LLC | mattmurphy.ai

———

Ready? Take the Password Reset and Edge Cases Exam →
