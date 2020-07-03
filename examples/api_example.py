import time
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
