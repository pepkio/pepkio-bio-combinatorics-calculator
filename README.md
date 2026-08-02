# pepkio-bio-combinatorics-calculator

Python client for the [Pepkio Bio Combinatorics Calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator) API.

## Install

```bash
pip install pepkio-bio-combinatorics-calculator
# or
uv add pepkio-bio-combinatorics-calculator
```

## API key

```bash
export PEPKIO_API_KEY="your-key"   # tools:run scope
```

Create keys at <https://www.pepkio.com/account/api-keys>.

## Quick start

```python
from pepkio_bio_combinatorics_calculator import PepkioClient

with PepkioClient() as client:
    result = client.run({"mode": "combination", "n": 10, "r": 3})
    print(result.result["count_exact"])   # "120"
    print(result.permalink)
```

## CLI

```bash
# Manifest (no API key needed)
pepkio-bio-combinatorics-calculator manifest
pepkio-bio-combinatorics-calculator manifest --examples

# Run a named example
pepkio-bio-combinatorics-calculator run --example combination_10_choose_3
pepkio-bio-combinatorics-calculator run --example iupac_rydh

# Run custom JSON
pepkio-bio-combinatorics-calculator run --input-json '{"mode":"permutation","n":5,"r":2}'
```

Options: `--api-key`, `--base-url`, `--label`, `--idempotency-key`.

## Environment variables

| Variable | Description |
|---|---|
| `PEPKIO_API_KEY` | Production API key |
| `LOCAL_PEPKIO_API_KEY` | Local dev key (used when `PEPKIO_API_BASE_URL` points to `localtest.me`) |
| `PEPKIO_API_BASE_URL` | Override API host (default: `https://tools.pepkio.com`) |
| `PEPKIO_SSL_VERIFY` | Set `0` to disable TLS verify (auto-disabled for `localtest.me`) |

## Development

```bash
uv sync
uv run pytest tests/test_client.py -v          # unit tests (no API key)
uv run pytest tests/test_integration.py -v     # live API tests
```

## Links

- **Web app:** <https://www.pepkio.com/tools/bio-combinatorics-calculator>
- **PyPI:** <https://pypi.org/project/pepkio-bio-combinatorics-calculator/>
- **GitHub:** <https://github.com/pepkio/pepkio-bio-combinatorics-calculator>
