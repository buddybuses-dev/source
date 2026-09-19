# Layer 6: Cloud & Compute — Study Guide

## The Engines That Run Your App Behind the Scenes

This is the study guide. Everything for Cloud & Compute is on this page — there's nothing to download.

## What This Study Guide Covers

This study guide covers Layer 6: Cloud & Compute — where your app actually runs and what it costs you every month. When your app is live on the internet, it's running on somebody else's computer in a data center. That computer has processing power, memory, and storage — and somebody has to pay for it. Cloud computing is the system that provides those computers on demand, and this layer is about understanding what you're paying for.

You're not going to set up servers by hand. Modern cloud platforms — like AWS, Google Cloud, and Azure — let you rent exactly the computing power you need, and many hosting platforms (Vercel, Netlify, Railway) handle the cloud details for you. Your job is to understand what's happening underneath so you don't get surprised by a bill, pick the right setup for your project, and know when your app needs more power (or less).

This study guide walks you through the concepts, tools, and checkpoints you need to pass the Cloud & Compute certification exam.

## Why It Matters

Cloud costs are the most common surprise bill in software. Your app works, your users are happy, and then you get an invoice that makes your stomach drop. It happens because most vibecoders don't understand what they're being charged for until the bill arrives. A function that runs every time a user loads a page might cost nothing with 10 users — and hundreds of dollars a month with 10,000 users.

AI tools will pick cloud services for you, but they optimize for getting things working — not for keeping costs down. They'll happily generate code that calls an expensive API on every page load, or set up a database that charges per-read in a way that scales linearly with your traffic.

This study guide teaches you how cloud costs work so you can ask the right questions, catch expensive patterns before they ship, and keep your app running without going broke.

## Certification Goal

You understand what cloud compute is, where your app runs, what you're being charged for, how to read a cloud bill, and how to avoid the most common cost surprises.

## What You Need to Know

You don't need to be a cloud architect. You need to understand the basics of what you're paying for so you can make smart decisions and avoid nasty surprises.

- **What "the cloud" actually means:** The cloud is just other people's computers in data centers around the world. When you deploy your app to Vercel or Railway, it runs on computers owned by Amazon (AWS), Google (GCP), or Microsoft (Azure). You rent the computing power instead of buying your own servers. It's like renting an apartment instead of buying a house — flexible, but the rent can change.
- **Serverless functions (code that runs on demand):** Serverless doesn't mean there's no server — it means you don't manage the server. Your code sits idle until someone triggers it (like a user clicking a button), runs for a few milliseconds, and stops. You pay only for the time your code actually executes. It's like a taxi — you pay per ride, not for owning the car. Most Vercel and Netlify apps use serverless under the hood.
- **How cloud billing works:** Cloud services charge based on usage — how many times your functions run, how much data you store, how much data you transfer. The tricky part: these charges add up in ways that aren't obvious. A function that runs 100 times a day might cost pennies. The same function running 100,000 times a day costs real money. You need to know where to look.
- **What "compute" means:** Compute is processing power — the actual CPU time and memory your app uses to do work. Loading a webpage, processing a form, resizing an image — these all use compute. More compute means faster results but higher costs. Your job is finding the balance: enough power to keep things fast, not so much that you're wasting money.
- **Free tiers and their limits:** Most cloud platforms offer a free tier — a certain amount of compute, storage, and data transfer at no cost. This is perfect for getting started, but there are hard limits. If your app suddenly gets popular and exceeds those limits, you start getting charged. Know where those limits are before your app goes viral.

## Your Toolkit

At Tier 1, your hosting platform handles most cloud decisions. These tools help you understand what's happening underneath.

- **Your hosting platform's billing dashboard (Vercel, Netlify, Railway):** The first place to check what you're spending and what's using the most resources. Check this weekly — don't wait for the monthly bill.
- **Cloud provider free tier calculators:** AWS, GCP, and Azure all have pricing calculators that show you what things will cost before you commit. Use them before picking a service.
- **Usage monitoring (built into your hosting platform):** Dashboards that show how many function invocations, how much bandwidth, and how much storage your app is using. These numbers tell you if a cost spike is coming.

## Certification Exam Topics

Every exam question is scenario-based. You'll see a real situation and need to identify what's right, what's wrong, or what to do next.

- **Cloud basics:** Your app is hosted on Vercel. Can you explain, in plain language, where your app is physically running and who owns that computer?
- **Cost awareness:** Your Vercel bill jumped from $0 to $45 this month. What's the first thing you check, and what could have caused it?
- **Serverless understanding:** Your app has a function that resizes user-uploaded images. It runs 50,000 times this month. Is this a serverless use case, and what should you watch for cost-wise?
- **Free tier limits:** You're on Vercel's free plan with 100,000 serverless function invocations per month. Your app gets featured on social media. What happens when you hit the limit?
- **Compute vs. storage:** Your cloud bill shows high compute charges but low storage charges. What does this tell you about how your app is using resources?
- **Data transfer costs:** Your app sends large images to users on every page load. How does this affect your cloud bill, and what's a simple fix?
- **Platform selection:** You need a simple API that responds to 500 requests per day. Should you use serverless functions or a dedicated server? Why?
- **Cost prevention:** Your AI tool generated code that calls an external API on every page load — even for data that doesn't change often. What's the cost risk, and how would you describe the fix to AI?

## Common Pitfalls

These are the mistakes vibecoders make most often with cloud and compute. No judgment — they're easy to make. But if you recognize any of them in your own workflow, fix them before sitting for the exam.

- **Never checking your cloud bill until the end of the month.** By then a runaway function or misconfigured service has been burning money for weeks. Check your usage dashboard weekly at minimum.
- **Assuming "serverless" means "free."** Serverless means you pay per execution. If your function runs on every page load and your app gets popular, those pennies add up to real money fast.
- **Letting AI pick cloud services without understanding the pricing model.** AI optimizes for working code, not cost-effective code. Always ask "what does this cost at 1,000 users? At 100,000 users?"
- **Running the same compute resources 24/7 when your app only has traffic 8 hours a day.** You're paying for 16 hours of empty servers. Auto-scaling and serverless exist for exactly this reason.
- **Ignoring data transfer costs.** Moving data between cloud services and out to your users often costs more than the compute itself. Large images, frequent API calls, and uncompressed assets add up quickly.
- **Not setting up billing alerts.** Every cloud platform lets you set a budget and get notified when you're approaching it. Set this up on day one, not after your first surprise bill.

## Self-Assessment Checklist

Before you take the exam, run through these questions. Every "no" is something to work on.

- Can you explain, in plain language, where your app's code actually runs when a user visits your site?
- Do you know what you're currently paying for cloud services each month, and which services cost the most?
- Have you set up billing alerts so you'll know if your cloud spending spikes unexpectedly?
- Can you explain the difference between serverless functions and a traditional server, and why it matters for your bill?
- Do you know what your app's free-tier limits are and how close you are to exceeding them?
- If your app suddenly got 10x more traffic tomorrow, do you know what would happen to your costs and performance?
- Can you identify at least one place in your app where caching or optimization could reduce your cloud bill?

## AI Audit Prompt Template

Copy this prompt into your AI coding tool to get a quick health check on your cloud and compute setup. It checks the same things the certification exam covers.

> Review my app's cloud and compute setup and check the following. For each one, tell me pass or fail with a specific example:
>
> Cost efficiency: Are there any functions, queries, or API calls that run more frequently than necessary, and could caching or batching reduce the compute cost?
>
> Resource sizing: Is the app using more compute power or memory than it actually needs, or is it under-provisioned and at risk of slowdowns?
>
> Serverless configuration: Are serverless function timeouts, memory limits, and concurrency settings appropriate for the workload?
>
> Data transfer: Are there large assets (images, videos, files) being served directly from the compute layer instead of through a CDN?
>
> Scaling readiness: If traffic increased 10x, which parts of the infrastructure would fail first, and what would need to change?
>
> Billing visibility: Are there billing alerts, budget limits, or cost monitoring dashboards set up to catch spending anomalies?
>
> Give me an overall score out of 6 and list the top 3 things to fix first.

## What's Next

Once you've gone through this study guide and can answer "yes" to the self-assessment checklist, you're ready for the Layer 6 certification exam at your target tier.

The best way to prepare: look at your actual cloud bill. Open your hosting platform's dashboard and study what you're paying for. Try the pricing calculator for a new service before you add it. Ask your AI tool to estimate the cost of a feature at different traffic levels. The exam tests whether you understand what you're spending and why — and that understanding comes from looking at real numbers.

## Certification Pathway

Associate Builder: Pass all 13 layers at Tier 1 Certified Builder: Pass all 13 layers at Tier 1 + Tier 2 MADE Certified: Pass all 39 tier exams + capstone project Each exam requires 80% to pass. You can retake after a 24-hour cooldown. No rush — take the time to build something real first.

———

Ready? Take the Cloud & Compute Exam →
