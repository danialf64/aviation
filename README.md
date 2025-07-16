# Aviation

A simple model of global aviation.

## Model/Analysis

This repository contains a single analysis script. [`aviation.py`](aviation.py) which implements the simple model for global aviation.
It outputs the required global fleet.
To execute the script, run:

```
uv run python aviation.py
```

## Dependencies

This repository uses [uv](https://docs.astral.sh/uv/) for comprehensive project management.
Dependency bounds are defined in [`pyproject.toml](pyproject.toml) and the locked environment is specified in [`uv.lock].

The dependencies can be installed using the following code:

To install the dependencies using a [virtual environment](https://docs.python.org/3/library/venv.html) the following command can be used:

```
uv sync
```

## Developer Guide

This repository uses [MkDocs](https://www.mkdocs.org/) to generate a static documentation site for users.

The source files for the site can be found in the `docs` folder.

The site configuration can be found in the [mkdocs.yml](mkdocs.yml) file.

To serve the site locally run `mkdocs serve`.
