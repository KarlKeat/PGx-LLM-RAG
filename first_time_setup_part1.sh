#!/usr/bin/bash

conda env create -f pgx_llm_rag.yml
conda activate pgx_llm_rag
python -m ipykernel install --user --name=pgx_llm
echo "run 'conda activate pgx_llm_rag' and then run './first_time_setup_part2.sh"
