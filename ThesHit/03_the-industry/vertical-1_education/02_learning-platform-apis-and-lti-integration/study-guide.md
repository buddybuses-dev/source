# Module 2: Learning Platform APIs & LTI Integration — Study Guide

## APIs & Backend Logic for Education Technology

This is the study guide. Everything for Learning Platform APIs & LTI Integration is on this page — there's nothing to download.

## What This Module Covers

This module covers APIs and backend logic as they apply specifically to education technology — the LTI integration standards, grade passback APIs, Student Information System connectors, and content interoperability protocols that let your EdTech product work inside the ecosystem that schools already use. You already know API fundamentals from the CADE program. This goes deeper into EdTech-specific patterns: LTI (Learning Tools Interoperability) which lets your tool launch inside Canvas, Blackboard, or Google Classroom without separate login; grade passback which sends scores from your tool directly into the school's grade book; SIS (Student Information System) integration which syncs rosters, enrollment, and demographics; and SCORM/xAPI standards for tracking learning activity across platforms. Your AI coding tool can build APIs quickly. But if your tool can't launch inside Canvas via LTI, if grades don't flow back to the teacher's grade book automatically, or if roster sync breaks when a student transfers mid-semester — your EdTech product sits outside the workflow and teachers stop using it.

## Why It Matters

Schools don't adopt standalone tools. They adopt tools that integrate into their existing LMS ecosystem. If a teacher has to leave Canvas to use your product, copy grades manually, and re-enter attendance data, your product creates work instead of reducing it. LTI integration is the price of admission for EdTech products selling to schools and districts. Grade passback is the single most important integration for teacher adoption. If a student completes an assessment in your tool and the grade appears automatically in Canvas, the teacher saves hours per week. If they have to manually transfer scores, your tool is the first thing cut when workload conversations happen. The EdTech API ecosystem is standardized but complex. LTI 1.3, LTI Advantage, OneRoster, SIF, SCORM, xAPI — each standard serves a different purpose and has different implementation requirements. Your AI tool needs clear direction on which standards matter for your product.

## Module Certification Goal

You can describe LTI integration, grade passback APIs, and SIS roster sync to an AI coding tool, evaluate the output for standards compliance and error handling, and ship an EdTech backend that works seamlessly inside the school's existing LMS ecosystem without requiring teachers to change their workflow.

## What You Need to Know
- **LTI (Learning Tools Interoperability):** LTI is the standard that lets your EdTech tool launch inside a Learning Management System like Canvas, Blackboard, or Schoology. When a teacher clicks your tool in their LMS, LTI handles authentication, passes user identity and course context, and opens your tool in an iframe — no separate login needed. LTI 1.3 uses OAuth 2.0 and JWTs for secure launches.
- **Grade passback (Assignment and Grade Services):** LTI Advantage includes AGS (Assignment and Grade Services) which lets your tool send scores directly to the LMS grade book. When a student completes a quiz in your tool, the grade appears in Canvas automatically. This requires setting up a line item (the assignment) and posting scores with the correct student-course-assignment mapping.
- **SIS integration and roster sync (OneRoster):** Student Information Systems hold enrollment, demographics, and class rosters. OneRoster is the standard API for syncing this data. Your platform needs to pull rosters at the start of each term, handle mid-year transfers (students joining or leaving), and map SIS course sections to your platform's courses.
- **Content standards (SCORM and xAPI):** SCORM packages let you deliver interactive content that tracks completion and scores. xAPI (Experience API) is the modern replacement — it tracks granular learning events (watched video, answered question, paused at minute 3:42). If your content needs to work across multiple LMS platforms, packaging it as SCORM or xAPI-tracked ensures portability.
- **Webhook-driven enrollment events:** When a student enrolls in a course, drops a class, or transfers schools, your system needs to know. SIS webhooks or scheduled sync jobs keep your roster current. Without this, withdrawn students retain access and new students can't log in.
- **Multi-LMS compatibility:** Schools use different LMS platforms — Canvas, Google Classroom, Blackboard, Schoology, Moodle. Your LTI integration needs to work across all of them, which means testing against each platform's LTI implementation quirks. What works perfectly in Canvas may break in Blackboard.

## Your Toolkit
- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — describe your LTI launch handlers, grade passback endpoints, and roster sync logic to it.
- **LTI reference implementation:** IMS Global's LTI 1.3 reference library or an open-source LTI library for your language. These handle the JWT validation and OAuth 2.0 flow.
- **LMS sandbox accounts:** Canvas Free-for-Teacher, Moodle sandbox, or Blackboard developer instance. You need at least two LMS platforms to test your LTI integration against.
- **API testing tools:** Postman for manually testing grade passback and roster sync endpoints. Stripe-style webhook forwarding for testing enrollment event handling locally.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:
- **LTI launch flow:** Can you evaluate whether an LTI 1.3 integration correctly handles the OAuth 2.0 launch sequence, validates JWTs, and extracts user identity and course context?
- **Grade passback implementation:** Can you assess whether grades flow from your tool to the LMS grade book correctly with proper student-assignment mapping?
- **Roster sync accuracy:** Can you verify that roster sync handles enrollments, drops, and mid-year transfers without leaving ghost students or blocking new ones?
- **Multi-LMS compatibility:** Can you identify when an LTI integration works in one LMS but fails in another due to platform-specific implementation differences?
- **Content standards compliance:** Can you evaluate whether learning content is packaged correctly for cross-platform delivery via SCORM or xAPI tracking?
- **Error handling in integrations:** Can you assess what happens when grade passback fails, a roster sync encounters duplicate students, or an LTI launch receives an invalid token?
- **Authentication and security:** Can you verify that LTI launches use proper JWT validation and that API keys for SIS integration are stored securely?
- **Enrollment event handling:** Can you evaluate whether your system correctly processes enrollment changes — adds, drops, transfers — from SIS webhooks or scheduled syncs?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Building a standalone login system instead of LTI integration. If teachers have to create separate accounts and manage separate passwords for your tool, adoption drops immediately. LTI lets students and teachers launch your tool from inside Canvas with zero friction. Not implementing grade passback. If teachers have to manually enter scores from your tool into their LMS grade book, you've added work to their day instead of removing it. Grade passback is the number one feature that determines whether teachers keep using an EdTech tool. Testing LTI integration against only one LMS. Canvas handles LTI launches differently than Blackboard, which handles them differently than Moodle. If you only test against Canvas, you'll break in every other LMS your customers use. Ignoring mid-year roster changes. Students transfer, drop courses, and enroll late. If your roster sync only runs at the start of the semester, you'll have students who can't access the platform and withdrawn students who still can. Hardcoding LMS-specific assumptions into your API. If your grade passback assumes Canvas's specific API format, you'll have to rewrite it for every other LMS. Use the LTI standard abstractions instead of platform-specific endpoints. Not handling grade passback failures gracefully. If a score fails to sync to the LMS, the teacher needs to know. A silent failure means grades disappear without anyone noticing until report card time.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. Can your tool launch inside Canvas or another LMS via LTI 1.3 without requiring a separate login? When a student completes an assignment in your tool, does the grade appear in the LMS grade book automatically? Does your roster sync handle mid-year enrollment changes — adds, drops, and transfers? Have you tested your LTI integration against at least two different LMS platforms? If grade passback fails, does your system notify the teacher and retain the score for retry? Are your SIS API credentials stored securely and not hardcoded in the application? Can your content be exported as SCORM or tracked via xAPI for cross-platform use?

## AI Audit Prompt Template

> Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my EdTech platform's API integrations and check the following. For each one, tell me pass or fail with a specific example: LTI integration: Does the tool launch correctly inside an LMS via LTI 1.3 with proper JWT validation and user context extraction? Grade passback: Do scores sync automatically to the LMS grade book with correct student-assignment mapping? Roster sync: Does the system handle enrollments, drops, and transfers from the SIS without ghost students or blocked access? Multi-LMS support: Has the integration been tested against at least two LMS platforms? Error handling: Do failed grade submissions notify the teacher and queue for retry?

> Security: Are all API keys and LTI secrets stored in environment variables, not in client code? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 2 exam. The best way to prepare: set up a Canvas Free-for-Teacher account and build an LTI 1.3 launch. Send a grade back to the Canvas grade book. Pull a roster from a test SIS. Every integration gap you discover during building is exactly what the exam tests.

## Certification Pathway
- **Industry Specialist — Education/EdTech:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

Ready? Take the Learning Platform APIs & LTI Integration Exam →
