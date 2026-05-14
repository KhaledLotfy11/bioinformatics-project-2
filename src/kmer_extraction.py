from Bio import SeqIO
import pandas as pd
from collections import Counter

fastq_file = "data/fastq/SRR390728_1.fastq"

k = 3

data = []

count = 0

for record in SeqIO.parse(fastq_file, "fastq"):

    sequence = str(record.seq)

    kmers = []

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if "N" not in kmer:
            kmers.append(kmer)

    kmer_counts = Counter(kmers)

    row = {
        "Read_ID": record.id
    }

    for kmer, freq in kmer_counts.items():
        row[kmer] = freq

    data.append(row)

    count += 1

    if count == 1000:
        break

df = pd.DataFrame(data)

df = df.fillna(0)

df.to_csv("results/kmer_features.csv", index=False)

print(df.head())

print("K-mer extraction completed!")