from Bio import SeqIO
import pandas as pd

fastq_file = "data/fastq/SRR390728_1.fastq"

data = []

count = 0

for record in SeqIO.parse(fastq_file, "fastq"):

    sequence = str(record.seq)

    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100

    avg_quality = sum(record.letter_annotations["phred_quality"]) / len(sequence)

    data.append({
        "Read_ID": record.id,
        "Length": len(sequence),
        "GC_Content": gc_percentage,
        "Average_Quality": avg_quality
    })

    count += 1

    if count == 1000:
        break

df = pd.DataFrame(data)

df.to_csv("results/features.csv", index=False)

print(df.head())

print("Feature extraction completed!")