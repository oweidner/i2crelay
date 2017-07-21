#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Creation:    06.06.2017
# Last Update: 21.07.2017
#
# Copyright (c) 2017 by Ole Weidner <https://oleweidner.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

def main():

    from i2crelay import I2CRelay
    import time

    I2C_ADDR = 0x20
    I2C_BUS = 1

    try:
        r1 = I2CRelay(I2C_BUS, I2C_ADDR)

        r1.switch_all_off()
        time.sleep(1.0)

        r1.switch_all_on()
        time.sleep(1.0)

        r1.switch_all_off()
        time.sleep(1.0)

        for relay in range(0, 8):
            print("Switching relay {}".format(relay+1))
            r1.switch_on(relay)
            time.sleep(0.5)
            r1.switch_off(relay)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Execution stopped by user")
        r1.switch_all_off()
