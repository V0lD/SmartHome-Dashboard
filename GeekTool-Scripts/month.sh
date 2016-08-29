# Run every 60s
# Colour Options for today
# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

cal_head=`cal | head -1`; cal_tail=`cal | tail -7`; today=`date "+%e"`; echo "$cal_head"; echo "${cal_tail/${today}/[1;32m${today}[0m}";
