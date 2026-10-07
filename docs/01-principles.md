# 01 — Principles

## Contents

1. Black boxes, not conversations
2. Every question is a defect upstream
3. Evidence over narrative
4. Bounded effort, then a human
5. One pipeline, many deployments
6. Built for humans and agents

## 1. Black boxes, not conversations

Each node is a black box. It sees its input and the rules; it emits one structured
handoff. Agents do not chat, negotiate, or leave free-form questions for each other.
Notes are allowed only inside the handoff's defined fields.

## 2. Every question is a defect upstream

If a receiving agent needs to ask a question, the producing node's output was incomplete.
The fix is to tighten the upstream contract, not to let the downstream agent guess or ask.
The **Intake** node exists to front-load ambiguity so later nodes have nothing left to decide.

## 3. Evidence over narrative

Statuses are a small, fixed vocabulary borrowed from change management and ticketing.
A failure is never "it didn't work": it is the command, the output, and the steps to
reproduce it, so the next agent can verify the fact rather than trust a story.

## 4. Bounded effort, then a human

Each node gets three attempts. After that, the work stops and lands with a human,
together with the full record of what was tried. No infinite loops, no silent thrashing.

## 5. One pipeline, many deployments

The factory is generic. The same nodes run in a home lab and in a regulated company.
Differences (who must approve, what may deploy, which providers are allowed) live in
**profiles**, not in forks of the pipeline.

## 6. Built for humans and agents

Files are small and modular, lead with a contents list, and state rules plainly so the
smallest model at medium effort can follow them and a human can audit them quickly.
