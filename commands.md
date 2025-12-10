 uv run -m bam.plot --actuator xl330 --logdir processed_data --sim --params params/xl330/m6.json

 uv run -m bam.fit --actuator xl330 --model m6 --logdir processed_data --method cmaes --output params/xl330/m6.json --trials 1000

 uv run -m bam.process --raw raw_data --logdir processed_data --dt 0.005

 uv run -m bam.dynamixel_v2.all_record --mass 0.004 --arm_mass 0.003 --length 0.075 --motor xl330 --logdir raw_data