#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    07.06.2015
# Last Update: 18.02.2017
#
# Copyright (c) 2015-2017 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

# import required modules
import smbus
import time

class I2CRelay:
    """An I2C Relay"""

    def __init__(self, i2c_bus, i2c_addr):

        self._i2c_bus = i2c_bus
        self._i2c_addr = i2c_addr

        # Create a new I2C object
        self._i2c = smbus.SMBus(i2c_bus)

    def all_off(self):
        self._i2c.write_byte(self._i2c_addr, 0xFF)

    def all_on(self):
        self._i2c.write_byte(self._i2c_addr, 0x00)

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

        r1.all_off()

        while True:
            time.sleep(1.0)
            r1.all_on()
            time.sleep(1.0)
            r1.all_off()

    except KeyboardInterrupt:
        print("Execution stopped by user")

#     try:
#         # init I2C bus
#         i2c = smbus.SMBus(I2C_BUS)
#
#         all_off(i2c, I2C_ADDR)
#
#         while True:
#             time.sleep(1.0)
#             all_off(i2c, I2C_ADDR)
#             time.sleep(1.0)
#             all_on(i2c, I2C_ADDR)
#
# #    for i in range (0, 8):
# #      # wait 1000ms
# #      time.sleep(0.1)
# #
# #      # send output data to PCF8574
# #      i2c.write_byte(I2C_ADDR, 0x0)
# #      print(output)
# #
# #      # shift the output variable
# #      output = output << 1
#
#     except KeyboardInterrupt:
#         print("Execution stopped by user")
