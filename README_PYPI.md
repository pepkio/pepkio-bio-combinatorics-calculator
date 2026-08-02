# pepkio-bio-combinatorics-calculator

Python client for the [Pepkio Bio Combinatorics Calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator).

Exact nPr/nCr and biology-specific combinatorics via the Pepkio REST API: index multiplexing, IUPAC primer degeneracy, Hamming barcode capacity, and CRISPR library cell scaling.

## Install

```bash
pip install pepkio-bio-combinatorics-calculator
```

## Quick start

```python
from pepkio_bio_combinatorics_calculator import PepkioClient

with PepkioClient() as client:
    result = client.run({"mode": "combination", "n": 10, "r": 3})
    print(result.result["count_exact"])  # "120"
```

## Links

- **Web:** <https://www.pepkio.com/tools/bio-combinatorics-calculator>
- **PyPI:** <https://pypi.org/project/pepkio-bio-combinatorics-calculator/>
- **GitHub:** <https://github.com/pepkio/pepkio-bio-combinatorics-calculator>
