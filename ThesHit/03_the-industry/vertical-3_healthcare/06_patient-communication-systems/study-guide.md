# Module 6: Patient Communication Systems — Study Guide

## T5 The Industry | Healthcare Practice AI Engineering

This is the study guide. Everything for Patient Communication Systems is on this page — there's nothing to download.

## What This Module Covers

This module teaches you to direct AI to build HIPAA-aware patient communication systems: appointment confirmations, post-visit instructions, recall and follow-up sequences, patient portals, secure messaging, and review generation that stays inside healthcare marketing rules. Every message a practice sends is a design decision, and you will learn to make those decisions deliberately.

## Why It Matters

Communication is where patients decide how they feel about a practice. Clinical care might be excellent, but if calls go to voicemail, lab results arrive late, and the only mail patients get is a bill, the practice reads as indifferent. The operational cost is just as real: a dermatology clinic without a recall system loses every annual skin-check patient who forgets to rebook, and a pediatric practice that cannot reach parents about overdue well-child visits watches its panel quietly erode. Recall sequences alone can recover thousands of visits a year for a mid-sized practice, which is why communication systems are often the highest-ROI build in the entire toolkit. But this is also the module where HIPAA boundaries get tested most often, because messaging is where PHI wants to leak: an appointment reminder that names the specialty, a review request that implies a diagnosis, a text thread that drifts into clinical detail. The builder who can deliver warmth at scale without leaking information is rare, and practices pay for rare.

## Certification Goal

Passing the Module 6 exam proves you can design the full communication architecture of a practice: the right message, channel, and timing for each moment in the patient relationship, with PHI boundaries respected in every template, and review generation that follows the rules instead of gaming them.

## What You Need to Know

**The message minimization principle.** Standard texts and emails are not secure channels, so messages sent there carry the minimum: practice name, date, time, and a link to a secure destination for anything more. "You have an appointment Tuesday at 2" is fine. "Reminder: your biopsy results follow-up" is a disclosure. Every template you build gets audited against this line.

**The communication calendar.** Map every touchpoint in the patient relationship: booking confirmation, reminder sequence, day-of logistics, post-visit instructions, results notification, recall, and re-engagement. Each touch has an owner, a channel, a trigger, and a template. This map is the deliverable that makes the rest of the build coherent.

**Recall and follow-up sequences.** Recalls bring patients back for care they are due: annual physicals, well-child visits, skin checks, postpartum follow-ups. The mechanics are a due-date registry, a multi-touch outreach sequence with escalating channels, and a booking link that closes the loop. Recall is retention, and retention is the practice's cheapest revenue.

**Patient portals and secure messaging.** Anything clinical, detailed, or sensitive belongs behind authentication. Portals hold results, instructions, forms, and message threads; the insecure channels just deliver the knock on the door. Know what the practice's existing EHR portal already provides so you extend the experience rather than build a competing inbox nobody checks.

**Post-visit and instruction delivery.** Patients forget most of what they hear in the exam room. Post-visit summaries, care instructions, and next-step checklists, delivered through the portal with a notification ping, measurably improve follow-through. Templates come from the practice's clinical staff; your build handles delivery, timing, and confirmation of receipt.

**Review generation inside the rules.** Reviews are won by asking at the right moment, usually shortly after a positive visit, with a direct link to the review platform. The boundaries: never reveal that someone is a patient in your own public responses, never condition rewards on positive reviews, never filter who gets asked based on predicted sentiment in ways platforms prohibit, and keep any health detail out of the loop entirely. Ask everyone, ask simply, respond generically.

## Your Toolkit

- **Messaging automation platforms.** HIPAA-eligible SMS and email services under BAA, such as Twilio-based builds or healthcare messaging platforms, driving your sequences from schedule and recall triggers.
- **Patient portal frameworks.** The EHR's native portal where possible, or AI-directed secure web apps where a gap exists, with authentication, message threads, and document delivery.
- **Recall registries.** AI-built due-date tracking keyed to visit types, generating outreach queues automatically instead of relying on a spreadsheet someone updates in December.
- **Review and reputation tools.** Post-visit review request flows with direct platform links, plus response templates that thank reviewers without confirming anyone is a patient.

## Exam Topics

The Module 6 exam will test you on:

1. Message minimization: what belongs in a text versus behind the portal
2. Mapping the full communication calendar for a practice
3. Recall sequence design: registry, touches, escalation, and booking links
4. Portal and secure messaging architecture around the existing EHR
5. Post-visit instruction delivery and confirmation of receipt
6. Review generation practices that stay inside platform and healthcare rules
7. Responding to public reviews without disclosing patient status
8. Channel and timing decisions across confirmations, recalls, and balance reminders

## Common Pitfalls

- **Leaking PHI through helpfulness.** The reminder that says "for your diabetes check" was written by someone being thorough. Thorough is how disclosures happen. Minimum in the message, detail in the portal.
- **Building a second inbox.** A custom portal patients must remember while the EHR portal also exists guarantees both go unread. Extend what exists before building parallel.
- **One-touch recalls.** A single postcard-style email recovers almost nobody. Recall works as a sequence with escalating channels and an actual booking link, not a "call us" dead end.
- **Replying to reviews with confirmation.** "We're so glad your procedure went well!" confirms patient status and details in public. Responses thank and invite offline contact, nothing more.
- **Gating review requests by sentiment.** Only asking patients you predict will be positive violates platform rules and looks exactly like what it is. Ask everyone consistently.
- **Sequences with no exit.** Reminders that keep firing after the patient booked, or recalls that message the deceased, are automation without state checks. Every sequence checks status before it sends.

## Self-Assessment Checklist

Answer yes or no. Six or more yes answers means you are ready for the exam.

- [ ] Can I audit a message template and strip it to the compliant minimum?
- [ ] Can I map a practice's complete communication calendar with trigger, channel, and owner for each touch?
- [ ] Can I design a recall sequence for a specific visit type with escalating touches and a booking link?
- [ ] Can I explain when to extend the EHR portal versus build a custom secure destination?
- [ ] Can I design post-visit instruction delivery with confirmation of receipt?
- [ ] Can I write a review request flow and a public response template that stay inside the rules?
- [ ] Can I identify the state checks every automated sequence needs before sending?

## AI Audit Prompt Template

Use this prompt to audit your communication build:

> "You are a HIPAA-aware patient experience reviewer auditing a communication system for a [specialty] practice. Here are my message templates, sequences, and triggers: [paste them]. Audit every template for PHI beyond the compliant minimum for its channel. Check every sequence for missing state checks, missing exits, and dead-end calls to action. Check the recall design for registry gaps and escalation logic. Check review flows for sentiment gating, incentives, or responses that confirm patient status. Return a findings list by severity, with the rewritten compliant version of every failing template."

## What's Next

Module 7 is the ship. Intake, scheduling, billing support, and communication come together as one Practice Admin Toolkit a real practice can run. The capstone covers integration, deployment sequencing, staff training, adoption measurement, and iterating on real usage. Everything you have built is about to become one system.

## Certification Pathway

This is the sixth of seven modules in Healthcare Practice AI Engineering, part of T5 The Industry. Pass all seven module exams to earn the Healthcare AI Specialist badge. Communication is the fourth and final component that feeds the Module 7 capstone build.

———

**Matt Murphy AI | The Faction Group LLC | mattmurphy.ai**

———

Ready? Take the Patient Communication Systems Exam →
