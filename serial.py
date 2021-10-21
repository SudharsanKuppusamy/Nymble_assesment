import serial
import crc8
from time import sleep

data = b'input data'

def compute_crc8_atm(datagram, initial_value=0):
	crc = initial_value
	for byte in datagram:
		for _ in range(0,8):
			if(crc >> 7) ^ (byte & 0x01):
				crc = ((crc << 1) ^ 0x07) & 0xFF
			else:
			    crc = (crc << 1) & 0xFF
		    byte = byte >> 1
	return crc

ser = Serial.Serial("/dev/ttyACM0", 2400)
ser.write((b'hello'))
crcData = compute_crc8_atm(data)
ser.write(crcData)