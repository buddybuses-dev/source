# Module 2: Patient Intake and Forms — Study Guide

## T5 The Industry | Healthcare Practice AI Engineering

This is the study guide. Everything for Patient Intake and Forms is on this page — there's nothing to download.

## What This Module Covers

This module teaches you to direct AI to build digital patient intake systems: demographics, medical history, insurance capture, consent forms, and pre-visit questionnaires. You will learn what data a practice actually needs, when to collect it, and how to design mobile-first intake that patients complete before they ever hit the waiting room.

## Why It Matters

Intake is the single most visible pain point in practice operations, and it is where most builders get their first paid healthcare project. Walk into a family medicine office at 8 a.m. and watch: patients hunched over clipboards, front desk staff deciphering handwriting and typing it into the practice management system, insurance cards being photocopied, and a line forming behind it all. Every clipboard is duplicate work. Every typo becomes a claim denial three weeks later, because the payer rejects a claim when the name or date of birth does not match the insurance record. A pediatric practice re-collects history forms every well-child visit. A dermatology clinic needs photo consent before the provider walks in. Digital intake done right removes twenty minutes of friction per patient and cuts denials at the source. Done wrong, it becomes one more portal password patients abandon, and the clipboards come back. The difference is design, and design is what you direct.

## Certification Goal

Passing the Module 2 exam proves you can specify a complete digital intake system for a real practice: the right fields, the right sequence, the right timing, consent handled correctly, insurance captured cleanly, and the whole flow usable on a phone. It proves you know what to build before you prompt a single screen.

## What You Need to Know

**The intake data stack.** Demographics, insurance details, medical history, medications and allergies, consent signatures, and visit-specific questionnaires. Each layer has a different shelf life. Demographics change rarely, insurance changes yearly, medications change constantly. Good intake design re-asks only what actually goes stale.

**Timing the collection.** The strongest pattern is pre-visit: a link sent at booking or in the reminder message, completed at home, reviewed at check-in. Collecting everything at the front desk recreates the clipboard on a tablet. Your job is to move data capture upstream of the appointment.

**Insurance capture and verification.** Capture the member ID, payer name, subscriber, and card images at intake, and verify eligibility before the visit, not after. Module 5 goes deeper on verification workflows. Here you learn that intake is where clean insurance data is born or lost.

**Consent management.** HIPAA acknowledgments, financial policies, telehealth consent, photo consent, and minor consent signed by a parent or guardian. Consents need versioning, timestamps, and signature capture. A pediatric practice where a grandparent brings the child in is a consent scenario you must design for, not discover in production.

**Mobile-first form design.** Most patients open the intake link on a phone. That means one question per screen where possible, large touch targets, progress indicators, save-and-resume, and no fields that demand a keyboard gymnastics routine. If it fails on a five-year-old Android phone, it fails.

**Conditional logic and questionnaires.** Intake should branch. New patients get the full history; returning patients confirm and update. An orthopedic intake asks about the injury mechanism; an OB intake asks very different questions. Direct AI to build branching flows so patients never see irrelevant screens.

## Your Toolkit

- **AI-directed form builders.** Direct AI to generate custom intake flows as web apps, or configure platforms like Jotform or Formsort when the practice wants managed hosting. Custom gives control; platforms give speed. Know when to choose which.
- **E-signature capture.** Signature components for consent forms with timestamping and stored versions of what was signed. The signed artifact matters as much as the signature.
- **OCR and card capture.** Camera-based capture that reads insurance cards and driver's licenses into structured fields, cutting typos out of the payer data that claims depend on.
- **Practice management system import paths.** CSV exports, APIs, or structured summaries that move intake data into the PMS. The intake tool that cannot deliver data where staff work is a data cul-de-sac.

## Exam Topics

The Module 2 exam will test you on:

1. Sequencing intake fields and screens for completion, not abandonment
2. Deciding what to collect pre-visit versus at check-in
3. Insurance data capture and why clean capture prevents downstream denials
4. Consent form design, versioning, and guardian scenarios
5. Mobile-first design decisions for patient-facing forms
6. Conditional branching for new versus returning patients and by specialty
7. Getting intake data into the practice's existing systems
8. Choosing between custom AI-directed builds and managed form platforms

## Common Pitfalls

- **Rebuilding the clipboard on a screen.** Forty questions on one scrolling page is the paper form with extra steps. Patients abandon it, and staff go back to paper.
- **Collecting data the practice never uses.** Every field costs completion rate. If nobody downstream reads it, cut it.
- **Ignoring the guardian scenario.** Pediatric and elder-care intake involves someone other than the patient completing forms. Design who signs what, or the consents are worthless.
- **Treating insurance as a text field.** Free-typed payer names produce garbage data. Use payer pickers and card capture so the billing team gets something they can verify.
- **Skipping save-and-resume.** Patients get interrupted. An intake flow that loses ten minutes of answers earns an abandoned form and an annoyed patient.
- **Forgetting the data destination.** If completed intake lands in an inbox as a PDF, staff still retype everything. The import path is part of the build, not an afterthought.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I list the core layers of the intake data stack and how often each goes stale?
- [ ] Can I explain why pre-visit collection beats front-desk collection, and what to still handle at check-in?
- [ ] Can I describe what clean insurance capture looks like and what it prevents downstream?
- [ ] Can I design a consent flow that handles versions, timestamps, and a guardian signing for a minor?
- [ ] Can I name five mobile-first design decisions that protect completion rates?
- [ ] Can I sketch a branching intake flow for a new patient versus a returning patient?
- [ ] Can I explain how intake data reaches the practice management system in my design?

## AI Audit Prompt Template

Use this prompt to audit your intake build before showing it to a practice:

> "You are a practice operations reviewer auditing a digital intake system for a [specialty] practice. Here is my form structure and flow: [paste spec or screens]. Audit it for: fields collected but never used downstream, missing consent scenarios including guardians and minors, insurance capture weaknesses that would cause claim denials, mobile usability failures, missing branching between new and returning patients, and gaps in how data reaches the practice management system. List every issue by severity and tell me the three changes that would most improve completion rate."

## What's Next

Module 3 moves to the calendar: scheduling and reminder systems. Intake and scheduling are joined at the hip, because the booking event is what triggers the intake link. Next you will direct AI to build the availability logic, reminder sequences, and no-show defenses that keep a practice's schedule full.

## Certification Pathway

This is the second of seven modules in Healthcare Practice AI Engineering, part of T5 The Industry. Pass all seven module exams to earn the Healthcare AI Specialist badge. Intake is the first component of the Practice Admin Toolkit you will assemble and ship in Module 7.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Patient Intake and Forms Exam →
