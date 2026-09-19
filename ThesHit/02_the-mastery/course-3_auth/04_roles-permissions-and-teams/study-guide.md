# Module 4: Roles, Permissions and Teams — Study Guide

## T4 The Mastery | Authentication Systems Build

This is the study guide. Everything for Roles, Permissions and Teams is on this page — there's nothing to download.

## What This Module Covers

This module covers authorization: the system that decides, on every request, whether this specific identity may do this specific thing to this specific resource. You will learn the difference between roles and permissions, why every check must run on the server, how teams and workspaces create the boundaries multi-user apps live inside, what tenant isolation protects, and the audit trail that turns access from an assumption into a record.

## Why It Matters

Authentication got the user through the door. Authorization decides which rooms they can enter, and this is where AI-built apps fail most quietly. Your AI hides the delete button from non-admins and reports the feature secure. But the API behind the button still accepts the request, and any user with browser dev tools can send it. The interface is a courtesy; the server is the security. This module is also where your app becomes a business. Teams, workspaces, roles, invitations, seat billing: these structures let one app serve many companies at once. With many companies comes the catastrophic failure mode of multi-tenant software: data crossing tenants, one company's user reading another company's records. A single incident of that kind ends customer relationships and sometimes companies. The discipline that prevents it is not clever, it is consistent: default deny, check on the server, scope every check to the specific resource, and log every grant. Your AI will scatter permission checks across forty route handlers if you let it. You direct the consolidation, define the roles, and test the denials.

## Certification Goal

Passing the Module 4 exam proves you can direct an AI to build an authorization system that defaults to deny, enforces every check server-side and per-resource, models teams with owner, admin, and member roles, keeps tenants fully isolated, revokes access completely when members leave, and logs every permission change with who, whom, and when.

## What You Need to Know

**Roles versus permissions.** A permission is one allowed action. A role is a named bundle of permissions assigned to a user. Keep roles few and meaningful: when the team asks for fifteen roles matching job titles, model the differences as permissions instead. The org chart is not the security model.

**Server-side, per-resource, default deny.** Permission checks run on the server, on every protected action, because everything sent to clients can be altered. Checks are scoped to the resource: "can edit documents" still has to confirm this user may edit that particular document. Default deny means anything not explicitly granted is refused, so forgotten configuration fails closed. A new user starts with the minimum needed, with access granted deliberately. The full check on any request: who they are, what they are asking, and whether that identity may do it to that resource.

**Teams and the ownership model.** A team or workspace is a boundary that owns members, data, and roles, keeping collaboration inside its walls. The owner role controls the workspace's existence and riskiest actions: billing, deletion, transfer. The last owner cannot simply leave; the flow forces an explicit ownership transfer first, so the workspace never exists uncontrolled. Invitations are expiring, single-use tokens tied to the invited address, with the role set by the inviter.

**Complete revocation and instant effect.** Removing a member revokes everything they hold: live sessions, API keys, shares, and tokens, not just the roster entry. Permission changes take effect on the next request: a demoted admin whose open session still carries admin claims is a design failure. Seat-based billing stays truthful with the roles system: adds, removals, and role changes that affect seat counts reflect in billing.

**Tenant isolation and internal access.** The catastrophic authorization failure in a multi-tenant app is data crossing tenants. Every query, every check, every share carries the tenant boundary. Your own staff never become members of customer workspaces: support access is a separate, logged, time-limited internal path. If support needs impersonation, it ships with explicit logging, visible indication, time limits, and no dangerous actions while inside.

**Audit and testing.** Every permission and role change is logged with who, whom, and when, because when access is abused or disputed, the grant trail is the evidence you need. Testing authorization means attempting forbidden actions as each role, including direct API calls, and confirming denial. Scattered permission logic gets consolidated into one policy layer, because scattered checks drift and develop gaps.

## Your Toolkit

- **A permission matrix.** A simple table of roles against actions, built by directing AI, that becomes the single source of truth for what each role may do. It is your spec, your test plan, and your documentation in one artifact.
- **A central policy layer.** One place in the codebase where authorization decisions live, instead of checks scattered across forty route handlers. Direct your AI to consolidate early.
- **Role-based testing accounts.** One test account per role, plus scripted attempts at forbidden actions through the API directly. Denial is the pass condition.
- **An audit log for access changes.** Every grant, revocation, and role change recorded with actor, target, and timestamp. Sharing features get the same treatment: scoped, expiring, revocable link tokens.

## Exam Topics

The Module 4 exam will test you on:

1. What authorization answers on every request and how it differs from authentication
2. Roles versus permissions and keeping the role list small and meaningful
3. Server-side enforcement, per-resource checks, and why hidden buttons secure nothing
4. Default deny as a posture and minimal access for new users
5. Team models: owner powers, safe invitations, and forced ownership transfer
6. Complete revocation on removal and permission changes that bind on the next request
7. Tenant isolation, staff access paths, and impersonation guardrails
8. Audit logging, billing coordination, link sharing, and testing by attempting forbidden actions

## Common Pitfalls

- **Frontend-only enforcement.** Hiding the button while the API accepts the request is decoration. Enforce on the server; treat the client copy as convenience.
- **Role sprawl.** A role per job title collapses into an unauditable mess. Few roles, differences expressed as permissions.
- **General checks for specific resources.** "Can edit documents" is not "can edit document 4571." Scope every check to the resource.
- **Roster-only removal.** Deleting the membership row while sessions, API keys, and shares survive means the departed member never actually left.
- **Staff inside customer workspaces.** Support access through membership or borrowed owner credentials destroys the audit trail. Separate, logged, time-limited path only.
- **Untested denial.** Confirming that admins can do things proves nothing. Authorization is tested by proving what each role cannot do, including through direct API calls.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I define a role, a permission, and the relationship between them?
- [ ] Can I explain default deny and why configuration should fail closed?
- [ ] Can I state the full check that runs when a valid session hits my API?
- [ ] Can I list everything that must be revoked when a team member is removed?
- [ ] Can I describe the guardrails around staff access and impersonation?
- [ ] Can I explain why tenant isolation is the failure that matters most?
- [ ] Could I test an authorization system by attempting forbidden actions as each role?

## AI Audit Prompt Template

Use this prompt to audit your authorization system before trusting it:

> "You are an authorization security reviewer. Here is my app's permission model: [paste roles, permission matrix, team structure, and policy layer description]. Verify every check runs server-side and is scoped to the specific resource, the posture is default deny, permission logic is consolidated, member removal revokes sessions, keys, shares, and tokens, role changes bind on the next request, tenants are isolated in every query, staff access is a separate logged path, and access changes are audit logged. Then list the forbidden actions I should attempt as each role to prove denial, and flag the most likely cross-tenant leak."

## What's Next

Module 5 hardens the individual account: two-factor authentication, backup codes, step-up checks for dangerous actions, and the takeover signals that tell you an attacker is working an account. The admin roles you just defined are exactly the accounts that will need it most.

## Certification Pathway

This module is the fourth step in the Authentication Systems Build course, a paid T4 The Mastery course inside Builder Access, alongside the SaaS Build and Database Design courses. Pass all seven module exams to earn the Auth Build Specialist badge, which tells The Faction your multi-user apps keep every tenant's data where it belongs.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Roles, Permissions and Teams Exam →
