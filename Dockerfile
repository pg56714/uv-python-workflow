FROM python:3.12.15-slim-trixie

# Pinned uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

# Use 'code' to avoid confusion with the 'app' directory
WORKDIR /code

# Compile bytecode, avoid symlinks, and use the system Python from the base image
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

# ---------- layer 1: dependencies ----------
# Cache only invalidates when these two files change
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-dev --no-install-project

# ---------- layer 2: application code ----------
COPY . /code

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Run as an unprivileged user
RUN useradd --system --uid 10001 --no-create-home app
USER app

# Put the venv at the beginning of PATH
ENV PATH="/code/.venv/bin:$PATH"

CMD ["python", "main.py"]
