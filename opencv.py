# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:08:49 2022

@author: betul
"""

import cv2
img = cv2.imread(r"C:\Users\betul\Pictures\Screenshots\a.png",1)
 
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("Cute Kitens", img)
 
# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(2000)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
#%%
import cv2  
import sys
img = cv2.imread(r"C:\Users\betul\Pictures\Screenshots\a.png",0)
if img is None :
    sys.exit("could not read img.")
cv2.imshow("img",img)
s = cv2.waitKey(0)
print("deger:",s)
if s == ord(input("value:")):
    cv2.imwrite("starry_night.png",img)
#%%
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()
while True :
    print("tefoli")
    ret, frame = cap.read()
    if not ret :
        print("cannot receive frame")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("framecolor", frame)
    if cv.waitKey(400) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()


#%%
a = [1,2,3,4]
print(id(a[3]))
b = [1,2,3,[1,3,4]]
print(b[3][2])
q = b[3] #bu şekilde aynı atanır ama list olarak yaparsan yeni adres yeni liste
print(id(q))
print(c := b[3])
print(type(c))
print(c[1])
#list nesnesi elemanların kendilerini değil adrslerini tutar
print(id(c))
print(id(b[3])) #adresler aynı çıkar çünkü atamalar adres üzerinden.
d = 20
v = d
print(id(d),id(v))
#listenin bir elemanı değiştiğinde aslında yeni bir nesne oluşturup o nesne
#nin adresini elemana yerleştiririz.ilk eleman kendiliğinden silinir
e = [2,3,445,5]
print(id(e[2]))
e[2] = 10
print(id(a[2]))
#%% matris
s=[[1,2,3],[2,3,4]]
print(s[1][2])
#%% listelerde dilimleme slicing
b = [1,2,3,[1,3,4]] #[starr,stop,step] [start:stop]
print(b[-2:-1])  #0. elemandan 3. elemana kadar 3 dahil değil
print(type(b[0:3]))
print(b[2:15])
print(b[-20:3])#-20 0 olarak kabul ediliyor çünkü len eklense de 0 dan küçük
#start belirtilmezse 0 belirtilmiş gibi işlem yapılır
#stop ddeğeri yazılmazsa listenin uzunluğu yazılmış kabul edilir
print(b[:])
#%% step için 
b = [1,2,3,[1,3,4]]
print(b[0:4:2]) #ikişeer ikişer yani bir atlıcak
#stepte negatif değer kullanılabilir.
print(b[-1:-4:-2]) #start büyük stop küçük olur
print(b[::-1])
b[-1:-4:-2]=[9,8]
print(b[::-1])
b[1:3]="ank" #silinenle yazılacak nesne sayısı aynı olacak
print(b)
c="ankara"
print(c[1]) #stringler iterable 
d=list(c)
d[:2]=[]#nesneler silinir
print(d)
#listeler hem iterable hem mutable,stringler iterabla immutable
#tuplelar da aynı şekilde
f=[10,20,30,40,50,60]
f[3:0:-2]=[0,9]
print(f)
f[5:2:-1]=[23,55,45] #sadece 1 durumunda böyle yazıldığında değişecek elemanla belirtilen elemN
#farkı sorun olmuyor sadece değişiklikte start stoptan büyük yazılır 
print(f)
print(f[::-1])
#%% list sınıfının metotları
#list bir sınıfın içindeki fonksiyonlar methodudur.(sınıf.mmethod)
#metotlar belli nesneler üzerinde işlem yapar
e=[1,3,45]
e.append(1)
print(e)
#%% extend
e=[1,3,45]
e.extend([45,66])
print(e)
print(e.count(45))
#string dolaşılabilir olduğu için
e.append("ankara")
print(e)
e.extend("ankara") #string dolaşılabilir olduğu için elemanları tek tek eklenir extendle
print(e)
c="elif"
print(c[0]) #dolaşılabilir immutable
#%% index bulma
d=["ankara",1,2,4,"ankara"]
print(d.index("ankara")) #ilk bulunan index 
d.pop()#boş kullanırsan son elemanı siler
d.pop(0)
print(d.pop(0))
print(d)
#%%
a=[1,2,34,4]
print(id(a))
a[3]=2
print (id(a))
a.remove(1) #elemanın indexi değil kendisi girilir
print(a)
#eleman listenin içinde birden çok kez
#kullanılıyorsa sadece ilk karşılaşılan
#eleman silinir
#a.clear()#listenin bütün elemanları sil.
print(a)
"""b=a yapıp bir liste oluştursak
yeni bir adres oluşmaz ancak copy yaparsal
farklı bir adreste yeni bir liste oluşturulur
"""
b=a.copy()
print(id(b)) #iki id farklı
print(id(a[0])) #aynı nesneyi göstertiyorlar
print(id(b[0])) #aynı nesne aynı adres
#%%
a=[print,input]
a[0]("3")
b=[1,2,34,5]
print(id(b))
print(id(b[::-1])) #başka bir liste
b.reverse()#anın  kendisi ters yüz oluyor [::-1]yeni liste oluşturur
print(id(b))
b.sort()
print(b) #geri dönüş değeri yok kendi listesini sort etti
#sort işleminde string girilirse karşılaştırma yapılmaz exception alınır ama bool elemanları
#olursa karşılaştırma yapılır.
#stringlerden oluşturulmuş liste sort edilebilir.stable sort
b.sort(reverse=True)#büyükten küçüğe
print(b)
s=(list(reversed("ankara")))
print(s)
e=(list(sorted("polatlı")))
print(e)
print(5 and 34 in b) #3 b de var mı
#%% del operatörü sadece listede değil mutablelarda da kullanılır
a=[12,34,67,89,78,678,678,899,99,0]
del(a[0::2]) #del önek bir operatör
del(a[1])
print(a)
#%%listelerin toplanması
a=[10,120,30,(2,24,4)]
b=[23,45,56]
print(a+b)
c=[10,20,10]+[12,24]
print(c)
print(5 not in a)
print(a.count(10))
#%% liste int değerle çarpılabilir
print((b:=[23,45,56])*3)
print(b)
a=[[],[],[],[]]
c=3*a
c[0].append(20)
print(c)
d=[["q"],["q"],["q"]]
d[0].append(100)
print(d)
#%% tuple
a=(2,3,4,5,6,7)
print(a[1])
b=sorted("polatlı")
print(b)
b.append(12)
print(b)
c=((),())
print(c*4)
#tek elemanlı tuple oluşturmak için (10,)yapılır yoksa öncelik parantezi olarak anlaşılır
e=(22,)
print(type(e))
#liste elemanı tuple tuple elemanı liste olabilir.
s=((3),(3),(5),(6),[3,4,5])
print(s)
s[4].append(5)
print(s)
#listeler mutable,tuplelar immutable append,insert vs yok,ancak in place sorted,reversed yapılabilir
#ayrıca eleman değişikliği yapmayan index ve count bulunur
k=[12,35,678,9]
k.insert(2,14)
print(k)
# mutable türler genelde hashlenebilir değildir,tupleların tüm elemanı heşlenirse heşlenebilir
d=[2,3,5]
print(id(d))
d.append(19)
print(id(d))
a=(1,2,3,5)
b=sorted(a)
f=20
print(id(f))
l=20
f=40
print(id(f))
#%% tuple parantezsiz kullanım
a=10,
print(type(a))
#listelerde += işlemi sonuna ekle anlamına geliyor
b=[1,3,56,654,43]
c=[99,13,23,244]
print(id(b))
b=b+c
print(id(b))
b+=c
print(id(b)) #%adres aynı kalır sadece sonuna eklenir aynı şekilde *= de geçerli
#tupleda sona ekleme olmadığı için id ler her türlü  farklı çıkacaktır
e=10,12,45
d=13,45,56
print(id(d))
d=d+e
print(id(d))
d+=e
print(id(d))
d=d+d+d
print(id(d))
#%%unpack
b="asdf"
x,y,z,t=b #elemanla eşit sayıda olmalı
print(x)
print(y)
d=[1,224,5356,6]
a,s,d,f=d
print(a)
w=2,43,45
f,g,h=w
print(f)
[f,g,h]=w
print(f)
l=[10,(12,34),65]
x,(y,z),a=l #köşeli ya da yay parantez farketmez
print(z,y)
x,[y,z],a=l
print(z,y)
#%%Range fonksiyonu dilimlenebilir ters sayabilir,elemanları değişmez,range immutable
b=range(30,20,-2)
print(tuple(b))
import numpy as np
a=np.arange(2.4,1.2,-0.2)
print(a)
r=range(19,29)
d=r[0:6]
print(d)
print(28 in b)
#rangelerde index ve count yapılabilir.
print(b.start,b.stop,b.step) #range liste tuple sequance container
#%%
a=10
b=29 #ikisinin adresini değişmek istersek
print(id(a))
print(id(b))
temp=a
a=b
b=temp
print(id(a))
print(id(b))
#ya da direkt
c=5
print(id(c))
d=34
print(id(d))
c,d=d,c
print(id(c),id(d)) #c nin adresi d de d ninki c de
print(c,d)
#%% kümeler sets mutabledır
a={3,45,6,"ali"} #sıra yoktur [] li işlemler olmaaz
print(type(a))
a.remove(45)
print(a)
#aynı elemandan 2 tane olması exception oluşturmaz
s={12,334,45,56,56} 
print(len(s))
#%%
# {} boş süslü parantezleboş küme değil boş sözlük oluşur.
a=set()
print(a)
b=1,24,566,574
s="ANKARA"
print(set(s)) #tekrarlı  olanlar kalkacak
d=set(range(2,10,2))
print(d)
#birbirinden farklı kaç harf var
print(len(set("ankara")))
#%%
a=input("please write a city name:")
c=set(a)
print(len(c))
#%%
a = {"1",2,4,5,4}
print(a)
#%% in not in kontrolü hash tablosuyla ya da ikili ağaçlarlaset(kümelerde çok hızlı yapılır)
#%%listeler küme elemanı yapılamaz hashlanebilir olmalı hızlı arama için hash tabloları kullanılmaktadir
#%%kümelerin kendisi de heahlenemez bir küme bir başka kümenin altbaşlığı olmaz
a=[1,23,4,4,6]
print(id(a))
b=a.append(3)
print(id(b)) #mutabledır
c=(2,34,56,52,544,[1,2]) #tuple değiştirilemez ama içeriğin değiştirilebilir olan kısmı değişir
c[5][0] =11
print(c) 
#%% var yok testi ve tekrarlananların atılması için set kullanılır
e = {1,24,567,9,79}
e.add(2334)#add 1argüman
print(e)
e.update((66,876,0)) #çift parantez
print(e)
a=e.pop()
print(e,a)
#%%
a=[10,20,30,40,50,60]

print(a[5:0:-1])
#dir ile kullanacağın yapıyı girersen dir(set) görebilirsin
#sette silmek için discard isimli bir metotta kullanılanilir
#bu remove gibi olmayan eleman olduğunda exception vermez
#pop çıkarılan değeri de veriyor
c=a.pop()
print(c)
print(a)
#%% intersection ortak elemam olması durumu &
e={1,24,5,789,98,2456}
c={2,34,5,789,98,45}
k=e.intersection(c)
print(k) #ortak elemanlar yazıldı.
#%% e ve c nin ortak elemanı için
e={1,24,5,789,98,2456}
c={2,34,5,789,98,45}
print(e&c)
# & sağ taraf set ya da frozen set olabilir.
# ikisi de set iken yer değişip yazılabilir ama
# biri liste biri setse eğer set öncesinde yazılmalıdır.
f={12,345,776,54,35}
k=[12,345,34,221,3]
l=f.intersection(k) #ancak l ile k yer değişirse exception oluşur.fnin metodu çünlü
print(l)
#%% union | birleşim işlemi 
f={12,345,776,54,35}
k=[12,345,34,221,3]
l={34,567,789}
s=f.union(k)
print(s) #1.set olduğu sürece sorun yok
print(s|l)
#%% farkları
f={12,345,776,54,35}
k=[12,345,34,221,3]
l={34,567,789}
print(f.difference(k))
d=f-l
print(d)
#%% a birleşim b  den kesişimlerin çıkmış hali
f={12,345,776,54,35}
k=[12,345,34,221,3]
l={34,567,789}
print(f^l)
d=f.symmetric_difference(l)
print(d)
#%%
f={12,345,776,54,35}
k={12,345,34,221,3}
f&=k
print(f)
f-=k
print(f)
#%%
f={12,345,776,54,35}
k={12,345,34,221,3}
f|=k
print(f)
f^=k
print(f)
#%%
f={12,345,776,54,35}
k={12,345,34,221,3}
#f.union_update(k)
f.update(k)
print(f)
f.difference_update(k) #f tamamen değişiyor
print(f)
#%% alt küme üst küme öz üst öz alt
a={12,34,56,78,98,13}
b={12,34,56,78,98,13}
if(a<b): #öz alt küme mi her küme kendisinin alt kümesi ya da üst kümesidir ama öz üst,alt değildir.
    print("successful")
else:
    print("fail")
#%% issubset proper_subset issuperset
a={12,34,56,78,98}
b={12,34,56,78,98,13}
if(b >= a): #üst küme
    print("successful")
else:
    print("fail")
#%% öz kümeler için issuperset ve issubset vardır alt ve üst kümede metot yok
a={12,34,56,78,98}
print(a.issubset(range(1,100,1)))
print(a.issuperset({12,34,78}))
b={8,9,0}
if(a.isdisjoint(b)): #ayrık küme 
    print("AA")
#%%frozenset immutable fs| s ise fs çıkar,s|fs ise set çıkar
#sözlükte anahtar hashable olmalı liste ve küme olamaz ancak,değerler farketmez
#%% dict
a=[["ali",10],["veli",20]]
print(dict(a))
a=("al","sa","na") #iterable nesne ve 2 elemanlı olması yeterli
print(dict(a))
#%%
a="ali"#a değişken değişkenşn gösterdiği adresin içindekine nesne deriz
#a nın içindeki nesnenin adresi alınır
c=dict(ali=12,mehmet=30) #1. anahtar 2. değer olarak alınır.
print(c)
print(c['ali']) #alinin değeri için
d={10:'ali','veli':45}
print(d[10]) #anahtar yazılarak işlem sağlanır. 
#yukarıdaki işlemler sonucunda hata varsa exception oluşur ancak
print(d.get(26,"fail")) #exception oluşmaz d.get(key)
if 10 in d :#anahtara bakar
    print("True")
print(20 in d) #false
print(len(d)) #anahtar değer çifti
#sözlük dolaşıldığında belli bir sıra olmaz ama tüm anahtarlar elde edilir
print(list(d))
#aynı anahtar sözlükte bir daha kullanılırsa değeri artık o son değerdir.
d[10]='tevfik' #10 un değeri değişti
print(d)
d[46]='can'
print(d) #46 anahtar olarak can değer olarak eklendi
d.update(((22,'ali'),(33,'kasım'))) #iterable olmalı
print(d)
d.update({'nazmiye':52,'ismet':55})
print(d)
w=d.pop(10)
print(w)
print(d)
#exception istemiyorsak
e=d.pop(34,"not found") #2. parametre olmasa exception oluşur
print(e)
print(d.keys()) #anahtarları verir
print(d.values()) #değerleri verir
#d.values,d.keys view nesne olarak adlandırılır yani bunlar aşağıda eleman eklenip
#çıkarılsa da etkilenir değişir
k=d.keys()
l=d.values()
z=d.items()
d[39] = 'sef'
print(k)
print(l)
print(z) #anahtar değer çiftlerini demet olarak verir
v={'emine':[100,20,30]}
v["emine"].append(34) #içerideki liste append ile eklenir
f=v.copy()
print(v)
v.clear()
print(v)
print(f)
print(f.setdefault('emine'))
f.setdefault(40) #exception vermez yeni değer ekler ona none değeri verir
print(f)
f.setdefault(39,'xxxx') #39 varsa değerini ver yoksa 39 için 'xxxx' ekle
print(f)
del f[39]
print(f)
#%% stringler
a="ayşe eve gel"
print(a[5]) #sequence type köeli paatntezle erişilen her şey
print(set(a))
print(len(a))
print(a[::-1])
#ikistring toplanabilir
c="ankara"
d="izmir"
print(c+" "+d)
print(c.capitalize()) #yazının ilk harfi büyük
e=c.capitalize() #başka bir string oluşturdu
k=a.title() #bütün sözcüklerin ilk harfini büuük yapar
print(k)
#%%center,finf
a="ankara"
print(a.center(20))
k=a.center(11,"x")
print(k)
f="tevfik betüşü seviyor"
print(f.find("tevfik")) #olmasaydı -1 verirdi
d="tevfik betüşü seviyor,evet evet tevfik betüşü çok seviyor"
print(d.find("tevfik",1,60))
path = r"file:///C:/Users/betul/Desktop/adli-sicil-kaydi.pdf"
index = path.rfind(r"/")   # 3 argüman girmek istersek yine baştan indexler olur 
fname=path[index+1:]
print(fname) 
print(d.count("tevfik"))
s="ali"
v=s.islower()
print(v)
print(s.isalpha())
print(s.isupper())
print(s.isdigit())
print(d[6].isspace())
'!'.join(s)
#%%
a = "ali,,,veli,,,selami"
new_a = a.split(',')
print(new_a)
b = "a/b/c/d"
print(b.split("/"))
c = "nazmiş\nismet\tbetüş "
print(c.split()) #bütün boşluk karakterlerini attırmak için kullanılır
d = "xxxankaraxxx"
print(d.strip('x'))
k = "xxxyyyyxxankarayy"
print(k.strip("xy"))
l = "   ankara   izmir  "
print(l.strip()) #iki str arası olanı atmaz
print(l.rstrip())
print(l.lstrip())
birthday = "14/02/1999"
new = ".".join(birthday.split("/"))
print(new)
#%% index paritition
z = "bugün hava çok güzel"
print(id(z))
print(z.index("bugün"))
x = "ankaraizmiristanbul" 
left,center,right = x.partition("izmir")
print(right)

e = "istanbul istanbul güzel istanbul"
c = e.replace("istanbul", "ankara")
print(c)
print(e.startswith("is"))
print(e.startswith("s"))
z += (' ' + e)
print(z)
print(id(z))

y="ANkara"
print(y.upper())
print(y.lower())
#%%
a=10
b=20
c=60
s='a={},b={},c={}'
print(s.format(a,b,c))
f='{1} {2} {0}'
print(f.format(a,b,c))
print('a={0},b={1},c={2}'.format(a,b,c))
#%%
a = 10
b = 30
print({:30}{:<30}.format(a,b))
#% <^


