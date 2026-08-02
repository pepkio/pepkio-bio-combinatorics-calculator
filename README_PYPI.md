# Pepkio Bio Combinatorics Calculator

Arbitrary-precision combinatorial calculation engine and Python API for evaluating permutation spaces, dual-index NGS multiplexing, degenerate PCR primer pools, error-correcting DNA barcodes, and CRISPR screening cell coverage.

# What It Does

Experimental design in molecular biology, genomics, and synthetic biology requires calculating exact combinatorial possibilities to avoid index collision, coverage loss, or quantitative errors. Conventional spreadsheets and floating-point calculators encounter integer overflow or precision loss when evaluating large factorials and combinations.

The **Pepkio Bio Combinatorics Calculator** provides arbitrary-precision algorithms paired with biological domain modules. It enables researchers to calculate exact combinations ($C(n,r)$), permutations ($P(n,r)$), multi-position NGS indexing capacities, IUPAC degenerate primer complexities, Hamming distance barcode limits, and cell transduction scaling requirements for pooled CRISPR screens.

# Features

* **Arbitrary-Precision Engine**: Computes exact combinations ($n \text{ choose } r$) and permutations ($n \text{ permute } r$) without floating-point precision loss.
* **NGS Dual-Index Multiplexing**: Calculates total unique sample capacities for Illumina i5/i7 dual-indexing and multi-position barcoding arrays.
* **IUPAC Degenerate Primer Analysis**: Determines exact sequence variant counts, GC-content range, and multiplicity for oligonucleotides with IUPAC ambiguity codes.
* **Error-Correcting Barcode Bounds**: Estimates maximum distinct DNA barcode capacity for given sequence lengths under specific minimum Hamming distance constraints.
* **CRISPR Screening Cell Scaling**: Computes minimum transduced cell numbers, culture vessel counts, and media volume required to maintain specified guide coverage at a defined MOI.
* **Python API & CLI**: Synchronous and asynchronous Python client with structured JSON responses, CLI utilities, and permalink generation.

# Installation

Install the package from PyPI using `pip`:

```bash
pip install pepkio-bio-combinatorics-calculator
```

# Quick Example

Run an IUPAC primer degeneracy or exact combination calculation using the Python API:

```python
from pepkio_bio_combinatorics_calculator import PepkioClient

# Initialize client (uses PEPKIO_API_KEY environment variable if set)
with PepkioClient() as client:
    # 1. Calculate IUPAC primer degeneracy for sequence 'RYDH'
    result = client.run({
        "mode": "iupac_degeneracy",
        "iupac_sequence": "RYDH"
    })

    print("Sequence Variants:", result.result["count_exact"])  # Output: "36"
    print("Interpretation:", result.result["interpretation"])
    print("Permalink:", result.permalink)

    # 2. Calculate exact combinations: C(10, 3)
    comb_result = client.run({"mode": "combination", "n": 10, "r": 3})
    print("Combinations C(10,3):", comb_result.result["count_exact"])  # Output: "120"
```

# Typical Use Cases

* **NGS Dual-Index Multiplexing**: Calculate total sample pooling capacity when combining i5 and i7 index adapters across 96-well or 384-well plates to avoid index collision.
* **Degenerate PCR Primer Design**: Compute total unique sequence variants contained within degenerate primer mixes targeting conserved genomic regions.
* **CRISPR Screen Library Setup**: Determine target cell transduction numbers and culture vessel requirements for pooled sgRNA libraries (e.g., Brunello, GeCKO) to maintain 200x–500x coverage at 0.3 MOI.
* **Combinatorial Library Planning**: Calculate theoretical library sizes for site-saturation mutagenesis, promoter shuffling, or antibody CDR randomization.
* **DNA Barcode Capacity Design**: Evaluate maximum distinct barcode counts for single-cell lineage tracing given barcode length $L$ and Hamming distance bounds ($d \ge 3$).

# Scientific Background

### Combinations and Permutations

Combinations ($C(n,r) = \frac{n!}{r!(n-r)!}$) and permutations ($P(n,r) = \frac{n!}{(n-r)!}$) define distinct subset choices without or with ordering. Arbitrary-precision math avoids 64-bit IEEE 754 float truncation beyond $2^{53} - 1$.

### IUPAC Nucleotide Ambiguity

Degenerate primer multiplicity ($D$) is computed as the product of base options at each position:

$$D = \prod_{i=1}^{L} d_i$$

Where IUPAC codes represent 1 base (A, C, G, T), 2 bases (R, Y, S, W, K, M), 3 bases (B, D, H, V), or 4 bases (N).

### Poisson Infection Statistics for CRISPR Scaling

In pooled viral CRISPR screens, transduction follows a Poisson distribution $P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$. At low Multiplicity of Infection ($\text{MOI} = \lambda = 0.3$), $\approx 74\%$ of infected cells receive a single viral particle, minimizing multiple guide integration per cell while requiring total cell scaling:

$$N_{\text{cells}} = \frac{N_{\text{guides}} \times \text{Coverage}}{1 - e^{-\lambda}}$$

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available:

Web Application: https://www.pepkio.com/tools/bio-combinatorics-calculator

The web interface features interactive parameter sliders, visual plate layout tools, exportable calculation summaries, and shareable permalinks.

# Documentation and Resources

* GitHub Repository: https://github.com/pepkio/pepkio-bio-combinatorics-calculator
* Web Application: https://www.pepkio.com/tools/bio-combinatorics-calculator
* Source and Issue Tracker: https://github.com/pepkio/pepkio-bio-combinatorics-calculator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro). The platform provides web utilities and programmatic APIs to assist quantitative protocol design, molecular data analysis, and experimental workflow planning.

# Keywords

* bio combinatorics
* combinations calculator
* permutations calculator
* nCr calculator
* nPr calculator
* IUPAC degeneracy
* degenerate primers
* NGS multiplexing
* dual index calculator
* CRISPR cell scaling
* sgRNA library coverage
* DNA barcode capacity
* Hamming distance barcodes
* molecular biology math
* arbitrary precision combinatorics
* Illumina index pooling
* site saturation mutagenesis
* Poisson MOI calculator
* biological combinations
* synthetic biology tools
* oligonucleotide multiplicity
* library size calculator
* bioinformatic calculator
* laboratory math tools
* single cell barcoding
* exact combinations and permutations calculator
* IUPAC degenerate PCR primer pool size
* NGS dual index multiplexing capacity planner
* CRISPR screening transduced cell number calculator
* Hamming distance error correcting DNA barcode bounds
* Illumina i5 i7 index combination calculator
* pooled sgRNA library cell culture scaling
* arbitrary precision factorial biological combinatorics
* site saturation mutagenesis library size calculation
* degenerate oligonucleotide sequence variant counter
* MOI cell transduction coverage calculation for CRISPR screens
