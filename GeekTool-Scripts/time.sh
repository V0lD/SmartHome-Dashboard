# Run every 1s
# Technically, these are 4 different scripts, but they all tell time.


# Current location time
date +"%l:%M"

var=$(date +"%H")
echo ${var:0:1} 

var=$(date +"%H")
echo ${var:1:1} 

var=$(date +"%M")
echo ${var:0:1} 

var=$(date +"%M")
echo ${var:1:1} 

var=$(date +"%S")
echo ${var:0:1} 

var=$(date +"%S")
echo ${var:1:1} 


# Current location second
date +'%S'


# Current location AM/PM
date +'%p'


# Time in other timezones
TZ=Asia/Taipei date +"Taiwan:  %l:%M %p"
echo
TZ=Canada/Eastern date +"Toronto: %l:%M %p"

