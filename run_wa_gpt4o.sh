#!/bin/bash

BASE_URL="http://ec2-34-226-200-114.compute-1.amazonaws.com"

export WA_SHOPPING="$BASE_URL:7770/"
export WA_SHOPPING_ADMIN="$BASE_URL:7780/admin"
export WA_REDDIT="$BASE_URL:9999"
export WA_GITLAB="$BASE_URL:8023"
export WA_WIKIPEDIA="$BASE_URL:8888/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
export WA_MAP="$BASE_URL:3000"
export WA_HOMEPAGE="$BASE_URL:42022"

python src/agentlab/experiments/launch_exp.py  \
        --exp_config=agentlab.agents.generic_agent.final_run \
        --agent_config=agentlab.agents.generic_agent.AGENT_4o \
        --benchmark=webarena \
        --n_jobs=1