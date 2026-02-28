# NeuralStack Debugger

## Overview
NeuralStack Debugger is a robust python and C++ tooling suite designed to automate AI inference training, evaluation, and benchmarking workflows. It provides architecture-specific optimization algorithms and detailed profiling to resolve critical runtime bugs.

## Key Features
- **Automated Workflows:** Decreases manual compiler overhead tracking time by ~60%.
- **Deep Profiling:** Profiles full inference stacks to identify bottlenecks.
- **Optimization Algorithms:** Accelerates inference speed by ~25% on custom hardware.
- **Bug Resolution:** Helping resolve critical runtime bugs in massively-parallel environments.

## Installation

```bash
pip install .
```

## Usage

To profile an inference application:

```bash
ns-profile --target ./app --duration 10s
```

To visualize results:

```bash
python tools/visualize.py --input profile.json
```
