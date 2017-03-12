#coding=UTF-8
import json
import time

inputfile = open('FM_user_count_good', 'r')
    #每一条评论
countgood = 0
for line in inputfile.readlines():
    #print line
    countgood +=1
    if countgood %10 !=2 :
        continue
    data_dict = json.loads(line, encoding='UTF-8')
    author = data_dict["author"]
    #print author
    author_mental_year = data_dict["mental_year_array"]
    author_mental_mouth = data_dict["mental_mouth_array"]
    author_body_year = data_dict["body_year_array"]
    author_body_mouth = data_dict["body_mouth_array"]
    #print author_mental_year
    #print author_body_mouth
    print "________________________________"
    print author
    bodysc = 0.0
    mentalsc = 0.0
    print "mental_month",'\t',
    for j in range(0,12):
        print author_mental_mouth[j],"\t",
    print " "

    print "body_month",'\t',
    for j in range(0,12):
        print author_body_mouth[j],"\t",
    print " "
    
    print "mental_year",'\t',
    for j in range(0,10):
        print author_mental_year[j],"\t",
        mentalsc += author_mental_year[j]
    print " "

    print "body_year",'\t',
    for j in range(0,10):
        print author_body_year[j],"\t",
        bodysc += author_body_year[j]
    print " "
    
    bodysc = bodysc/9.0
    mentalsc = mentalsc/9.0
    print "bodyscore = ", '\t',round(bodysc,2)
    print "mentalscore = ",'\t',round(mentalsc,2)


    print " "















