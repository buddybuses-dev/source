# Module 3: Solution Validation — Study Guide

## Stop building things nobody wants. Validate demand before you write a single prompt.

## What This Module Covers

In Module 2 you validated that a real problem exists. Now comes the trap that catches most builders: assuming that because the problem is real, your solution is the right one. Those are two completely different bets. Module 3 teaches you how to test your proposed solution before you build it, using tools that cost days instead of months.

You will learn the full solution testing toolkit: landing page tests, waitlists, pre-sales, concierge MVPs, wizard-of-oz approaches, fake doors, and smoke tests. You will also learn what "minimum viable" actually means: not a smaller version of your product, but the smallest thing that tests your riskiest assumption. By the end, you can design a test that gets a real yes or no from the market before your AI builds anything more than a single page.

## Why It Matters

Here is a scenario I have watched hundreds of times inside The Faction. A builder gets excited about a CRM for dentists. The problem is real, dentists do juggle patient follow-ups badly. So the builder spends three months prompting a full product into existence: pipelines, reminders, integrations. Launch day comes. Silence. Dentists did not want another login, they wanted their existing software to stop being terrible. The solution was wrong, and that was discoverable in one weekend instead of one quarter.

You can be right about the problem and still lose on the solution. Vibecoding makes building fast, which is a gift and a curse: it is now easier than ever to build the wrong thing quickly. Solution validation protects your most limited resources, which are not tokens or prompts. They are your time, your energy, and your credibility with your audience.

## Certification Goal

Passing this exam proves you can design a solution test for any idea: pick the riskiest assumption, choose the right test type, define pass or fail signals in advance, and interpret results honestly. That is the core skill of a Validation Specialist.

## What You Need to Know

### The Riskiest Assumption

Every idea rests on a stack of assumptions, and one is most likely to kill you. For the dentist CRM, it is not "can I build a CRM," it is "will a dental office manager change their workflow for this." Minimum viable means the smallest thing that tests that specific assumption, and you test it first, because if it fails, nothing else matters.

### Landing Page Tests and Waitlists

A landing page test is a single page describing your solution as if it exists, with one clear call to action. The percentage of visitors who click or sign up is your demand signal. A waitlist email says "notify me," which is weak commitment, so treat it as directional, not proof.

### Pre-Sales: The Gold Standard

Money is the only signal that cannot lie to you. A pre-sale asks people to pay, or put down a deposit, for something you have not built yet. If ten dentists put down fifty dollars for early access, you have real evidence. If nobody will, you just saved three months, and that is a win.

### Concierge MVPs

A concierge MVP delivers the outcome of your product manually, by hand, for a handful of customers. Before building an automated follow-up tool, you personally send follow-ups for three dental offices for two weeks. You learn exactly what the product must do, and whether customers value the outcome, before a single feature exists.

### Wizard-of-Oz Tests

A wizard-of-oz test looks automated from the outside but is powered by you behind the curtain. The customer uses what feels like a real product while you manually do the work the software would eventually do. It tests whether people use and value the experience without you building the engine underneath it.

### Fake Doors and Smoke Tests

A fake door is a button or feature that does not exist yet: "Export to QuickBooks" leads to "coming soon, want early access?" Clicks measure real demand for that specific thing. A smoke test is the broader family of these tactics: put the promise in front of people and measure who reaches for it. Always tell people the truth after they click. Signal is the goal, not deception.

## Your Toolkit

- **The Assumption Map:** A one-page list of every assumption behind your idea, ranked by how likely it is wrong and how dead you are if it is. The top item is what you test first.
- **The One-Page Landing Test:** A single page you direct your AI to build in an hour: headline, problem, promised solution, one call to action, analytics wired in. The only thing you are allowed to build in this module.
- **The Pre-Sale Offer Script:** A short, honest pitch: what you are building, when it ships, what early buyers get, and a refund promise. It turns "sounds cool" into "here is my card" or a revealing no.
- **The Signal Threshold Sheet:** A written commitment, made before the test runs, of what counts as pass, kill, or iterate. Example: "100 visitors, 15 signups, 3 pre-orders, or I do not build."

## Exam Topics

- The definition of "minimum viable" as the smallest thing that tests the riskiest assumption
- How to identify the riskiest assumption in a given idea scenario
- The difference between a landing page test, a waitlist, and a pre-sale, and the strength of signal each provides
- When to use a concierge MVP versus a wizard-of-oz test, and what each reveals
- How fake door and smoke tests work, and the ethical requirement to be honest with people who click
- Why payment is a stronger validation signal than signups, clicks, or verbal enthusiasm
- Why pass and fail thresholds must be set before a test runs, not after
- Matching the right test type to a scenario, such as a dentist CRM or a mobile app idea

## Common Pitfalls

- **Building the product and calling it a test.** If your "MVP" took six weeks of prompting, it was not minimum, it was the product.
- **Testing the easy assumption instead of the risky one.** Proving "I can build this" is worthless, your AI can build almost anything. Prove "someone will use and pay for this" instead.
- **Treating waitlist signups as proof of demand.** Emails are free to give. A thousand signups with zero pre-orders is a maybe dressed up as a yes.
- **Moving the goalposts after the test.** "Three signups out of 200 visitors is not bad for a first try" is how builders talk themselves into three wasted months.
- **Running a fake door test and never following up.** Leaving clickers hanging burns trust with the exact people who wanted your product most. Close the loop honestly.
- **Skipping the concierge phase because it does not scale.** It is not supposed to scale, it is supposed to teach. Doing it by hand first is the fastest way to learn what to build.

## Self-Assessment Checklist

- I can identify the riskiest assumption behind my idea and explain why it gets tested first
- I can explain what "minimum viable" actually means and spot an MVP that is really a full product in disguise
- I can design a landing page test with one clear call to action and a way to measure conversion
- I can explain why a pre-sale is stronger evidence than a waitlist, and structure an honest pre-sale offer
- I can describe the difference between a concierge MVP and a wizard-of-oz test, and pick the right one for a scenario
- I can run a fake door or smoke test ethically, including closing the loop with people who clicked
- I can set pass, kill, and iterate thresholds in writing before a test runs, and stick to them

## AI Audit Prompt Template

Before you launch your test, have your AI audit the design. Fill in the brackets and run it.

> You are a ruthless validation coach auditing my solution test before I run it. My idea: [one-sentence description] The problem it solves: [validated problem from Module 2] My riskiest assumption: [the assumption that kills the idea if wrong] My test type: [landing page / waitlist / pre-sale / concierge MVP / wizard-of-oz / fake door] My test design: [what I will put in front of people, and where traffic comes from] My pass threshold: [specific numbers: visitors, signups, pre-orders] My kill threshold: [the result that means I do not build this] Audit my design: 1. Is the assumption I listed actually the riskiest one? If not, what is? 2. Does my chosen test type actually test that assumption, or something easier? 3. Is my test the smallest possible thing, or am I secretly building the product? 4. Are my thresholds specific and honest, or vague enough to rationalize later? 5. How could I strengthen the signal, for example converting signups into pre-orders? 6. List the top three ways I might fool myself with this test, and how to prevent each. Be direct. Do not soften the verdict.

## What's Next

Your solution test tells you whether individual people want what you are proposing. Module 4: Market Sizing and Demand Signals zooms out to the bigger question: are there enough of those people to make this worth building? You will learn to size your market honestly and read demand signals at scale, so a promising test does not lead you into a market too small to matter.

## Certification Pathway

Pass this module's exam at 80 percent, that is 20 of 25 questions, to earn the Module 3 badge. Pass all 7 module exams to earn the Validation Specialist badge. The exam is free, retakes are free, and everything you need to pass is in this guide and the module lessons.
