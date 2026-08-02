"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_bio_combinatorics_calculator.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "bio-combinatorics-calculator"
    names = live_client.list_examples()
    assert "combination_10_choose_3" in names
    assert "iupac_rydh" in names
    assert "crispr_scaling" in names


def test_run_combination_example(live_client: PepkioClient):
    """C(10,3) = 120 combinations."""
    inp = live_client.get_example_input("combination_10_choose_3")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("ready") is True
    # The tool returns exact BigInt count as string
    assert result.result.get("count_exact") == "120"
    assert result.result.get("count_formatted") is not None
    assert result.result.get("interpretation") is not None


def test_run_index_multiplex_example(live_client: PepkioClient):
    """8 × 12 = 96 dual-index combinations."""
    inp = live_client.get_example_input("index_multiplex_96_well")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("ready") is True
    # 8 * 12 = 96
    assert result.result.get("count_exact") == "96"


def test_run_iupac_example(live_client: PepkioClient):
    """IUPAC degeneracy of primer RYDH."""
    inp = live_client.get_example_input("iupac_rydh")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("ready") is True
    # R=2, Y=2, D=3, H=3 → 2*2*3*3 = 36
    assert result.result.get("count_exact") == "36"


def test_run_crispr_scaling_example(live_client: PepkioClient):
    """CRISPR cell scaling: 62500 guides, 200x coverage, 2 replicates, MOI 0.3."""
    inp = live_client.get_example_input("crispr_scaling")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("ready") is True
    # Should return count_exact and interpretation
    assert result.result.get("count_exact") is not None
    assert result.result.get("interpretation") is not None


def test_run_custom_input_permutation(live_client: PepkioClient):
    """Custom permutation: P(5,2) = 20."""
    result = live_client.run({"mode": "permutation", "n": 5, "r": 2})
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("count_exact") == "20"
