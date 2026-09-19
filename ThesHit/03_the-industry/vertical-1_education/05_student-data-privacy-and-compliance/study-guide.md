# Module 5: Student Data Privacy & Compliance — Study Guide

## Module 5: Student Data Privacy & Compliance

Security & RLS for Education Technology

This is the study guide. Everything for Student Data Privacy & Compliance is on this page — there's nothing to download.

———

## What This Module Covers

This module covers security and compliance as they apply specifically to education technology—the FERPA requirements, COPPA obligations, state-level student privacy laws, data minimization principles, breach notification procedures, and the contractual frameworks that school districts require before they'll let your platform near their student data. You already know security fundamentals from the CADE program. This goes deeper into **EdTech-specific requirements:** FERPA which governs who can access student education records, COPPA which protects children under 13 from data collection, state laws like California's SOPIPA and New York's Education Law 2-d which add requirements on top of federal law, and the Student Data Privacy Consortium's National Data Privacy Agreement which most districts now require vendors to sign.

## Why It Matters

EdTech vendors that mishandle student data don't get a warning—they get banned. School districts share vendor blacklists. A FERPA violation or data breach triggers mandatory notification to every affected family, potential loss of federal funding for the school, and immediate contract termination. In many states, the vendor faces direct penalties. Beyond the legal risk, student data privacy is a moral obligation. These are children's records. Their grades, behavior notes, disability accommodations, and personal information deserve the highest standard of protection. Building EdTech without understanding the regulatory landscape isn't just risky—it's irresponsible.

## Module Certification Goal

You can describe FERPA-compliant data handling, COPPA consent workflows, state-level privacy requirements, and breach notification procedures to an AI coding tool, evaluate the output for regulatory compliance across federal and state frameworks, and ship an EdTech product that school districts can approve through their data privacy review process.

## What You Need to Know

**FERPA fundamentals for EdTech vendors:** FERPA (Family Educational Rights and Privacy Act) protects student education records. As a vendor, you operate as a 'school official' under the district's FERPA obligations. This means you can only access student data for the purposes specified in your contract, you cannot share it with third parties, and you must return or delete it when the contract ends.

**COPPA and under-13 protections:** COPPA requires verified parental consent before collecting personal information from children under 13. For EdTech products used in schools, the school can consent on behalf of parents for educational use only—but this consent must be documented, and the data cannot be used for commercial purposes.

**State-level student privacy laws:** Many states add requirements beyond FERPA. California's SOPIPA prohibits using student data for advertising or building marketing profiles. New York's Ed Law 2-d requires a Data Privacy Agreement and a Parents' Bill of Rights. Illinois' SOPPA requires annual data collection transparency reports. Your platform must comply with every state where your customers operate.

**Data minimization and purpose limitation:** Collect only the student data you actually need. If your platform doesn't need a student's home address, don't collect it. If you collect assessment scores for grading, you can't repurpose that data for product analytics without consent. Every data point collected must have a documented educational purpose.

**Breach notification requirements:** If student data is exposed, you must notify the district within the timeframe specified in your contract (often 24-72 hours). The district then notifies affected families. Some states require direct vendor notification to parents. Your incident response plan must include education-specific breach notification procedures.

## Your Toolkit

**AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code—describe your data handling policies, encryption requirements, and compliance controls to it.

**Student Data Privacy Agreement templates:** The Student Data Privacy Consortium's NDPA (National Data Privacy Agreement) is the standard framework. Review it to understand what districts will require.

**Data inventory tool:** A spreadsheet or database documenting every student data element you collect, why you collect it, where it's stored, who can access it, and when it's deleted.

**Encryption verification:** Tools to verify encryption at rest (database-level) and in transit (TLS). Student data must be encrypted in both states.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

**FERPA vendor obligations:** Can you evaluate whether your platform's data handling meets FERPA requirements for a school official designation?

**COPPA consent workflows:** Can you assess whether parental consent is properly collected, documented, and revocable for students under 13?

**State law compliance:** Can you identify when a platform's data practices violate state-specific student privacy laws beyond FERPA?

**Data minimization:** Can you evaluate whether a platform collects only the student data necessary for its educational purpose?

**Breach notification readiness:** Can you assess whether the team has a documented breach response plan with education-specific notification timelines?

**Third-party data sharing:** Can you identify when student data is being shared with analytics providers, advertising networks, or other third parties in violation of FERPA?

**Data retention and deletion:** Can you evaluate whether student data is retained only for the contractually specified period and properly deleted when the contract ends?

**Encryption and access controls:** Can you verify that student data is encrypted at rest and in transit with access limited to authorized personnel?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment—they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Using student data for product analytics without consent. FERPA limits data use to the educational purposes specified in your contract. Using student performance data to improve your algorithm is a gray area that many districts explicitly prohibit. Embedding third-party tracking scripts (Google Analytics, Mixpanel, Hotjar) on pages that display student data. These scripts can transmit student information to third parties—a FERPA and COPPA violation. Use privacy-respecting analytics or exclude student-facing pages from tracking. Not having a breach notification plan before you need it. When a breach occurs, you have 24-72 hours to notify the district. If you're figuring out your response plan during the crisis, you'll miss the window. Assuming FERPA is the only law you need to follow. State laws add requirements. California, New York, Illinois, Colorado, and many other states have their own student privacy statutes. Your platform must comply with all of them. Keeping student data after a district contract ends. When a contract terminates, the district's data must be returned or deleted within the specified timeframe. Keeping it 'just in case' is a compliance violation. Not maintaining a data inventory. If you can't document what student data you collect, where it's stored, and who can access it, you can't pass a district's data privacy review. Districts ask these questions before signing contracts.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. Can you document every student data element your platform collects, its educational purpose, and where it's stored? Does your platform limit student data use to the purposes specified in your district contracts? Are third-party tracking scripts excluded from pages that display student information? Do you have a documented breach notification plan with education-specific timelines? Does your platform comply with state-level student privacy laws beyond FERPA? Is student data encrypted at rest and in transit? When a district contract ends, do you have a documented process for returning or deleting their student data?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my EdTech platform's data privacy and compliance posture and check the following. For each one, tell me pass or fail with a specific example: FERPA compliance: Is student data use limited to the educational purposes specified in district contracts? Third-party exposure: Are analytics scripts excluded from pages displaying student data? Data minimization: Does the platform collect only the student data necessary for its educational function? Breach readiness: Is there a documented breach notification plan with 24-72 hour notification timelines? Encryption: Is student data encrypted at rest and in transit? Data inventory: Can you produce a complete inventory of all student data elements, their purposes, and storage locations? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 5 exam. The best way to prepare: create a data inventory for your platform. Document every student data element, its purpose, and where it's stored. Review the NDPA template. Check whether your platform uses third-party scripts on student-facing pages. Every compliance gap you find is exactly what the exam tests.

## Certification Pathway

**Industry Specialist — Education/EdTech:** Pass all 7 module exams in this course

**CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges

**CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush—take the time to build something real first.

MATT MURPHY .AI © 2026 Matt Murphy .AI. All rights reserved.

———

Ready? Take the Student Data Privacy & Compliance Exam →
