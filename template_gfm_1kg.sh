#!/bin/bash
#SBATCH --partition=pi_gerstein
#SBATCH --ntasks=1 --nodes=1
#SBATCH --mem-per-cpu=60000
#SBATCH --time=50:00:00
#SBATCH --mail-user=jagath@caltech.edu
#SBATCH --mail-type=ALL

module load Python
module load Biopython
module load matplotlib/1.5.1-foss-2016a-Python-2.7.11
module load BEDTools

python generate_feature_matrix.py --svtype TYPE_SV  -c INPUT_FILE -o OUTPUT_FILE -b feature_files/geneExprsn.bw feature_files/GM12878/Histones/wgEncodeBroadHistoneGm12878H4k20me1StdSig.bigWig feature_files/GM12878/Histones/wgEncodeBroadHistoneGm12878H3k36me3StdSig.bigWig feature_files/GM12878/Histones/wgEncodeBroadHistoneGm12878H3k79me2StdSig.bigWig feature_files/GM12878/Histones/wgEncodeBroadHistoneGm12878H2azStdSig.bigWig feature_files/GM12878/Histones/wgEncodeBroadHistoneGm12878H3k04me3StdSigV2.bigWig -g feature_files/fragileSites/common_fragile_sites.txt
