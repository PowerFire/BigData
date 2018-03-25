
'''
Python 2.x必須在檔案開頭撰寫# -*- coding: UTF-8 -*-，
Python 3.x則預設使用UTF-8字元集，原始碼檔案撰寫時必須使用UTF-8編碼，
        也就不用在檔案開頭撰寫魔法註解。
'''

import numpy as np


# create from python list
#1-維度
array_1=np.arange(1,16,2)
print(array_1)
#2-維度
array_2=np.array([np.arange(1,5), np.arange(6,10)])
print(array_2)

array_3=np.array([np.arange(1,5,dtype=float), np.arange(6,10)])

#array 行列  大小
print(array_2.shape)

#array內數值型態
print("array2 型態:",array_2.dtype)
print("array3 型態:",array_3.dtype)

#全 0 矩陣
print("np.zeros(5)=,",np.zeros(5))
print("np.zeros([5,2])=",np.zeros([5,2]))

#單位矩陣
print("np.eye(3)=",np.eye(3))

#訪問元素
print("array_1[2:6]=",array_1[2:6])
print("array_2[1][:]=",array_2[1][:])



'''
    創建矩陣
'''
#創造 randon 數組
print("np.random.randn(5)=",np.random.randn(5))

print("np.random.randint(10)=",np.random.randint(10))

print("np.random.randint(10,size=(2,3))=\n",np.random.randint(6,size=(2,3)))

print("np.random.randint(10,size=10).reshape(2,5)=\n",np.random.randint(10,size=10).reshape(2,5))

'''
    矩陣運算
'''
#array 2 matrix
a=np.random.randint(10,size=20).reshape(4,5)
b=np.random.randint(10,size=20).reshape(4,5)
print(np.mat(a))
mat_a=np.mat(a)
mat_b=np.mat(b)

print("a+b=\n",a+b)
print("mat_a+mat_b=\n",mat_a+mat_b)

'''
   Array 常用函數
'''
a=np.random.randint(10,size=20).reshape(4,5)
print(a)
print("np.unique(a)=",np.unique(a))
print("sum(a)=",sum(a))
print("a.max=()=",a.max())
print("max(a[0])=",max(a[0]))
print("max(a[:,0])=",max(a[:,0]))


'''
   Array 的 input & output
'''
print("\n\n============================")
print("使用pickly序列化numpy array")
#以前的方法
import pickle
x= np.arange(10)
f=open('x.pkl','wb')
pickle.dump(x,f)
f.close()
f=open('x.pkl','rb')
print(pickle.load(f))
f.close()

#引入 numpy