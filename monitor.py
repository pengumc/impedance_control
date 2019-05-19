#! /usr/bin/env python

from serial import Serial
import sys
import time

if __name__ == "__main__":
    ser = Serial("/dev/ttyUSB0", baudrate=10000, timeout=1.0)
    ser.read(100000)
    for i in range(10):
        ser.write(chr(int(sys.argv[1]) & 0xff)+ chr(int(sys.argv[1])>>8))
        time.sleep(0.1)
    while 1:
        r = [ord(c) for c in ser.read(7)]
        if "{:08b}".format(r[6])[::-1] != "{:08b}".format(sum(r[:6]) & 0xFF):
            print("failed", r)
            continue
        torque = r[2] + (r[3] << 8) + (r[4] << 16) + (r[5] << 24)
        print("{:03} {:03} {:06} {}".format(r[0], r[1], torque, "#"*((torque-26000)//10)))
        # time.sleep(0.1)
        # sys.stdout.write("\r A = {}, B = {}".format(ord(ser.read()), ord(ser.read())))
    print("\n")
