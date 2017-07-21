# I2CRelay: A library to control relay boards via the PCF8574 I2C I/O extender

I2CRelay is a small Python library that provides a simple API for controlling
multiple relay boards connected to a PCF8574 I2C I/O expander.

This library was designed with the following hardware in mind:

- PCF8574 I2C I/O Expansion Board (http://a.co/bdogwFe)
- SainSmart 8-Channel Relay Module (http://a.co/48AtFQ6)

You can solder it together into a single unit:

[![Relay Board](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_small.jpeg)](https://raw.githubusercontent.com/oweidner/i2crelay/media/img/relay_fullsize.jpg)

## Installation

To install the latest version from GitHub:

    git clone https://github.com/oweidner/i2crelay.git
    cd i2crelay
    pip install --upgrade .

## Example

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

The code above should do something like this:

![relay_test](https://raw.githubusercontent.com/oweidner/i2crelay/media/vid/relay_test.gif)

## I2C Device Permissions

The user running the scripts needs access to the i2c devices in the Linux
device tree. Instead of running the code as root you can add your user to the
i2c group.
