# Bioinformatics Pipeline Project

A complete bioinformatics workflow for FASTQ quality control, trimming, feature extraction, K-mer analysis, and machine learning classification using Python and Dockerized bioinformatics tools.

---

# Project Structure

```text
bioinformatics_project/
│
├── data/
│   ├── fastq/
│   └── trimmed/
│
├── results/
│   ├── fastqc_raw/
│   ├── fastqc_trimmed/
│   ├── fastp/
│   ├── multiqc/
│   ├── features.csv
│   ├── kmer_features.csv
│   └── qc_report.txt
│
├── src/
│   ├── fastq_parser.py
│   ├── feature_extraction.py
│   ├── kmer_extraction.py
│   └── ml_model.py
│
├── requirements.txt
└── README.md
```

---

# Technologies & Tools

## Programming & Libraries
- Python
- Biopython
- Pandas
- Scikit-learn

## Bioinformatics Tools
- FastQC
- Fastp
- MultiQC

## Containerization
- Docker

---

# Phase 1 — Data Acquisition & Project Setup

## Completed Tasks
- Created project directory structure
- Created Python virtual environment
- Installed required packages
- Downloaded FASTQ datasets using SRA Toolkit
- Generated requirements.txt

## Deliverables
- Structured project folders
- FASTQ files
- requirements.txt

---

# Phase 2 — FASTQ Parsing & Quality Control

## FASTQ Parsing

Implemented a custom FASTQ parser using Biopython to extract:

- Read IDs
- DNA sequences
- Quality scores

## Quality Control Metrics

Calculated:

- Total Reads
- Average Read Length
- Average Quality Score
- GC Content Percentage
- Q20 Percentage
- Q30 Percentage
- Per-base Quality

## Generated Output
- qc_report.txt

---

# Phase 3 — Dockerized QC & Trimming Pipeline

## FastQC Analysis

Executed FastQC on:

- Raw FASTQ files
- Trimmed FASTQ files

## Fastp Processing

Performed:

- Adapter trimming
- Low-quality filtering
- Read cleaning

## MultiQC Aggregation

Combined all QC reports into a single summary report.

## Generated Output Files

- FastQC reports
- Fastp HTML reports
- Fastp JSON reports
- MultiQC report

---

# Phase 4 — Feature Extraction & K-mer Analysis

## Feature Extraction

Extracted sequence-based features including:

- Read Length
- GC Content
- Average Quality

## Generated File
- features.csv

---

# K-mer Frequency Extraction

Implemented:

- 3-mer extraction
- K-mer frequency counting
- Noise filtering by excluding K-mers containing N

## Example K-mers
- ATG
- GCT
- TGA
- CGA

## Generated File
- kmer_features.csv

These features were used for downstream machine learning analysis.

---

# Phase 5 — Machine Learning Classification

## Model Used
- Random Forest Classifier

## Workflow
- Loaded K-mer feature dataset
- Split dataset into training/testing sets
- Trained machine learning model
- Evaluated classification performance

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score

## Final Accuracy
```text
73%
```

---

# Results Summary

| Task | Status |
|------|------|
| FASTQ Parsing | Completed |
| Quality Control | Completed |
| FastQC | Completed |
| Fastp Trimming | Completed |
| MultiQC | Completed |
| Feature Extraction | Completed |
| K-mer Extraction | Completed |
| Machine Learning Model | Completed |

---

# Authors

- Khaled Lotfy — ID: 4221168
- AbdulRahman Mahjoub — ID: 4231010
- Mohamed Hazem — ID: 421206
- Abdallah Sameh — ID: 4221079

___
Abdallah Sameh
ID: 4221079
