# Module 5: Agent Testing and Validation — Study Guide

## Measuring Reliability in Systems That Don't Behave the Same Way Twice

## What This Module Covers

This module covers how to test systems that think: measuring agent behavior in rates instead of single passes, catching hallucinations, building golden datasets and mechanical validation, using AI judges without trusting them blindly, and keeping validation running after launch, because launch is where the real test begins.

Here's your real situation: testing an AI agent differs fundamentally from testing traditional software, because the same input can produce different outputs. Everything you know about pass-fail testing gets replaced by a statistical mindset: you don't ask whether the agent passed, you ask how often it succeeds across many runs. That single shift, from runs to rates, is the foundation of every technique in this module.

You own the validation architecture. You define the acceptance thresholds the stakes require, build the datasets the agent gets scored against, decide what gets checked mechanically versus judged, and design the rollout that earns production traffic gradually. The agent generates. Your system verifies.

## Why It Matters

Untested agents fail in the most expensive way possible: confidently. A hallucination isn't a stammer or an error message. It's fabricated facts, sources, or results presented as real, delivered with the same fluent certainty as the correct answers. Fluent certainty and correctness are separate things, and every stakeholder who doesn't understand that will trust the demo, ship the system, and discover the failure rate in front of customers.

The demo is the trap. One successful run on friendly input tells you almost nothing, because production is thousands of runs on hostile input. Builders who validate properly ship systems whose reliability is a measured number tied to a threshold the stakes demand. Builders who don't ship vibes. In a market where 88% of agent pilots fail, measured reliability is the differentiator clients can't get elsewhere. This module teaches you to produce it.

## Module Certification Goal

You can design validation that measures agent behavior in rates across many runs against ground truth, combine golden datasets, mechanical checks, calibrated AI judges, and human sampling into a working pipeline, and keep systems validated after launch through monitoring, gradual rollout, and a feedback loop that turns failures into test cases.

## What You Need to Know

- **Rates, not runs:** The same input can produce different outputs, so behavior is measured in rates across many runs, never one lucky pass. Before trusting an agent, run the same scenario many times so you know the success rate. High variance on identical input is itself a reliability problem to fix, not creativity to celebrate. Reliability gets expressed as measured rates: how often it succeeds, fails, or degrades across many real runs. And the bar isn't universal: setting an acceptance threshold means deciding what reliability the stakes require. An internal draft tool and a customer-facing action need different bars.
- **Hallucinations get caught by ground truth, not by rereading:** A hallucination is confident output that is fabricated or wrong: invented facts, sources, or results presented as real. The reliable catch is verifying claims against ground truth: the actual data, documents, or systems referenced. Not rereading the output, not checking its confidence wording, and never asking the same agent whether it hallucinated. A golden dataset makes this systematic: a curated set of inputs with known correct outputs, used to score the agent's answers against truth.
- **Layer the checks: mechanical, adversarial, regression:** Beyond judging quality, every output gets mechanical validation: structure and bounds checks, right format, required fields present, values within sane ranges. Feed the agent malformed, hostile, and weird inputs deliberately, because production will do exactly that, and you want to learn the failure behavior first. And every instruction change triggers a rerun of the existing suite: fixes routinely break other behaviors, and regressions hide silently. Test data follows one rule: real customer secrets and live credentials stay out; test data is representative, not sensitive. When the agent's job includes calling tools, testing needs the extra layer from Module 2: verifying the calls themselves, right tool, right parameters, right handling of results.
- **Judges scale you, humans calibrate the judges:** Using a second AI model to grade outputs at scale works, with one discipline attached: the judge is fallible too, so calibrate it against human judgment and spot-check its scores. Human review keeps a permanent role even in automated pipelines: regular sampling, humans inspecting a slice of outputs to catch what automated checks miss. And validation itself needs independent eyes: someone other than only the builder designs and judges it, because independent eyes catch what the maker's pride skips.
- **Categorize failures, guard the known weaknesses:** Counting failures tells you how much is wrong. Categorizing tells you what to do: different failure types have different fixes, a format bug, a knowledge gap, and a tool error need different work. And a validated agent still has known weaknesses. The professional move is to document the limitations and design around them: guardrails where it's weak, humans where it fails. Not concealment, not endless pre-launch polishing. Engineering around measured reality.
- **Launch is where validation moves, not where it ends:** After shipping, validation becomes continuous monitoring: production outputs sampled, scored, and alarmed on drift. New systems reach full traffic gradually: a small slice first, watched closely, expanding as metrics hold. When the provider upgrades the model behind your agent, disciplined validation re-runs the evaluation suite before trusting it with the same work. And real user feedback feeds the loop: complaints and corrections become test cases the suite runs forever after. The one run that impressed the client in the demo proves nothing. The rates prove everything.

## Your Toolkit

- **Claude Code:** Where evaluation suites get built and run: repeated scenarios, scored outputs, and regression runs on every change.
- **A golden dataset (yours, built per system):** The curated inputs with known correct outputs that turn "seems good" into a scored rate.
- **A judge model with calibration (a second model grading at scale):** Scales your scoring, spot-checked against human judgment so the grader itself stays honest.
- **Production monitoring (your platform's dashboards or one you direct AI to build):** Sampled outputs, drift alarms, and the failure categories that tell you what kind of fix each problem needs.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- Can you explain why agent testing differs fundamentally from traditional software testing, and what one passing run does and doesn't prove?
- Can you define hallucination, identify the reliable way to catch fabricated facts, and explain what an agent's confidence tells you about accuracy?
- Can you construct a golden dataset, apply mechanical structure and bounds checks, and set the rule for test data sensitivity?
- Can you justify adversarial testing, rerun suites after instruction changes, and add the tool-call verification layer?
- Can you use an AI judge with calibration, place human sampling in an automated pipeline, and assign validation to independent eyes?
- Can you express reliability as measured rates, diagnose high variance on identical input, and set acceptance thresholds by stakes?
- Can you categorize failures by fix type, and design around documented weaknesses with guardrails and human coverage?
- Can you run post-launch validation: continuous monitoring, gradual rollout, re-evaluation on model upgrades, and user feedback becoming test cases?

## Common Pitfalls

These are the mistakes vibecoders make most often at this stage. No judgment, they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- You treat one pass as proof. It worked, so it works. Non-deterministic systems don't extend that courtesy. The same scenario runs many times, and the rate is the result. One pass is one sample, and one sample is a coin flip wearing a lab coat.
- You validate by vibe. Two weeks of casual use felt convincing, and it measured nothing. Golden datasets, scored runs, and thresholds turn impressions into numbers. Trust rates, not feelings.
- You ask the agent to check itself. It produced the answer, so it can confirm the answer, right? Models don't audit themselves accurately, and confident wording proves nothing. Verification runs against ground truth: the actual data, documents, and systems referenced.
- You ship the fix without rerunning the suite. The instruction change solved the reported problem and quietly broke two behaviors nobody was watching. Regressions hide silently. Every change reruns the existing tests, every time.
- You trust the judge without calibrating it. The grading model scaled your evaluation beautifully, and nobody checked whether its scores match human judgment. A fallible judge scoring at scale is fallibility at scale. Calibrate it, then spot-check it forever.
- You treat the demo as the finish line. It nailed the client presentation, one run on friendly input, and production is thousands of runs on hostile input. Roll out gradually, monitor continuously, and let real complaints become permanent test cases.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Can you state your agent's success rate on its core scenario, from actual repeated runs?
- Does a golden dataset exist for your system, with known correct outputs to score against?
- Does every output pass mechanical structure and bounds checks before anything downstream trusts it?
- Has your system been fed deliberately malformed and hostile inputs, and do you know what it did?
- Does every instruction change trigger a full suite rerun?
- If you use an AI judge, has it been calibrated against human judgment, and is human sampling still running?
- Is there an acceptance threshold tied to the stakes, monitoring in production, and a path from user complaints to new test cases?

## AI Audit Prompt Template

Copy this prompt into your AI assistant to get a quick health check on your validation pipeline. It checks the same things the certification exam covers.

> Review my agent validation setup and check the following. For each one, tell me pass or fail with a specific example: Rates: Here is how I currently test [describe it]. Am I measuring success rates across repeated runs, or trusting single passes and demos? Ground truth: How are factual claims verified, and does a golden dataset with known correct outputs exist for the core scenarios? Layers: Do outputs pass mechanical format and bounds checks, has the system faced deliberately hostile inputs, and do instruction changes trigger full regression reruns? Judging: If a model grades outputs, how is it calibrated against human judgment, and what human sampling remains? Thresholds and weaknesses: What acceptance threshold do the stakes require, and are known weaknesses documented with guardrails or human coverage designed around them? Post-launch: Describe my monitoring, rollout, and feedback loop [describe them]. Are production outputs sampled and alarmed on drift, does traffic grow gradually, and do complaints become test cases? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 5 exam. The best way to prepare: pick one agent you run today and build its first real evaluation: a twenty-case golden dataset, thirty runs, a measured rate, and one adversarial session trying to break it. The number you get back, and what you do about it, is exactly what the exam tests.

## Certification Pathway

- **Frontier Specialist — Agent Orchestration:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush, take the time to build something real first.

---

Ready? Take the Agent Testing and Validation Exam →
