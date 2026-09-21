# What If Your AI System Could Predict the Blast Radius of a Release Before You Ship It?

AI engineering now has gateways, tracing, evaluations, prompt registries, routing, drift detection, and agent observability. But a release still leaves an uncomfortable question:

**What production behavior is likely to move because of this change?**

AICI — AI Change Intelligence — explores that problem.

## The idea

AICI is a pre-release impact engine for AI/ML/LLM systems. It treats a release as a behavioral-system change rather than only a Git diff.

A release can change a model, prompt, retrieval index, tool schema, guardrail, memory policy, or inference configuration. Different cohorts can experience very different effects.

AICI combines:

Change contract
→ dependency graph
→ historical behavior
→ affected cohorts
→ risk model
→ release policy

The output is an explicit ALLOW, REVIEW, or BLOCK decision with evidence and model contributions.

## Why cohorts matter

A global regression rate can hide the real blast radius.

For example:

General traffic: 0.8% regression
Billing: 6.9%
Refund workflows: 8.4%
Tool-calling agents: 11.2%

The average is not enough. AICI treats cohorts as first-class inputs.

## The risk model

The reference implementation contains a dependency-free logistic learner using:

- change density
- dependency centrality
- cohort exposure
- historical regression
- latency delta
- cost delta
- incident rate
- change-kind diversity

The model is deliberately explainable. It is a decision-support component, not an oracle.

## Model versus policy

AICI keeps prediction separate from organizational policy.

The model estimates risk.

The policy determines what risk is acceptable.

For example:

review_at = 0.50
block_at = 0.75
max_affected_traffic = 0.90

Different workloads can therefore use different release controls without changing the prediction engine.

## Why this matters for MLOps and LLMOps

The larger lifecycle is:

Build → Evaluate → Release → Observe → Learn → Improve

AICI focuses on the transition between learning from previous releases and deciding how the next release should be introduced.

Historical production evidence becomes an input to release engineering.

## Connection to AI provenance

AICI complements AI runtime provenance systems.

A provenance system answers:

What actually happened?

AICI asks:

Given what happened before, what could this proposed change affect?

That creates a useful loop:

AICI predicts impact
→ release
→ runtime evidence records behavior
→ observed outcomes
→ next AICI forecast

## Design principles

The core is provider-neutral and dependency-light.

The system should work with AI applications regardless of whether they use a hosted model, local model, custom inference service, agent framework, or a traditional ML pipeline.

The abstraction is intentionally simple:

what changed
+ where it changed
+ who it can affect
+ what history says
= release impact forecast

## Current implementation

The public reference implementation includes:

- typed change contracts
- dependency graph construction
- historical outcome ingestion
- explainable feature extraction
- logistic risk learner
- cohort impact scoring
- configurable release gates
- JSON schema
- CLI
- deterministic examples
- unit tests
- GitHub Actions CI
- architecture and roadmap documentation

## What comes next

The roadmap includes OpenTelemetry ingestion, AIBPE manifest integration, calibrated probabilities, feature-store interfaces, PR comments, model-registry adapters, scheduled retraining, Prometheus metrics, dashboards, signed evidence bundles, policy-as-code, and shadow-release learning.

The long-term direction is an AI release-engineering control plane where production evidence continuously informs the risk of the next AI change.

The central question is simple:

**Before changing an AI system, can we estimate what behavior is likely to move — and show the evidence behind that estimate?**

That is what AICI is built to explore.

Project: AICI — AI Change Intelligence
Focus: MLOps, LLMOps, AI reliability, release engineering, ML risk modeling
License: Apache-2.0
