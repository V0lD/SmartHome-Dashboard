#!/usr/bin/env python3

# Test Client application.
#
# This program attempts to connect to all previously verified Flic buttons by this server.
# Once connected, it prints Down and Up when a button is pressed or released.
# It also monitors when new buttons are verified and connects to them as well. For example, run this program and at the same time the scan_wizard.py program.


import fliclib
import socket
import select

import binascii

client = fliclib.FlicClient("localhost")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setblocking(0)
server_address = ('192.168.6.255', 56700)
off = bytes.fromhex('2a00003400000000000000000000000000000000000000000000000000000000750000000000e8030000')
on = bytes.fromhex('2a0000340000000000000000000000000000000000000000000000000000000075000000ffffe8030000')
getPower = bytes.fromhex('00000034010000000000000000000000000000000000000000000000000000007400')
getState = bytes.fromhex('00000034010000000000000000000000000000000000000000000000000000006500')
#p00 = bytes.fromhex('00000034010000000000000000000000000000000000000000000000000000006600000000000000000000ac0d00000000')
setColorPrefix = '00000034010000000000000000000000000000000000000000000000000000006600000000'
setColorDuration = 'e8030000'
p10 = bytes.fromhex(setColorPrefix+'00000000651fac0d'+setColorDuration)
p90 = bytes.fromhex(setColorPrefix+'00000000cde7ac0d'+setColorDuration)
p100 = bytes.fromhex(setColorPrefix+'00000000ffffac0d'+setColorDuration)

onHold = False
onDouble = False

#sock.sendto(bytes.fromhex('00000034010000000000000000000000000000000000000000000000000000006500'), server_address)
#ready = select.select([sock], [], [], 1)
#if ready[0]:
#	data, server = sock.recvfrom(1024)
#	print(binascii.hexlify(data.strip()[36:44]))


def controlLifx(clickType):
	global onHold
	global onDouble
	if (not onHold and not onDouble):
		if (clickType == 'ClickType.ButtonSingleClick'):
			sock.sendto(getPower, server_address)
			ready = select.select([sock], [], [], 1)
			if ready[0]:
				data, server = sock.recvfrom(1024)
				if (data.strip()[-2:] == b'\xff\xff'):
					sock.sendto(off, server_address)
				else:
					sock.sendto(on, server_address)
		elif (clickType == 'ClickType.ButtonDoubleClick'):
			onDouble = True
		elif (clickType == 'ClickType.ButtonHold'):
			onHold = True
	elif (onDouble):
		onDouble = False

		sock.sendto(getState, server_address)
		ready = select.select([sock], [], [], 1)
		if ready[0]:
			data, server = sock.recvfrom(1024)
			hueSaturation = binascii.hexlify(data.strip()[36:40]).decode('ascii')
			brightness = int.from_bytes(data.strip()[40:42], 'little')
			kelvin = binascii.hexlify(data.strip()[42:44]).decode('ascii')
#			print(binascii.hexlify(data.strip()[36:44]))
#			print(brightness)
			step = 3277
			if (clickType == 'ClickType.ButtonDoubleClick'):
				if (data.strip()[46:48] != b'\xff\xff'):
					brightness = 0

				brightness = binascii.hexlify(min(brightness+step, 65535).to_bytes(2, 'little')).decode('ascii')
#				print(brightness)
				sock.sendto(bytes.fromhex(setColorPrefix+hueSaturation+brightness+kelvin+setColorDuration), server_address)

				sock.sendto(on, server_address)
			else:
				brightness = binascii.hexlify(max(brightness-step, 1).to_bytes(2, 'little')).decode('ascii')
				sock.sendto(bytes.fromhex(setColorPrefix+hueSaturation+brightness+kelvin+setColorDuration), server_address)
	else:
		onHold = False

		if (clickType == 'ClickType.ButtonSingleClick'):
			sock.sendto(p10, server_address)
		elif (clickType == 'ClickType.ButtonDoubleClick'):
			sock.sendto(p90, server_address)
		elif (clickType == 'ClickType.ButtonHold'):
			sock.sendto(p100, server_address)

		sock.sendto(on, server_address)
	return 


def got_button(bd_addr):
	cc = fliclib.ButtonConnectionChannel(bd_addr)
	
	cc.on_button_single_or_double_click_or_hold = lambda channel, click_type, was_queued, time_diff: controlLifx(str(click_type)) 
	
	client.add_connection_channel(cc)

def got_info(items):
	print(items)
	for bd_addr in items["bd_addr_of_verified_buttons"]:
		got_button(bd_addr)

client.get_info(got_info)

client.on_new_verified_button = got_button

client.handle_events()
