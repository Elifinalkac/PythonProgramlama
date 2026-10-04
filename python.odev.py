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

#11)
"""
Bir sayı eğer 4 basamaklı ise ve sayıyı oluşturan rakamlardan her birinin 4. kuvvetinin toplamı  (3 basamaklı sayılar için 3.kuvveti) o sayıya eşitse 
bu sayıya "Armstrong" sayısı denir.
Örnek: 1634 = 14 + 64 + 34 + 44 = 1634
Kullanıcıdan alınan bir sayının "Armstrong" sayısı olup olmadığını bulan yazılımı python dilinde programlayınız.
"""
"""
sayi = input("Sayi giriniz:")
toplam =0

for i in range(len(sayi)):
    toplam += int(sayi[i])**len(sayi)

if int(sayi) == toplam:
    print("Girilen sayi bir Armstrong sayidir.")

else:
    print("Girilen sayi bir Armstrong sayi degildir.")
"""

#12) 
"""
215 = 32768 ve basamaklarının toplamı 3 + 2 + 7 + 6 + 8 = 26 'dır.
Buna göre, klavyeden girilecek x ve y sayılarından oluşacak xy sayısının değerinin basamakları toplamını hesaplayan yazılımı python dilinde yazınız.
"""
"""
import math

x = int(input("Taban degerini giriniz:"))
y= int(input("Us degerini giriniz:"))

sonuc = pow(x,y)

basamak_toplami = 0
for i in str(sonuc):
    basamak_toplami += int(i)

print(f"{x}^{y} ifadesinin sonucu: {sonuc} ve basamaklari toplami :{basamak_toplami}")
"""

#13)  Klavyeden girilecek n sayısı için 11+22+33+…..nn değerini hesaplayan yazılımı python dilinde yazınız.
"""
n= int(input("Bir sayi giriniz:"))
toplam =0
for i in range(1,n+1):
    toplam += i**i

print(f"Sonuc:{toplam}")
"""

#14) 
"""
 3'ün veya 5'in katı olan 10'dan küçük tüm doğal sayıları listelersek, 3, 5, 6, ve 9'u elde ederiz. Bu katların toplamı 23'tür.
3'ün veya 5'in 1000'den küçük tüm katlarının toplamını hesaplayan yazılımı python dilinde programlayınız.
"""
"""
toplam = 0
for i in range(1,1000):
    if(i % 3 == 0 ) or (i%5 ==0):
        toplam += i
print(f"3'ün veya 5'in 1000'den küçük tüm katlarının toplamı:{toplam}")
"""

#15)
"""
k > 0 olmak şartıyla (k-1) sayısı 4’e tam bölünüyorsa hilbert sayısı olarak adlandırılır. 
Örnek: 9 sayısının 1 ekseği olan 8 sayısı 4'e tam bölündüğü için 9 sayısı hilbert sayıdır.
1000'den küçük tüm hilbert sayılarını listeleyen yazılımı python dilinde yazınız.
"""
"""
for k in range(1,1000):
    if (k-1)%4 == 0:
        print(k)
"""

#16) 
"""
n! şu şekilde yazılabilir : 1*2*3*......(n-1)*n
Örneğin, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800.
Ve 10! sayısının basamaklarının toplamı da 3 + 6 + 2 + 8 + 8 = 27 'dir.
Yukarıdaki örnekte olduğu gibi, girilen sayının faktöriyel değerinin basamakları toplamını hesaplayan yazılımı python dilinde yazınız.
"""
"""
n= int(input("Bir sayı giriniz:"))
faktoriyel_sonuc=1

for i in range(n,0,-1):
    faktoriyel_sonuc *= i


toplam = 0
for j in str(faktoriyel_sonuc):
    toplam += int(j)

print(f"Faktoriyel sonucu:{faktoriyel_sonuc} \n Sonucun toplami:{toplam}")
"""

#17) Kullanıcının girdiği sayıyı 2'lik sayı sistemine çeviren yazılımı python dilinde yazınız.
"""
sayi = int(input("Sayi giriniz:"))
sonuc = ""

if sayi == 0:
    sonuc = "0"

gecici_sayi = sayi
while(gecici_sayi>0):
    kalan = gecici_sayi%2
    sonuc= str(kalan) +sonuc
    gecici_sayi = gecici_sayi//2

print(f"{sayi} sayisinin 2'lik sistemdeki karsiligi: {sonuc}")
"""

#18)
# Aşağıdaki tekrarlama dizisi pozitif tam sayılar için tanımlanmıştır:
# n → n/2 (n çift)
# n → 3n + 1 (n tek)
# Yukarıdaki kuralı uygulayarak ve 13'ten başlayarak aşağıdaki diziyi üretiriz:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 13'ten başlayıp 1'de sonlanan bu dizinin 10 adet terim içerdiği görülebilir. Henüz kanıtlanmış olmasa da (Collatz Problemi), bütün başlangıç 
# sayılarının 1'de sonuçlanacağı sanılmaktadır.
# Siz de, klavyeden girilecek herhangi bir pozitif tam sayının collatz zincirini oluşturan yazılımı python dilinde yazınız.

"""
n = int(input("Pozitif bir tamsayi giriniz:"))


if(n<0):
    print("Lütfen pozitif bir tamsayı giriniz!")
    exit()

# while(True):
#     n = int(input("Pozitif bir tamsayi giriniz:"))
#     if n>0:
#         break
#     print("Lütfen pozitif bir tamsayı giriniz!")

zincir = [n]
while n>1 :
    if n%2==0:
        n = n//2
    else:
        n=3*n+1
    zincir.append(n)

print("->".join(map(str,zincir)))
print(f"Toplam terim sayisi: {len(zincir)}")
"""

#19)
# Üçgensel sayı dizileri ardışık doğal sayıların toplanmasıyla üretilir. 
# Örneğin 7. üçgensel sayı 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'dir. İlk 10 üçgensel sayı şöyledir:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
# Siz de, klavyeden girilecek herhangi bir pozitif tam sayının üçgensel sayı değerini hesaplayan yazılımı python dilinde yazınız
"""
sayi = int(input("Tamsayı giriniz:"))

toplam=0
dizi =[sayi]
for i in range(1,sayi+1):
    toplam += i
    dizi.append(i)
print(f"{dizi}={toplam}")
"""

#20)
# 10'dan küçük asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir.
# 2 milyondan küçük bütün asal sayıların toplamını bulan yazılımı python dilinde yazınız.

      
