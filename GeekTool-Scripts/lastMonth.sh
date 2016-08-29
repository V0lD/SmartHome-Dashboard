# Run every 60s

month=`date +%m`
year=`date +%Y`

lastMonth=$((10#$month-1))

if [[ $lastMonth -eq 0 ]]
then
lastMonth=12
year=$(($year-1))
fi

cal $lastMonth $year
