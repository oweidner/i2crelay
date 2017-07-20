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

# import required modules
import smbus2
import time

class I2CRelay:
    """An I2C Relay"""

    def __init__(self, i2c_bus, i2c_addr):

        # The initial state of the relay board is all off
        self._state = 0b11111111

        self._i2c_bus = i2c_bus
        self._i2c_addr = i2c_addr

        # Create a new I2C object
        self._i2c = smbus2.SMBus(i2c_bus)

    def _commit_state (self):
        """(private) write the new state to the I2C bus.
        """
        self._i2c.write_byte(self._i2c_addr, self._state)

    def get_state(self):
        """Return the current state in binary format.
        """
        return bin(self._state)

    def switch_all_off(self):
        """Switch all realys off.
        """
        self._state = 0b11111111
        self._commit_state()

    def switch_all_on(self):
        """Switch all realys on.
        """
        self._state = 0b00000000
        self._commit_state()

    def switch_on(self, relay_number):
        """Switch a specific relay to on.
           TODO: make sure that relay_number is valid
        """
        # set the relay_number-th bit to 0
        self._state &= ~(1 << relay_number)
        self._commit_state()

    def switch_off(self, relay_number):
        """Switch a specific relay to on.
           TODO: make sure that relay_number is valid
        """
        # set the relay_number-th bit to 1
        self._state |= (1 << relay_number)
        self._commit_state()

def main():

    # define I2C bus
    # 0: Raspberry Pi Model B Rev 1.0
    # 1: Raspberry Pi Model B Rev 2.0, Model A, Model B+, Model A+, Raspberry Pi 2 Model B and  Raspberry Pi 3 Model B
    I2C_BUS = 1

    # define I2C address of PCF8574 8-Bit I/O expander
    # depends on the hardware pins A0 - A2
    I2C_ADDR = 0x20

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
