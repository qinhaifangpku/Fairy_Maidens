#coding=UTF-8
import json
import time

hour_score=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hour_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

output = open("FM_general_interaction",'w')
for i in range(0,32):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)

    print file_detail

    input = open("FM_comment_"+file_detail,'r')

    for line in input:
        data_dict = json.loads(line, encoding='UTF-8')

        old_time = data_dict["time"]
        value = time.localtime(float(old_time))
        year = time.strftime('%Y', value)
        mouth =  time.strftime('%m', value)
        day =  time.strftime('%d', value)
        hour = time.strftime('%H', value)
        hour = int(hour) -8
        if hour <0:
            hour = hour +24

        textscore = data_dict["textscore"]
        if hour >= 24:
            hour = 0

        hour_score[hour] = round((hour_score[hour]*hour_count[hour]+float(textscore))/(hour_count[hour]+1),2)
        hour_count[hour] = hour_count[hour] + 1

result = {}
result["hour_score"] = hour_score
json.dump(result, output)
output.write('\n')
output.close()



