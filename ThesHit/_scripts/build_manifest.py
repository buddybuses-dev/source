import re, json, os

def slugify(title):
    t = title
    t = t.replace('\u2014', ' ')  # em dash
    for ch in [':', ',', '.', '&', "'", '\u2019']:
        t = t.replace(ch, '')
    t = re.sub(r'\s+', ' ', t).strip().lower()
    t = t.replace(' ', '-')
    t = re.sub(r'-+', '-', t)
    return t

ROOT = "C:/Users/Mizgin2/ThesHit"

entries = []

# ---------------- 02_the-mastery ----------------
mastery_courses = [
 ("course-1_platform-mastery-saas", [
    ("01_saas-dashboard-and-data-layer","Module 01: SaaS Dashboard \u2014 Study Guide"),
    ("02_subscription-endpoints-and-webhooks","Module 02: Subscription Endpoints & Webhooks \u2014 Study Guide"),
    ("03_multi-tenant-data-architecture","Module 03: Multi-Tenant Data Architecture \u2014 Study Guide"),
    ("04_users-teams-and-rbac","Module 04: Users, Teams & RBAC \u2014 Study Guide"),
    ("05_saas-deployment-pipelines","Module 05: SaaS Deployment Pipelines \u2014 Study Guide"),
    ("06_api-throttling-and-usage-metering","Module 06: API Throttling & Usage Metering \u2014 Study Guide"),
    ("07_production-monitoring-for-saas","Module 07: Production Monitoring for SaaS \u2014 Study Guide"),
 ]),
 ("course-2_databases", [
    ("01_data-modeling-fundamentals","Module 1: Data Modeling Fundamentals \u2014 Study Guide"),
    ("02_relationships-and-normalization-decisions","Module 2: Relationships and Normalization Decisions \u2014 Study Guide"),
    ("03_indexes-and-query-performance","Module 3: Indexes and Query Performance \u2014 Study Guide"),
    ("04_migrations-without-downtime","Module 4: Migrations Without Downtime \u2014 Study Guide"),
    ("05_seeding-backups-and-restores","Module 5: Seeding, Backups and Restores \u2014 Study Guide"),
    ("06_scaling-and-read-replicas","Module 6: Scaling and Read Replicas \u2014 Study Guide"),
    ("07_ship-production-database","Module 7: Ship: Production Database \u2014 Study Guide"),
 ]),
 ("course-3_auth", [
    ("01_auth-architecture-and-session-models","Module 1: Auth Architecture and Session Models \u2014 Study Guide"),
    ("02_email-password-and-magic-links","Module 2: Email, Password and Magic Links \u2014 Study Guide"),
    ("03_social-and-sso-logins","Module 3: Social and SSO Logins \u2014 Study Guide"),
    ("04_roles-permissions-and-teams","Module 4: Roles, Permissions and Teams \u2014 Study Guide"),
    ("05_two-factor-and-account-security","Module 5: Two-Factor and Account Security \u2014 Study Guide"),
    ("06_password-reset-and-edge-cases","Module 6: Password Reset and Edge Cases \u2014 Study Guide"),
    ("07_ship-production-auth","Module 7: Ship: Production Auth \u2014 Study Guide"),
 ]),
 ("course-4_nextjs", [
    ("01_next-js-architecture-and-routing","Module 1: Next.js Architecture and Routing \u2014 Study Guide"),
    ("02_server-and-client-components","Module 2: Server and Client Components \u2014 Study Guide"),
    ("03_data-fetching-and-caching","Module 3: Data Fetching and Caching \u2014 Study Guide"),
    ("04_api-routes-and-server-actions","Module 4: API Routes and Server Actions \u2014 Study Guide"),
    ("05_seo-metadata-and-performance","Module 5: SEO Metadata and Performance \u2014 Study Guide"),
    ("06_vercel-deployment-and-environments","Module 6: Vercel Deployment and Environments \u2014 Study Guide"),
    ("07_ship-production-next-js-app","Module 7: Ship: Production Next.js App \u2014 Study Guide"),
 ]),
 ("course-5_supabase", [
    ("01_supabase-architecture-and-project-setup","Module 1: Supabase Architecture and Project Setup \u2014 Study Guide"),
    ("02_postgres-tables-and-relationships","Module 2: Postgres Tables and Relationships \u2014 Study Guide"),
    ("03_row-level-security-policies","Module 3: Row-Level Security Policies \u2014 Study Guide"),
    ("04_auth-and-user-management","Module 4: Auth and User Management \u2014 Study Guide"),
    ("05_storage-realtime-and-edge-functions","Module 5: Storage Realtime and Edge Functions \u2014 Study Guide"),
    ("06_backups-and-environments","Module 6: Backups and Environments \u2014 Study Guide"),
    ("07_ship-production-backend","Module 7: Ship: Production Backend \u2014 Study Guide"),
 ]),
 ("course-6_payments-stripe", [
    ("01_payments-architecture-and-account-setup","Module 1: Payments Architecture and Account Setup \u2014 Study Guide"),
    ("02_one-time-checkout-flows","Module 2: One-Time Checkout Flows \u2014 Study Guide"),
    ("03_subscriptions-and-billing-portal","Module 3: Subscriptions and Billing Portal \u2014 Study Guide"),
    ("04_webhooks-and-payment-state","Module 4: Webhooks and Payment State \u2014 Study Guide"),
    ("05_invoices-taxes-and-receipts","Module 5: Invoices, Taxes and Receipts \u2014 Study Guide"),
    ("06_failed-payments-and-dunning","Module 6: Failed Payments and Dunning \u2014 Study Guide"),
    ("07_ship-live-payment-system","Module 7: Ship: Live Payment System \u2014 Study Guide"),
 ]),
 ("course-7_apis-as-products", [
    ("01_api-architecture-and-endpoint-design","Module 1: API Architecture and Endpoint Design \u2014 Study Guide"),
    ("02_auth-keys-and-rate-limiting","Module 2: Auth Keys and Rate Limiting \u2014 Study Guide"),
    ("03_documentation-and-developer-experience","Module 3: Documentation and Developer Experience \u2014 Study Guide"),
    ("04_usage-metering-and-billing","Module 4: Usage Metering and Billing \u2014 Study Guide"),
    ("05_versioning-and-error-design","Module 5: Versioning and Error Design \u2014 Study Guide"),
    ("06_monitoring-and-uptime","Module 6: Monitoring and Uptime \u2014 Study Guide"),
    ("07_ship-live-api-product","Module 7: Ship: Live API Product \u2014 Study Guide"),
 ]),
]
for course_dir, mods in mastery_courses:
    for mod_dir, title in mods:
        entries.append((f"02_the-mastery/{course_dir}/{mod_dir}", "the-mastery", title))

# ---------------- 03_the-industry (only missing ones) ----------------
industry = [
 ("vertical-1_education", [
    ("04_classroom-roles-and-parent-access","Module 4: Classroom Roles & Parent Access \u2014 Study Guide"),
    ("05_student-data-privacy-and-compliance","Module 5: Student Data Privacy & Compliance \u2014 Study Guide"),
    ("06_course-content-delivery-and-media","Module 6: Course Content Delivery & Media \u2014 Study Guide"),
    ("07_assessment-resilience-and-academic-continuity","Module 7: Assessment Resilience & Academic Continuity \u2014 Study Guide"),
 ]),
 ("vertical-2_construction", [
    ("01_contractor-and-project-dashboards","Module 1: Contractor & Project Dashboards \u2014 Study Guide"),
    ("02_estimating-and-bidding-apis","Module 2: Estimating & Bidding APIs \u2014 Study Guide"),
    ("03_project-records-and-multi-site-data","Module 3: Project Records & Multi-Site Data \u2014 Study Guide"),
    ("04_crew-roles-and-subcontractor-access","Module 4: Crew Roles & Subcontractor Access \u2014 Study Guide"),
    ("05_job-site-safety-and-compliance-data","Module 5: Job Site Safety & Compliance Data \u2014 Study Guide"),
    ("06_blueprint-and-document-delivery","Module 6: Blueprint & Document Delivery \u2014 Study Guide"),
    ("07_project-continuity-and-disaster-recovery","Module 7: Project Continuity & Disaster Recovery \u2014 Study Guide"),
 ]),
 ("vertical-3_healthcare", [
    ("01_the-clinical-practice-workflow-map","Module 1: The Clinical Practice Workflow Map \u2014 Study Guide"),
    ("02_patient-intake-and-forms","Module 2: Patient Intake and Forms \u2014 Study Guide"),
    ("03_scheduling-and-reminder-systems","Module 3: Scheduling and Reminder Systems \u2014 Study Guide"),
    ("04_hipaa-boundaries-for-builders","Module 4: HIPAA Boundaries For Builders \u2014 Study Guide"),
    ("05_billing-and-insurance-admin-tools","Module 5: Billing and Insurance Admin Tools \u2014 Study Guide"),
    ("06_patient-communication-systems","Module 6: Patient Communication Systems \u2014 Study Guide"),
    ("07_ship-practice-admin-toolkit","Module 7: Ship: Practice Admin Toolkit \u2014 Study Guide"),
 ]),
]
for vert_dir, mods in industry:
    for mod_dir, title in mods:
        entries.append((f"03_the-industry/{vert_dir}/{mod_dir}", "the-industry", title))

# ---------------- 04_the-vault (only missing: course-3 02-07) ----------------
vault_c3 = [
    ("02_the-13-layer-audit-framework","Module 2: The 13-Layer Audit Framework \u2014 Study Guide"),
    ("03_automated-scanning-direction","Module 3: Automated Scanning Direction \u2014 Study Guide"),
    ("04_manual-review-hotspots","Module 4: Manual Review Hotspots \u2014 Study Guide"),
    ("05_findings-severity-and-reporting","Module 5: Findings, Severity and Reporting \u2014 Study Guide"),
    ("06_remediation-sprints","Module 6: Remediation Sprints \u2014 Study Guide"),
    ("07_ship-complete-codebase-audit","Module 7: Ship: Complete Codebase Audit \u2014 Study Guide"),
]
for mod_dir, title in vault_c3:
    entries.append((f"04_the-vault/course-3_ai-code-auditing/{mod_dir}", "the-vault", title))

# ---------------- 05_the-launchpad (missing: course-2 m07, course-3 all) ----------------
entries.append(("05_the-launchpad/course-2_idea-validation/07_ship-your-validated-idea-brief", "the-launchpad", "Module 7: Ship: Your Validated Idea Brief \u2014 Study Guide"))
launchpad_c3 = [
    ("01_why-positioning-beats-marketing","Module 1: Why Positioning Beats Marketing \u2014 Study Guide"),
    ("02_finding-your-positioning-sweet-spot","Module 2: Finding Your Positioning Sweet Spot \u2014 Study Guide"),
    ("03_designing-your-offer","Module 3: Designing Your Offer \u2014 Study Guide"),
    ("04_articulating-your-value-proposition","Module 4: Articulating Your Value Proposition \u2014 Study Guide"),
    ("05_competitive-differentiation","Module 5: Competitive Differentiation \u2014 Study Guide"),
    ("06_testing-and-refining-your-position","Module 6: Testing and Refining Your Position \u2014 Study Guide"),
    ("07_ship-your-positioning-package","Module 7: Ship: Your Positioning Package \u2014 Study Guide"),
]
for mod_dir, title in launchpad_c3:
    entries.append((f"05_the-launchpad/course-3_positioning-and-offers/{mod_dir}", "the-launchpad", title))

# ---------------- 06_the-frontier (missing: course-2 m06-07, course-3 all) ----------------
entries.append(("06_the-frontier/course-2_prompt-engineering/06_production-prompt-patterns", "the-frontier", "Module 6: Production Prompt Patterns \u2014 Study Guide"))
entries.append(("06_the-frontier/course-2_prompt-engineering/07_ship-professional-prompt-architecture", "the-frontier", "Module 7: Ship: Professional Prompt Architecture \u2014 Study Guide"))
frontier_c3 = [
    ("01_what-context-engineering-is","Module 1: What Context Engineering Is \u2014 Study Guide"),
    ("02_context-window-architecture","Module 2: Context Window Architecture \u2014 Study Guide"),
    ("03_information-retrieval-and-selection","Module 3: Information Retrieval and Selection \u2014 Study Guide"),
    ("04_memory-and-conversation-design","Module 4: Memory and Conversation Design \u2014 Study Guide"),
    ("05_dynamic-context-assembly","Module 5: Dynamic Context Assembly \u2014 Study Guide"),
    ("06_context-quality-and-debugging","Module 6: Context Quality and Debugging \u2014 Study Guide"),
    ("07_ship-production-context-system","Module 7: Ship: Production Context System \u2014 Study Guide"),
]
for mod_dir, title in frontier_c3:
    entries.append((f"06_the-frontier/course-3_context-engineering/{mod_dir}", "the-frontier", title))

manifest = []
for local_dir, space_slug, title in entries:
    slug = slugify(title)
    url = f"https://the-faction.mn.co/posts/{space_slug}-{slug}"
    manifest.append({"dir": local_dir, "title": title, "url": url, "status": "pending"})

print(f"Total entries: {len(manifest)}")
with open(os.path.join(ROOT, "_scripts", "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
