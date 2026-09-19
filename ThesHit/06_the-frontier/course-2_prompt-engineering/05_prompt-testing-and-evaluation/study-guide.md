# Module 5: Prompt Testing and Evaluation — Study Guide

## "Direct AI with the precision, structure, and repeatability that separates professionals from hobbyists."

## What This Module Covers

This module is where prompt engineering stops being a craft and becomes a discipline. Everything you built in Modules 1 through 4 only holds up in production if you can prove it works. Module 5 teaches you how to prove it: defining evaluation criteria before you write a single prompt, building test sets that catch regressions, A/B testing prompt versions, and measuring output quality.

You will learn the development loop professional builders run on every serious system: draft, test, measure, iterate. By the end, "it looked good when I tried it" will sound to you the way "it compiled on my machine" sounds to a seasoned engineer: not evidence, just an anecdote. The Faction ships prompts into systems that run thousands of times a day without a human watching. This module makes that safe.

## Why It Matters

Consider a customer support bot handling 10,000 conversations a day. You tweak one line of the system prompt to make refund responses warmer, and it looks great on the three conversations you eyeball. What you did not see: the change also made the bot promise refunds it cannot issue, 400 times a day. Without a test set, you find out from angry customers. With one, you find out in ninety seconds.

The stakes compound at scale. An extraction system that hallucinates a field value 2 percent of the time means 200 corrupted records per 10,000 documents flowing silently into your database. A content pipeline that drifts off brand voice on 1 in 20 posts erodes trust one publish at a time. Testing converts "the AI usually gets it right" into a number you can defend, monitor, and improve. Builders who cannot measure their prompts cannot responsibly ship them.

## Certification Goal

Passing the Module 5 exam proves you can define evaluation criteria before building, maintain a regression test set, run systematic A/B comparisons, and measure output quality across accuracy, consistency, format compliance, and hallucination rate. It certifies you as a builder who ships prompts on evidence, not vibes.

## What You Need to Know

### Why "It Looked Good" Is Not a Testing Strategy

Spot-checking a handful of outputs tells you almost nothing about a prompt that will run thousands of times against inputs you never imagined. Eyeballing cannot detect inconsistency, rare failure modes, or regressions, and it is biased toward the easy inputs you happened to try. Professional testing turns pass or fail into a measurement instead of an impression.

### Evaluation Criteria Before the Prompt

Before you draft a prompt, write down what a correct output looks like: required fields, allowed values, tone constraints, length bounds, failure conditions. This is test-driven development for prompts, and it forces clarity that makes the prompt itself better. If you cannot define success precisely, you are not ready to build.

### Regression Test Sets

A regression test set is a saved collection of real and edge-case inputs, each paired with pass criteria, that you run after every prompt change. Its job is to answer one question: did this change break anything that used to work? Every production failure you fix becomes a new test case, so the set grows into a record of everything your prompt must never break again.

### A/B Testing Prompts Systematically

When comparing version A against version B, change one variable at a time, run both against the same input set, and score with the same criteria. Run each input multiple times, because outputs vary and a single run can flatter either version. Declare a winner on aggregate scores, not on the single most impressive output.

### The Four Quality Dimensions

Measure every production prompt on accuracy (is the content correct?), consistency (does the same input produce equivalent output across runs?), format compliance (does the output follow the required structure every time?), and hallucination rate (how often does the output invent facts not grounded in the input?). A prompt can score well on three and still be unshippable on the fourth: an extraction prompt that hallucinates 3 percent of field values is a liability no matter how clean its formatting.

### The Prompt Development Loop

Professional prompt work runs a tight cycle: draft against your predefined criteria, test against the full input set, measure across the four dimensions, and iterate on the weakest failure mode until the numbers clear your ship threshold. The loop never fully closes: production failures feed back in as new test cases, and every future change reruns the whole set.

## Your Toolkit

- **Evaluation Rubric Document:** A written spec, created before the prompt, that defines pass and fail for every output dimension. It is the contract your prompt must satisfy and the scoring key for every test run.
- **Regression Test Set:** A versioned file of 20 to 100 plus inputs with pass criteria, spanning common cases and known edge cases. Run it on every prompt change and grow it with every production failure.
- **A/B Comparison Harness:** A script or spreadsheet workflow that runs two prompt versions against identical inputs, multiple times each, and tallies scores side by side. Direct your AI to build it for you in an afternoon.
- **Quality Scorecard:** A tracked record of the four quality dimensions for each prompt version over time. It turns "is the prompt getting better?" into a chart instead of a debate.

## Exam Topics

- Why single-output spot-checking fails as validation for production prompts
- Writing evaluation criteria before drafting a prompt, and how this improves the prompt itself
- Constructing a regression test set: input selection, edge cases, pass criteria
- Detecting regressions: verifying a prompt change does not break previously passing cases
- Designing a valid A/B test: single-variable changes, identical inputs, repeated runs
- Defining and measuring accuracy, consistency, format compliance, and hallucination rate
- Calculating and interpreting hallucination rate in a data extraction scenario
- The stages of the development loop and how production failures feed back into the test set

## Common Pitfalls

- **Testing only happy-path inputs:** Clean inputs pass while production feeds your prompt typos, hostile users, and malformed data. Edge cases are where prompts die.
- **Changing multiple variables between versions:** Rewrite three instructions at once and you have no idea which change helped and which is silently hurting you.
- **Judging on a single run:** Outputs vary between runs, so one great result proves nothing. Consistency is measured, not assumed.
- **Skipping the regression run on "small" changes:** The one-word tweak you did not test is exactly the one that breaks a working case. Every change reruns the full set.
- **Measuring format compliance but not hallucination:** An output can be perfectly structured and confidently wrong. Structure checks catch broken JSON, not invented invoice numbers.
- **Letting the test set go stale:** If production failures are not becoming test cases, your safety net has holes and no longer reflects real traffic.

## Self-Assessment Checklist

- I can explain why spot-checking is insufficient validation for a production prompt
- I can write evaluation criteria before I draft the prompt itself
- I can build a regression test set with representative inputs, edge cases, and pass criteria
- I can rerun a test set after a prompt change and identify any regressions
- I can design an A/B test that isolates a single variable and uses repeated runs
- I can measure a prompt on accuracy, consistency, format compliance, and hallucination rate
- I can run the full loop and feed production failures back into my test set

## AI Audit Prompt Template

Give this prompt to your AI to audit your current prompt testing practice and expose the gaps before production does.

> You are a prompt testing auditor for a production AI system. Audit my testing practice for the prompt below. PROMPT UNDER AUDIT: [paste your prompt] PRODUCTION CONTEXT: [system, volume, what happens downstream with the output] CURRENT TESTING PRACTICE: [how you test changes today, honestly] TEST SET: [paste it, or say "none"] Audit against these standards: 1. Written evaluation criteria exist and were defined before the prompt was built. 2. A regression test set exists with representative inputs, edge cases, and clear pass criteria, and it is rerun on every change. 3. Version comparisons are controlled A/B tests: one variable changed, same inputs, multiple runs, aggregate scoring. 4. All four quality dimensions are measured: accuracy, consistency, format compliance, hallucination rate. 5. Production failures feed back into the test set. For each standard: PASS or FAIL, the specific gap, and the production failure it could cause. Then give me the three highest-impact fixes and a first test set of 15 inputs, including at least 5 edge cases. Be blunt. Do not soften findings.

## What's Next

Module 6: Production Prompt Patterns hardens the prompts you can now test with the reusable patterns professionals deploy again and again: guardrails, fallbacks, routing, and output validation. With the evaluation discipline from this module, you can prove those patterns work, not just trust that they do.

## Certification Pathway

Pass this module's exam at 80 percent, 20 of 25 questions, to earn the Module 5 badge. Pass all 7 module exams to earn the Advanced Prompting Specialist badge and certify at T8 The Frontier level.
