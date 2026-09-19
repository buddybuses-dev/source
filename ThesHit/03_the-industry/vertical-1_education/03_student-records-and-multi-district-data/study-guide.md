# Module 3: Student Records & Multi-District Data — Study Guide

## Database & Storage for Education Technology

This is the study guide. Everything for Student Records & Multi-District Data is on this page — there's nothing to download.

## What This Module Covers

This module covers database and storage architecture as it applies specifically to education technology — the student record schemas, grade book data models, multi-district tenancy patterns, transcript structures, and academic calendar-aware data management that let your EdTech product safely store and organize the most sensitive data in a school system: student information. You already know database fundamentals from the CADE program. This goes deeper into EdTech-specific patterns: student records that must be retained for years but access-controlled by FERPA, grade data that flows between your platform and the school's SIS, multi-district tenancy where District A must never see District B's students, and academic calendar structures that reset courses by semester or trimester while retaining historical data for transcripts. Your AI coding tool can create database tables in minutes. But if your student records schema doesn't account for students who transfer between schools mid-year, if your grade book can't handle weighted categories and dropped lowest scores, or if a district admin query accidentally returns students from another district — you've created a FERPA violation that can end a contract instantly.

## Why It Matters

Student data is among the most regulated and most sensitive data categories in the United States. FERPA governs who can see what, when, and under what circumstances. A database that leaks student records across districts isn't just a bug — it's a federal compliance violation that triggers mandatory breach notification, potential loss of federal funding for the school, and immediate contract termination for your product. Beyond compliance, the data model drives every feature in your platform. Grade calculations depend on correctly structured assignment categories and weighting rules. Transcripts depend on properly archived historical data. Roster sync depends on correctly mapped student-to-section-to-teacher relationships. If the schema is wrong, every feature built on top of it inherits the error.

## Module Certification Goal

You can describe student record schemas, multi-district data isolation, and academic calendar-aware data models to an AI coding tool, evaluate the output for FERPA-compliant access control, proper grade calculation support, and cross-district isolation, and ship a database architecture that safely stores student data for districts that trust your platform with their most sensitive information.

## What You Need to Know
- **Student record data modeling:** A student record includes far more than name and email. It includes enrollment status, demographic data (race, ethnicity, gender — required for federal reporting), grade level, homeroom assignment, IEP/504 status, guardian contacts, and historical enrollment across schools and years. Your schema needs to capture this complexity while keeping queries fast and access controlled.
- **Multi-district tenancy:** Districts are the tenant boundary in K-12 EdTech. Each district has its own schools, teachers, students, and policies. A multi-district platform must isolate data at the district level — with Row-Level Security enforcing that District A's administrators cannot see District B's student records, even accidentally, even in aggregate reports.
- **Grade book data architecture:** Grade calculations require structured data: assignment categories (homework, exams, projects) with weights, individual assignment scores, dropped-lowest-score rules, extra credit handling, incomplete/missing markers, and late penalty calculations. This isn't a single table — it's a relational structure that supports the grading policies of every teacher in every school.
- **Academic calendar and term structures:** Schools operate on semesters, trimesters, quarters, or custom schedules. Your database needs to track which term a course belongs to, when grades are final, and when historical data gets archived to transcripts. A course section in Fall 2026 is different from the same course in Spring 2027 — different students, different grades, same curriculum.
- **Transcript and historical data retention:** Transcripts require permanent retention of course names, grades, credits, and GPA calculations — even after the student graduates or the course is no longer offered. Your schema needs to archive completed term data in a way that survives curriculum changes, school restructuring, and platform migrations.

## Your Toolkit
- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — describe your student record schemas, grade book models, and district isolation policies to it.
- **A database viewer with RLS testing:** Supabase dashboard or pgAdmin. Test RLS policies by querying as different district roles to verify isolation.
- **Migration tools:** Prisma Migrate, Drizzle, or raw SQL migration files. Schema changes in production education databases must be reversible and tested on staging first.
- **Test data generator:** Scripts that populate your database with realistic multi-district, multi-school, multi-grade data so you can test isolation and query performance at scale.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:
- **Student record completeness:** Can you evaluate whether a student records schema captures enrollment, demographics, grade level, IEP status, and guardian contacts correctly?
- **District isolation:** Can you verify that RLS policies prevent cross-district data access at the database level?
- **Grade book data integrity:** Can you assess whether grade calculations handle weighted categories, dropped scores, extra credit, and missing assignments correctly?
- **Academic calendar support:** Can you evaluate whether the schema supports multiple term structures (semester, trimester, quarter) across different schools in the same district?
- **Historical data retention:** Can you verify that completed terms are archived in a way that supports transcript generation even after curriculum changes?
- **Transfer student handling:** Can you assess what happens when a student transfers between schools or districts mid-year — does their data follow them correctly?
- **Performance at scale:** Can you identify when queries against student data slow down as the district grows and prescribe the right indexing strategy?
- **Data export and portability:** Can you evaluate whether student data can be exported in standard formats for SIS sync, state reporting, or platform migration?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Treating student data like any other user data. Student records have legal retention requirements, access restrictions, and mandatory fields that regular user tables don't. A generic users table won't work for K-12. Not isolating data at the district level. If your database serves multiple districts, RLS must prevent any query from returning students outside the requesting district's boundary. A district admin accidentally seeing another district's students is a FERPA violation. Building a flat grade book instead of a structured one. A single 'grade' column per student per course isn't enough. Teachers need categories, weights, dropped scores, and late penalties. If the schema doesn't support this, the grade book feature is useless. Not planning for term transitions. When a semester ends, course data needs to be archived for transcripts while new sections open for the next term. Without term-aware data management, historical grades get overwritten or lost. Ignoring the transfer student scenario. Students move between schools and districts regularly. If your schema can't handle a student existing in one district's records and then appearing in another's, you create duplicate records or orphaned data. Storing demographic data without proper access controls. Race, ethnicity, IEP status, and disability information require tighter access than general student records. Not every teacher needs to see every field.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. Does your student records schema capture enrollment, demographics, grade level, IEP status, and guardian contacts? Are Row-Level Security policies enforced at the district level to prevent cross-district data access? Does your grade book schema support weighted categories, dropped scores, and late penalties? Can your database handle multiple term structures (semesters, trimesters) across schools in the same district? Are completed terms archived for transcript generation without losing data when curricula change? Have you tested with a student who transfers mid-year between schools? Can student data be exported in standard formats for SIS sync and state reporting?

## AI Audit Prompt Template

> Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my EdTech platform's database schema and check the following. For each one, tell me pass or fail with a specific example: Student records: Does the schema capture enrollment status, demographics, grade level, IEP/504 status, and guardian contacts? District isolation: Are RLS policies enforced so no query returns students from outside the requesting district? Grade book: Does the schema support weighted categories, dropped lowest scores, and per-teacher grading policies? Academic calendar: Can the system handle different term structures across schools?

> Transcript archival: Are completed terms preserved for transcript generation? Transfer handling: Can a student transfer between schools without data loss or duplication? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 3 exam. The best way to prepare: build a multi-school database with realistic student data. Create two districts, add schools to each, enroll students, and verify that District A can't see District B's records. Build a grade book with weighted categories. Archive a term and verify transcript data persists. Every isolation gap or data loss you find is exactly what the exam tests.

## Certification Pathway
- **Industry Specialist — Education/EdTech:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

Ready? Take the Student Records & Multi-District Data Exam →
