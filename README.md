# I2CRelay: A library and command line tool to control PCF8574 I2C relay boards

I2CRelay is a small Python library that provides a simple API for controlling
multiple relay boards that are connected to a PCF8574 I2C I/O expander.

This library was tested with the following hardware:

- PCF8574 I2C I/O Expansion Board (http://a.co/bdogwFe)
- SainSmart 8-Channel Relay Module (http://a.co/48AtFQ6)

You can solder those together into a single unit like this:

[![Relay Board](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_small.jpeg)](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_fullsize.jpg)

## Installation

To install the latest version from GitHub:

    git clone -b master --single-branch https://github.com/oweidner/i2crelay.git
    cd i2crelay
    pip install --upgrade .

## Command-Line Tool

    i2crelay --i2c-type=1 --i2c-addr=0x20 0:on 1:off 2:on 8:toggle

## API Example

    from i2crelay import I2CRelay

    # define I2C bus type
    # 0: Raspberry Pi Model B Rev 1.0
    # 1: Raspberry Pi Model B Rev 2.0, Model A, Model B+, Model A+, Raspberry Pi 2 Model B and  Raspberry Pi 3 Model B
    I2C_BUS = 1

    # define I2C address of PCF8574 8-Bit I/O expander
    # depends on the hardware pins A0 - A2
    I2C_ADDR = 0x20

    r1 = I2CRelay(I2C_BUS, I2C_ADDR)

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

The code above should result in something like this:

![relay_test](https://raw.githubusercontent.com/oweidner/i2crelay/media/vid/relay_test.gif)

## I2C Device Permissions

The user running the scripts needs access to the i2c devices in the Linux
device tree. Instead of running the scripts as root you can add your user to the
i2c group.

## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
