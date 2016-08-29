# Run every 60s

month=`date +%m`
year=`date +%Y`

nextMonth=$((10#$month+1))

if [[ $nextMonth -gt 12 ]]
then
nextMonth=1
year=$(($year+1))
fi

cal $nextMonth $year
