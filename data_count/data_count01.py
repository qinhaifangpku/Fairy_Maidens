#coding=UTF-8
import urllib2
import json
import happy as h
import time


#get data
for i in range(0,1):
    if i < 10:
        url_detail = "0"+str(i)
    else:
        url_detail = str(i)
    print url_detail
    url ='https://storage.googleapis.com/jinhu-experimental/hacker_news/comments_0000000000'+url_detail
    data = urllib2.urlopen(url)
    count = 0    #计数
    author_count = {}
    output = open('FM_comment_'+url_detail, 'w')
    for line in data:
        data_dict=json.loads(line,encoding='UTF-8')
        #除去删掉数据
        if data_dict.get('deleted')==True:
            continue
        #计数
        count = count +1
        print(count)
        #if count>100:
         #   break

        #统计评论用户信息
        author_name = data_dict.get("author")
        text = data_dict.get("text")
        """
        if author_name in author_count.keys():
            author_count[author_name] = author_count[author_name] + 1
        else:
            author_count[author_name] = 1
        """
        result ={}
        result["id"] = data_dict.get('id')
        result["author"] = data_dict.get('author')
        result["time"] = data_dict.get('time')
        result["parent"] = data_dict.get('parent')
        score = h.hi(text, 4, 4)
        if score== None :
            continue
        result["textscore"] = str(round(score,3)*10)
        json.dump(result, output)
        output.write('\n')

    output.close()
