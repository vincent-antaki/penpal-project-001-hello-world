# 001 Hello World

A starter sketch demonstrating the basic structure of a Penpal project.

## Overview

This project serves as a template and minimal working example for creating SVG outputs within the monorepo environment. It depends on penpal-core.

## Structure

- `main.py`: Contains the `run(params, output_path)` function.
- `params.py`: Defines the experimental parameters (e.g., coordinates, sizes).

## Execution

### From the root of the monorepo

You can do a formal run (requires clean Git state) :

```bash
python tools/runner.py 001_hello_world
```

Or a development run (skips Git checks):

```bash
python tools/runner.py 001_hello_world --dev
```

### From within the project

