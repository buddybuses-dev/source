# Module 1: Student & Teacher Portals — Study Guide

## Frontend Foundations for Education Technology

This is the study guide. Everything for Student & Teacher Portals is on this page — there's nothing to download.

## What This Module Covers

This module covers frontend foundations as they apply specifically to education technology — the student dashboards, teacher admin panels, parent portals, and course interfaces that make a learning platform feel intuitive instead of overwhelming. You already know frontend basics from the CADE program. This goes deeper into the patterns unique to EdTech: role-based views where the same course looks different to a student, teacher, and administrator, progressive disclosure that reveals complexity only when the user is ready, accessibility requirements that go beyond general web standards into educational accommodation mandates, and mobile-first design for students who access everything from their phones. Your AI coding tool can build a learning dashboard quickly. But if the teacher can't find the grade book, if a parent can't see their child's progress without clicking through six screens, or if the course interface doesn't work on a Chromebook with a slow school network — your EdTech product fails the people it was built to serve.

## Why It Matters

Education technology serves four distinct user types with four different needs: students who need simplicity, teachers who need control, parents who need visibility, and administrators who need oversight. Most EdTech products fail because they build for one persona and force the others to adapt. A student portal cluttered with admin controls is confusing. A teacher dashboard missing bulk grading tools is unusable. A parent view that shows raw grade data without context is alarming. The frontend is where trust is built or lost in education. Teachers adopt tools that feel like they respect their time. Students engage with interfaces that feel like apps they already use. Parents trust platforms that surface the right information without requiring a tutorial. AI can build all four views — but only if you tell it exactly how each role's experience should differ.

## Module Certification Goal

You can describe role-based education interfaces to an AI coding tool — student dashboards, teacher admin panels, parent portals, and admin oversight views — evaluate the output for accessibility, device compatibility, and role-appropriate information density, and ship a frontend that serves all four user types without forcing any of them to navigate screens that weren't designed for them.

## What You Need to Know
- **Role-based view architecture:** The same platform looks different depending on who's logged in. A student sees their courses, assignments, and grades. A teacher sees their roster, grade book, and assignment creator. A parent sees their child's progress and attendance. An admin sees school-wide analytics and user management. Your frontend needs a view layer that renders different layouts based on the authenticated user's role.
- **Progressive disclosure in learning interfaces:** Students don't need to see every feature on day one. New users should see a simplified view — their next assignment, their current grade, upcoming deadlines. Advanced features (discussion forums, resource libraries, study groups) reveal themselves as the student engages deeper. This reduces overwhelm and increases adoption.
- **Chromebook and low-bandwidth optimization:** K-12 students often access platforms on school-issued Chromebooks with limited processing power and shared network bandwidth. Your frontend must work on Chrome OS, load quickly on slow connections, and degrade gracefully when bandwidth drops. Heavy JavaScript frameworks and unoptimized images break the experience.
- **Educational accessibility requirements:** EdTech accessibility goes beyond WCAG compliance. Students with IEPs (Individualized Education Programs) may need extended time displays, larger text options, screen reader compatibility for all interactive elements, and keyboard-only navigation. These aren't optional nice-to-haves — they're legal requirements under Section 508 and ADA.
- **Assignment and course content display:** Course content needs structured rendering: lessons in sequence, assignments with due dates and submission status, resources organized by unit, and progress indicators showing completion percentage. Your AI tool can build a content feed — but a course isn't a social feed. It needs pedagogical structure.
- **Teacher grade book interfaces:** The grade book is the teacher's most-used tool. It needs to handle bulk grading (grade 30 students on one assignment in one view), weighted categories, late submission policies, grade overrides, and export to the school's Student Information System. If the grade book is slow or clunky, teachers abandon the platform entirely.

## Your Toolkit
- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code — describe your role-based views, course layouts, and grade book interfaces to it.
- **A component library with table support:** Shadcn/ui, Radix, or TanStack Table. EdTech frontends rely heavily on data tables — rosters, grade books, attendance logs — that need sorting, filtering, and inline editing.
- **Device testing tools:** Chrome DevTools device emulation for Chromebook testing, BrowserStack for cross-device verification, and Lighthouse for performance auditing on slow networks.
- **Accessibility testing tools:** axe DevTools, WAVE, or Lighthouse accessibility audit. Test with actual screen readers (NVDA, VoiceOver) to verify the student experience for users with disabilities.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:
- **Role-based view design:** Can you evaluate whether a platform correctly shows different interfaces to students, teachers, parents, and admins based on their role?
- **Progressive disclosure:** Can you identify when an EdTech interface overwhelms new users with features they don't need yet instead of revealing complexity gradually?
- **Device compatibility:** Can you assess whether a learning platform works on Chromebooks, tablets, and phones — not just the developer's MacBook?
- **Educational accessibility:** Can you identify when an interface fails accessibility requirements that are legally mandated for educational technology?
- **Course content structure:** Can you evaluate whether course content is displayed with proper pedagogical structure — sequenced lessons, due dates, progress tracking — or dumped as a flat list?
- **Grade book usability:** Can you assess whether a grade book supports bulk operations, weighted categories, and data export that teachers actually need?
- **Navigation and information architecture:** Can you verify that each user role can reach their most-used features within two clicks from their dashboard?
- **Performance on constrained devices:** Can you diagnose when a learning platform loads too slowly on school networks and identify the bottleneck?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Building one dashboard and showing it to all user types. A student seeing admin controls is confusing. A teacher seeing the student view is useless. Role-based views aren't a nice-to-have — they're the baseline. Designing for the developer's MacBook Pro instead of a student's Chromebook. If your platform doesn't work on a 4-year-old Chromebook with a school network, it doesn't work for half your users. Skipping accessibility because AI doesn't add it by default. Educational platforms have legal accessibility requirements. Missing alt text, broken keyboard navigation, or insufficient color contrast isn't just bad design — it's a compliance failure. Building a course interface that looks like a social media feed instead of a structured learning path. Courses have sequences, prerequisites, and completion requirements. A chronological feed doesn't communicate academic structure. Not testing the grade book with realistic class sizes. It works with 5 test students. Does it work with 35? Does bulk grading still feel fast? Does scrolling through a semester of assignments stay responsive? Forgetting the parent view entirely. Parents are a primary stakeholder in K-12 education. If they can't see their child's grades and assignments without creating their own account and learning a new interface, the platform loses a key advocacy group.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. Does your platform show different interfaces to students, teachers, parents, and admins based on their authenticated role? Can a brand new student find their next assignment within 10 seconds of logging in? Does your platform load and function correctly on a Chromebook with limited bandwidth? Have you tested accessibility with a screen reader — not just an automated checker? Is your course content displayed with pedagogical structure (sequenced, with progress tracking) rather than as a flat list? Can a teacher grade an entire class on one assignment in a single view? Can a parent see their child's current grades, upcoming assignments, and attendance without navigating more than two screens?

## AI Audit Prompt Template

> Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my education platform's frontend and check the following. For each one, tell me pass or fail with a specific example: Role-based views: Does the interface change appropriately for students, teachers, parents, and administrators? Device compatibility: Does the platform work correctly on a Chromebook at 375px width with slow network throttling? Accessibility: Does the platform meet Section 508 requirements — screen reader compatible, keyboard navigable, sufficient contrast?

> Course structure: Is content displayed with proper sequence, due dates, and progress indicators?

> Grade book: Can a teacher bulk-grade, filter by assignment, and export grades in a single workflow?

> Parent portal: Can a parent view their child's progress in under 3 clicks? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 1 exam. The best way to prepare: build a role-based education dashboard. Create four views — student, teacher, parent, admin — for the same course. Test it on a Chromebook. Run an accessibility audit. Every gap you find between roles is exactly what the exam tests.

## Certification Pathway
- **Industry Specialist — Education/EdTech:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

Ready? Take the Student & Teacher Portals Exam →
