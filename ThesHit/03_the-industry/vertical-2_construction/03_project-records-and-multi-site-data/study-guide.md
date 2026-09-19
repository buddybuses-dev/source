# Module 3: Project Records & Multi-Site Data — Study Guide

## Module 3: Project Records & Multi-Site Data

Database & Storage for Construction Technology

*Tier 5 — The Industry • Construction Technology*

———

## What This Module Covers

This module covers database architecture for construction technology—the project data models, multi-site tenancy patterns, job costing schemas, materials tracking, subcontractor relationship data, and document storage for permits, blueprints, and inspection records that form the data backbone of a construction platform. Construction projects generate enormous amounts of structured and unstructured data. A single commercial project may produce thousands of daily reports, tens of thousands of photos, hundreds of RFIs and submittals, dozens of change orders, and years of financial transactions. Your database must organize this data by project, make it searchable across projects for portfolio reporting, and retain it for years after project completion for warranty claims and litigation support. Multi-site data isolation is critical. A general contractor managing 15 active projects needs each project's data isolated for financial reporting, but aggregated for company performance dashboards. Subcontractors working on multiple projects for the same GC should see only the projects they're assigned to.

## Why It Matters

Construction litigation can surface 7 to 10 years after project completion. Daily reports, photos, RFIs, inspection records, and change orders are legal documents that must be retained and retrievable. A database that loses project data after completion or can't produce a daily report from 2019 puts the contractor at legal risk. Job costing—tracking actual costs against estimated costs by cost code—is how contractors know if they're making money. If the database can't break down costs by division, by phase, by subcontractor, and by cost code, the contractor is flying blind on the most important metric in their business.

## Module Certification Goal

You can describe construction-specific database schemas to an AI coding tool—project data models, multi-site isolation, job costing structures, document storage, and long-term retention policies—evaluate the output for data integrity and retrieval speed, and ship a database architecture that serves active construction projects and retains records for years of post-completion needs.

## What You Need to Know

**Project-centric data modeling:** In construction, the project is the primary organizing entity. Every record—daily reports, RFIs, submittals, change orders, photos, timecards, safety incidents—belongs to a project. Your schema must make project the top-level foreign key with cascading relationships to every document type.

**Multi-site isolation and portfolio reporting:** A GC's active projects must be isolated for financial and access control purposes. Project A's costs don't bleed into Project B's reports. But the company also needs portfolio-level views: total committed costs across all projects, company-wide safety incident rates, and labor utilization across crews. Your schema supports both isolation and aggregation.

**Job costing and cost code structures:** Job costing tracks actual expenditures against budget by cost code. The CSI MasterFormat (Division 1-49) is the standard cost code system. Each expenditure is coded to a division, phase, and cost type (labor, material, equipment, subcontractor). Your schema must support multi-level cost code hierarchies with rollup reporting at every level.

**Document and file storage:** Construction generates massive document volumes: blueprint PDFs (50-200MB each), daily photos (hundreds per project), submittals, RFIs, permits, inspection reports. These need structured metadata (project, date, type, status, author) and must be retrievable by any combination of filters. Object storage with database metadata indexing is the standard pattern.

**Long-term retention and archival:** Construction records must be retained for 7-10 years minimum for warranty claims, insurance disputes, and litigation. Completed projects should be archived to cold storage but remain queryable. Your retention policy must balance storage costs with legal obligations and business needs.

## Your Toolkit

**AI coding tool (pick one):** Cursor, Lovable, Bolt, Claude Code—describe your project schemas, cost code structures, and document storage requirements to it.

**Object storage:** AWS S3, Cloudflare R2, or equivalent for blueprint PDFs, photos, and documents. Store files in object storage, metadata in your database.

**Cost code reference:** CSI MasterFormat division structure for standardized cost coding. Your schema should align with or map to this industry standard.

**Database migration tools:** Prisma Migrate, Drizzle, or raw SQL migrations for evolving your schema as project data requirements grow.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

**Project-centric schema design:** Can you evaluate whether a construction database correctly organizes all records under a project hierarchy with proper foreign keys?

**Multi-site data isolation:** Can you verify that project data is isolated for financial reporting while supporting portfolio-level aggregation?

**Job costing structure:** Can you assess whether cost code schemas support multi-level hierarchies with rollup calculations by division, phase, and type?

**Document storage architecture:** Can you evaluate whether large files are stored in object storage with structured metadata in the database for filtered retrieval?

**Retention and archival:** Can you verify that completed project data is archived per retention policy and remains queryable for litigation and warranty needs?

**Subcontractor data scoping:** Can you assess whether subcontractors see only the projects they're assigned to and not the full project portfolio?

**Photo and media management:** Can you evaluate whether field photos include metadata like timestamp, GPS coordinates, project association, and categorization?

**Performance at scale:** Can you identify when queries against multi-year project data slow down and prescribe indexing strategies for construction volumes?

## Common Pitfalls

These are the mistakes vibecoders make most often in this area. No judgment—they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam. Organizing data by user instead of by project. In construction, projects are the primary entity. A user works on multiple projects. Daily reports, costs, and documents all belong to a project first, a user second. Not using standardized cost codes. Custom cost code schemes don't translate when a contractor needs to compare costs across projects or share data with owners, banks, or bonding companies who expect CSI MasterFormat divisions. Storing blueprint PDFs in the database. A 200MB blueprint PDF in a database row destroys query performance. Store files in object storage, keep metadata and references in the database. Deleting completed project data to save storage costs. Construction litigation surfaces years after completion. Deleted daily reports, photos, and RFIs that can't be produced in court create legal liability far exceeding storage costs. Not indexing document metadata for search. When a project manager needs 'all RFIs from February 2025 for the mechanical scope,' the query must be fast. Without indexes on project, date, type, and trade, these searches scan millions of records. Treating subcontractor data access like employee access. Subcontractors are external parties who should see only their assigned projects and scopes. Giving them the same data access as internal employees exposes competitive information.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on. Is every record in your database associated with a project as the primary organizing entity? Does your cost code structure align with CSI MasterFormat or an equivalent industry standard? Are large files stored in object storage with metadata indexed in the database? Can completed project data be retrieved 7+ years after project closeout? Are subcontractor users scoped to see only their assigned projects? Does your schema support portfolio-level aggregation across all active projects? Can you query all RFIs for a specific project, trade, and date range in under 2 seconds?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check. It checks the same things the certification exam covers. Review my construction platform's database architecture and check the following. For each one, tell me pass or fail with a specific example: Project hierarchy: Is every record organized under a project entity? Cost codes: Does the schema support standardized multi-level cost coding? **Document storage:** Are large files in object storage with metadata in the database? Retention: Can completed project data be retrieved years after closeout? Isolation: Are subcontractors scoped to only their assigned projects? Performance: Can common queries execute in under 2 seconds at scale? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer yes to the self-assessment checklist, you're ready for the Module 3 exam. The best way to prepare: build a project database with 3 projects, cost codes across 5 divisions, and 100 daily reports. Verify subcontractors can only see their projects. Query for RFIs by date range and trade. Every data model gap you find is exactly what the exam tests.

## Certification Pathway

**Industry Specialist — Construction:** Pass all 7 module exams in this course

**CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges

**CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush—take the time to build something real first.

MATT MURPHY .AI © 2026 Matt Murphy .AI. All rights reserved.
