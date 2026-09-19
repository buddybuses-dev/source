# Module 3: Protecting Your Database — Study Guide

## Database Security for AI Directed Engineers

This is the study guide. Everything for Protecting Your Database is on this page — there's nothing to download.

## What This Module Covers

This module covers the security of your database — the place where your most sensitive data lives. Your frontend is what attackers see. Your API is what they probe. Your database is what they want. If they get through the first two layers, the database is the prize. SQL injection remains one of the most common and most devastating attack vectors. A single unsanitized query parameter can let an attacker read, modify, or delete your entire database. Beyond injection, exposed database ports, default credentials, unencrypted data at rest, and overly permissive database users create paths for attackers to access data without going through your application at all. AI tools generate database queries quickly. They build ORMs, write raw SQL, and configure connection strings — often with convenience prioritized over security. Your job is to verify that every query is parameterized, every connection is encrypted, every database user has minimum necessary privileges, and backups are protected as carefully as the production database.

## Why It Matters

A database breach is not a bug to fix. It's an event that can end a business. Customer data, financial records, personal information, and credentials — once exfiltrated, this data can never be un-stolen. The breach notification costs, legal liability, regulatory fines, and reputation damage compound far beyond the cost of implementing security controls in the first place. Every builder in this community stores user data. That data is a responsibility. Protecting your database isn't optional — it's the minimum standard for operating a product that other people trust with their information.

## Module Certification Goal

You can identify database security vulnerabilities in an AI-built application — SQL injection risks, exposed ports, default credentials, unencrypted storage, and overly permissive access — direct your AI to implement proper protections, and verify that your database is secured against both application-layer and network-layer attacks.

## What You Need to Know

- **SQL injection:** SQL injection occurs when user input is concatenated directly into a database query string. If a login form builds the query 'SELECT * FROM users WHERE email = ' + userInput, an attacker can input a string that modifies the query logic — bypassing authentication, extracting data, or deleting tables. Parameterized queries and ORMs prevent this by separating data from query structure.
- **Parameterized queries and ORMs:** Parameterized queries send user input as data values, never as part of the SQL structure. ORMs like Prisma, Drizzle, and SQLAlchemy do this by default when used correctly. But AI tools sometimes generate raw SQL concatenation even when an ORM is available. Audit every database query in your codebase for string concatenation.
- **Database access credentials:** Your application connects to the database with a username and password. If that credential has full admin access, a compromised application gives the attacker full database control. Create a dedicated application user with only the permissions your app needs — SELECT, INSERT, UPDATE on specific tables. Never connect with the database root or admin account.
- **Encryption at rest:** Data at rest means data stored on disk. If an attacker gains access to your database server's storage — through a cloud misconfiguration, stolen backup, or physical access — unencrypted data is immediately readable. Encryption at rest scrambles the stored data so it's useless without the decryption key.
- **Network exposure and port security:** Databases should never be directly accessible from the internet. A database listening on a public IP with port 5432 (Postgres) or 3306 (MySQL) open is an invitation. Database connections should only be accepted from your application server's IP or through a private network.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — direct it to audit your queries for injection vulnerabilities and implement parameterized queries throughout.
- **SQL injection testing tool:** SQLMap or manual testing through your API with injection payloads. Test every endpoint that accepts user input and passes it to a database query.
- **Database security scanner:** DbProtect, pgAudit for Postgres, or cloud-native database security features. These audit your database configuration for known vulnerabilities.
- **Network scanning tool:** Nmap or cloud security group audit to verify your database ports are not exposed to the public internet.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **SQL injection identification:** Can you recognize when a database query is vulnerable to injection because user input is concatenated rather than parameterized?
- **Parameterized query verification:** Can you evaluate whether your ORM or query builder correctly separates user data from SQL structure in every database operation?
- **Credential management:** Can you assess whether your application uses a least-privilege database user instead of root or admin credentials?
- **Encryption at rest:** Can you verify that your database encrypts stored data so a storage-level breach doesn't expose readable records?
- **Network exposure:** Can you check whether your database port is accessible from the public internet or properly restricted to your application server?
- **Backup security:** Can you evaluate whether database backups are encrypted and stored in a location with access controls separate from production?
- **Query logging:** Can you assess whether your database logs queries for security monitoring without logging sensitive data values in the query parameters?
- **Default credential elimination:** Can you verify that default database passwords and sample accounts have been removed or changed before production deployment?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- Using string concatenation for database queries because the AI generated it that way. Even one concatenated query in your entire codebase is a SQL injection risk. Search your code for string interpolation in any file that touches the database.
- Connecting your application to the database with root credentials. If the application is compromised, the attacker has full database access. Create an application-specific user with only the permissions it actually needs.
- Leaving your database port open to the public internet. If 5432 or 3306 is accessible from any IP address, attackers will find it. Restrict database access to your application server's IP or private network.
- Not encrypting backups. Your production database might be encrypted at rest, but if your nightly backup is an unencrypted dump file stored in an S3 bucket with loose permissions, the backup is the weak point.
- Logging full query strings including user data. Query logs that contain 'SELECT * FROM users WHERE ssn = 123-45-6789' are themselves a data exposure. Log query structure and metadata, not parameter values.
- Not rotating database credentials. If the same password has been used since the database was created and it's been shared in Slack channels, old emails, and documentation, the credential surface is enormous.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Have you searched your codebase for any SQL query that uses string concatenation or interpolation with user input?
- Does your application connect to the database with a dedicated least-privilege user, not root or admin?
- Is your database port restricted to accept connections only from your application server or private network?
- Is your database encrypted at rest?
- Are database backups encrypted and stored with separate access controls from production?
- Have all default database passwords and sample accounts been changed or removed?
- Do your query logs capture structure and metadata without logging sensitive parameter values?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers.

> Review my database security configuration and check the following. For each one, tell me pass or fail with a specific example: SQL injection: Are all queries parameterized with no string concatenation? Access credentials: Does the app use a least-privilege database user? Network exposure: Is the database port restricted from public access? Encryption at rest: Is stored data encrypted? Backup security: Are backups encrypted with separate access controls? Default credentials: Have all defaults been changed? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 3 exam. The best way to prepare: search your codebase for every file that touches the database. Check if queries are parameterized. Check your database user's permissions. Run nmap against your database port from outside your network. Every misconfiguration you find is exactly what the exam tests.

## Certification Pathway

- **Security Specialist — Foundations:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the Protecting Your Database Exam →
