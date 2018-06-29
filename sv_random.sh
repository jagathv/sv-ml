#!/bin/bash


SVsim -i $1 -r $3 -o $2

perl fasta_to_fastq.pl $2.fasta > $2.fastq

bowtie2 -x hs_index -U $2.fastq -S $2.sam

samtools view -b -S -o $2.bam $2.sam

samtools mpileup -g -f $3 $2.bam > $2.bcf

bcftools call -c -v $2.bcf > $2.vcf
