# Copyright 2025 Marc Duclusaud & Grégoire Passault

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:

#     http://www.apache.org/licenses/LICENSE-2.0

import os
import numpy as np
from rustypot import Xl330PyController

class DynamixelActuatorV2:
    def __init__(self, port: str, id: int = 22):
        self.id = id
        self.port = port
        self.baudrate = 57600
        self.timeout = 1

        self.controller = Xl330PyController(self.port, self.baudrate, self.timeout)

    def set_p_gain(self, gain: int):
        # Set P gain
        self.controller.write_position_p_gain(self.id, gain)

    def set_torque(self, enable: bool):
        # Enable torque
        self.controller.write_torque_enable(self.id, enable)

    def set_goal_position(self, position: float):
        self.controller.write_goal_position(self.id, position)

    def read_data(self):
        # Read present position
        position = self.controller.read_present_position(self.id)[0]

        # Read present speed
        speed = self.controller.read_present_velocity(self.id)[0]

        if speed > 1024:
            speed = -(speed - 1024)
        speed = speed * 0.229 * 2 * np.pi / 60.0 # Get rad/s

        # Read present load
        load = self.controller.read_present_current(self.id)[0]
        if load > 1024:
            load = -(load - 1024)
        # Read present voltage
        voltage = self.controller.read_present_input_voltage(self.id)[0] / 10

        # Read present temperature
        temperature = self.controller.read_present_temperature(self.id)[0]

        return {
            "position": position,
            "speed": speed,
            "load": load,
            "input_volts": voltage,
            "temp": temperature,
        }

if __name__ == "__main__":
    actuator = DynamixelActuatorV2("/dev/ttyACM0", 22)
    print(actuator.read_data())