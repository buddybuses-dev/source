# Bonus Module: I Ran a Business Back Office on Claude Agents. Here's the Whole Thing.

**Time:** about 30 minutes reading, 45 more if you build the exercise. **Hands-on:** optional but recommended. This is a case study with the real files in it.

## Why this module exists

Everything in modules 1 through 8 taught you skills. This module shows you what they stack into: a real business back office, sales research to outreach drafts, run by scheduled Claude agents while the owner did other things.

Full disclosure up front, because it makes the lesson better, not worse: the business this back office served never landed a paying client, and I eventually shut it down because the *delivery* side needed hours per client I didn't have. The automation worked. The business model didn't fit my life. You get to learn from both halves.

## The business, in one paragraph

The service was a systems audit for small business owners: they pay a few hundred dollars, fill out a questionnaire, we do a discovery call, they get a written roadmap. Standard consulting-shaped offer. The bottleneck in any offer like this is the top of the funnel: finding prospects, researching whether they're a fit, and writing outreach that doesn't read like spam. Done by hand, that's hours per week of repetitive, judgment-light work. Which should be setting off your Module 7 alarm: any brief you'd type three times is a product waiting to be built.

## The architecture: three agents and a spreadsheet

The whole system was an Airtable base (a spreadsheet with a nicer interface) plus three scheduled Claude agents, each one just a markdown file describing a job. That's it. No code, in the sense you feared before Module 1.

**The pipeline:**

1. **I drop names into an intake table.** People from my LinkedIn network, local business owners, referrals. Name, LinkedIn URL, status: Queued. Ten seconds each, done from my phone.
2. **Agent one: prospect research.** On a schedule, it checks the intake table for anything Queued, then for each prospect: reviews their public LinkedIn presence, searches for their website and social accounts, looks for evidence of the specific pains my service fixed (scheduling chaos, solo operation, posts about being overwhelmed), and scores fit from 1 to 5 against written criteria. Then it writes a full pipeline record: company, vertical, contact info if publicly findable, the evidence it found, and a one-sentence outreach angle referencing something real, a specific video title, a blog post, a booking page. It marks the intake row Complete and moves on.
3. **Agent two: fit-check briefs.** Before any sales call, it assembled everything known about the prospect into a one-page brief so I walked in prepared without prep time.
4. **Agent three: outreach drafts.** For researched prospects above a fit threshold, it drafted the personalized first-contact email using the research angle, saved as a draft for my review. Drafts, not sends. The human approves anything that leaves the building. That rule is not negotiable, and it's the same rule you learned about permissions in Module 7, scaled up to a business.

## The actual agent file

Here's a condensed version of the real research agent, so you can see there's no magic. It's a brief. You could have written it after Module 3.

```markdown
---
name: prospect-research
description: Automated prospect research
---

Check the Intake table in my Airtable base for records where
Research Status equals Queued. If there are none, stop.

For each Queued record:
1. Set Research Status to In Progress.
2. Review their LinkedIn profile: title, company, team size,
   posts about systems, workflows, or overwhelm.
3. Search for their name and business. Check their website,
   YouTube, Instagram. Look for scheduling or onboarding pain,
   solo operation, revenue signals.
4. Score fit 1-5: solo or micro-team required for anything
   above 1; scheduling-heavy business required above 2;
   revenue signals add a point; public pain signal adds a point.
5. Write a one-sentence outreach angle referencing something
   REAL the research found. Generic angles score low.
6. Create a pipeline record with all fields filled.
7. Set Research Status to Complete. Continue to the next.

If research is inconclusive after a reasonable search, score 1,
note the limitation, and move on.
```

Read that twice and notice what it is: a job description for a diligent assistant, with the judgment criteria written down. The scoring rubric matters most. "Score how good a fit they are" produces mush; "solo or micro-team is required for any score above 1" produces decisions you can audit.

## What it was like to operate

Mornings, I'd open Airtable to a table of researched prospects, scored and sorted, each with an outreach angle grounded in something the agent actually found. The research that would have eaten my evenings happened without me. Real outputs from the real table: bookkeepers and photographers scored 3 to 5 with public pain signals quoted; enterprise employees who'd slipped into my intake list scored 1 and auto-archived with the reason noted. The filtering alone justified the setup, because the most expensive outreach is the well-written email to someone who was never going to buy.

Costs, honestly: a few sessions to set up the Airtable base and tune the agent briefs, then roughly zero marginal effort per prospect. The tuning was mostly tightening the scoring rules after early batches scored too generously. You'll recognize that loop from every module: run it, read the output, sharpen the brief.

## Why I shut it down anyway, and what that teaches

The back office scaled beautifully. The service didn't: every client meant hours of calls and report writing from me personally, and my weeks didn't have those hours. Automation multiplies a business; it doesn't change what the business is. Multiply a time-for-money service by great automation and you get a very efficient way to sell your unavailable time.

The takeaways worth paying for:

1. **Automate the funnel, but check the engine.** Before building a back office, make sure the thing it feeds is something you can actually deliver at volume.
2. **Agents are briefs on a schedule.** Everything you learned about writing good briefs is the skill. The scheduling is a detail.
3. **Judgment criteria go in writing.** The 1-to-5 rubric is what separated useful automation from confident noise.
4. **Drafts, not sends.** Autonomy at the edges of your business, human approval at the boundary where it touches other people.
5. **A system you can shut down cleanly is a system that was built well.** When I killed the service, the agents were three files to archive and one table to flag. Build so that stopping is cheap, because some experiments should stop.

## The exercise: build a one-agent back office

Pick a recurring research task in your own work. Prospects, competitors, grant deadlines, local permits, whatever you look up repeatedly. Then, in a session:

> "I want a recurring agent that [your task]. Interview me about the judgment criteria until you could score results 1 to 5 without me, then write the agent file with those criteria in it, and set it up to run on a schedule. Its output goes to [a file, a spreadsheet], and it never contacts anyone or posts anything."

Note what you're doing in that prompt: making Claude extract your judgment into written rules before any automation exists. That interview is the exercise. The agent is just where the answers live.

Run it for two weeks. Tighten the rubric when the output disagrees with your gut, because your gut is usually detecting a rule you haven't written down yet.

That's the course. You came in wondering whether you could use a developer tool. You're leaving with a back office pattern that businesses pay consultants five figures to design. Go build the boring thing that gives you your evenings back.
