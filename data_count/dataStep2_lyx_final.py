# -*- coding: utf-8
import json
import time

def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))


write_j = {}
for i in range(0,27):
    if i < 10:
        url_detail = "0"+str(i)
    else:
        url_detail = str(i)
    write_j[i] = open('FM_user_comment_'+url_detail,'w')


for i in range(0,32):
    print "i = ",i
    countt = 0
    if i < 10:
        url_detail = "0"+str(i)
    else:
        url_detail = str(i)
    filetmp = open('./step1data/FM_comment_'+url_detail)
    for line in filetmp.readlines():
        #print '__________________'
        #print line
        data = json.loads(line,encoding='UTF-8')
        numm = ord(data["author"][0])
        #print numm
        #print "==========================="
        if numm >= 97 and numm <= 122:
            numm = numm -96
        elif numm >=65 and numm <=90:
            numm = numm - 64
        else :
            numm = 0
        #print line
        countt += 1
        write_j[numm].writelines(line)
    
    print "i = ",i,", count comment = ",countt
    filetmp.close()



for i in range(0,27):
    write_j[i].close()


'''
{"textscore": "56.73", "time": "1371867336", "id": "5922279", "parent": "5914470", "author": "47"}
'''