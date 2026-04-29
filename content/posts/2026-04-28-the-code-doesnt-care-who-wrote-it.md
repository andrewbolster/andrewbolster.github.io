---
title: "The Code Doesn't Care Who Wrote It: Why Context, Not AI Fear, Will Define Modern Application Security"
date: 2026-04-28T00:00:00+00:00
draft: true
categories: [AI, Security]
tags: [AI, application security, AppSec, DevOps, LLM, code generation, context, vibe coding, SAST, vulnerability management, Black Duck]
description: "Originally published on DevOps.com — why the AI authorship debate misses the real challenge in modern application security."
---

*This post was originally published on [DevOps.com](https://devops.com/the-code-doesnt-care-who-wrote-it-why-context-not-ai-fear-will-define-modern-application-security/) on April 28, 2026.*

---

AI has already arrived in the software development lifecycle; not as a pilot program or controlled experiment, but as an everyday reality. Developers are using AI coding assistants to generate functions, refactor modules, review pull requests, and accelerate delivery, often in direct tension with corporate policies meant to limit or control that use.

While it's tempting to consider this some kind of 'Shadow AI' or 'Governance Failure', it is a signal of things to come in this brave new world of AI-accelerated software engineering.

Recent industry surveys show that [well over half of developers now rely on AI coding assistants](https://www.blackduck.com/resources/analyst-reports/state-of-devsecops.html) in their daily work, with many using them frequently or constantly. At the same time, more than three-quarters of organisations have formal policies that restrict or prohibit that same usage. From a security perspective, that tension is understandable but may be misplaced, because from the standpoint of application risk, the code itself doesn't care who wrote it.

Whether a snippet, a function, a module, or a review was produced by a human engineer, a junior intern, an open source package, or the latest frontier language model is ultimately irrelevant. Vulnerabilities don't discriminate based on authorship. Licenses don't behave differently because the code was "AI-generated". The risk profile of an application is defined by what is deployed, not by how human or virtuous or compliant the development process appears on paper.

AI is not introducing a new category of security threats. It is acting as an accelerant for risks that already existed.

## A Throughput Problem, Not a Threat to Singularity

The rise of large language models and agentic development tools has dramatically increased the speed at which software is written, modified, and shipped. Codebases are growing faster than most AppSec programs were designed to handle. Over the past five years, average file counts have [grown by more than 200%](https://www.blackduck.com/resources/analyst-reports/open-source-security-risk-analysis.html), while vulnerability volumes have increased at a similar pace — doubling in some ecosystems in a single year.

This isn't a "security singularity." It's the same fundamental challenge application security has always faced: keeping feedback loops intact while systems scale.

Unfortunately, many security pipelines still scale linearly in a world that is now exponential. Nearly 60% of teams deploy to production daily or more frequently, yet a large proportion still rely on manual security testing. Even among mature organisations, most test less than two-thirds of their application portfolios. Unsurprisingly, more than 80% of teams report that security testing slows development.

"AI" didn't create this bottleneck, but it has exposed it.

When releases outpace review, organisations respond with exceptions, escalations, and deferred remediation. Feedback arrives weeks or months after the relevant code was written, long after the developer context has dissolved. The result is a familiar spiral: growing backlogs, increasing noise, and diminishing trust in security outputs.

## The Confidence Paradox

That erosion of trust shows up clearly in how security teams describe their own effectiveness. Nearly 90% of security professionals express confidence in their organisation's ability to manage AI-related risks; yet a majority also describe the alerts they receive as "mostly noise."

High confidence. Low discrimination.

This paradox isn't caused by bad tooling. It's caused by missing context.

For years, the industry has tolerated high false-positive rates in exchange for theoretical completeness. That trade-off becomes untenable when AI-accelerated development floods pipelines with findings faster than teams can triage them. Every noisy alert consumes human attention, delays delivery, and reduces the likelihood that truly meaningful issues are addressed in time.

The solution isn't more alerts. It's better information, earlier.

## What AI Knows and What It Doesn't

The latest generation of Large Language Models are exceptionally good at sampling general patterns from historical data that they've been trained on. That's why they're effective at writing syntactically correct code or identifying common vulnerability classes. But there are entire categories of knowledge they fundamentally lack:

- Your organisation's specific threat model
- The historical triage decisions your teams have made, and why
- Architectural context behind prior trade-offs
- Business priorities shaping acceptable risk
- The real-time state of incidents, remediation, and delivery pressure

Attempting to "fix" these gaps through fine-tuning or prompt engineering has proven expensive and brittle. Business and technical context evolves too quickly for static retraining to keep pace. This isn't a model‑capability problem; it's a knowledge topology problem.

Which leads to a critical shift in perspective: securing AI-driven development isn't about making models smarter. It's about giving them the right context at the right moment. Preventing security issues before they even hit the editor, let alone the build pipeline.

## Context is the Differentiator

Organisations that succeed with AI-powered security aren't those with the most advanced models. They are the ones that have been deliberate about curating and governing context. In practice, we see that context falls into three distinct categories:

**Facts.** Objective, structured, verifiable data: known vulnerabilities, security advisories, SBOMs, license identifiers, component versions, and severity scores. These are table stakes, but essential ones nonetheless. At scale, this means billions of commits, millions of components, and decades of curated security intelligence.

**History.** The hardest (and most valuable) context to acquire and maintain. Not just what was found, but what was triaged, accepted, rejected, reopened, and remediated over time. History captures organisational reality: why certain risks were tolerated, how threat models evolved, and which patterns repeatedly failed. Lose this, and you lose institutional wisdom.

**Opinion.** Expert judgment, encoded and scaled. This is what turns dozens of raw findings into actionable priorities. It reflects how experienced assessors reason about risk; not abstractly, but in practice. Opinion transforms data into signal.

Individually, these elements are limited; A system with only Facts is a database. A system with only History is a log. A system with only Opinion is a consultant you can't afford to scale. Together, they form something more powerful: context-aware security.

## Participating With Agents—Constructively

AI agents can absolutely help absorb development velocity, but only if they operate within this richer context. Treated correctly, agents become natural language interfaces to lived security knowledge. They can check AI-generated code for license risk before it hits a repository. They can suggest remediations aligned with prior decisions. They can help developers understand *why* a finding matters, not just *that* it exists.

Crucially, this approach shifts security left without shifting blame. The goal is not to audit authors (human or machine) but to support better decisions in the moment that they're made.

## The Scalable Path Forward

Regulatory pressure is increasing. Reporting timelines are shrinking. Budgets are tighter. In this environment, the question is not how to run more scans faster. It's how to provide the right security context directly inside the development workflow, before pipelines saturate and feedback loops collapse.

AI didn't make application security harder. It made existing scaling inefficiencies impossible to ignore.

The code doesn't care who wrote it. What matters isn't chasing SWE benchmarks or PR merge rates for every bot or agent or vendor that tries to sell you on something, but what decision support your agentically enhanced developers and security program managers can bring to bear in situ to prevent security risks before they hit your editor, and accelerate decision making if a security risk does.

That's how to build True Scale Application security, at the speed of AI.
