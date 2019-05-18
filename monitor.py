#! /usr/bin/env python

from serial import Serial
import sys
import time

if __name__ == "__main__":
    ser = Serial("/dev/ttyUSB0", baudrate=10000)
    while 1:
        ser.write(chr(int(sys.argv[1]) & 0xff)+ chr(int(sys.argv[1])>>8))
        r = ser.read(6)
        print([hex(ord(c)) for c in r])
        time.sleep(0.1)
        # sys.stdout.write("\r A = {}, B = {}".format(ord(ser.read()), ord(ser.read())))
    print("\n")
