#coding=UTF-8
import json
import time

partt = 0

for i in range(partt,partt+1):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)

    print file_detail
    input = open("./step2data/FM_user_comment_"+file_detail,'r')
    output = open('./step3data/FM_user_count_'+file_detail, 'w')

    author_count={}
    newlist10 = [0,0,0,0,0,0,0,0,0,0]
    newlist12 = [0,0,0,0,0,0,0,0,0,0,0,0]
    author_mental_year = {}
    author_mental_mouth = {}
    author_body_year = {}
    author_body_mouth = {}
    author_year_count={}
    author_mouth_count={}
    author_all_year = {}
    author_all_mouth = {}

    #每一条评论
    for line in input:
        #print line
        data_dict = json.loads(line, encoding='UTF-8')
        author_name = data_dict["author"]

        #时间整理
        old_time = data_dict["time"]
        value = time.localtime(float(old_time))
        year = time.strftime('%Y', value)
        mouth =  time.strftime('%m', value)
        day =  time.strftime('%d', value)
        hour = time.strftime('%H', value)
        hour = int(hour) -8
        if hour <0:
            hour = hour +24
        #hour = str(hour)
        #print year,mouth,hour

        #精神健康
        if author_name not in author_mental_year.keys():
            author_mental_year[author_name] = [0,0,0,0,0,0,0,0,0,0]
            author_year_count[author_name] = [0,0,0,0,0,0,0,0,0,0]

        if author_name not in author_mental_mouth.keys():
            author_mental_mouth[author_name] = [0,0,0,0,0,0,0,0,0,0,0,0]
            author_mouth_count[author_name] = [0,0,0,0,0,0,0,0,0,0,0,0]

        mental_score = data_dict["textscore"]
        year_index = int(year)-2006
        mouth_index = int(mouth)-1

        #近十年
        #print author_mental_year[author_name]
        author_mental_year[author_name][year_index] += float(mental_score)
        author_year_count[author_name][year_index] += 1

        #近一年每个月
        if year =="2015":
            author_mental_mouth[author_name][mouth_index] += float(mental_score)
            author_mouth_count[author_name][mouth_index] +=1

        #评论次数
        if author_name in author_count.keys():
            author_count[author_name] = author_count[author_name] + 1
        else:
            author_count[author_name] = 1

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

        if author_name not in author_body_year.keys():
            author_body_year[author_name] = [0,0,0,0,0,0,0,0,0,0]
        if author_name not in author_body_mouth.keys():
            author_body_mouth[author_name] = [0,0,0,0,0,0,0,0,0,0,0,0]

        year_index = int(year)-2006
        mouth_index = int(mouth)-1

        author_body_year[author_name][year_index] += body_score
        if year =="2015":
            #print author_body_mouth[author_name][mouth_index]
            author_body_mouth[author_name][mouth_index] += body_score
            #print author_body_mouth[author_name][mouth_index]


    for author_name in author_count:
        list10 = [0,0,0,0,0,0,0,0,0,0]
        list12 = [0,0,0,0,0,0,0,0,0,0,0,0]
        result = {}
        result["author"] = author_name

        year_count = author_year_count[author_name]
        mouth_count = author_mouth_count[author_name]

        if year_count[9] == 0:
            continue

        for i in range(0,10):
            if year_count[i]!=0:
                author_mental_year[author_name][i] = round(author_mental_year[author_name][i]/year_count[i],2)
            else:
                author_mental_year[author_name][i] = 0
        result["mental_year_array"] = author_mental_year[author_name]

        for i in range(0,12):
            if mouth_count[i] != 0:
                author_mental_mouth[author_name][i] = round(author_mental_mouth[author_name][i]/mouth_count[i],2)
            else:
                author_mental_mouth[author_name][i] = 0
        result["mental_mouth_array"] = author_mental_mouth[author_name]

        for i in range(0,10):
            if year_count[i]!=0:
                author_body_year[author_name][i] = round(author_body_year[author_name][i]/year_count[i],2)
            else:
                author_body_year[author_name][i] = 0
        result["body_year_array"] = author_body_year[author_name]

        for i in range(0,12):
            if mouth_count[i]!=0:
                author_body_mouth[author_name][i] = round(author_body_mouth[author_name][i]/mouth_count[i],2)
            else:
                author_body_mouth[author_name][i] = 0
        result["body_mouth_array"] = author_body_mouth[author_name]

        all_mouth = [0,0,0,0,0,0,0,0,0,0,0,0]
        all_year = [0,0,0,0,0,0,0,0,0,0]
        for i in range(0,12):
            all_mouth[i] = round((result["body_mouth_array"][i]+result["mental_mouth_array"][i])/2,2)
        result["all_mouth_array"] = all_mouth

        for i in range(0,10):
            all_year[i] = round((result["body_year_array"][i]+result["mental_year_array"][i])/2,2)
        result["all_year_array"] = all_year

        result["mouth_mental_score"] = author_mental_mouth[author_name][11]
        result["mouth_body_score"] = author_body_mouth[author_name][11]
        result["year_mental_score"] = author_mental_year[author_name][9]
        result["year_body_score"] = author_body_year[author_name][9]
        result["mouth_all_score"] = round((result["mouth_mental_score"]+result["mouth_body_score"])/2,2)
        result["year_all_score"]=round((result["year_body_score"]+result["year_mental_score"])/2,2)
        json.dump(result, output)
        output.write('\n')

        #print year_count[9], mouth_count[11]

    output.close()

















