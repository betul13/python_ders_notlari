# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:18:10 2022

@author: betul
"""
#%%
for i in range(0,12):
    if i==10:
        continue
    print(i)
#belirli zaman aralıklarıyla bir şey bastırmak istersek
#%%
print("ali")
for i in range(2000000):
    pass
print("zeki")
#%%
for i in range(10):
    for a in range(2000000):
        pass
    print(i)
#%%
from math import *
print(sqrt(10))
print(pow(10,2))
print(sin(0.5))
#%% rastgele sayı üretme
from numpy import random
print(random.randint(100))
print(random.random()) # 0 ile 1 arası rastgele sayı
for i in range(10):
    a = random.random()
    if a > 0.5 :
        print(a)
#%%

# import the random module
import random
  
# determining the values of the parameters
mu = 100 #ortalama
sigma = 50 #standart sapma
  
# using the gauss() method
print(random.gauss(mu, sigma))
#%% cnhoice
import random
print(random.choice([1,2,34,56,46]))
a = [2,3,5,6]
print(random.sample(a,3))

# Python3 program to demonstrate the use of
# choice() method 
  
# import random 
import random
  
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6] 
print(random.choice(list1))
  
# prints a random item from the string 
string = "striver" 
print(random.choice(string))  
#%%

import random
  
mylist = ["apple", "banana", "mango"]
  
print(random.choices(mylist, weights = [3, 1, 1], k = 6))
#%%
import random
print(random.randrange(2,20,3))
#%% shuffle listenin elemanlarını rastgele tekrar diziyor
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)
#%% shuffle'ın çalışma şekli
import random
def myshuffle(a):
    for i in range(len(a)):
        k = random.randrange(len(a))
        a[k], a[i] = a[i], a[k]
              
a = [1, 2, 3, 4, 5]
print(a)
myshuffle(a)
print(a)
#%%Aşağıdaki örnekte bir oyun kartı destesi oluşturulmuş sonra da bu deste dört oyuncuya dağıtılmıştır. Ancak oyunculara dağıtılan kartlar sıraya da dizilmiştir.

import random

def create_deck():
    card_type = ['Sinek', 'Maça', 'Karo', 'Kupa']
    card_name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz', 'As']
    
    deck = []
    for cname in card_name:
        for ctype in card_type:
            deck.append(ctype + '-' + cname)
            
    return deck
       
def keyfunc(s):
    card_type = ['Sinek', 'Maça', 'Karo', 'Kupa']
    card_name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz', 'As']
    
    ctype, cname = s.split('-')
    index_name = card_name.index(cname)
    index_type = card_type.index(ctype)
    
    return index_name * 4 + index_type
    
def distribute_deck(deck):
    cards = ([], [], [], [])
    for i in range(len(deck)):
        cards[i % 4].append(deck[i])
        
    for c in cards:
        c.sort(key=keyfunc, reverse=True)
        
    return cards

deck = create_deck()
random.shuffle(deck)
north, east, south, west = distribute_deck(deck)

print(north, end='\n\n')
print(east, end='\n\n')
print(south, end='\n\n')
print(west, end='\n\n')
#%% pi sayısı bulma
import random 
import math
def getpi(n):
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance < 1:
            inside += 1
            
    return 4 * inside / n
pi = getpi(10000000)
print(pi)
#%% rastgele eleman seçme
import random
b = [12,34,34]
print(random.choice(b))
print(random.sample(b,2))
#%% 1 ile 49 arasında (49 dahil) 6 tane farklı sayı üretmek aslında basit bir biçimde şöyle yapılabilir:
#result = random.sample(range(1, 50), 6)
#Aşağıda bu işlemin çeşitli yapım biçimlerini görüyorsunuz.

import random 

def get_column():
    column = []
    for _ in range(6):
        while True:
            val = random.randint(1, 49)    
            if val not in column:
                break
        column.append(val)
        
    return column
    
result = get_column()
print(result)

def get_column():
    column = set()
    while len(column) != 6:
        val = random.randint(1, 49)    
        column.add(val)
        
    return list(column)

result = get_column()
print(result)

result = random.sample(range(1, 50), 6)
print(result)
#%% enumerate
names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

iterator = enumerate(names)
for t in iterator:
    print(t)
    
iterator = enumerate(names)
for index, x in iterator:
    print(index, x)
    
for index, x in enumerate(names):
    print(index, x)

#%%
 """enumerate fonksiyonu bir dolaşılabilir nesneyi for döngüsü ile dolaşırken hem elemanların index numaralarını hem de 
    elemanların değerlerini elde etmek için kullanılşmaktadır. enumerate fonksiyonunun ikinci bir parametresi de vardır. Bu ikinci 
    parametreye default olarak 0 değeri verilmiştir. Bu ikinci parametre indeksin nereden başlatılacağını belirtir. Örneğin:"""
names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']
for t in enumerate(names, 10):
    print(t)

#Burada artık şu demetler elde edilecektir:  (10, 'ali'), (11, 'veli'), (12, selami), (13, 'ayşe'), (14, 'fatma')
#------------------------------------------------------------------------------------------------------------------------

names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

for t in enumerate(names, 10):
    print(t)
#%%
x = 10
def foo():
    print(x)
def bar():
    global x
    x = 20
    print(x)
foo() #10
bar() #20
#%% map fonksiyonu 
def foo(a):
    return a**2
x = [1,2,3,4]
b = map(foo,x)
for x in b :
    print(x)
#%% map 2
x = 0
a = "123 377 86787"
c = map(int,a.split())
for i in c :
    x+=i
    print(x)
#%% sum fonksiyonu
x = 0
a = "123 377 86787"
c = map(int,a.split())
print(sum(c))   
#%% map3
a = [1,2,3]
b = (4,5,6,7)
c = (10,11,12,13,14)
def foo(x,y,z):
    return x*y+z
for i in map(foo,a,b,c):
    print(i)
#%% iç içe fonksiyon  asallık testş önemli
import math 

def print_primes(n):
    def isprime(val):
        if val % 2 == 0:
            return val == 2
        for i in range(3, int(math.sqrt(val)) + 1, 2):
            if val % i == 0:
                return False
        return True
    
    for x in range(2, n + 1):
        if isprime(x):
            print(x, end=' ')
        
print_primes(100)
#%% compherension
total = sum([i*i for i in range(1,11)])
print(total)
a = [i*i for i in range(1,11)]
print(a)
b = [c.upper() for c in 'ankara']
print(b)
#%%
names = ["ali","Ahmet","veli"]
a = [name for name in names if name[0] == "a" or name[0] == "A"]
print(a) #a ve A ile başlayan isimleri yazdıran bi comprension
#%% compherension
cities = ["eskişehir","İstanbul","ankara"]
city = [city.upper() for city in cities]
print(city)
#%% verilen yazıda palindromes sayıları bulma
sentences = ["anastas mum satsana","izmir","ey edip adanada pide ye"]
sentence = [sentence for sentence in sentences if sentence == sentence[::-1]]
print(sentence)
print(sentence[::-1])
#%% palidrom sayıları bulma
a = [123,224,121,323]
b = [number for number in a if str(number) == str(number)[::-1] ]
print(b)
#%% şehir plaka eşlemesi
cities = [("ankara",6),("izmr",35)]
result = [city + '-' + str(plate) for city,plate in cities]
print(result)
#%% asallık
def isprime(val) :
    if val % 2 == 0 :
        return val == 2
    for i  in range(3, val,2) : 
        if val % i == 0:
            return False
    return True
primes = [a for a in range(2,1000) if isprime(a)]
print(primes)
#%% listenin elemanını 1 atlayarak ilerleme  
a = [10,20,30,40,50] 
result = [a[i] for i in range(0,len(a),2)]
print(result) 
#%%
a = [1,3,4]
b = [2,35,5]
c = [x*y for x in a for y in b]
print(c)
    
#%%
b = [[1,2,3],[4,5,6]]
result = [[y for y in x if y % 2 == 0 ]for x in b]
print(result) 
b = [[1,2,3],[4,5,6]]
result = [y for x in b for y in x if y % 2 == 0 ]
print(result) 
#%%
text = "bugün hava çok güzel"
b = [y for y in  [x[::-1] for x in text.split()] if y[0] == 'n']
print(b)
#%%
c = [[1,2,3],[4,5,6],[7,8,9]]
d = [zip(i,y,z) for i,y,z in c for a in range(3) ]
print(d)

#%%
m =[1,2,3,4,5]
c = {i + k for i in m for k in m }
print(c)
#%%
a = ["ali","veli","selami","ayşe"]
b = [1,2,3,4,5]
c = [123,2443,244,1234]
for x,y,z in zip(a,b,c):
    print(x,y,z)
    print(x)
    print(y)
    print(z)
#%%
s = [(1,'ali'),(2,'veli')]
d = zip(*s)
for t in d :
    print(t)
#%% classes
class Sample :
    pass 
s = Sample()
s.a = 10
s.b = "20"
print(s.b)
#%%
class Sample :
    def foo(self,a,b):
        return a*b
    def bar(self,c):
        return c
def tar(x):
    return x**2
s = Sample()
print(s.foo(10, 20))    
#%% aynı değişkeni gösterme
class Sample :
    pass
s = Sample()
s.a = 10
k = s 
print(k.a)
#%% self
class Sample :
    def foo(self) :
        print(self.a)
s = Sample()
s.a = 10
s.foo()
#%%
class Sample :
    def foo(self) :
        self.a = 10
        self.b = 20
s = Sample()
s.foo()
print(s.a,s.b,sep = "..")

       

