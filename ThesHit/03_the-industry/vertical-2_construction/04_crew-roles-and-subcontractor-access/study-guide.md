# Module 4: Crew Roles & Subcontractor Access — Study Guide

## Module 4: Crew Roles & Subcontractor Access

Auth & Permissions for Construction Technology

This is the study guide. Everything for Crew Roles & Subcontractor Access is on this page — there's nothing to download.

———

## What This Module Covers

This module covers auth and permissions as they apply specifically to construction technology—the role hierarchies between general contractors, subcontractors, owners, and inspectors, the project-level permission scoping that controls who sees what on each job, the field worker access patterns on shared job site devices, and the subcontractor portal access controls that protect competitive information. Construction has a unique identity challenge: the people using your platform don't all work for the same company. A general contractor, 15 subcontractors, the project owner, the architect, and the building inspector all need access to the same project but with radically different visibility and permissions. The electrician shouldn't see the plumber's contract price. The owner shouldn't edit the schedule. The inspector should see everything but change nothing.

## Why It Matters

In construction, data visibility is competitive intelligence. If a subcontractor sees what other subs bid for their trade, it affects future pricing. If an owner sees the GC's cost breakdown with markup percentages, it affects negotiations. If a field worker on a shared tablet can access admin functions, it creates data integrity risks. Construction permissions aren't just about security—they're about business relationships. Getting them wrong doesn't just expose data. It damages trust between the parties who must collaborate to build the project.

## Module Certification Goal

You can describe construction-specific role hierarchies and permission models to an AI coding tool—GC, subcontractor, owner, inspector roles with project-level scoping and competitive information protection—evaluate the output for proper data boundaries, and ship an auth system that protects business relationships while enabling the collaboration construction requires.

## What You Need to Know

**Construction role hierarchy:** The standard hierarchy: Company Admin (manages all projects and users), Project Manager (manages one or more projects), Superintendent (manages daily field operations on a project), Foreman (manages a specific crew), Field Worker (enters time and daily data). External roles: Subcontractor (sees their scope only), Owner (sees progress and budget), Architect (sees RFIs and submittals), Inspector (sees inspection items, read-only).

**Project-level permission scoping:** Users are assigned to projects, not given platform-wide access. A superintendent on Project A has no visibility into Project B unless explicitly assigned. This is different from school-based EdTech where teachers see their whole school—in construction, each project is an independent permission boundary.

**Subcontractor portal and competitive isolation:** Subcontractors need to see their scope of work, their schedule, their payments, and documents relevant to their trade. They must NOT see other subcontractors' pricing, the GC's markup, or scopes of work outside their trade. This competitive isolation is fundamental to construction business relationships.

**Shared device authentication:** Field workers often share tablets at job site trailers. Your auth system must support quick user switching without requiring full login/logout cycles. PIN-based access, badge scanning, or simplified login flows let workers switch identities on a shared device without seeing each other's data.

**Inspector and owner read-only access:** Building inspectors and project owners need visibility but should never modify project data. An inspector who can edit an inspection result or an owner who can change the schedule creates data integrity issues. These roles need comprehensive read access with zero write permissions.

## Your Toolkit

**AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code—describe your role hierarchy, project scoping, and subcontractor isolation requirements to it.

**Auth provider with custom claims:** Clerk, Auth0, or Supabase Auth with custom claims for role, company_id, and project assignments.

**Role testing matrix:** A spreadsheet mapping every role to every feature with expected access level (full, read-only, none) that you test against.

**Shared device testing:** A tablet at your desk that you use to test the quick-switch authentication flow between multiple user accounts.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

**Role hierarchy design:** Can you evaluate whether a construction platform correctly implements roles from company admin through field worker with appropriate permission levels?

**Project-level scoping:** Can you verify that users only see data from projects they're explicitly assigned to and cannot access other projects?

**Subcontractor competitive isolation:** Can you assess whether subcontractors are prevented from seeing other subs' pricing, the GC's markup, or scopes outside their trade?

**Shared device authentication:** Can you evaluate whether field workers can switch users on shared devices quickly without exposing the previous user's data?

**Owner and inspector read-only:** Can you verify that owners and inspectors have comprehensive read access but zero write or edit permissions on project data?

**Cross-company data boundaries:** Can you assess whether companies working on the same project are properly isolated so each sees only what they should?

**Invitation and onboarding flow:** Can you evaluate whether subcontractors and external parties can be invited to specific projects with pre-configured role permissions?

**Access revocation:** Can you verify that when a subcontractor's contract ends, their project access is revoked promptly without affecting other active projects?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment—they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Giving subcontractors the same access level as internal employees. Subcontractors are external parties with limited scope. They should never see other trades' pricing, the GC's internal costs, or projects they're not working on. Using platform-wide roles instead of project-level assignments. A superintendent on Project A should not have any access to Project B. Every permission should be scoped to a specific project assignment. Not protecting the GC's markup from owner visibility. The GC's profit margin is competitive information. An owner who sees the cost breakdown with markup percentages will negotiate harder on the next project. Requiring full login/logout on shared job site tablets. If switching users takes 60 seconds with email and password, field workers will share one login. Quick-switch authentication (PIN, badge) preserves individual accountability. Giving inspectors edit access because they need to mark inspections as passed or failed. Create a dedicated inspection workflow where inspectors submit results through a controlled form, not by editing project records directly. Not revoking subcontractor access when their contract is complete. A subcontractor who finished electrical work 3 months ago should not still have access to the project's current schedule, costs, and documents.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. **Does your platform implement at minimum 6 distinct roles:** admin, PM, superintendent, foreman, subcontractor, and owner? Are all user permissions scoped to specific project assignments, not platform-wide? Can subcontractors see only their own scope, schedule, and payment status without visibility into other trades' pricing? Can field workers switch users on shared tablets in under 10 seconds? Are owner and inspector roles strictly read-only with no edit capabilities? When a subcontractor's contract is complete, is their project access revoked? Have you tested every role against every feature to verify proper access boundaries?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my construction platform's auth and permissions and check the following. For each one, tell me pass or fail with a specific example: Role hierarchy: Are 6+ distinct roles implemented with appropriate permissions? Project scoping: Are all permissions scoped to specific project assignments? Subcontractor isolation: Can subs only see their own scope and pricing? Shared devices: Can field workers switch users quickly and securely? Read-only roles: Are owners and inspectors prevented from editing data? Access revocation: Is access removed when a sub's contract ends? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 4 exam. The best way to prepare: create test accounts for every role. Log in as a subcontractor and try to see another sub's pricing. Log in as an owner and try to edit the schedule. Test quick-switch on a shared tablet. Every boundary gap you find is exactly what the exam tests.

## Certification Pathway

**Industry Specialist — Construction:** Pass all 7 module exams in this course

**CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges

**CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush—take the time to build something real first.

MATT MURPHY .AI © 2026 Matt Murphy .AI. All rights reserved.

———

Ready? Take the Crew Roles & Subcontractor Access Exam →
