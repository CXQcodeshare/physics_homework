#本代码需要用到matplotlib.pyplot库，没有安装的先自行安装，实在不会就问我吧
#本代码也可以用matlab书写，注意变换代码格式
import matplotlib.pyplot as plt

#定义受力函数，（这里求导预先算好了，节约时间）有需要可以对其更改
def F_x(x):
    return -x**3 + a0*x

#初始化变量（所有变量均初始化为浮点值）
x = [float(0) for i in range(100000)]
v = [float(0) for i in range(100000)]
a = [float(0) for i in range(100000)]

# T = [0.00001*i for i in range(100000)]
#需要使用T作变量数列绘图时反注释上面一行（删掉前面#号）

m = 1
a0 = -200
delta_t = 0.0001


#用户自定义变量初始值（x绝对值不要定太大，否则会崩溃）
print("Please enter x")
x[0] = float(input())
print("Please enter v")
v[0] = float(input())


#循环计算
i = 0
while i < 99999:
     a[i+1] = F_x(x[i])/m
     v[i+1] = v[i] + a[i+1]*delta_t
     x[i+1] = x[i] + v[i]*delta_t
     i += 1


#生成图片并显示，用matlab可以跳过，直接对应关系生成图像即可
plt.figure(figsize=(10, 10), dpi=100)
plt.plot(x, v, label="x")
plt.show()
