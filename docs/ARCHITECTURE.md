# Architecture

AICI has five layers:

1. Change contract — typed description of what changed.
2. Evidence graph — connects changed AI components to historical cohorts and releases.
3. Feature engine — converts graph topology and historical behavior into numeric features.
4. Risk model — dependency-free logistic learner in the reference implementation; pluggable in production.
5. Release gate — policy layer that turns a probabilistic forecast into an explicit operational action.

## Why a graph?

AI behavior is rarely coupled to one artifact. A retrieval index can affect a prompt, a prompt can alter tool selection, and a model migration can change latency and output structure. A flat change list loses this relationship.

## Why cohorts?

Average metrics hide blast radius. A release can look healthy globally while breaking a small but important task family. Cohorts make impact distribution explicit.

## Why keep model and policy separate?

The model estimates risk. The organization decides what risk is acceptable. Keeping those concerns separate makes the system auditable and configurable.
