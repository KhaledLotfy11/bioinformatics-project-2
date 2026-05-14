# Bioinformatics Pipeline Project

## Project Overview

This project implements a complete Bioinformatics pipeline for FASTQ processing, quality control, feature extraction, K-mer analysis, and machine learning classification.

The workflow was developed using Python, Docker, and standard Bioinformatics tools to analyze sequencing data and generate machine learning-ready features.

---

# Workflow Summary

The pipeline includes:

1. Data Acquisition & Project Setup
2. FASTQ Parsing & Quality Control
3. Dockerized FastQC & Fastp Pipeline
4. Feature Extraction & K-mer Analysis
5. Machine Learning Classification

---

# Project Structure

```bash
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
_____________________
Technologies & Tools
Programming & Libraries
Python
Biopython
Pandas
Scikit-learn
Bioinformatics Tools
FastQC
Fastp
MultiQC
Containerization
Docker
____________________
Phase 1 — Data Acquisition & Project Setup
Completed Tasks
Created project directory structure
Created Python virtual environment
Installed required packages
Downloaded FASTQ datasets from SRA Toolkit
Generated requirements.txt
Deliverables
Structured project folders
FASTQ files
requirements.txt
____________________
Phase 2 — FASTQ Parsing & Quality Control
FASTQ Parsing

Implemented a custom FASTQ parser using Biopython to extract:

Read IDs
DNA sequences
Quality scores
Quality Control Metrics

Calculated:

Total Reads
Average Read Length
Average Quality Score
GC Content Percentage
Q20 Percentage
Q30 Percentage
Per-base Quality
Output

Generated:

qc_report.txt
____________________
Phase 3 — Dockerized QC & Trimming Pipeline
FastQC

Executed FastQC on:

Raw FASTQ files
Trimmed FASTQ files
Fastp

Performed:

Adapter trimming
Low-quality filtering
Read cleaning

Generated:

HTML report
JSON report
MultiQC

Aggregated all QC reports into a single report.

Output Files

Generated:

FastQC reports
Fastp reports
MultiQC report
____________________
Phase 4 — Feature Extraction & K-mer Analysis
Feature Extraction

Extracted:

Read length
GC content
Average quality

Generated:

features.csv
____________________
K-mer Frequency Extraction

Implemented:

3-mer extraction
K-mer frequency counting
Noise filtering by excluding K-mers containing N

Generated:

kmer_features.csv

Example K-mers:

ATG
GCT
TGA
CGA

These features are useful for downstream machine learning analysis.
____________________
Phase 5 — Machine Learning Classification
Model Used
Random Forest Classifier
Workflow
Loaded K-mer features
Split dataset into training/testing sets
Trained ML model
Evaluated performance
Evaluation Metrics
Accuracy
Precision
Recall
F1-score
Final Accuracy
73%
____________________
Results Summary
Task	                      Status
FASTQ Parsing	             Completed
Quality Control	           Completed
FastQC	                   Completed
Fastp Trimming	           Completed
MultiQC	                   Completed
Feature Extraction	       Completed
K-mer Extraction	         Completed
Machine Learning Model	   Completed
____________________
Author
Khaled Lotfy
ID: 4221168
___
AbdulRahman Mahjoub
ID: 4231010
___
Mohamed Hazem
ID: 421206
___
Abdallah Sameh
ID: 4221079
