#coding=UTF-8
import json
import time

output = open('FM_label_result', 'w')
lan = ["c++","java","python","c#","javascript","php"]
com = ["google","microsoft","amazon","facebook","twitter","IBM"]

lan_body_result = {}
com_body_result = {}
lan_mental_result = {}
com_mental_result = {}
lan_co = {}
com_co = {}
for i in range(0,6):
    lan_body_result[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    com_body_result[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    lan_mental_result[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    com_mental_result[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    lan_co[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    com_co[i]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    
for i in range(0,2):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)

    print file_detail
    inputfile = open("FM_comment_label_"+file_detail,'r')

    #每一条评论
    for line in inputfile.readlines():
        #print line
        data_dict = json.loads(line, encoding='UTF-8')
        author_name = data_dict["author"]
        label_lan = data_dict["label_lan"]
        label_com = data_dict["label_com"]
        mental_score = float(data_dict["textscore"])
        #时间整理
        old_time = data_dict["time"]
        value = time.localtime(float(old_time))
        year = time.strftime('%Y', value)
        yearf = int(year) - 2006
        
        ##get body score
        hour = time.strftime('%H', value)
        hour = int(hour) -8
        if hour <0:
            hour = hour +24
        #hour = str(hour)
        #print year,mouth,hour
        #身体健康
        if hour > 5:
            body_score = 90
        elif hour ==1:
            body_score = 30
        elif hour ==2:
            body_score = 20
        elif hour ==3:
            body_score = 10
        elif hour ==4:
            body_score = 5
        elif hour ==5:
            body_score = 10
        body_score = float(body_score)
        ## language
        for tti in range(0,6):
            #print  tti
            if lan[tti] in label_lan:
                co_tmp = lan_co[tti][yearf]
                lan_body_result[tti][yearf] = round((lan_body_result[tti][yearf]*co_tmp+body_score)/(co_tmp+1.0),2)
                lan_mental_result[tti][yearf] = round((lan_mental_result[tti][yearf]*co_tmp+mental_score)/(co_tmp+1.0),2)
                lan_co[tti][yearf] = co_tmp +1.0
        
        ## com
        for tti in range(0,6):
            if com[tti] in label_com:
                #print com_body_result[tti][yearf]
                #print com_co[tti][yearf]
                co_tmp = com_co[tti][yearf]
                com_body_result[tti][yearf] = round((com_body_result[tti][yearf]*co_tmp+body_score)/(co_tmp+1.0),2)
                com_mental_result[tti][yearf] = round((com_mental_result[tti][yearf]*co_tmp+mental_score)/(co_tmp+1.0),2)
                com_co[tti][yearf] = co_tmp + 1.0


for i in range(0,6):
    print lan_body_result[i]
    print com_body_result[i]
    print lan_mental_result[i]
    print com_mental_result[i]
    print lan_co[i]
    print com_co[i]

com_co.pop(5)    
com_mental_result.pop(5)
com_body_result.pop(5)
result = {}
result["lan"] = ["c++","java","python","c#","javascript","php"]
result["com"] = ["google","microsoft","amazon","facebook","twitter"]    
result["lan_body_result"] = lan_body_result
result["lan_mental_result"] = lan_mental_result
result["lan_count"] = lan_co
result["com_body_result"] = com_body_result
result["com_mental_result"] = com_mental_result
result["com_count"] = com_co
json.dump(result, output)
output.write('\n')
output.close()

















