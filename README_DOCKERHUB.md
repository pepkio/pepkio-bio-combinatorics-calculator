# Pepkio Bio Combinatorics Calculator

Run the Pepkio bio-combinatorics-calculator CLI in Docker to compute exact permutation spaces, NGS dual-index multiplexing capacities, IUPAC degenerate primer complexities, and CRISPR screening cell coverage without a local Python install.

# What It Does

The image runs `pepkio-bio-combinatorics-calculator`, a client for the Pepkio Bio Combinatorics Calculator REST API. It evaluates arbitrary-precision combinations ($C(n,r)$) and permutations ($P(n,r)$), dual-index sample multiplexing for NGS libraries, IUPAC nucleotide ambiguity codes, error-correcting DNA barcode capacity under Hamming distance bounds, and viral transduction cell scaling for pooled CRISPR screens. Calculator logic runs on Pepkio servers; provide a network connection and API key for `run` commands.

# Features

- Arbitrary-precision factorial and combination engine (no 64-bit float overflow)
- NGS dual-indexing combinatorial capacity (e.g., Illumina i5/i7)
- IUPAC primer degeneracy analysis and GC-content multiplicity
- Hamming distance DNA barcode bounds for error detection/correction
- CRISPR guide library coverage and cell culture volume scaling
- Manifest inspection without an API key

# Quick Start

```bash
docker pull pepkio/bio-combinatorics-calculator:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/bio-combinatorics-calculator:0.1.0 \
  pepkio-bio-combinatorics-calculator run --example combination_10_choose_3
```

Manifest only (no API key):

```bash
docker run --rm pepkio/bio-combinatorics-calculator:0.1.0 \
  pepkio-bio-combinatorics-calculator manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

```bash
docker run --rm -e PEPKIO_API_KEY="$PEPKIO_API_KEY" pepkio/bio-combinatorics-calculator:0.1.0 \
  pepkio-bio-combinatorics-calculator run --input-json \
  '{"mode":"iupac_degeneracy","iupac_sequence":"RYDH"}'
```

# Typical Use Cases

- Verify sample multiplexing capacity across Illumina i5/i7 dual-index arrays
- Calculate degenerate PCR primer pool complexity and variant counts
- Size pooled CRISPR knockout screens (e.g. Brunello, GeCKO) for target cell culture numbers at 0.3 MOI
- Bound DNA barcode library capacity given read length and minimum Hamming distance
- Integrate exact combinatorial math into automated Nextflow, Snakemake, or Docker CI pipelines

# Scientific Background

Combinatorial calculations in molecular genomics exceed standard 64-bit IEEE 754 precision limits beyond $n > 20$. IUPAC nucleotide degeneracy computes total primer sequences across ambiguous positions ($\prod d_i$). Pooled lentiviral CRISPR screens follow a Poisson distribution, requiring cell scaling $N_{\text{cells}} = (N_{\text{guides}} \times \text{Coverage}) / (1 - e^{-\text{MOI}})$ to retain library representation.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/bio-combinatorics-calculator

The web interface features interactive parameter sliders, visual plate layout tools, exportable calculation summaries, and shareable permalinks.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-bio-combinatorics-calculator

PyPI Package: https://pypi.org/project/pepkio-bio-combinatorics-calculator/

Web Application: https://www.pepkio.com/tools/bio-combinatorics-calculator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

A semantic, AI-native version of this document in the K2F format is available at https://k2f.dev (https://k2f.dev/v/72cfd6ae1f215e5e95f9fd004bbd71334da917c69f852a54f0cad95099b6f7ff)
