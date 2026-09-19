# Module 8 Capstone: Build and Publish a Real Website

**Time:** about 90 minutes, entirely hands-on. You finish with a live URL.

## Objectives

Ship a real website to the public internet using everything from Modules 1 through 7: briefing, plan mode, iteration, CLAUDE.md, git and GitHub, and verification. Without writing code yourself.

A web agency would quote four figures for what you're about to do in an afternoon. That's not a knock on agencies. That's the point of the last seven modules.

---

## 8.1 Choose your build

Pick whichever one is real for you. Real stakes make real learning. A site you actually care about will teach you twice as much as a throwaway.

- **A.** A personal or professional site (about, services or work, contact)
- **B.** A small-business site for someone you know (a real client!)
- **C.** A hobby or interest site (a guide, a collection, a local resource)

Whatever you pick, the bar is the same: at least 3 pages or sections, looks respectable on a phone, live on the internet at the end. No partial credit on that last one.

## 8.2 Stage 1: Brief and plan (use plan mode)

Make a new project folder, put it under git from minute one, and switch to plan mode. Then give the brief. Yours will look something like:

> "I want a simple, fast, professional website for [X]. The audience is [who]. It needs: [pages/sections]. Tone and look: [for example, clean and warm, not corporate]. I'll deploy it free on Cloudflare Pages or GitHub Pages. Pick whichever is simpler for this project and tell me why. Keep the tech as boring and low-maintenance as possible, because I'm a beginner maintaining this alone. Propose a plan including the folder structure and what each page contains."

Two points of technique, and the first one is worth the module by itself.

You named the *qualities* of the technology (boring, low-maintenance) rather than the technology. Claude picks the stack; you gave it the selection criteria. This is how a non-expert supervises expert decisions: in websites, in hiring, in everything. You don't need to know the answer. You need to know what a good answer has to satisfy.

Review the plan like a client, not an engineer. Are the pages right? Is anything missing? Does the maintenance story sound like something you'd actually keep up with?

Approve the plan and let it build. Then commit.

## 8.3 Stage 2: See it, shape it

> "Run this site locally so I can see it in my browser."

You'll get a local address like `http://localhost:8080`. Open it. Now iterate the way you practiced in Module 3, one targeted correction at a time, checking the browser after each:

- "The headline is weak. Give me five alternatives with a more concrete benefit and less poetry."
- "Make the photos consistent in size and add breathing room between the sections."
- "Show me this at phone width. That menu is broken, fix it."

This stage is interior design, not construction. You point, it moves the couch. Commit at every state you'd be sad to lose. If an iteration makes things worse, "undo that last change." This is exactly why git came before the capstone. You get to experiment like it's free, because it is.

A note on the words: have Claude draft copy from your bullet points, but you own the final text. Read every sentence on the site out loud once. Drafted by AI, approved by a human. Your name is on this.

## 8.4 Stage 3: Pre-flight checks

Delegate the QA, then verify a sample of it yourself:

> "Before we publish: check every link works, check spelling and grammar on all pages, confirm it looks right at phone, tablet, and desktop widths, make sure images are compressed for fast loading, and give me a plain-English report of anything questionable."

Read the report, then spot-check two of its claims yourself. Click a link. View the site at phone width. Trust it, but sample it. That habit, delegate the inspection, then inspect the inspector, is how you scale trust without gambling.

## 8.5 Stage 4: Publish

> "Publish this. Walk me through anything that needs my accounts or my decisions, one step at a time."

What to expect: pushing to GitHub (you learned how in Module 6), connecting the host (Cloudflare Pages and GitHub Pages both deploy free, straight from a GitHub repository), and a couple of browser steps only you can do, like creating an account and clicking authorize. Claude narrates, you click.

Then the moment. A real URL. Open it on your phone, off your wifi. That's the actual internet. That's your site. You shipped it. Send the link to somebody.

Optional, about $10 to $15 a year: a custom domain. "I want this at [yourname].com. Walk me through buying the domain and connecting it." Fifteen minutes of DNS steps that Claude navigates for you.

## 8.6 Stage 5: Make it maintainable

Here's the difference between a project and a demo: what happens next month. Demos die the day after launch. Don't build a demo.

1. > "Write a CLAUDE.md for this project: what it is, how it's structured, how deployment works, and the rules for changes (always check phone width, always commit before big changes, never break existing URLs)."
2. Learn the update loop for future-you: open the folder, run `claude`, describe the change, check it locally, commit, push, and it deploys automatically. Ask Claude to add that recipe to CLAUDE.md too.
3. Test it. Close everything, come back later, ask for one small change (update a sentence, add an FAQ), and push it live. This loop is the real deliverable of the course: a durable ability, not a one-time artifact. The site is proof. The loop is the product.

---

## Wrapping up the course

Look at the shape of what you just did. Brief with quality criteria. Plan before build. Iterate in small corrections. Commit at good states. Delegate QA but sample-check it. Publish. Document for future-you.

None of that is website-specific. That's the template for everything you'll do with an agent from here on: reports, automations, data work, the next tool you build. You didn't learn to make a website. You learned to run an employee that works for $20 a month. The website was just the final exam.

Where to go next:

- Keep the Module 4 recognition checklist around for another two weeks. The reflex is the asset that compounds.
- When a service keeps making you export and copy-paste, revisit MCP (section 7.3). That's your trigger.
- Check `/help` and Anthropic's docs for what's changed since this course was written. The concepts stay stable. The features keep growing. You now have the skill to absorb new features on contact. That was the plan all along.

## Final checkpoint

The course is complete when your site is live at a public URL, the repository is on GitHub with a real commit history (not one giant commit), CLAUDE.md documents the update loop, and you've done one post-launch change end to end.
