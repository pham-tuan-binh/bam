# Copyright 2025 Marc Duclusaud & Grégoire Passault

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:

#     http://www.apache.org/licenses/LICENSE-2.0

import argparse
import os
import time


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--mass", type=float, required=True)
arg_parser.add_argument("--arm_mass", type=float, required=True)
arg_parser.add_argument("--length", type=float, required=True)
arg_parser.add_argument("--motor", type=str, required=True)
arg_parser.add_argument("--port", type=str, default="/dev/ttyACM0")
arg_parser.add_argument("--logdir", type=str, required=True)
arg_parser.add_argument("--speak", action="store_true")
args = arg_parser.parse_args()

kps = [200, 300, 400]
trajectories = ["sin_sin", "lift_and_drop", "up_and_down", "sin_time_square"]

command_base = f"uv run -m bam.dynamixel_v2.record --mass {args.mass} --arm_mass {args.arm_mass} --length {args.length}"
command_base += f" --port {args.port} --logdir {args.logdir} --motor {args.motor}"


for kp in kps:
    for trajectory in trajectories:
        sentence = f"Kp {kp}, trajectory {trajectory.replace('_', ' ')}"
        print(sentence)

        if args.speak:
            from gtts import gTTS 
            myobj = gTTS(text=sentence, lang='en', slow=False) 
            myobj.save("/tmp/message.mp3")
            os.system("mpg321 /tmp/message.mp3")

        command = f"{command_base} --kp {kp} --trajectory {trajectory}"
        os.system(command)

        if trajectory == "sin_time_square":
            time.sleep(3)
