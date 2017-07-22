#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Creation:    06.06.2017
# Last Update: 21.07.2017
#
# <https://codewerft.net>
#
# Copyright (c) 2017 Codewerft UG (haftungsbeschränkt)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import smbus2

class I2CRelayBoard:
    """Represents an PCF8574 I2C relay board"""

    def __init__(self, i2c_bus, i2c_addr):

        self._i2c_bus = i2c_bus
        self._i2c_addr = i2c_addr

        # Create a new I2C bus object
        self._i2c = smbus2.SMBus(i2c_bus)

        # Read the initial state of the PCF8574
        self._state = self._i2c.read_byte(self._i2c_addr)

    def _commit_state (self):
        """(private) write the new state to the I2C bus.
        """
        self._i2c.write_byte(self._i2c_addr, self._state)

    def is_on(self, relay_number):
        """Return true if the relay is switched on.
        """
        return not(self._state >> relay_number-1) & 1

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
        """Switch relay on.
           TODO: make sure that relay_number is valid
        """
        # set the relay_number-th bit to 0
        self._state &= ~(1 << relay_number-1)
        self._commit_state()

    def switch_off(self, relay_number):
        """Switch relay off.
           TODO: make sure that relay_number is valid
        """
        # set the relay_number-th bit to 1
        self._state |= (1 << relay_number-1)
        self._commit_state()

    def toggle(self, relay_number):
        """Toggle relay.
        """
        if self.is_on(relay_number):
            self.switch_off(relay_number)
        else:
            self.switch_on(relay_number)
