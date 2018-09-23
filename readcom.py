#!/usr/bin/env python      
      
import time
import datetime
import serial
import uinput
          
ser = serial.Serial(          
	port     = '/dev/ttyAMA0',
	baudrate = 9600,
	parity   = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout  = 1
	)
          
device = uinput.Device([
	uinput.KEY_1,
	uinput.KEY_2,
	uinput.KEY_3,
	uinput.KEY_4,
	uinput.KEY_5,
	uinput.KEY_6,
	uinput.KEY_7,
	uinput.KEY_8,
	uinput.KEY_9,
	uinput.KEY_0,
	uinput.KEY_ENTER
	])
		  
while 1:
	s = ser.readline()
	if len(s) > 0:
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		f  = open('/home/admin/readcom.log', 'a')
		f.write(st+' - '+s)
		f.close()

		#
		for i in range(0, len(s) -1):
			#
			if s[i] == '1':
				device.emit_click(uinput.KEY_1)
			#	
			if s[i] == '2':
				device.emit_click(uinput.KEY_2)
			#
			if s[i] == '3':
				device.emit_click(uinput.KEY_3)
			#
			if s[i] == '4':
				device.emit_click(uinput.KEY_4)
			#
			if s[i] == '5':
				device.emit_click(uinput.KEY_5)
			#
			if s[i] == '6':
				device.emit_click(uinput.KEY_6)
			#
			if s[i] == '7':
				device.emit_click(uinput.KEY_7)
			#
			if s[i] == '8':
				device.emit_click(uinput.KEY_8)
			#
			if s[i] == '9':
				device.emit_click(uinput.KEY_9)
			#
			if s[i] == '0':
				device.emit_click(uinput.KEY_0)
			#
		#
		device.emit_click(uinput.KEY_ENTER)