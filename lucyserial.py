import serial
import time

port=serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=1)


while True:
	#rcv = port.read(10)
#	print(rcv)
	port.flushOutput()
	rpi_debug = "\0x02\0x16\0x20\0x00\0x00\0x00\0x38" 
#	rpi_debug = "\0x09"
	port.write(rpi_debug)
        port.flush()
	time.sleep(1)
