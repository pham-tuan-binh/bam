#!/bin/bash

#ACTUATOR="erob80_100"
#VAL_KP=25

ACTUATOR="xl330"

#ACTUATOR="mx64"
#VAL_KP=8

#ACTUATOR="mx106"
#VAL_KP=8

DATA="processed_data/"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <model>"
    exit 1
fi

N=`ls output/fit_*.log|wc -w`
N=$[$N + 1]
mkdir -p output/

uv run -m bam.fit --logdir $DATA \
	--model $1 \
	--workers 1 --trials 10000 \
	--actuator $ACTUATOR \
	--output $N \
	> output/fit_$N.log 2>&1


