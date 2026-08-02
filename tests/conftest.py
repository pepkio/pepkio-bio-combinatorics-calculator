"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "tool_id": "bio-combinatorics-calculator",
        "title": "Bio Combinatorics Calculator",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "combination_10_choose_3",
                "input": {"mode": "combination", "n": 10, "r": 3},
                "output": {"ready": True},
            },
            {
                "name": "index_multiplex_96_well",
                "input": {"mode": "index_multiplex", "choices_per_position": [8, 12]},
                "output": {"ready": True},
            },
            {
                "name": "iupac_rydh",
                "input": {"mode": "iupac_degeneracy", "iupac_sequence": "RYDH"},
                "output": {"ready": True},
            },
            {
                "name": "crispr_scaling",
                "input": {
                    "mode": "crispr_cell_scaling",
                    "library_size": 62500,
                    "coverage_per_guide": 200,
                    "replicates": 2,
                    "moi": 0.3,
                },
                "output": {"ready": True},
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_test_comb_123",
        "status": "completed",
        "result": {
            "ready": True,
            "count_exact": "120",
            "count_formatted": "120",
            "interpretation": "C(10,3) = 120 combinations",
            "methods_text": "Combination without repetition: n! / (r! × (n-r)!)",
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_test_comb_123",
        "permalink": "https://tools.pepkio.com/r/run_test_comb_123",
    }
