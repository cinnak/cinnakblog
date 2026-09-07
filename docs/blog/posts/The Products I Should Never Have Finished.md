---
date: 2026-09-07
draft: false
title: The Products I Should Never Have Finished
categories:
  - Building
description: What two years of AI-assisted side projects taught me about product judgment, implementation speed, and knowing when not to build.
tags:
  - Vibe Coding
  - Product Development
  - AI-Assisted Software
comments: true
---

My GitHub profile looks productive.

There are AI tools, personal dashboards, reading apps, calendar analyzers, and an investment system. Many have tests, deployment pipelines, polished interfaces, and documentation that calls them “production-ready.”

Most never became part of my life.

They became codebases I kept improving until I ran out of patience or found something else to do. For a long time, this bothered me more than I wanted to admit.

Was I bad at finishing? Did I lack focus? Did I simply have poor product sense?

The answer I eventually arrived at was less flattering, but more useful:

> **I was not forcing myself, early enough, to decide which products should never be fully built.**

<!-- more -->

## My GitHub Looked Productive

Over the last two years, I have built with Codex, Claude Code, Google Antigravity, OpenCode, and Hermes.

Different agents produced the same effect: vague ideas became working software at a speed that still feels unreal.

One calendar project arrived in a single commit containing 45 files and more than 10,000 lines. EmotionFlow accumulated 35 commits across eight active days. My grid-trading strategy website reached 76 commits across twelve.

These numbers do not prove that the code was bad. Much of it built, passed tests, and worked as specified.

They show that I was making product, architecture, data, and interface decisions faster than I could learn whether those decisions were right.

Before AI coding, implementation friction was an accidental filter. If a feature took two weeks, I had reasons to question it first. When it takes an afternoon, questioning it can feel slower than simply making it.

So I made it.

Then I made the settings page, the analytics view, the export flow, the polished empty state, and the deployment pipeline for a product I had barely used.

AI did not remove the need for product judgment. It removed the delay that used to force some judgment to happen.

## The Same Ideas Kept Returning

The clearest example is my recurring attempt to understand my life through Google Calendar.

In 2024, I built SyncDay. In 2025, I built Calendar Vibes. In 2026, I built Calendar Wise.

Each version was more capable. The latest had read-only Google Calendar sync, a local database, category extraction, overlap-aware calculations, goals, trends, and a carefully designed review interface.

But the question underneath it kept changing.

Was I tracking time, reviewing habits, or comparing intention with reality? Did a calendar event represent what I planned to do or what I actually did? Should the system infer goals, ask for them, or avoid them?

Calendar Wise added scheduled email reports, then removed them the next day. Goals disappeared and later returned in another form. Even its documents disagreed about the product’s primary purpose.

I was not iterating around a stable idea. I was implementing my way toward the question.

My grid-trading strategy website followed a similar path. It began as a cost calculator and grew into a strategy engine with market-data fallbacks, backtesting, transaction reconstruction, account replay, encrypted sync, and CI/CD.

The engineering became increasingly defensible. Yet after several “completed” milestones, I opened the deployed product and still could not comfortably answer the only question that mattered:

> What, if anything, should I pay attention to today?

One screen could warn that historical evidence did not support a strategy, then show precise buy and sell prices below. Several variants offered different “next” prices. The code was increasingly correct; the product remained hard to trust.

There is nothing wrong with using software as a thinking medium. A prototype can reveal what I could not articulate beforehand.

My mistake was letting each exploratory implementation harden into a product before I had learned enough from it.

I did not close a failed hypothesis. I reincarnated it with a new name and a better stack.

## I Had Product Taste, Not Product Discipline

I had been circling this problem for a long time without being able to name it.

I knew many of the products were not useful enough. But every time I noticed a problem, I could also imagine a fix. With an AI coding agent, that fix was cheap enough to attempt, so the project continued.

Eventually, I brought the question to Codex directly. We first discussed my grid-trading strategy website and Calendar Wise. Then I realized I was still framing the problem too narrowly.

I asked it to look across two years of repositories instead.

The same development signature appeared repeatedly: a large initial build, a burst of fixes and polish, several changes to the product’s purpose, and then silence when my attention moved elsewhere.

During that conversation, one distinction finally made the pattern clear.

Product taste is recognizing that something feels wrong after seeing it. Product judgment is deciding what matters before and during construction. Product discipline is stopping when the evidence no longer justifies more work.

I had product taste. I could see contradictory actions, meaningless dashboards, overloaded pages, and software that worked without answering a human question.

What I lacked was the discipline to make that judgment early enough.

It was easier to request another revision than to admit that the premise might be weak. A new feature produced visible progress. A rejected idea produced no interface, no deployment, and no satisfying commit graph.

AI coding agents made this easier to avoid. They could always find a real inconsistency, write a sensible plan, implement a fix, add tests, and identify the next priority.

None of those steps was irrational. Together, they formed an endless loop around products that might have needed a pause rather than another improvement.

The problem was not that the agents gave me bad code. It was that I kept asking powerful local optimizers to settle a question outside the codebase: whether the larger objective was still worth pursuing.

## What I Will Do Differently

I do not want to stop vibe coding. Fast, playful construction is useful, and some projects should last only a day. A small experiment is not a failed product simply because I never return to it.

What I need is a harder boundary between an experiment and a product.

An experiment can help me discover the question. It can be messy, excessive, and disposable. But it does not earn another round of development merely because I can see how to improve it.

It has to earn that work through use.

My new rule is simple: after building a prototype, I must stop building long enough to observe it. If I do not voluntarily use it, or if it does not improve a real decision, the next task is not a redesign.

The next task may be to archive it.

I am not sure this rule will be easy to follow. The pleasure of watching an idea become software is immediate. The evidence that it deserves to exist arrives slowly, if it arrives at all.

AI can accelerate construction. It cannot accelerate the week that must pass before a weekly review, the repeated moments needed to form a habit, or the time required to learn what I actually value.

The next skill I need is not building faster. AI has already given me that.

It is deciding, while an idea is still small, whether it deserves to become a product at all.
