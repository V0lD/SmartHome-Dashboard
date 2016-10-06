#!/bin/bash

# Change your "Success Image" and "Failure Image" on your GeekTool to suit your needs

# Change the IP for your bulb
IP="192.168.6.6"

GetPower="\x24\x00\x00\x34\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x74\x00\x00\x00"

reply=$(echo -e "$GetPower" | nc -w 1 -u $IP 56700)
power=$(echo -n $reply | tail -c 2 | xxd -p )

if [ $power = "ffff" ]; then
	exit 0
else
	exit 1
fi
