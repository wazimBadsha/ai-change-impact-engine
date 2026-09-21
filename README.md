# AI Change Impact Engine

A lightweight, explainable MLOps/LLMOps engine for estimating the behavioral blast radius of AI system changes before release.

## Why

AI systems change across models, prompts, retrieval, tools, policies, infrastructure, and dependencies. A passing evaluation suite does not necessarily tell you which production cohorts may be affected.

AI Change Impact Engine turns historical evidence and dependency structure into an explicit release-risk forecast and policy decision.

## Pipeline

Change -> dependency graph -> historical evidence -> behavioral cohorts -> risk model -> impact forecast -> release policy

## Features

- Change and dependency graph representation
- Cohort-aware historical evidence
- Explainable feature extraction
- Dependency-free logistic risk model
- Impact forecast with contributing factors
- ALLOW / REVIEW / BLOCK policy evaluation
- JSON schemas and deterministic examples
- CLI for local release analysis
- Unit tests and GitHub Actions CI

## Status

v0.1.0 — working reference implementation. Designed as an extensible foundation for production MLOps/LLMOps integration; not a claim of production certification.

## Quick start

python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/release_forecast.py

## Architecture

See docs/ARCHITECTURE.md, docs/ROADMAP.md, and medium/medium-post.md.

## Relationship to AI runtime provenance

This project complements AI runtime evidence systems: provenance tells you what happened; Change Impact Engine asks what a proposed change may affect before release.

## License

Apache-2.0
