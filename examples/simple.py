#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Creation:    06.06.2017
# Last Update: 23.07.2017
#
# <https://codewerft.net>
#
# Copyright (c) 2017 Codewerft UG (haftungsbeschränkt)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from i2crelay import I2CRelayBoard
import time

# Define I2C bus type
# 0: Raspberry Pi Model B Rev 1.0
# 1: Raspberry Pi Model B Rev 2.0, Model A, Model B+, Model A+,
#    Raspberry Pi 2 Model B and  Raspberry Pi 3 Model B
I2C_BUS = 1

# Define I2C address of PCF8574 8-Bit I/O expander -
# depends on the hardware pins A0 - A2
I2C_ADDR = 0x20

if __name__ == "__main__":

    try:
        relay1 = I2CRelayBoard(I2C_BUS, I2C_ADDR)

        relay1.switch_all_off()
        time.sleep(1.0)

        relay1.switch_all_on()
        time.sleep(1.0)

        relay1.switch_all_off()
        time.sleep(1.0)

        for i in range(0, 10):
            for relay in range(1, 9):
                print("Switching relay {}".format(relay))
                relay1.switch_on(relay)
                time.sleep(0.1)
                relay1.switch_off(relay)
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("Execution stopped by user")
        relay1.switch_all_off()
