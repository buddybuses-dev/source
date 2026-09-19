# Module 5: Two-Factor and Account Security — Study Guide

## T4 The Mastery | Authentication Systems Build

This is the study guide. Everything for Two-Factor and Account Security is on this page — there's nothing to download.

## What This Module Covers

This module covers the second lock on the door: two-factor authentication and the account security system around it. You will learn the three factor categories and why authenticator apps beat SMS, how backup codes and device trust work, what step-up authentication protects, why recovery flows are the attacker's favorite entrance, and the signals that reveal an account takeover in progress.

## Why It Matters

A password is one secret, and Module 2 taught you how often that secret leaks. A second factor adds an independent proof, so a stolen password alone is no longer enough to get in. That sentence is most of this module's value, but the craft lives in what surrounds it, because every strengthening of the front door creates pressure on the side doors. Add 2FA and attackers move to the recovery flow, which exists precisely to bypass normal factors. Harden recovery and they call your support line with a convincing story. Offer "trust this device" and every trusted device becomes a standing bypass of the factor you just added. Security is a system, and this module keeps returning to one theme: factors, recovery, and support must hold together, because the attacker gets to choose the weakest of the three. This is also a design module. A 2FA rollout that locks out half your user base is a failure even if the cryptography is perfect. You will learn to roll out mandatory 2FA without chaos, teach what matters at enrollment, and balance lockouts against attackers who fail 2FA on purpose to jail the real owner.

## Certification Goal

Passing the Module 5 exam proves you can direct an AI to build a 2FA system on proven libraries, choose factors deliberately, store TOTP secrets and device-trust tokens correctly, require 2FA where takeovers do the most damage, design recovery that resists social engineering, and read the signals of a takeover in progress.

## What You Need to Know

**Factors and what each adds.** The three classic categories: something you know, something you have, and something you are, each proven separately. A second factor is an independent proof, not a longer password. Authenticator apps beat SMS because SMS can be intercepted or SIM-swapped, while app codes never travel over a network. Emailing the 2FA code is a structural failure: the email account resets the password too, so both factors collapse into one inbox. Passkeys are the next step: cryptographic credentials bound to a device or account, replacing passwords entirely.

**Where 2FA is required, not offered.** Admin accounts and dangerous actions, where a takeover does the most damage. For accounts with admin power, 2FA is mandatory without exceptions, because these accounts are where a takeover becomes a breach. Step-up authentication extends the idea: fresh or stronger proof at the moment of a sensitive action, not just at login. After 2FA completes, the session is marked strongly verified, and that standing is what sensitive actions check.

**Backup codes and device trust.** Backup codes exist for regaining access when the second factor is lost, stored safely offline by the user. The enrollment flow has thirty seconds to teach one thing: save the backup codes now, in a real place, because that is the step users skip and regret. "Trust this device for 30 days" is a standing bypass of the second factor, so scope and expiry matter, and the cookie behind it must be its own scoped, revocable token, not a longer-lived copy of the session.

**Implementation discipline.** Direct your AI to use an established 2FA library, because the algorithms have edge cases like clock drift that libraries already handle. TOTP secrets are stored encrypted server-side with tight access, since anyone reading them can mint valid codes. Rate-limit code attempts specifically, because six-digit codes fall to brute force under unlimited guesses. Balance the lockout: deliberately failing 2FA to jail the owner is a denial-of-service angle, so slow attackers without locking owners out.

**Recovery and the human side door.** Recovery flows are the attacker's favorite target because they exist to bypass normal factors: a weak flow undoes every strong factor. A user who has lost phone, backup codes, and old number gets real identity verification with friction and delay, because this is the takeover path. Support follows verification procedures every time, with no sympathy exceptions, because urgency is the attacker's main tool. Rolling out mandatory 2FA to an existing base: announce it, start with admins, offer a grace window, and support users through it.

**Detection and notification.** The real owner is the best intrusion detector you have, if you give them the signal early: notify on logins from new devices or locations. Takeover fingerprint: new device, new location, factor changes, and recovery attempts clustered in time. Security notification emails must themselves be safe: inform and point users to the app they know, rather than pushing urgent links to click.

## Your Toolkit

- **An established TOTP library or provider feature.** Code generation, clock drift, and verification handled by components with years of fixes. Direct configuration, not invention.
- **Backup code generation and storage flow.** Single-use codes issued at enrollment, with an enrollment screen designed around the one behavior that matters: saving them somewhere real.
- **Encrypted secret storage.** TOTP secrets encrypted server-side with tight access, separate from password hashes, because these secrets mint valid codes for anyone who reads them.
- **Login anomaly notifications.** New device and new location alerts wired from day one, turning every real user into a tripwire against takeover.

## Exam Topics

The Module 5 exam will test you on:

1. The three factor categories and what an independent second proof adds
2. TOTP versus SMS versus email codes, and what passkeys are
3. Where 2FA is mandatory, step-up authentication, and the strongly verified session
4. Backup codes, device trust scope and expiry, and the trusted-device token
5. Library use, encrypted TOTP secret storage, and rate limiting code attempts
6. Recovery design, support verification procedures, and social engineering defense
7. Rolling out mandatory 2FA without chaos and what enrollment must teach
8. Takeover signals, login notifications, and safe security emails

## Common Pitfalls

- **2FA codes by email.** The inbox that receives the code also resets the password. Two factors just collapsed into one.
- **Strong factors, weak recovery.** A recovery flow that hands out access on a sad story undoes every factor above it. Recovery gets the same design rigor as login.
- **Unlimited code guesses.** Six digits fall fast to brute force. Rate-limit 2FA attempts specifically, not just passwords.
- **Device trust as a session clone.** The remember-this-device cookie must be its own scoped, revocable token with real expiry, not an immortal session.
- **Enrollment that skips backup codes.** Users who breeze past the backup code screen become next quarter's lockout tickets and takeover targets.
- **Overnight mandatory 2FA.** Flipping the requirement on for everyone at once trades one security gap for a support fire. Announce, start with admins, offer a grace window.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I name the three factor categories and explain what independence buys?
- [ ] Can I rank TOTP, SMS, and email codes and justify the order?
- [ ] Can I say where 2FA must be mandatory and what step-up auth adds?
- [ ] Can I describe how TOTP secrets and device-trust tokens must be stored?
- [ ] Can I design a recovery path that resists social engineering?
- [ ] Can I list four signals that suggest a takeover in progress?
- [ ] Could I plan a mandatory 2FA rollout for an existing user base?

## AI Audit Prompt Template

Use this prompt to audit your 2FA and account security build:

> "You are an account security reviewer. Here is my 2FA design: [paste factors, enrollment flow, recovery path, device trust, and support procedure]. Verify an established library handles code generation, TOTP secrets are encrypted server-side, code attempts are rate limited, 2FA is mandatory for admins, sensitive actions use step-up checks, device trust uses a scoped revocable token with expiry, backup codes are issued and taught at enrollment, recovery requires real verification with friction, and new device logins trigger notifications. Tell me which side door an attacker tries first: recovery, support, or device trust, and why."

## What's Next

Module 6 goes deep on the flow attackers love most: password reset. Token anatomy, enumeration resistance, link scanners that eat single-use tokens, account deletion, dormant accounts, and the edge cases that separate a real auth system from a demo.

## Certification Pathway

This module is the fifth step in the Authentication Systems Build course, a paid T4 The Mastery course inside Builder Access, alongside the SaaS Build and Database Design courses. Pass all seven module exams to earn the Auth Build Specialist badge, the mark in The Faction of accounts that stay in their owners' hands.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Two-Factor and Account Security Exam →
