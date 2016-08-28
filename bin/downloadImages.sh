#!/bin/bash

# Use the following command to add the next following line to cron
# sudo crontab -e
# 10 * * * * /var/www/html/bin/downloadImages.sh > /dev/null 2>&1

sudo wget -q -nc --retry-connrefused -P /var/www/html/satelliteImages/ $(eval echo http://rammb.cira.colostate.edu/ramsdis/online/images/himawari-8/australia_true_color/australia_true_color_{$(date --date="-2 hour" +'%Y')..$(date +'%Y')}{$(date --date="-2 hour" +'%m')..$(date +'%m')}{$(date --date="-2 hour" +'%d')..$(date +'%d')}{$(date --date="-2 hour" +'%H')..$(date +'%H')}{0..5}000.jpg)
