I2CRelay: A library to control 8-channel relay boards via PCF8574 I2C
=====================================================================

WORK IN PROGRESS - Not really usable yet.

I2C is a small Python library that provides a simple API for controlling
8-channel relay cards via a PCF8574 I2C I/O expander.

Why? Because controlling relay boards directly via the GPIO pins of a
Raspberry PI requires, well, a lot of pins. With I2C we can control multiple
relay cards with just 2 GPIO pins.

Hardware
--------

- PCF8574 I2C I/O Expansion Board (http://a.co/bdogwFe)
- SainSmart 8-Channel Relay Module (http://a.co/48AtFQ6)

I2C Device Permissions
----------------------

The user running the scripts needs access to the i2c devices in the Linux
device tree. Instead of running the code as root you can add your user to the
i2c group.
