import json
import time

co = 0
for i in range(0,27):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)

    print file_detail
    input = open("FM_user_count_"+file_detail,'r')

    for line in input:
        co = co + 1
print co

