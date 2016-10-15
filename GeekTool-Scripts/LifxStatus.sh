#!/bin/bash

# Change your "Success Image" and "Failure Image" on your GeekTool to suit your needs

# Change the IP for your bulb
IP="192.168.6.249"

if ! ping -c 1 -t 1 $IP &> /dev/null
then
	exit 1
fi

GetPower="\x24\x00\x00\x34\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x74\x00\x00\x00"

power=$(echo -e "$GetPower" | nc -w 1 -u $IP 56700 | tail -c 2 | xxd -p)

#echo $power
while [ -z "$power" ]
do
	#echo ${#power}
	power=$(echo -e "$GetPower" | nc -w 1 -u $IP 56700 | tail -c 2 | xxd -p);
done

#echo $power

if [ $power = "ffff" ] ; then
	exit 0
else
	exit 1
fi
