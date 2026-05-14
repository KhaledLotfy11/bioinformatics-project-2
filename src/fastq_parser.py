from Bio import SeqIO

fastq_file = "data/fastq/SRR390728_1.fastq"

total_reads = 0
total_length = 0
total_quality = 0
quality_count = 0

q20_count = 0
q30_count = 0

per_base_quality = []

for record in SeqIO.parse(fastq_file, "fastq"):

    sequence = record.seq
    qualities = record.letter_annotations["phred_quality"]

    if len(per_base_quality) < len(qualities):
        per_base_quality.extend([0] * (len(qualities) - len(per_base_quality)))

    for i in range(len(qualities)):
        per_base_quality[i] += qualities[i]

    total_reads += 1
    total_length += len(sequence)

    total_quality += sum(qualities)
    quality_count += len(qualities)

    for q in qualities:

        if q >= 20:
            q20_count += 1

        if q >= 30:
            q30_count += 1

average_length = total_length / total_reads
average_quality = total_quality / quality_count

q20_percentage = (q20_count / quality_count) * 100
q30_percentage = (q30_count / quality_count) * 100

gc_count = 0

for record in SeqIO.parse(fastq_file, "fastq"):

    sequence = str(record.seq)

    gc_count += sequence.count("G")
    gc_count += sequence.count("C")

gc_percentage = (gc_count / total_length) * 100

print("Total Reads:", total_reads)
print("Average Read Length:", average_length)
print("Average Quality Score:", average_quality)
print("GC Content Percentage:", gc_percentage)
print("Q20 Percentage:", q20_percentage)
print("Q30 Percentage:", q30_percentage)

average_per_base_quality = []

for q in per_base_quality:
    average_per_base_quality.append(q / total_reads)

print("Per-base Quality:")
print(average_per_base_quality)

report = open("results/qc_report.txt", "w")

report.write(f"Total Reads: {total_reads}\n")
report.write(f"Average Read Length: {average_length}\n")
report.write(f"Average Quality Score: {average_quality}\n")
report.write(f"GC Content Percentage: {gc_percentage}\n")
report.write(f"Q20 Percentage: {q20_percentage}\n")
report.write(f"Q30 Percentage: {q30_percentage}\n")
report.write(f"Per-base Quality: {average_per_base_quality}\n")

report.close()

print("QC report generated!")