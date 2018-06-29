#!/bin/bash


SVsim -i $1 -r hs37d5.fa -o $2

perl fasta_to_fastq.pl $2.fasta > $2.fastq

bowtie2 -x hs_index -U $2.fastq -S $2.sam

samtools view -b -S -o $2.bam $2.sam

samtools mpileup -g -f hs37d5.fa $2.bam > $2.bcf

bcftools call -c -v $2.bcf > $2.vcf
