#!/bin/bash

# Use the following command to add the next following line to cron
# sudo crontab -e
# 10 * * * * /var/www/html/bin/deleteOldImages.sh > /dev/null 2>&1

sudo find /var/www/html/satelliteImages/ -mmin +1500 -exec rm -f {} \;
