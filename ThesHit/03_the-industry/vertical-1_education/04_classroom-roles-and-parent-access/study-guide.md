# Module 4: Classroom Roles & Parent Access — Study Guide

## Auth & Permissions for Education Technology

This is the study guide. Everything for Classroom Roles & Parent Access is on this page — there's nothing to download.

## What This Module Covers

This module covers auth and permissions as they apply specifically to education technology—the role hierarchies, classroom-level permissions, guardian consent flows, and age-gated account creation that let your EdTech product serve the complex identity landscape of K-12 and higher education. You already know auth fundamentals from the CADE program. This goes deeper into EdTech-specific patterns: five or more user roles (student, teacher, parent/guardian, school admin, district admin) each with different data access rights, classroom-level scoping where a teacher sees only their students not the entire school, guardian linking where a parent account connects to one or more student accounts with consent verification, and age-gated onboarding where students under 13 require parental consent before account creation under COPPA.

## Why It Matters

Education has the most complex role hierarchy of any industry vertical. A teacher should see their 35 students but not the 600 other students in the school. A parent should see their child's grades but not any other student's. A school admin should see all students in their building but not students in other schools. A district admin should see everything in their district but nothing from neighboring districts. Getting these boundaries wrong isn't just a UX problem—it's a FERPA violation. COPPA adds another layer: students under 13 cannot create accounts or share personal information without verified parental consent. Your auth system must handle this before a single child uses the platform.

## Module Certification Goal

You can describe education-specific role hierarchies, classroom-level permission scoping, guardian consent workflows, and COPPA-compliant age verification to an AI coding tool, evaluate the output for proper data access boundaries at every role level, and ship an auth system that protects student data while giving each stakeholder exactly the access they need.

## What You Need to Know

- **Education role hierarchy:** EdTech platforms typically need at minimum: Student (sees own data), Teacher (sees their classroom's data), Parent/Guardian (sees linked child's data), School Admin (sees their school's data), District Admin (sees all schools in their district). Each level has additive visibility but the boundaries must be enforced at the database query level, not just the frontend.
- **Classroom-level scoping:** A teacher isn't granted access to 'all students'—they're granted access to students in their assigned sections. If Ms. Garcia teaches Period 2 Biology and Period 5 Chemistry, she sees those students and only those students. Section assignment is the permission boundary, not school-wide access.
- **Guardian-student linking:** Parents need accounts that are linked to their children's accounts. This linking must be verified—you can't let any adult claim to be any child's parent. Schools typically provide the linkage via SIS data (parent contact records), invitation codes from the school, or admin-verified requests.
- **COPPA compliance and age gating:** The Children's Online Privacy Protection Act requires verified parental consent before collecting personal information from children under 13. Your platform must verify age during account creation, block under-13 accounts until parent consent is obtained, and provide parents the ability to review and delete their child's data.
- **Delegated administration:** District admins often delegate user management to school admins, who delegate classroom management to teachers. Your permission system needs to support this chain of delegation without requiring district-level intervention for routine operations like resetting a student's password or adding a parent to a classroom.

## Your Toolkit

- **AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code—describe your role hierarchy, classroom scoping, and guardian workflows to it.
- **Auth provider with custom claims:** Clerk, Auth0, or Supabase Auth. You'll need custom claims for role, school_id, district_id, and section assignments.
- **Test account matrix:** Create test accounts for every role (student, teacher, parent, school admin, district admin) and verify each one sees only the data they should.
- **Consent management platform:** A workflow for collecting, storing, and revoking parental consent. This can be built custom or integrated with a consent management service.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- **Role hierarchy enforcement:** Can you evaluate whether each role—student, teacher, parent, school admin, district admin—sees only the data appropriate to their level?
- **Classroom-level scoping:** Can you verify that a teacher sees only students in their assigned sections, not every student in the school?
- **Guardian-student linking:** Can you assess whether parent accounts are properly linked to student accounts with verified authorization from the school?
- **COPPA compliance:** Can you identify whether the platform correctly handles age verification and parental consent for students under 13?
- **Delegated administration:** Can you evaluate whether school admins can manage their building's users without requiring district-level intervention?
- **Permission boundary testing:** Can you catch when a role can access data outside its intended boundary—a teacher seeing another teacher's students, a parent seeing another child?
- **Session and token handling:** Can you assess whether role changes (teacher moves to a new school, student transfers) are reflected in active sessions immediately?
- **Account deprovisioning:** Can you evaluate what happens when a student graduates, a teacher leaves, or a parent's custody arrangement changes?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment—they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Giving teachers school-wide access instead of classroom-level access. A teacher should see their sections, not every student in the building. School-wide access is for administrators. Allowing any adult to self-link to any student account. Guardian-student linking must be verified through the school—a parent should not be able to claim a child who isn't theirs by simply knowing the student's name. Skipping COPPA compliance for students under 13. If your platform collects any personal information from children under 13 without verified parental consent, you're in violation of federal law. This isn't optional. Using a flat two-role system (admin/user) for an education platform. EdTech needs five or more distinct roles. Cramming teacher, parent, and student into 'user' means you can't enforce proper data boundaries. Not handling custody complexities. Divorced parents may both need access. A court order may restrict one parent's access. Your system needs to support these real-world scenarios without a full engineering escalation each time. Forgetting to deprovision accounts when students graduate or teachers leave. Graduated students who retain platform access can see current student data. Former teachers who aren't deprovisioned retain access to student records.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

Does your platform enforce five distinct role levels: student, teacher, parent, school admin, and district admin? Are teacher permissions scoped to their assigned classroom sections only? Are parent-student linkages verified through the school rather than self-asserted? Does your account creation flow handle COPPA age verification and parental consent for students under 13? Can school admins manage their building's users without district-level intervention? When a student transfers or a teacher leaves, is their access revoked from active sessions immediately? Have you tested every role's data access to confirm proper boundaries?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my EdTech platform's auth and permissions system and check the following. For each one, tell me pass or fail with a specific example: Role hierarchy: Are five distinct roles enforced with appropriate data boundaries? Classroom scoping: Can a teacher only see students in their assigned sections? Guardian linking: Are parent accounts verified through the school before linking to student accounts? COPPA compliance: Is parental consent collected and verified before under-13 students can use the platform? Delegated admin: Can school admins manage users without district intervention? Deprovisioning: Are graduated students and departing teachers removed from active access? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 4 exam. The best way to prepare: build a permission system with five roles. Create two teachers, each with different sections. Verify Teacher A can't see Teacher B's students. Link a parent to a student and verify the parent can only see that child. Every boundary gap you find is exactly what the exam tests.

## Certification Pathway

- **Industry Specialist — Education/EdTech:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush—take the time to build something real first.

———

Ready? Take the Classroom Roles & Parent Access Exam →
