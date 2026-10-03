"""
a =15
cevap =15*7*14
print ("Bir öğ rencini harcad ığı toplam süre: ", cevap ,"dk 'dır") 
"""

""""
istenen_stok = 0
stok = 3
istenen_stok = int ( input ("Lü tfen kaç adet ürün almakistedi ğ inizi giriniz : "))
while True :
    if istenen_stok > 3:
        print (" Stokta istenilen kadar ürün bulunmamakta .")
        break
    print("Sipariş başarılı.")
    break
"""

"""
def ders_saatleri_baslat():
    saat =8 
    dakika =15

    while True:
        print(f"{saat}:{dakika:02d} - Ders Zili")
        dakika += 45
        if dakika >= 60:
            dakika -= 60
            saat += 1


        if saat == 17:
            print("Mesali sona erdi.")
            break

ders_saatleri_baslat()
"""

""""
#Vücut Kitle Endeksi Hesaplama
boy = float (input("Lütfen boyunuzu metre cinsinden giriniz:"))
kilo = float(input("Lütfen kilonuzu kilogram cinsinden giriniz:"))

vki = kilo / (boy **2)
print(f"Vücut Kitle İndeksiniz: {vki: .2f}")

if vki <18.5:
    print("Zayıf")
elif 18.5 <= vki < 24.9:
    print("Normal")
elif 15 <= vki < 29.9:
    print("Fazla Kilolu")
else:
    print("Obez")
"""

""""
#Fibonacci Serisi
n = int(input("Kaç terim görmek istiyorsunuz?"))
fibonacci = [0,1]
for i in range(2,n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci[:n])
"""

"""
#Çaprım tablosu 
for i in range (1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 20)
"""

#En büyük ve en küçük sayıyı bulma
"""
def faktoriyel(sayi):
    if sayi == 1 or sayi == 0:
        return 1
    else:
       return sayi*faktoriyel(sayi-1)

sayi = int(input("Bir sayı giriniz:"))
print(f"{sayi}! =  {faktoriyel(sayi)}")
"""

import random 

rastgele_sayi = random.randint(1,100)
print("1 ile 100 arasında bir sayı tuttum. Tahmin edin!")

while True:
    tahmin = int(input("Tahmininiz: "))
    if tahmin < rastgele_sayi:
        print("Daha büyük bir sayı deneyin!")
    elif tahmin > rastgele_sayi:
        print("Daha küçük bir sayı deneyin!")
    else:
        print("Tebrikler! Doğru tahmin.")
        break