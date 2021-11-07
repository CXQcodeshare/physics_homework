#这里又用到matplotlib了，下载命令为( pip install matplotlib )
#另外还引入了numpy库，下载命令为( pip install numpy )
import numpy as np
import matplotlib.pyplot as plt

#注意这里我使用了三维向量空间与多维向量运算，为的是以后工作的方便，再加上 delta—t 设置得十分小，可能需要好久(实测2min)才能出结果。如果介意运算速度的话，删除最后一个维度并调小循环次数会快很多。
#本文件不能适配复数运算



def kvecmul(k, pos_vec_a):
    return k * pos_vec_a
#数乘运算

def dot(pos_vec_a, pos_vec_b):
    return np.dot(pos_vec_a, pos_vec_b)
#点乘

def cross(pos_vec_a, pos_vec_b):
    return np.cross(pos_vec_a, pos_vec_b)
#叉乘

def magnitude(pos_vec_a):
    mag = float(0)
    for i in range(len(pos_vec_a)):
        mag += pos_vec_a[i] ** 2
    mag = np.sqrt(mag)
    return mag
#模

def force_field(p, k0, s):
    acc = kvecmul(-k0*magnitude(s)**(p), s)
    return acc
#定义力场函数，建立加速度与位移关系

def motion(t, s, v):
    ns = s + kvecmul(t, v)
    return ns
#定义运动过程中迭代关系

for i in range(3):#此处循环3次
	plt.figure(figsize=(10, 10), dpi=100)
	
	delta_t = 0.0001
	k = 1  #需要改变k值调这里
	print("Input 'r' index")
	p = float(input()) - 1
	#输入r指数
	
	S = [np.array([0, 0, 0]) for i in range(5000000)]
	V = [np.array([0, 0, 0]) for i in range(5000000)]
	A = [np.array([0, 0, 0]) for i in range(5000000)]
	#初始化数组

	S[0] = np.array([2, 0, 0])#x(0)=2;y(0)=0
	V[0] = np.array([0, 0.5, 0])#x'(0)=0;y'(0)=0.5
	#录入初始值
	
	for i in range(4999999):
	    S[i+1] = motion(delta_t, S[i], V[i])
	    V[i+1] = motion(delta_t, V[i], A[i])
	    A[i+1] = force_field(p, k, S[i])


	Sx = [S[i][0] for i in range(5000000)]
	Sy = [S[i][1] for i in range(5000000)]
	Sz = [S[i][2] for i in range(5000000)]
	#录入待显示数据
	
	plt.plot(Sx, Sy,label="x")
	plt.show()
