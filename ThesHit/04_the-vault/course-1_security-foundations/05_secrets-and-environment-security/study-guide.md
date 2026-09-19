# Module 5: Secrets & Environment Security — Study Guide

## Credential Management for AI Directed Engineers

This is the study guide. Everything for Secrets & Environment Security is on this page — there's nothing to download.

## What This Module Covers

This module covers how your application manages secrets — API keys, database credentials, service tokens, encryption keys, and any other sensitive values that your application needs to function but that should never be visible to users, stored in version control, or exposed in logs. This is the single most common security mistake in AI-built applications. AI tools hardcode credentials directly into source files because it's the fastest way to make the code work. The API key goes in the fetch call. The database URL goes in the connection config. The Stripe secret key goes in the payment handler. The code works — and every secret is now visible in your Git repository, your client-side bundle, or your CI/CD logs. Secrets management is the practice of keeping sensitive values separate from your code, storing them in secure locations, rotating them on a schedule, and ensuring they're never exposed in places where unauthorized people can read them.

## Why It Matters

A leaked API key can run up thousands of dollars in cloud charges in hours. A leaked database credential gives direct access to every record. A leaked Stripe secret key lets an attacker process fraudulent transactions. And secrets committed to Git live in the repository history forever — even if you delete the file, the commit that added it is still there. GitHub scans for leaked secrets and reports millions of exposed credentials per year. Automated bots monitor public repositories and exploit leaked credentials within minutes of exposure. If your AI tool hardcoded a secret and you pushed it to GitHub, assume it has already been found.

## Module Certification Goal

You can identify exposed secrets in AI-built applications — hardcoded credentials in source code, secrets in Git history, API keys in frontend bundles, and sensitive values in logs — direct your AI to implement proper secrets management, and verify that no secret is accessible outside its intended secure storage.

## What You Need to Know

- **Environment variables:** Environment variables store configuration values outside your code. Instead of writing const API_KEY = 'sk-abc123' in your source file, you read process.env.API_KEY at runtime. The value lives in your deployment environment's configuration, not in your codebase. This is the foundational pattern for secrets management.
- **.env files and .gitignore:** .env files store environment variables locally during development. They must NEVER be committed to Git. Your .gitignore file should include .env on its first line. AI tools frequently create .env files with real credentials and don't always add them to .gitignore. Check immediately after your AI creates any configuration file.
- **Secrets in Git history:** If a secret was ever committed to Git, it lives in the repository history forever. Deleting the file or replacing the value in a new commit does not remove the original commit. Anyone who clones the repository can find it. If a secret was committed, it must be rotated — the old value must be invalidated and replaced.
- **Frontend vs. backend secrets:** Secrets used in frontend code are visible to every user. Environment variables prefixed with NEXT_PUBLIC_ or VITE_ in modern frameworks are bundled into the client-side JavaScript. Only non-sensitive configuration should use these prefixes. Secret keys, database URLs, and service credentials must only be accessed server-side.
- **Secrets rotation:** Secrets should be rotated regularly — replaced with new values on a schedule. If a secret is compromised, rotation limits the window of exposure. If your database password hasn't changed in two years and has been shared in Slack and documentation, the number of people and systems that know it has grown unchecked.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to move all hardcoded secrets to environment variables and verify .gitignore includes .env files.
- **Git secret scanner:** GitLeaks, TruffleHog, or GitHub's built-in secret scanning to search your repository history for leaked credentials.
- **Secrets manager:** AWS Secrets Manager, Doppler, or Vault by HashiCorp for storing production secrets with access controls, audit logging, and automatic rotation.
- **Environment variable validator:** A startup check in your application that verifies all required environment variables are set before the app begins serving requests.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **Hardcoded secret detection:** Can you find API keys and credentials hardcoded directly in source code files rather than stored in environment variables?
- **.gitignore verification:** Can you verify that .env files and other secret-containing files are properly excluded from version control?
- **Git history exposure:** Can you assess whether secrets that were previously committed to Git have been rotated to invalidate the exposed values?
- **Frontend secret exposure:** Can you identify secrets that are incorrectly prefixed for client-side access when they should be server-side only?
- **CI/CD secret handling:** Can you evaluate whether build and deployment pipelines handle secrets securely without exposing them in build logs?
- **Secrets rotation policy:** Can you assess whether critical credentials are rotated on a regular schedule and after any suspected compromise?
- **Environment separation:** Can you verify that development, staging, and production environments use different credentials rather than sharing the same secrets?
- **Logging sanitization:** Can you check whether application logs accidentally capture and store secret values in plain text?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Hardcoding an API key in your code because the AI put it there and it worked. The code works the same whether the key is hardcoded or in an environment variable. The difference is who else can read it.
- Adding .env to .gitignore after the file was already committed. The file is in Git history. Adding it to .gitignore prevents future commits but doesn't remove the existing one. The secret must be rotated.
- Using NEXT_PUBLIC_ or VITE_ prefixes on secret keys. These prefixes tell the framework to include the value in the client-side bundle. Your Stripe secret key with NEXT_PUBLIC_ prefix is in every user's browser.
- Sharing secrets in Slack, email, or shared documents. Every channel where a secret appears becomes a potential leak point. Use a secrets manager and share access, not the values themselves.
- Never rotating credentials. If the same database password has been in use since the project started, every person who has ever had access to it still knows it. Rotate credentials quarterly at minimum.
- Not checking CI/CD build logs for secret exposure. Build processes that echo environment variables or print configuration during deployment can expose secrets in log files that are retained for weeks or months.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Have you searched your codebase for any hardcoded API keys, database URLs, or service credentials?
- Is .env listed in your .gitignore file and has it been there since before any .env file was committed?
- Have you scanned your Git history for previously committed secrets using GitLeaks or TruffleHog?
- Are all secrets that are only needed server-side excluded from client-side environment variable prefixes?
- Do your CI/CD pipeline logs sanitize or mask secret values?
- Are different credentials used for development, staging, and production?
- When was the last time your production database password was rotated?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my secrets management practices and check the following. For each one, tell me pass or fail with a specific example: Hardcoded secrets: Are all secrets stored in environment variables, not code? .gitignore: Are .env files excluded from version control? Git history: Have previously committed secrets been rotated? Frontend exposure: Are secret keys excluded from client-side bundles? CI/CD logs: Are secrets masked in build and deployment output? Rotation: Are credentials rotated on a regular schedule? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 5 exam. The best way to prepare: run GitLeaks against your own repository. Search your codebase for strings that look like API keys. Check your .gitignore. Inspect your CI/CD build logs for exposed values. Every leaked secret you find is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the Secrets & Environment Security Exam →
