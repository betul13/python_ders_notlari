# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:31:22 2022

@author: betul
"""

"""
a = [1,2,3,4]
b = [2,3,4,5]
ab = []
for i in range(0,len(a)):
    c = a[i]* b[i]
    ab.append(a[i]* b[i])
    print(c)
    print(ab)
"""
import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])          
print(a*b) #array olarak bastırır
print(list(a*b)) #dizi oluşturur

#%%NumPy arrayi oluşturmak (nd arrayoluşturmak)
import numpy as np
c = np.array([1,2,3,4,5]) #listeden bir array oluşturuldu istenirse atama yapılıt
print(type(c))
x = np.zeros(10,dtype=float) #float olarak sıfırlardan oluşan array
print(x)
y = np.random.randint(0,10,size=9) # 0 ile 10 arasında 9 boyutunda bir array
print(y,type(y))
z = np.random.normal(10,4,(3,5))
print(z)
print(list(z))
#%% Numpy array özellikleri
import numpy as np 
a = np.array([12,334,54,45])
print(np.ndim(a))
z = np.random.normal(10,4,(3,5)) 
print(np.ndim(z)) #boyut sayısı
print(np.shape(z)) #boyut bilgisi
print(np.size(z)) #eleman sayısı
print(z.dtype)
#%% reshaping
print(np.random.randint(10,size = 9).reshape(3,3))
a = np.array([12,334,54,45])
b = a.reshape(2,2) #eleman sayısına dikkat edilerek yapılmalı
print(b)
z = np.random.normal(10,4,(3,5)) 
c = z.reshape(5,3) #eleman sayısı eskisiyle aynı olmalı
#%%index seçimi
#listelerde olduğu gibidir sadece iki boyutularda 2 karakter girişi olur
z = np.random.normal(10,4,(3,5)) 
z[2,3] = 12
print(z)
print(z[0:2,0:3]) #slice
#%%Fancy index
import numpy as np
v = np.arange(2,11,3)
print(v)
c = [0,2] #birden fazla index yakalama
print(v[c])
#%% np de koşullu ifadeler
v = [0,1,2,3,4,5,6]
c = []
for i in v:
    if v[i]>3:
        c.append(v[i])
        print(c)
#%% np de koşullu ifadeler bütün mantıksal operatörler kullanılabilir.
import numpy as np
v = np.array([0,1,2,3,4,5,6])
print(v[v>3])
#%% matematiksel işlemler
import numpy as np
v = np.array([0,1,2,3,4,5,6])
print(v**2)
print(v-2)
#%% mat işlemler devam
import numpy as np
#5 * x0 + x1 = 12
#6 * x0 + 3*x1 = 10
a = np.array([[5,6],[1,3]])
b = np.array([12,10])
print(np.linalg.solve(a,b))
