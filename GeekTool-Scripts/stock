#!/bin/bash

# Run as frequent as you like. Please keep in mind it runs after hours as well. 

# Add code into stockList.txt
# NASDAQ:AAPL
# ASX:BHP
stockList="/YOUR/LOCAL/PATH/stockList.txt"



echo "Last Update: $(date '+%Y/%m/%d %l:%M:%S %p')"

while read line
do

[ -z $line ] && continue

url=$(echo "http://www.google.com/finance?q=$line")

html=$(curl $url)

companyId=$(echo "$html" | grep setCompanyId | tr -dc '[0-9]')
companyName=$(echo "$html" | grep _companyName | head -1 | awk -F\' '{print $(NF-1)}')
companyCode=$(echo "$html" | grep _ticker | head -1 | awk -F\' '{print $(NF-1)}')

priceRange=$(echo "$html" | grep -Eo '[0-9]+.[0-9]+ - [0-9]+.[0-9]+' | head -1)
priceRange52=$(echo "$html" | grep -Eo '[0-9]+.[0-9]+ - [0-9]+.[0-9]+' | tail -1)

price="$(echo "$html" | grep "ref_$companyId_l" | grep -Eo '[+-]*[0-9]+\.[0-9]+[%]*' | head -1)"
priceChange="$(echo "$html" | grep "ref_$companyId_c" | grep -Eo '[+-]*[0-9]+\.[0-9]+[%]*' | sed -n '2p' )"
priceChangePercentage="$(echo "$html" | grep "ref_$companyId_cp" | grep -Eo '[+-]*[0-9]+\.[0-9]+[%]*' | sed -n '3p')"

#echo $companyId
echo "$companyName ($companyCode)"



red="\033[1;31m"
green="\033[1;32m"
normal="\033[0m"

if [[ $priceChange =~ ^[+] ]]
then

echo -e "$green$price$normal \t $green$priceChange$normal \t $green$priceChangePercentage$normal"

elif [[ $priceChange =~ ^[-] ]]
then

echo -e "$red$price$normal \t $red$priceChange$normal \t $red$priceChangePercentage$normal"

else

echo -e "$price \t $priceChange \t $priceChangePercentage"

fi


echo "Range: $priceRange"
echo "52 Wk: $priceRange52"
echo

done < $stockList


