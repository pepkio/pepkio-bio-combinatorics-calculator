# Pepkio Bio Combinatorics Calculator

Compute exact combinations, permutations, NGS index multiplexing capacities, IUPAC degenerate primer complexities, Hamming distance barcode bounds, and CRISPR sgRNA library cell scaling requirements in Python and via web interface.

# Overview

Experimental protocol design in molecular biology, high-throughput sequencing, synthetic biology, and functional genomics requires precise combinatorial mathematics. Researchers routinely need to compute the total number of unique experimental conditions when pooling sample barcoding indices, designing degenerate PCR primers with IUPAC ambiguity codes, planning pooled CRISPR sgRNA screening libraries, constructing error-correcting DNA barcodes, or setting up multi-factor combinatorial assays.

Calculating these combinatorial spaces manually or with basic calculators often leads to integer overflow errors, miscalculated sampling coverage requirements, or flawed experimental multiplexing strategies. Standard floating-point implementations cannot represent exact large factorials or combinatorial combinations accurately, while simple spreadsheets lack bio-specific modules for nucleic acid degeneracy and cell transduction scaling calculations.

The **Pepkio Bio Combinatorics Calculator** solves these challenges by providing arbitrary-precision combinatorial algorithms paired with domain-specific biological modules. It allows bioinformaticians, laboratory technicians, and molecular biologists to calculate exact combinations ($C(n,r)$), permutations ($P(n,r)$), multi-position indexing capacities, IUPAC primer pool sizes, error-correcting barcode limits, and cell transduction scaling for pooled functional screens.

The hosted web tool is available at the [Pepkio Bio Combinatorics Calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator) web application for instant browser-based calculations without installation. A programmatic Python client and CLI are maintained in the software repository for workflow integration.

Common search terms and alternative names for this tool include bio combinatorics calculator, biological combination calculator, NGS index multiplexing calculator, IUPAC primer degeneracy calculator, DNA barcode capacity calculator, CRISPR library cell scaling calculator, combinatorial library size calculator, and $C(n,r)$ bioinformatic tool.

# Features

- **Exact BigInt Math Engine**: Computes combinations ($n \text{ choose } r$) and permutations ($n \text{ permute } r$) without floating-point precision loss or integer overflow.
- **NGS Index Multiplexing**: Calculates total unique dual-index and multi-index combinatorics for multiplexed Next-Generation Sequencing (NGS) libraries (e.g., Illumina i5/i7 dual-indexing, MGI, or PacBio barcoding).
- **IUPAC Degenerate Primer Analysis**: Evaluates total sequence variants, GC-content range, and sequence multiplicity for degenerate PCR primers containing IUPAC nucleic acid codes (R, Y, S, W, K, M, B, D, H, V, N).
- **Hamming Distance & Barcode Capacity**: Estimates maximum distinct DNA barcode capacity for given barcode lengths under specific minimum Hamming distance constraints for error detection and error correction.
- **CRISPR sgRNA Screening Cell Scaling**: Computes minimum cell transductions, total cell numbers, culture vessel volumes, and viral packaging volumes required to maintain specified guide coverage (e.g., 200x–500x) at a defined Multiplicity of Infection (MOI).
- **CLI & Python API**: Command-line interface and asynchronous/synchronous Python client supporting JSON input/output, manifest auto-discovery, and offline execution via API keys.
- **Reproducible Permalinks**: Generates permanent calculation URLs to share exact experimental parameters across research teams and laboratory notebooks.

# Common Use Cases

- **NGS Dual-Index Multiplexing**: Determine total pooled sample capacity when combining $N$ i5 indices and $M$ i7 indices across 96-well or 384-well plates to avoid index collision.
- **Degenerate Primer & Probe Design**: Compute the exact number of unique oligo sequences present in a degenerate PCR primer mix targeting conserved genomic motifs across divergent viral or bacterial isolates.
- **Pooled CRISPR Knockout / CRISPRi / CRISPRa Screening**: Calculate the minimum number of target cells to transduce with lentiviral sgRNA libraries (e.g., GeCKO, Brunello, TKOv3) to ensure 200x–1000x coverage per guide at an MOI of 0.3, avoiding guide representation loss.
- **Combinatorial Variant Library Synthesis**: Calculate theoretical library sizes for site-saturation mutagenesis, synthetic promoter shuffling, or antibody single-chain variable fragment (scFv) CDR loop randomization.
- **Error-Correcting DNA Barcode Design**: Evaluate how many unique cell barcodes can be generated for single-cell RNA-seq (scRNA-seq) or lineage tracing given a barcode length $L$ and Hamming distance $d \ge 3$.
- **Serial Dilution & Assay Scaling**: Integrate combinatorial condition counting with downstream liquid handling volume and serial dilution setup for high-throughput screening assays.

# Why This Tool Exists

Conventional spreadsheets (such as Excel or Google Sheets) use 64-bit floating-point arithmetic (IEEE 754), which truncates numbers larger than $2^{53} - 1$ ($\approx 9 \times 10^{15}$). In biological combinatorics, factorials like $30!$ or combinations like $C(100, 15)$ exceed these bounds, resulting in loss of exact integer precision or scientific notation rounding.

Furthermore, general-purpose scientific calculators lack bio-aware domain models. Converting a theoretical combination count into actionable bench protocols—such as translating a 65,000 sgRNA library into the precise number of $T_{225}$ flasks, total media volume, and transduced cells required at MOI 0.3—typically requires error-prone manual calculations.

The **Pepkio Bio Combinatorics Calculator** solves this by unifying exact mathematical algorithms with biological domain models. By integrating nucleic acid degeneracy lookup tables, Poisson infection statistics for MOI cell scaling, and arbitrary-precision integer evaluation, it ensures both mathematical rigor and practical laboratory utility. Researchers can access these algorithms online via the [bio combinatorics web calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator) or through the Python client package.

# Installation

Install the Python client package from PyPI using `pip`:

```bash
pip install pepkio-bio-combinatorics-calculator
```

Or using `uv`:

```bash
uv add pepkio-bio-combinatorics-calculator
```

Package distribution details are indexed on [PyPI](https://pypi.org/project/pepkio-bio-combinatorics-calculator/).

# Quick Start

### Python API Usage

Set your API key as an environment variable:

```bash
export PEPKIO_API_KEY="your_pepkio_api_key"
```

Run exact combination, IUPAC degeneracy, or CRISPR cell scaling calculations in Python:

```python
from pepkio_bio_combinatorics_calculator import PepkioClient

# Initialize client
with PepkioClient() as client:
    # 1. Combination calculation: C(10, 3)
    comb_result = client.run({"mode": "combination", "n": 10, "r": 3})
    print("Combinations C(10,3):", comb_result.result["count_exact"])  # Output: "120"
    print("Permalink:", comb_result.permalink)

    # 2. IUPAC primer degeneracy for sequence RYDH (R=A/G, Y=C/T, D=A/G/T, H=A/C/T)
    iupac_result = client.run({"mode": "iupac_degeneracy", "iupac_sequence": "RYDH"})
    print("IUPAC Sequence Variants:", iupac_result.result["count_exact"])  # Output: "36"

    # 3. CRISPR Library Cell Scaling calculation
    crispr_input = {
        "mode": "crispr_cell_scaling",
        "library_size": 62500,
        "coverage_per_guide": 200,
        "replicates": 2,
        "moi": 0.3
    }
    crispr_result = client.run(crispr_input)
    print("CRISPR Cell Scaling Summary:", crispr_result.result["interpretation"])
```

### Command Line Interface (CLI)

The package includes a built-in CLI executable `pepkio-bio-combinatorics-calculator`:

```bash
# View available manifest examples (no API key required)
pepkio-bio-combinatorics-calculator manifest --examples

# Execute a pre-configured example calculation
pepkio-bio-combinatorics-calculator run --example combination_10_choose_3

# Execute custom JSON payload
pepkio-bio-combinatorics-calculator run --input-json '{"mode": "permutation", "n": 12, "r": 4}'
```

Repository source code and technical implementation details are maintained on [GitHub](https://github.com/pepkio/pepkio-bio-combinatorics-calculator).

# Example Output

API responses return structured JSON containing the calculation status, exact BigInt string values, human-readable interpretations, and reproducible web permalinks.

### Representative Result Object (`mode: combination`)

```json
{
  "run_id": "run_comb_9876543210",
  "status": "completed",
  "result": {
    "ready": true,
    "count_exact": "120",
    "count_formatted": "120",
    "interpretation": "C(10,3) = 120 unique combinations without repetition.",
    "methods_text": "Formula used: C(n, r) = n! / (r! * (n - r)!)."
  },
  "error": null,
  "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_comb_9876543210",
  "permalink": "https://tools.pepkio.com/r/run_comb_9876543210"
}
```

### Calculation Modes Overview

| Calculation Mode | Key Input Parameters | Representative Output | Primary Biological / Laboratory Context |
| :--- | :--- | :--- | :--- |
| `combination` | `n`: 10, `r`: 3 | `count_exact`: "120" | Subsampling combinatorial wells or pool selection |
| `permutation` | `n`: 5, `r`: 2 | `count_exact`: "20" | Ordered assembly step evaluations |
| `index_multiplex` | `choices_per_position`: [8, 12] | `count_exact`: "96" | Illumina 96-well dual-index multiplexing (i5 x i7) |
| `iupac_degeneracy` | `iupac_sequence`: "RYDH" | `count_exact`: "36" | Degenerate PCR primer sequence variant count |
| `crispr_cell_scaling` | `library_size`: 62500, `coverage`: 200, `moi`: 0.3 | `count_exact`: "83333333" | Total cells needed for 200x screening at 0.3 MOI |

# Scientific Background

### Combinations and Permutations

In combinatorial mathematics:
- **Combinations without repetition** ($C(n,r)$ or $\binom{n}{r}$) represent the number of ways to choose $r$ items from a set of $n$ distinct elements regardless of selection order:

$$C(n, r) = \frac{n!}{r! (n - r)!}$$

- **Permutations without repetition** ($P(n,r)$) represent the number of ordered arrangements of $r$ items chosen from $n$ distinct elements:

$$P(n, r) = \frac{n!}{(n - r)!}$$

- **Combinations with repetition** (multiset coefficient) describe selecting $r$ items from $n$ categories where duplicate selections are permitted:

$$\left(\!\binom{n}{r}\!\right) = C(n + r - 1, r) = \frac{(n + r - 1)!}{r! (n - 1)!}$$

### IUPAC Nucleic Acid Ambiguity Codes

IUPAC nucleotide ambiguity codes allow single character representations of degenerate positions in primers and probes:

| IUPAC Code | Meaning / Bases | Base Count ($d_i$) |
| :---: | :---: | :---: |
| A, C, G, T | Adenine, Cytosine, Guanine, Thymine | 1 |
| R | Purine (A or G) | 2 |
| Y | Pyrimidine (C or T) | 2 |
| S | Strong interaction (G or C) | 2 |
| W | Weak interaction (A or T) | 2 |
| K | Keto (G or T) | 2 |
| M | Amino (A or C) | 2 |
| B | Not A (C, G, or T) | 3 |
| D | Not C (A, G, or T) | 3 |
| H | Not G (A, C, or T) | 3 |
| V | Not T (A, C, or G) | 3 |
| N | Any base (A, C, G, or T) | 4 |

The total degeneracy ($D$) of an oligonucleotide of length $L$ with base degeneracies $d_1, d_2, \dots, d_L$ is given by the product:

$$D = \prod_{i=1}^{L} d_i$$

### NGS Dual-Index Multiplexing

When pooling samples for high-throughput sequencing, unique combinations of sample barcoding indices (such as dual i5 and i7 index adapters) prevent sample misassignment:

$$N_{\text{multiplex}} = \prod_{k=1}^{P} M_k$$

Where $M_k$ is the number of distinct indices available at position $k$. For dual-indexing with $M_1 = 8$ (i5) and $M_2 = 12$ (i7), the total capacity is $8 \times 12 = 96$ unique dual-indexed samples.

### Hamming Distance & Error-Correcting Barcodes

For a set of DNA barcodes of length $L$, the Hamming distance $d_H(\mathbf{x}, \mathbf{y})$ between two sequence strings $\mathbf{x}$ and $\mathbf{y}$ is the number of positions at which the corresponding nucleotides differ.
- To **detect** up to $e$ errors, the minimum Hamming distance between any pair of barcodes must satisfy $d_{\min} \ge e + 1$.
- To **correct** up to $e$ errors, $d_{\min} \ge 2e + 1$.

The maximum number of valid barcodes $N_{bc}$ of length $L$ over an alphabet of size $q=4$ (A, C, G, T) with minimum Hamming distance $d$ satisfies the sphere-packing (Hamming) bound:

$$N_{bc} \le \frac{4^L}{\sum_{k=0}^{\lfloor \frac{d-1}{2} \rfloor} \binom{L}{k} 3^k}$$

### CRISPR sgRNA Library Screening & MOI Poisson Statistics

Pooled CRISPR screens rely on transducing a population of target cells with a viral library (e.g., lentivirus) encoding single-guide RNAs (sgRNAs). To ensure single-copy integration per cell and avoid combinatorial guide interactions, screens are performed at a low Multiplicity of Infection ($\text{MOI} \le 0.3$).

According to the Poisson distribution, the proportion of cells receiving exactly 1 viral particle at a given MOI ($\lambda$) is:

$$P(X = 1) = \lambda e^{-\lambda}$$

The proportion of infected cells (transduction efficiency $\eta$) is:

$$\eta = P(X \ge 1) = 1 - e^{-\lambda}$$

At $\lambda = 0.3$, $\eta \approx 1 - e^{-0.3} \approx 0.259$ (25.9% of total cells are transduced). The proportion of infected cells that carry a single viral integration is:

$$\frac{P(X = 1)}{P(X \ge 1)} = \frac{\lambda e^{-\lambda}}{1 - e^{-\lambda}} \approx \frac{0.3 \times 0.7408}{0.2592} \approx 85.7\%$$

To maintain $C_{\text{target}}$ coverage (e.g., 200x) for a library of $N_{\text{guides}}$ sgRNAs across $R$ biological replicates, the total number of single-transduced target cells required at transduction is:

$$N_{\text{transduced}} = N_{\text{guides}} \times C_{\text{target}} \times R$$

The total number of target cells to harvest and transduce at infection time ($N_{\text{total\_cells}}$) is:

$$N_{\text{total\_cells}} = \frac{N_{\text{transduced}}}{\eta} = \frac{N_{\text{guides}} \times C_{\text{target}} \times R}{1 - e^{-\text{MOI}}}$$

For a library of 62,500 guides with 200x coverage, 2 replicates, and $\text{MOI} = 0.3$:
- $N_{\text{transduced}} = 62,500 \times 200 \times 2 = 25,000,000$ cells.
- $N_{\text{total\_cells}} = \frac{25,000,000}{1 - e^{-0.3}} \approx \frac{25,000,000}{0.25918} \approx 96,457,400$ cells.

# Frequently Asked Questions

**What is the Pepkio Bio Combinatorics Calculator?**  
The Pepkio Bio Combinatorics Calculator is a specialized scientific software tool for computing exact mathematical combinations, NGS indexing capacities, IUPAC primer degeneracies, DNA barcode capacity bounds, and CRISPR library cell scaling parameters.

**What is serial dilution?**  
Serial dilution is a step-by-step sequential dilution of a substance in solution. The concentration decreases logarithmically across a series of tubes or wells, allowing precise preparation of standard curves, antimicrobial susceptibility testing (MIC), or viral titer assays.

**How do I calculate a dilution factor?**  
The dilution factor ($DF$) is calculated as the ratio of final solution volume ($V_2$) to transferred stock volume ($V_1$), or initial concentration ($C_1$) to final concentration ($C_2$): $DF = V_2 / V_1 = C_1 / C_2$.

**How do I prepare a standard curve?**  
To prepare a standard curve, perform a serial dilution of a known reference standard (e.g., 1:2 or 1:10 dilution series across 6–8 points), measure signal output (such as fluorescence, absorbance, or $C_t$ value in qPCR), and plot concentration versus response to quantify unknown samples.

**What is $C_1V_1 = C_2V_2$?**  
$C_1V_1 = C_2V_2$ is the dilution equation relating initial stock concentration ($C_1$), stock volume transferred ($V_1$), desired final concentration ($C_2$), and total final volume ($V_2$).

**How do I design a dilution series for qPCR?**  
For qPCR standard curves, prepare a 5-to-8 point 10-fold (1:10) or 2-fold (1:2) serial dilution series using certified low-binding tubes and nuclease-free water, ensuring concentrations span the full expected dynamic range of experimental samples.

**What is the difference between combinations and permutations?**  
Combinations ($C(n,r)$) count selections where order does not matter (e.g., selecting 3 pooled sub-libraries out of 10). Permutations ($P(n,r)$) count arrangements where order is critical (e.g., sequential multi-step enzymatic assembly order).

**How does IUPAC primer degeneracy calculation work?**  
It multiplies the number of possible nucleotide bases at each position along the oligonucleotide sequence according to IUPAC ambiguity standards (e.g., R=2, Y=2, N=4), giving the total number of distinct physical sequence variants in the primer mix.

**Why does low MOI matter in CRISPR screening?**  
Low Multiplicity of Infection ($\text{MOI} \le 0.3$) ensures that over 85% of infected cells receive only a single viral particle, preventing multiple sgRNAs from entering a single cell and confounding phenotype-to-genotype mapping.

**How many cells do I need for a 60,000 sgRNA CRISPR screen?**  
At 500x guide coverage and 0.3 MOI, you need $60,000 \times 500 = 30,000,000$ transduced cells. Accounting for $25.9\%$ transduction efficiency at 0.3 MOI, you must infect approximately $115,750,000$ cells at transduction.

**What is Hamming distance in DNA barcoding?**  
Hamming distance is the number of point substitutions required to transform one DNA barcode string into another. A minimum Hamming distance of $d=3$ permits single-base substitution error correction in sequencing reads.

**How does dual-index NGS multiplexing prevent index hopping?**  
Dual-indexing uses unique i5 and i7 barcode combinations for each sample. When index hopping occurs during Illumina cluster generation, unexpected i5/i7 pairings are identified as demultiplexing artifacts and filtered out during bioinformatic analysis.

**Does this calculator handle large factorials without rounding?**  
Yes. The Pepkio BigInt engine evaluates arbitrary-precision integers, preventing scientific notation rounding or 64-bit float overflow even when evaluating factorials exceeding $1000!$.

**Can I run calculations programmatically in Python workflows?**  
Yes. Installing `pepkio-bio-combinatorics-calculator` enables programmatic access via Python code or terminal CLI commands.

**How do I cite the Pepkio Bio Combinatorics Calculator?**  
Please cite the software tool using the repository metadata and web tool reference provided in the Citation section below.

# Web Application

The web version provides an interactive interface, shareable links, protocol generation, printable worksheets, and visualization tools.

Access the hosted web tool at [https://www.pepkio.com/tools/bio-combinatorics-calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator).

It allows researchers to perform calculations instantly without software installation, inspect step-by-step mathematical breakdowns, export calculation summaries to laboratory notebooks, and restore complete session states via persistent permalinks.

# Related Resources

- GitHub Repository: [https://github.com/pepkio/pepkio-bio-combinatorics-calculator](https://github.com/pepkio/pepkio-bio-combinatorics-calculator)
- PyPI Package: [https://pypi.org/project/pepkio-bio-combinatorics-calculator/](https://pypi.org/project/pepkio-bio-combinatorics-calculator/)
- Web Application: [https://www.pepkio.com/tools/bio-combinatorics-calculator](https://www.pepkio.com/tools/bio-combinatorics-calculator)

# About Pepkio

Pepkio ([https://www.pepkio.com/](https://www.pepkio.com/)) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services ([https://www.pepkio.com/cro](https://www.pepkio.com/cro)).

Pepkio provides research support and custom data processing workflows across core computational biology disciplines, including:
- RNA-seq analysis
- Single-cell RNA-seq analysis
- Spatial transcriptomics analysis
- Functional enrichment analysis
- Custom bioinformatics workflows

For documentation, web tools, and platform resources, visit [https://www.pepkio.com/](https://www.pepkio.com/).

# Citation

If you use the Pepkio Bio Combinatorics Calculator in your research, protocol publications, or software pipelines, please cite it as follows:

```bibtex
@software{pepkio_bio_combinatorics_calculator_2026,
  author       = {{Pepkio Bioanalytical Group}},
  title        = {Pepkio Bio Combinatorics Calculator: Exact Combinatorial Mathematics and Library Scaling for Life Science Research},
  year         = {2026},
  url          = {https://www.pepkio.com/tools/bio-combinatorics-calculator},
  note         = {GitHub: https://github.com/pepkio/pepkio-bio-combinatorics-calculator}
}
```

# License

Distributed under the MIT License. See `LICENSE` for details.

# Keywords

bio combinatorics calculator
combinatorics calculator
biology combination calculator
NGS index multiplexing calculator
IUPAC primer degeneracy calculator
DNA barcode capacity calculator
CRISPR library cell scaling calculator
combinatorial library size calculator
nCr calculator biology
nPr calculator bioinformatics
exact BigInt factorial calculator
dual index demultiplexing capacity
Illumina i5 i7 index calculator
degenerate PCR primer designer
Hamming distance DNA barcode bound
Poisson viral infection MOI calculator
CRISPR knockout cell transduction volume
site saturation mutagenesis library size
synthetic biology promoter shuffling math
serial dilution factor calculator
qPCR standard curve calculator
C1V1 C2V2 dilution formula
molarity concentration calculator
oligonucleotide pool complexity
single cell RNA-seq barcode designer
pooled functional screen cell capacity
combinatorial chemistry array planner
antibody scFv CDR randomization size
error correcting DNA barcode designer
high throughput screening plate combinatorics
multiplexed amplicon sequencing index capacity
IUPAC nucleic acid ambiguity codes
Poisson distribution cell transduction
lentiviral CRISPR screen MOI scaling
molecular biology laboratory calculator
bioinformatics protocol generator
exact permutation calculation Python
life science experimental design tool
pepkio bio combinatorics calculator
pepkio laboratory tools
bioinformatics python API package
NGS library pooling calculator
single cell lineage barcode capacity
PCR degenerate primer sequence variants
cell culture transduction cell count formula
high throughput assay dilution planner
exact integer factorials bioinformatics
combinatorial mutagenesis complexity estimator
biological sample multiplexing capacity
quadruple index NGS capacity formula
sgRNA guide coverage cell count calculator
