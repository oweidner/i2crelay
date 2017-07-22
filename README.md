# I2CRelay: A Python library and command line tool to control PCF8574 I2C relay boards

I2CRelay is a small Python library that provides a simple API for controlling
multiple relay boards that are connected to a PCF8574 I2C I/O expander.

This library was tested with the following hardware:

- PCF8574 I2C I/O Expansion Board (http://a.co/bdogwFe)
- SainSmart 8-Channel Relay Module (http://a.co/48AtFQ6)

You can solder these into a single unit like this:

[![Relay Board](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_small.jpeg)](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_fullsize.jpg)

## Installation

To install the latest version from GitHub:

    git clone -b master --single-branch https://github.com/oweidner/i2crelay.git
    cd i2crelay
    pip install --upgrade .

## Command-Line Tool

Together with the Python module installs the `i2crelay` command line tool:

    Usage: i2crelay [OPTIONS] [CMDS]...

      Control a PCF8574 I2C relay board.

    Options:
      --i2c-bus  INTEGER  The I2C bus  (0 or 1)  [required]
      --i2c-addr TEXT     The I2C device address, e.g. 0x20  [required]
      --help              Show this message and exit.

 For example, run this command to switch on relay 1 and 2, switch off relay 3 and toggle relay 8:

    i2crelay --i2c-bus=1 --i2c-addr=0x20 1:on 3:off 2:on 8:toggle

## API Example

    from i2crelay import I2CRelayBoard

    # define I2C bus type
    # 0: Raspberry Pi Model B Rev 1.0
    # 1: Raspberry Pi Model B Rev 2.0, Model A, Model B+, Model A+, Raspberry Pi 2 Model B and  Raspberry Pi 3 Model B
    I2C_BUS = 1

    # define I2C address of PCF8574 8-Bit I/O expander
    # depends on the hardware pins A0 - A2
    I2C_ADDR = 0x20

    r1 = I2CRelayBoard(I2C_BUS, I2C_ADDR)

    r1.switch_all_on()
    time.sleep(1.0)

    r1.switch_all_off()
    time.sleep(1.0)

    for relay in range(1, 9):
        print("Switching relay {}".format(relay))
        r1.switch_on(relay)
        time.sleep(0.5)
        r1.switch_off(relay)
        time.sleep(0.5)

The code above should result in something like this:

![relay_test](https://raw.githubusercontent.com/oweidner/i2crelay/media/vid/relay_test.gif)

### Other Examples

    The `examples` directory contains a few additional examples:

    * [rest_api.py](examples/rest_api.py) - A simple REST API example with Flask

## I2C Device Setup

### Bus and Device Numbers

On Linux you can use the `i2cdetect` tool to figure out bus and device numbers:

To find out the I2C bus number, run:

    i2cdetect -l

    i2c-1	i2c       	bcm2835 I2C adapter             	I2C adapter

To find out the I2C device number, run:

    i2cdetect -y 1

         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: 20 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

### Device Permissions

The user running the scripts needs access to the i2c devices in the Linux
device tree. Instead of running the scripts as root you can add your user to the
i2c group.

## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
