#coding=UTF-8
import json
import time
import matplotlib.pyplot as plt
import numpy as np

inputfile = open("FM_label_result")
for linea in inputfile.readlines():
    line = linea
    result = json.loads(line, encoding='UTF-8')
    #print result
    lan = result["lan"] 
    print lan[2]
      
result = json.loads(line, encoding='UTF-8')
print result.keys()
#result["lan"] = ["c++","java","python","c#","javascript","php"]
#result["com"] = ["google","microsoft","amazon","facebook","twitter"]    
lan = result["lan"] 
com = result["com"]
lan_body_result = result["lan_body_result"]
lan_mental_result = result["lan_mental_result"]
lan_co = result["lan_count"]
com_body_result = result["com_body_result"]
com_mental_result = result["com_mental_result"]
com_co = result["com_count"]

x = np.arange(0,10)
y = x * x
print y
print lan_body_result["1"]
#plt.plot(x, y, marker='o')
#plot1 = plt.plot(x,lan_body_result["1"],'r')
#plot2 = plt.plot(x,lan_body_result["2"],'b')
#hmental=[71.94, 67.48, 66.49, 68.25, 71.99, 74.8, 69.56, 71.76, 73.66, 70.77, 69.32, 71.37, 65.93, 70.02, 66.95, 69.15, 72.17, 67.91, 73.17, 72.47, 71.36, 72.02, 72.59, 70.38]
#hmental=[70.12, 67.35, 69.31, 70.62, 68.28, 70.2, 69.75, 68.88, 71.84, 68.59, 70.75, 70.96, 68.94, 68.72, 70.14, 70.26, 70.12, 70.48, 71.62, 70.5, 69.69, 70.83, 70.83, 68.58]
#hmental=[50.21, 49.08, 50.02, 49.67, 49.97, 49.02, 49.84, 49.46, 50.45, 49.97, 49.76, 50.04, 50.03, 50.08, 50.41, 50.66, 50.77, 50.66, 51.2, 50.95, 50.26, 50.76, 50.5, 50.24]
#plt.plot(x,hmental)

''''
for i in range(0,6):
    print lan[i],"=",
    for j in range(0,10):
        print lan_body_result[str(i)][j],"\t",
    plt.plot(x,lan_body_result[str(i)],label=lan[i])
'''
'''
for i in range(0,6):
    print lan[i],"=",
    for j in range(0,10):
        print lan_mental_result[str(i)][j],"\t",
    plt.plot(x,lan_mental_result[str(i)],label=lan[i])
'''


'''
for i in range(0,5):
    print com[i],"=",
    for j in range(0,10):
        print com_mental_result[str(i)][j],"\t",
    plt.plot(x,com_mental_result[str(i)],label=com[i])
'''



plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#plt.legend([plot1, plot2],('red line', 'green circles'),'best', numpoints=1)
#plt.plot(int(lan_co[1]),lan_body_result[1])

plt.show()













