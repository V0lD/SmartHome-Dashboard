#!/bin/bash

sudo find /var/www/html/satelliteImages/ -mmin +1500 -exec rm -f {} \;
