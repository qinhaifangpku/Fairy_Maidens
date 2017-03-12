#coding=UTF-8
import json
import time

output = open('FM_user_count_good', 'w')
countgood = 0
for i in range(0,27):
    if i < 10:
        file_detail = "0"+str(i)
    else:
        file_detail = str(i)
    print i
    #print file_detail
    inputfile = open("FM_user_count_"+file_detail,'r')

    #每一条评论
    for line in inputfile.readlines():
        #print line
        data_dict = json.loads(line, encoding='UTF-8')
        author = data_dict["author"]
        #print author
        author_mental_year = data_dict["mental_year_array"]
        author_mental_mouth = data_dict["mental_mouth_array"]
        author_body_year = data_dict["body_year_array"]
        author_body_mouth = data_dict["body_mouth_array"]
        #print author_mental_year
        #print author_body_mouth
        markk = 0
        for ti in xrange(1,10):
            if author_mental_year[ti] <=0.001 or author_body_mouth[ti] <= 0.001:
                markk = 1
                break
        if markk == 0:
            print "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFind!!"
            countgood += 1
            output.writelines(line)
     
        #print year_count[9], mouth_count[11]

output.close()

print countgood















