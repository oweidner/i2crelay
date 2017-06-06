I2CRelay: A library to control 8-channel relay boards via PCF8574 I2C
=====================================================================

WORK IN PROGRESS - Not really usable yet.

Hardware
--------

- PCF8574 I2C I/O Expansion Board (http://a.co/bdogwFe)
- SainSmart 8-Channel Relay Module (http://a.co/48AtFQ6)

I2C Device Permissions
----------------------

The user running the scripts needs access to the i2c devices in the /dev tree.
Instead of running the code as root you can add your user to the i2c group.
