# 1) 2 veya 3'e tam bölünebilen 10000'dan küçük kaç adet sayı olduğunu bulan yazılımı python dilinde yazınız.
"""
sayi = 0

for i in range(1,1000):
    if  (i % 2 == 0) or (i % 3 == 0) :
        print (i)
        sayi +=1

print("Sayi:", sayi)
"""

# 2) Kullanıcıdan aldığı x ve y değeri ile xy sayısını döngü yapılarını kullanarak hesaplayan yazılımı python dilinde yazınız.
"""
taban = int(input("Taban olacak sayıyı giriniz:"))
us = int(input("Üs olacak sayıyı giriniz:"))
    
sayi=1
for i in range(0,us):
    sayi = taban * sayi

print(f"{taban} uzeri {us} sonucu: {sayi}")
"""
# 3)1 ile 5000 arasındaki tek sayıların ve çift sayıların toplamını ayrı ayrı hesaplayıp, ekrana yazdıran yazılımını python dilinde yazınız.
"""
tek_sayi_toplami=0
cift_sayi_toplami=0
for i in range(1,5001):
    if(i % 2 == 0):
        tek_sayi_toplami +=i
    if(i % 2 != 0):
        cift_sayi_toplami +=i

print(f"Tek sayi toplamlari: {tek_sayi_toplami} \n Cift sayi toplamlari: {cift_sayi_toplami}")
"""

# 4)  Klavyeden girilen iki sayıyı çarpma operatörü (*)  kullanmadan çarpan yazılımı python dilinde kodlayınız.
"""
sayi1 =  int(input("İlk sayıyı giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz:"))

eksi_kontrolu=0
if(sayi2 < 0):
    sayi2 = -sayi2
    eksi_kontrolu +=1

sonuc = 0

for i in range (0,sayi2):
    sonuc =  sayi1 + sonuc

if (sayi1<0 and eksi_kontrolu == 1) or eksi_kontrolu== 1:
    sayi2 = - sayi2
    sonuc = -sonuc

print(f"{sayi1} ve {sayi2} carpiminin sonucu: {sonuc}")
"""
# 4)
"""
sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

adet = abs(sayi2)
deger = abs(sayi1)

sonuc = 0
for _ in range(adet):
    sonuc += deger

# Sayılardan yalnızca biri negatifse sonuç negatiftir
if (sayi1 < 0 and sayi2 > 0) or (sayi1 > 0 and sayi2 < 0):
    sonuc = -sonuc

print(f"{sayi1} ve {sayi2} carpiminin sonucu: {sonuc}")
"""

"""
5) Ritmik sayma sayıları şu şekildedir.
2-4-6-8….
3-6-9-12…
4-8-12-16…
…
9-18-27-36
1'den 10'a kadar olan tüm sayıların 100'e kadar olan ritmik sayılar tablosunu iç-içe döngü yapılarını kullanarak python dilinde kodlayınız.
"""
"""
for i in range (2,10):
    for j in range (1,100):
        if j % i == 0:
            print(j," ")    
    print("\n" + "*"*10)
"""


#6)Klavyeden girilen ikilik sayı sistemindeki herhangi bir sayıyı 10'luk sayı sistemine çeviren yazılımı python dilinde yazınız. 
"""
ikilik_sayi= input("Ikilik sayi sisteminden bir sayi giriniz:")

onluk_sayi = 0

ters_sayi = ikilik_sayi[::-1]
for i in range(len(ikilik_sayi)):
    onluk_sayi += int(ters_sayi[i])*(2**i)

print(f"{ikilik_sayi} sayisinin 10'luk tabandaki degeri: {onluk_sayi}")
"""

#7)
"""
7) 0 ile 100 arasında rastgele sayı üretip, kullanıcının bu sayıyı tahmin etmesini isteyen ve kaç tahmin sonunda sayıyı bulduğunu kullanıcıya gösteren 
yazılımı python dilinde kodlayınız.
Not: Sistemin rastgele sayı üretmesi için random modülünden yararlanabilirsiniz.
import random
sayi=random.randint(1,100) 
"""
"""
import random 

random_sayi = random.randint(1,100)

print("Sayı tahmin oyununa hoşgeldiniz!")

tahmin_sayisi = 1

while(True):
    girilen_sayi = int(input(f"{tahmin_sayisi}. tahmininizi yapınız:"))

    if girilen_sayi < random_sayi:
        print("Daha yüksek bir tahmin yapınız.")
    else:
        print("Daha küçük bir tahmin yapınız.")

    if( girilen_sayi !=  random_sayi):
        tahmin_sayisi +=1

    else:
        print(f"Tebrikler! {tahmin_sayisi}. tahminde doğru buldunuz.")
        break
"""

#8) 11 + 22 + 33 + ... + 10001000 işleminden elde edilen sayının son 10 rakamını hesaplayan yazılımı python dilinde yazınız.
"""
toplam =0

for i in range(1,1001):
    toplam += i**1

son_on_rakam = str(toplam)[-10:]
print(f"Elde edilen sonucun son 10 rakamı:{son_on_rakam}")
"""

#9) 
"""
ilk 10 doğal sayının kareleri toplamı:
12 + 22 + ... + 102 = 385
ilk 10 doğal sayının toplamlarının karesi:
(1 + 2 + ... + 10)2 = 552 = 3025
Bunlar arasındaki fark = 3025-385 = 2640'dır. Buna göre;
ilk 100 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki farkı hesaplayan yazılımı python dilinde yazınız.
"""
"""
karelerin_toplami = 0
toplam=0
for i in range(1,101):
    karelerin_toplami += i**2 
    toplam += i

fark = (toplam**2) - karelerin_toplami

print(f"ilk 100 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki fark: {fark}")
"""

#10)İç içe for döngü yapısını kullanarak çarpım tablosunu ekrana yazdıran yazılımı python dilinde yazınız.
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}: {i*j} ")
    print("*"*15)
"""