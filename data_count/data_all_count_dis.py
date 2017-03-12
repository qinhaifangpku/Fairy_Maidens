#coding=UTF-8
import json
import time

co = 0
mental_year_count=[0,0,0,0,0,0,0,0,0,0]
body_year_count = [0,0,0,0,0,0,0,0,0,0]
all_year_count = [0,0,0,0,0,0,0,0,0,0]
mental_mouth_count=[0,0,0,0,0,0,0,0,0,0,0,0]
body_mouth_count = [0,0,0,0,0,0,0,0,0,0,0,0]
all_mouth_count = [0,0,0,0,0,0,0,0,0,0,0,0]
output = open("FM_general_count",'w')

for i in range(0,27):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)

    print file_detail
    input = open("FM_user_count_"+file_detail,'r')

    for line in input:
        data_dict = json.loads(line, encoding='UTF-8')

        mental_year = data_dict["mental_year_array"]
        body_year = data_dict["body_year_array"]
        all_year = data_dict["all_year_array"]

        mental_mouth = data_dict["mental_mouth_array"]
        body_mouth = data_dict["body_mouth_array"]
        all_mouth = data_dict["all_mouth_array"]

        for i in range(0,10):
            mental_year_count[i] = round((mental_year_count[i]*co + mental_year[i])/(co+1),2)
            body_year_count[i] = round((body_year_count[i]*co + body_year[i])/(co+1),2)
            all_year_count[i] = round((all_year_count[i]*co + all_year[i])/(co+1),2)
        for i  in range(0,12):
            mental_mouth_count[i] = round((mental_mouth_count[i]*co + mental_mouth[i])/(co+1),2)
            body_mouth_count[i] = round((body_mouth_count[i]*co + body_mouth[i])/(co+1),2)
            all_mouth_count[i] = round((all_mouth_count[i]*co + all_mouth[i])/(co+1),2)

        co = co + 1

result={}
result["average_mental_year"] = mental_year_count
result["average_body_year"] = body_year_count
result["average_all_year"] = all_year_count
result["average_mental_month"] = mental_mouth_count
result["average_body_month"] = body_mouth_count
result["average_all_month"] = all_mouth_count
json.dump(result, output)
output.write('\n')
output.close()





