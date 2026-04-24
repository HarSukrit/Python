import matplotlib.pyplot as plt
import numpy as np
#1
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points)
# plt.show()

#Code snippet-2
# y_points=np.array([10,20,50,40])
# plt.plot(y_points)
# plt.show()

#Code snippet-3
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points,marker='*')
# plt.show()

#Code snippet-4
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points,'^-r')
# plt.show()

#Code snippet-5
#ms:marker size,mec:marker edge color, mfc:marker face color
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points,'^-r',ms=20,mec='blue',mfc='hotpink')
# plt.show()

#Code snippet-6
#ls:line style
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points,ls='dashed',color='r',lw=8)
# plt.show()

#Code snippet-7: Multiple lines
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points,ls='dashed',color='r',lw=8)
# plt.show()

#Code snippet-8: Titles and labels
# plt.xlabel("Average Pulse",color='hotpink',size=20)
# plt.ylabel("Calorie",color='blue',size=20)
# plt.title("Sports Data",color='r',size=30,loc='left')#loc can be left,right,center
# plt.show()

#Code Snippet-9 : GRID
# x_points=np.array([10,5,20])
# y_points=np.array([40,50,60])
# plt.plot(x_points,y_points)
# plt.grid(axis='x')# plt.grid() 
# plt.show()

#Code snippet-10:Sub-plots
# x_points=np.array([10,5,20])
# y_points=np.array([20,50,60])
# plt.subplot(1,2,1)
# plt.title("Plot 1",size=20)
# plt.plot(x_points,y_points)

# x_points=np.array([1,5,20])
# y_points=np.array([40,50,60])
# plt.subplot(1,2,2)
# plt.title("Plot 2",size=20)
# plt.plot(x_points,y_points,color='r')

# plt.suptitle("PLOTS",size=30,color='b')

# plt.show()

#Code Snippet-11
#Scatter: It only points the points and doesn't connect them.
# x_points=np.array([10,15,20,25,30,35])
# y_points=np.array([20,30,40,50,60,70])
# plt.scatter(x_points,y_points,s=90,marker='*',color='r')
# plt.show()

#Code Snippet-12: BARS
# x_points=np.array([10,15,20,25,30,35])
# y_points=np.array([20,30,40,50,60,70])
# plt.barh(x_points,y_points) #plt.bar(x_points,y_points)
# plt.show()

#COde Snippet-13: PIE CHARTS
points=np.array([10,15,25,20])
my_colors=np.array(['red','green','hotpink','blue'])
my_labels=np.array(['apple','cherry','orange','grapes'])
plt.pie(points,colors=my_colors,labels=my_labels,shadow=True)
plt.legend(title="FRUITS")
plt.show()