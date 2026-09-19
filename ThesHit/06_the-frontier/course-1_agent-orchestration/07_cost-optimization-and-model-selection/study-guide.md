# Module 7: Cost Optimization and Model Selection — Study Guide

## Token Economics, Model Routing, and Paying for Outcomes Instead of Habits

## What This Module Covers

This module covers the economics of running AI systems: token billing, the real trade between frontier and smaller models, model routing, batch versus real-time processing, caching, retry discipline, and the financial controls that keep a deployed system from surprising anyone with an invoice.

Here's your real situation: you're finishing the tier that made you an orchestrator, and every architecture decision you've learned has a price tag attached. The step counts in your pipelines, the context sizes in your sessions, the retries in your error handling: all of it bills. Cost optimization isn't a finance chore bolted onto engineering. It's an architectural discipline, and at scale it decides whether the systems you ship for clients are assets or liabilities.

You make the economic calls: which model each task deserves, what runs in batch, where caching pays, what the monthly bill will be before it exists, and how run costs enter your client pricing. The models do the work at whatever price you architected. This module is how you architect it well.

## Why It Matters

AI spend fails quietly and compounds loudly. The verbose agent that rambles for pages bills those pages on every call. The boilerplate repeated in every prompt multiplies across all your volume. The retry loop without discipline triples a bill overnight. None of these announce themselves. They arrive as an invoice, weeks after the architectural decision that caused them, on a system that "worked fine."

The deeper failure is optimizing the wrong number. Cheap tokens that fail are expensive: the real metric is cost per successful outcome, and the builder who routed a hard reasoning task to the cheapest model paid more than frontier would have cost, in retries, rework, and cleanup. For a builder shipping client systems, this module is also a professional obligation: know the run cost of what you ship, price so margins survive it, and answer the client's "what does this cost monthly" with real data. This module teaches the discipline end to end.

## Module Certification Goal

You can route each workload to the model its difficulty and stakes require and measure cost per successful outcome, architect for token economics through context discipline, caching, batching, and retry limits, and operate deployments with budgets, alerts, estimates before commitment, and run costs priced into client engagements.

## What You Need to Know

- **Tokens are the meter, and both directions bill:** The basic billing unit is the token, covering both what you send into the model and what it generates back. That single fact drives three disciplines. Input side: pages of rarely changing boilerplate cost money on every call, recurring bulk multiplied across all your volume. Output side: unbounded verbosity is a spend leak on every call, worth fixing beyond style. And when many requests reuse the same large context, caching addresses it: providers can reuse recently seen context at a fraction of the original price. Context discipline from Module 4 now has a second payoff: every token in context is billed on every call, so lean context compounds into real savings.
- **Fit the model to the task:** The honest trade: frontier buys peak capability at higher cost and latency; smaller is cheaper and faster but shallower. Model routing sends each task to the model that fits it: light work to cheap models, hard work to frontier. Per workflow step, the choice runs on the difficulty and stakes of that step, matched against what each model reliably handles. Frontier prices are justified by high-stakes or genuinely hard work: complex reasoning, critical accuracy, novel problems. And the cautionary tale runs the other way too: the hard reasoning task routed to the cheapest model failed repeatedly and cost more than frontier would have. Cost per token is the sticker. Cost per successful outcome is the truth.
- **Real-time is for someone waiting:** A workload needs real-time responses when a human or process is actively waiting on the answer to proceed. Everything else is a batching candidate: when results aren't needed instantly, bulk jobs run cheaper off the interactive path. When rate limits bite at peak hours, the mature options are smoothing load, batching what can wait, requesting higher tiers, or routing across models. Free tiers and trial credits have exactly one professional role: prototyping, cheap experiments to validate an approach before real budgets commit. Never production hosting.
- **Architecture is a bill you design:** A single agent task that fired forty tool calls and model steps billed every one of them: each step bills tokens, so loops and chattiness multiply cost invisibly inside one task. The retry story is sharper: a transient error retried aggressively all night tripled a bill, and the missing piece was retry discipline: capped attempts, backoff, and alerts, so failures don't compound into spend. Before committing to any high-volume workflow, estimate: tokens per run times volume times price, the monthly bill, roughly, before it surprises you. And optimization has a season: after it works. Prove quality first, then cut costs where measurements say it's safe.
- **Switching and deprecation run on evidence:** A cheaper model replacing the current one isn't a pure savings until your evaluation suite runs on it: the discount only counts if quality holds at your bar. That's Module 5's suite earning its keep again. When a provider deprecates the model your system depends on, managed selection means planned migration: evaluate successors early, test against your suite, switch on your schedule. Not panic switching on announcement day, and not pretending the notice doesn't apply to you.
- **Money controls and the client conversation:** Serious deployments carry financial controls: budgets, alerts, and per-workflow spend visibility, so anomalies surface in hours, not invoices. For client systems, model costs enter your pricing as accounted overhead: know the run cost of what you ship and price so margins survive it. And when the client asks what their system costs to run monthly, professional practice is a clear answer from real usage data, with the drivers explained and levers identified. That answer, delivered confidently, is the difference between a vendor and an advisor.

## Your Toolkit

- **Claude Code:** Where routing, batching, and retry discipline get built into workflows, and where step counts and context sizes get trimmed.
- **Your provider's usage dashboard and API pricing (Claude Platform for Claude models):** The real numbers behind every estimate: per-model pricing, caching economics, and actual consumption.
- **A cost model you direct AI to build (a spreadsheet or script):** Tokens per run times volume times price, per workflow, so the monthly bill exists on paper before it exists on an invoice.
- **Budget alerts and per-workflow spend tracking:** The controls that surface anomalies in hours: budgets, thresholds, and visibility into which workflow is spending what.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a situation and need to identify what's right, what's wrong, or what to do next. Here's what gets tested:

- Can you identify the basic billing unit, why boilerplate-heavy prompts matter financially, and what caching addresses?
- Can you state the honest trade between frontier and smaller models, define model routing, and choose per step by difficulty and stakes?
- Can you identify the flaw in optimizing cost per token, and diagnose what routing a hard task to the cheapest model actually cost?
- Can you determine which workloads need real-time responses, when batch processing wins, and the mature responses to rate limits?
- Can you spot the architectural cost drivers: step counts inside agent tasks, verbose outputs, and context size at scale?
- Can you apply retry discipline, run the estimate before committing to high-volume workflows, and time optimization for after quality is proven?
- Can you require evaluation before switching to a cheaper model, and manage a provider's model deprecation on your schedule?
- Can you specify the financial controls a serious deployment carries, price run costs into client work, and answer a client's monthly cost question professionally?

## Common Pitfalls

These are the mistakes vibecoders make most often at this stage. No judgment, they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- You default everything to frontier. Capability headroom felt safe, so the formatting tasks ride the most expensive model in the catalog. Fit the model to the task. Frontier is for the work that's genuinely hard or genuinely high-stakes, and the rest is margin you're donating.
- You default everything to the cheapest model. The sticker price won, the hard tasks failed repeatedly, and retries plus rework plus cleanup dwarfed the per-call savings. Cheap tokens that fail are expensive. Measure cost per successful outcome and let that number choose.
- You let the agent ramble on your dime. Pages where a paragraph would do, billed on every call, at volume. Output verbosity is a spend leak, not a personality trait. Bound it.
- You retry without limits. A transient error, an aggressive retry loop, and a bill three times its normal size by morning. Capped attempts, backoff, and alerts. Failures should page you, not compound silently into spend.
- You discover the bill instead of estimating it. The workflow shipped at volume and the invoice was the first anyone heard of the economics. Tokens per run, times volume, times price. Five minutes of math before commitment beats a month of explaining afterward.
- You switch models on price alone. The cheaper model was API-compatible, so the swap felt free, and quality quietly fell below your bar. The discount only counts if the evaluation suite says quality holds. Run it first, every time.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Do you know the monthly run cost of your highest-volume workflow, from real usage data?
- Is each step in your workflows routed to a model chosen by difficulty and stakes, not habit?
- Have you identified what in your systems can move to batch, and what caching would save on repeated context?
- Do your retry policies have capped attempts, backoff, and alerts?
- Do you run the tokens-times-volume-times-price estimate before committing any high-volume workflow?
- Would a cheaper model have to pass your evaluation suite before replacing a current one?
- Do budgets, alerts, and per-workflow visibility exist, and do your client prices carry the run costs?

## AI Audit Prompt Template

Copy this prompt into your AI assistant to get a quick health check on your AI spend. It checks the same things the certification exam covers.

> Review my AI cost structure and check the following. For each one, tell me pass or fail with a specific example: Routing: Here are my workflows and the models they use [list them]. Is each step matched to its difficulty and stakes, and where am I paying frontier prices for light work or cheap-model prices for hard work? Token discipline: Here is a typical prompt and output [paste them]. What recurring boilerplate, oversized context, or unbounded verbosity is billing on every call, and would caching help? Batching: Which of my workloads has a human or process actively waiting, and what should move off the interactive path? Safety rails: Do my retries have capped attempts, backoff, and alerts, and what budgets and per-workflow spend visibility exist? Estimates: For my highest-volume workflow [give tokens per run, volume, and price], calculate the monthly bill and flag any surprise. Client economics: For systems I ship [describe one], is the run cost known, priced into margins, and answerable from real usage data? Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you can answer "yes" to the self-assessment checklist, you're ready for the Module 7 exam, and for the Frontier Specialist badge itself. The best way to prepare: audit one real system end to end. Pull the actual usage data, run the estimate, reroute one overserved step, bound one verbose output, and cap one retry policy. The bill you lower is exactly what the exam tests, and the discipline behind it is what makes everything you build at this tier profitable.

## Certification Pathway

- **Frontier Specialist — Agent Orchestration:** Pass all 7 module exams in this course
- **CADE Specialist (meta-credential):** CADE Certified + 3 specialist badges
- **CADE Distinguished:** CADE Certified + 6 specialist badges

Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush, take the time to build something real first.

---

Ready? Take the Cost Optimization and Model Selection Exam →
