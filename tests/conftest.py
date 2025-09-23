"""
Pytest configuration to ensure `src.*` imports work during tests.

This adds the project root directory to ``sys.path`` so that the ``src``
directory is importable as a top-level package in tests.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
