# uv-python-workflow

A modern Python workflow powered by [uv](https://github.com/astral-sh/uv).
This template integrates **CI/CD, Docker, pre-commit hooks, and Pyright type checking** for a reproducible and maintainable development setup.

## ✨ Features

- 🚀 **uv** for fast, reliable dependency management
- ✅ **pre-commit** hooks (lint, format, type-check) (uv add --dev pre-commit)
- 🔎 **Pyright** for static type checking (uv add --dev "pyright[nodejs]")
- 🐳 **Dockerfile** for reproducible environments
- 🔄 **CI/CD (GitHub Actions)** with linting, formatting, type checking, and tests

## 📦 Getting Started

```bash
# Install dependencies
uv sync

# Run app
uv run main.py
```

## 🧹 Pre-commit Hooks

Configured with [pre-commit](https://pre-commit.com/):

```bash
pre-commit install --install-hooks --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
pre-commit run --all-files  # Run all hooks on all files (only needed once after installation)
```

## 🐳 Docker

```bash
docker build -t uv-python-workflow .
docker run --rm uv-python-workflow
```

## 🔄 CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs:

- Dependency install with `uv`
- Linting & formatting with `ruff`
- Type checking with `pyright`
- Tests with `pytest`

## 🧭 Commitizen (Conventional Commits)

```powershell
# Install (dev)
uv add --dev commitizen

# Stage changes
git add .

# Interactive commit
cz commit or cz c

# Semantic version bump + tag (optional)
cz bump --yes
```
