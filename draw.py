#统计直方图
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects1 =plt.bar(left = (0.2),height = (0.5),color=('g'),label=(('no1')),width = 0.2,align="center",yerr=0.000001)
rects2 =plt.bar(left = (1),height = (1),color=('r'),label=(('no2')),width = 0.2,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.2,1),('frst','second'))
plt.title('Pe')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
plt.show()
#折线图
'''import numpy as np  
import matplotlib.pyplot as plt  
#X轴，Y轴数据  
x = [0,1,2,3,4,5,6]  
y = [0.3,0.4,2,5,3,4.5,4]  
plt.figure(figsize=(8,4)) #创建绘图对象  
plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）  
plt.xlabel("Time(s)") #X轴标签  
plt.ylabel("Volt")  #Y轴标签  
plt.title("Line plot") #图标题  
plt.xticks((0,1,2,3,4,5,6),('k=1','k=2','k=3','k=4','k=5','k=6'))
plt.show()  #显示图  '''
'''from sklearn.cluster import KMeans
dataSet=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,1],[4,2],[4,5]]
clf=KMeans(3)
s=clf.fit(dataSet)
print(s)  '''