import serial
import time

port=serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=1)


while True:

	bytesToRead = port.inWaiting()
    rcv = port.read(bytesToRead)
    port.flushInput()

	rpi_debug = "\0x02\0x16\0x20\0x00\0x00\0x00\0x38"
#	rpi_debug = "\0x09"
#	rpi_debug = ("abcdefghij")
	port.write(rpi_debug)
    port.flushOutput()
	time.sleep(1)
