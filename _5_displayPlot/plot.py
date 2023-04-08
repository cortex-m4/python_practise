import numpy as np
import matplotlib.pyplot as plt

#generate data
x1=np.arange(0,7,0.1)    #use 0.1 as unit generate 0~7 num
y1=np.sin(x1)
y2=np.cos(x1)
#display data
plt.plot(x1,y1,label="sin")
plt.plot(x1,y2,linestyle="--",label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin and cos")

plt.legend()
plt.show()


