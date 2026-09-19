# Module 4: Context Window Management — Study Guide

## "Direct AI with the precision, structure, and repeatability that separates professionals from hobbyists."

## What This Module Covers

Every model you direct has a hard ceiling on how much it can hold in working memory at once. That ceiling is the context window, the most misunderstood constraint in professional prompt work. This module teaches you what it actually is, what happens when you approach or exceed it, and why "just paste the whole document in" is the mark of a hobbyist, not a builder.

You will learn the core strategies for material too large or too expensive to hold in one call: chunking, summarization, and retrieval-augmented approaches that pull in only what the task needs. You will also learn prompt compression, and the decision framework for splitting a task across multiple calls versus keeping it in one. This builds directly on the architecture work from Modules 2 and 3.

## Why It Matters

In production, context failures are silent. A support bot handling 10K conversations a day does not throw an error when a long conversation pushes the refund policy out of effective attention. It just starts answering wrong, politely and confidently, and you find out from angry customers, not logs. A data extraction system fed a 200-page contract in one shot does not tell you it skimmed the middle. It hallucinates field values for the sections it lost, and they look as plausible as the real ones.

The cost side is just as real. Tokens are billed on every call, and a bloated context multiplied across thousands of daily runs turns a profitable pipeline into a money leak. Faction builders who master context management ship systems that are cheaper, faster, and more accurate at once, because all three come from one discipline: exactly the right information in front of the model, nothing else.

## Certification Goal

Passing the Module 4 exam proves you can diagnose context-related failures, choose the right strategy for long inputs (chunking, summarization, or retrieval), compress prompts without losing fidelity, and make defensible single-call versus multi-call decisions based on cost, quality, and reliability.

## What You Need to Know

### The Context Window Is Working Memory, Not Storage

The context window is the total token budget for everything in a call: system prompt, conversation history, retrieved documents, and the model's own output. It does not persist between calls. Every call starts from what you explicitly provide, so what you include and exclude is a design decision you own.

### What Gets Pushed Out and What Stays

When inputs grow past the limit, something has to go, and if you have not designed the eviction, naive truncation decides: the oldest turns get cut first, exactly where original instructions and key facts live. Professional systems pin what must survive (system prompt, task spec, critical entities) and compress or drop the rest. Even within the window, material buried mid-context gets weaker attention than material at the edges.

### Chunking: Divide the Document, Not the Task

Chunking splits a long input into pieces the model can process fully, each paired with the complete instruction set. Split on natural boundaries (sections, clauses, records), not character counts, and overlap chunks slightly so facts straddling a boundary are never lost. The failure mode is a chunk stripped of needed context, like a contract clause separated from its defined terms.

### Summarization as State Management

For long-running work, compress the history into a dense summary and carry that forward: "customer on Pro plan, billing dispute over March invoice, refund offered and declined" instead of forty raw turns. The skill is deciding what must survive: decisions, commitments, identifiers, and constraints stay; pleasantries and dead ends do not.

### Retrieval-Augmented Approaches

Store the knowledge base outside the model and retrieve only the passages relevant to the current query. This is how a support bot answers from a 500-page help center while seeing a few pages per call. Retrieval quality becomes your ceiling: if the right passage is not retrieved, the model fails or fabricates, so instruct it to answer only from provided material.

### The Cost, Context, and Quality Triangle

More context is not free and not automatically better. Every added token raises cost and latency, and past a point, irrelevant context degrades quality by diluting attention. The professional target is minimum sufficient context: the smallest input that fully supports the required output.

## Your Toolkit

- **Token Budgeting:** Assign an explicit token budget to each prompt section (system, examples, retrieved context, history, output headroom) and enforce it. A written budget turns context bloat into a reviewable diff.
- **A Chunking Pipeline:** A repeatable workflow that splits documents on semantic boundaries, adds overlap, attaches full instructions to every chunk, and merges results with a reconciliation pass.
- **Rolling Summary Pattern:** A standing prompt that compresses history into a structured state summary at regular intervals, preserving decisions, entities, and constraints while discarding filler.
- **Prompt Compression Pass:** A deliberate editing step that strips redundant phrasing, collapses repeated instructions, converts prose rules into tight lists, and cuts examples that no longer earn their tokens.

## Exam Topics

- Define the context window and identify everything that counts against it, including model output.
- Predict which content is lost first under naive truncation and why that endangers system instructions.
- Explain degraded attention on mid-context material and how to position critical instructions.
- Select and justify chunking, summarization, or retrieval for a given long-document scenario.
- Design a chunking approach with semantic boundaries, overlap, and a reconciliation step.
- Apply prompt compression techniques that reduce tokens while preserving instruction fidelity.
- Analyze the cost impact of context size on a system running 10K conversations a day.
- Decide single-call versus multi-call using quality, cost, and failure-isolation criteria.

## Common Pitfalls

- **Stuffing the full document into every call:** You pay for tokens the model barely attends to, mid-document quality drops, and cost scales with document size instead of task size.
- **Chunking by character count instead of meaning:** Splitting mid-section severs facts from their context, and the model misreads clauses it can only half see.
- **Letting history truncate itself:** When the platform silently drops your oldest turns, your original instructions and the user's stated goal are the first casualties.
- **Summaries that lose load-bearing facts:** A summary that drops an order ID or a prior commitment poisons every downstream call that trusts it.
- **Treating retrieval as infallible:** Untested retrieval means the model fills gaps with plausible fabrications, fatal for systems that must never hallucinate field values.
- **Splitting tasks that need shared context:** Calls that each lack what the others know produce contradictory outputs, like a content pipeline whose sections read as different brands.

## Self-Assessment Checklist

- I can state what counts against the context window and estimate my prompts' token footprint.
- I can predict what gets pushed out of a growing conversation and pin what must survive.
- I can design a chunking strategy with semantic boundaries, overlap, and reconciliation.
- I can write a rolling summary prompt that preserves decisions, entities, and constraints.
- I can explain when retrieval beats full-document context and guard against retrieval gaps.
- I can compress a prompt significantly without losing instruction fidelity.
- I can justify single-call versus multi-call using cost, quality, and failure isolation.

## AI Audit Prompt Template

Give your AI this prompt, with your actual prompts attached, to audit your context management strategy.

> You are a senior prompt engineer auditing my context window management. My system: [describe pipeline, model, context window size, call volume]. My prompts and a sample assembled context: [paste them]. Audit these six areas, reporting findings with severity (critical, warning, minor): 1. Token budget: estimate each section's footprint and flag anything not earning its tokens. 2. Eviction risk: what gets truncated as inputs grow, and whether critical instructions are at risk. 3. Position: flag critical instructions buried mid-context where attention is weakest. 4. Strategy fit: is chunking, summarization, or retrieval the right primary strategy here? 5. Compression: rewrite my most bloated section with fewer tokens and zero loss of fidelity. 6. Call architecture: recommend single-call or multi-call, stating the cost and quality tradeoff. End with the top three changes ranked by impact per hour of work.

## What's Next

Module 5: Prompt Testing and Evaluation puts these strategies under measurement. You will build eval sets, score outputs systematically, and prove your chunking, compression, and retrieval decisions hold up across hundreds of real cases, not the three examples you eyeballed.

## Certification Pathway

Pass this module's exam at 80% (20 of 25 questions) to earn the Module 4 badge. Pass all 7 module exams to earn the Advanced Prompting Specialist badge, certifying you as a Faction builder who directs AI at a professional level.
