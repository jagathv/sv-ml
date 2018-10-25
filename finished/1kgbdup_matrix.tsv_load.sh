#!/bin/bash
#SBATCH --partition=pi_gerstein
#SBATCH --ntasks=1 --nodes=1
#SBATCH --mem-per-cpu=60000
#SBATCH --time=100:00:00
#SBATCH --mail-user=jagath@caltech.edu
#SBATCH --mail-type=ALL

module load Python

python load_model.py -i 1kgbdup_matrix.tsv  -d indices -m dupext_ten_models.pkl -t 0 -o 1kgbdup_matrix.tsvall_scored.txt