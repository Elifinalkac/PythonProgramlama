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

# rastgele_sayi = random.randint(1,100)
# print("1 ile 100 arasında bir sayı tuttum. Tahmin edin!")

# while True:
#     tahmin = int(input("Tahmininiz: "))
#     if tahmin < rastgele_sayi:
#         print("Daha büyük bir sayı deneyin!")
#     elif tahmin > rastgele_sayi:
#         print("Daha küçük bir sayı deneyin!")
#     else:
#         print("Tebrikler! Doğru tahmin.")
#         break


# sayi = int(input("Bir sayi girin:"))

# if  sayi%2 == 0:
#     print("Girdiğiniz sayi cift sayıdir.")
# else:
#     print("Girdiginiz sayi tek sayidir.")


# for i in range(1,101):
#     print(i,end=" ")

# tr_harfler = "ŞşÇçĞğÖöÜüİı"
# parola = input("Parolanız:")
# for karakter in parola:
#     if karakter in tr_harfler:
#         print("Parolada Türkçe karakter kullanılamaz")



# sayi = int(input("Sayi giriniz:"))

# karekok = sayi**0.5

# print(f"Sonuc:{karekok}")

# import time
# baslangicZamani  = time.perf_counter()
# time.sleep(5)
# ad = input("İsminizi giriniz:")
# zaman = time.perf_counter() - baslangicZamani
# print("İsminizi tam", zaman, "saniyede girdiniz.")
# print(f"Baslangic zamani: {baslangicZamani}")

# import random
# for i in range(1):
#     print(random.randrange(1, 100))


# kelime = input("Bir kelime giriniz:")
# uzunluk = len(kelime)
# kontrol = 0
# for i in range(0,uzunluk//2):
#     if kelime[i] != kelime[uzunluk-i-1] :
#         print("Kelime palindrom değil")
#         kontrol +=""
#         exit()
# if kontrol ==0:
#     print("Kelime palindrom")  

# metin = input("Bir metin giriniz:")
# kelimeler = metin.split(",")
# print(kelimeler)

# metin = input("Bir metin giriniz:")
# kelimeler =  metin.split()
# frekans = {}
# for kelime in kelimeler:
#     if kelime in frekans:
#         frekans[kelime] += 1
#     else:
#         frekans[kelime] = 1
# for kelime, sayi in frekans.items():
#     print(f"{kelime}: {sayi}")



# for i in range(1,5):
#     for n in range(1,4-i):
#         print(" ",end="")
#     for j in range (1,i):
#         print("**",end="")
#     print("\n")

# hava_durumu = input("Yozgat'taki hava durumu nasıl? (güneşli/ yağmurlu / soğuk) : ")

# if hava_durumu == "güneşli":
#     print("Tişört ve şağka giymelisin!")

# elif hava_durumu == "yağmurlu":
#     print("Şemsiyeni almayı unutma!")
# elif hava_durumu == "soğuk":
#     print("Mont ve atkı giymelisin!")
# else: 
#     print("Geçersiz bir hava durumu girdiniz.")

# while(True):
#     hava_durumu = input("Yozgat'taki hava durumu nasıl? (güneşli/ yağmurlu / soğuk) : ")

#     if hava_durumu == "güneşli":
#         print("Tişört ve şağka giymelisin!")

#     elif hava_durumu == "yağmurlu":
#         print("Şemsiyeni almayı unutma!")
#     elif hava_durumu == "soğuk":
#         print("Mont ve atkı giymelisin!")
#     else: 
#         print("Geçersiz bir hava durumu girdiniz.")
       
# vize = int(input("Vize notunuzu giriniz:"))
# final = int(input("Final notunuzu giriniz:"))

# ortalama = (vize * 0.4) + (final*0.6)

# if ortalama >= 60 and final >= 50:
#     print(f"Tebrikler! {ortalama: .2f}ortalama ile geçtiniz.")
# else:
#     print(f"Maalesef, {ortalama:.2f} ortalama ile kaldınız.")

# ilceler = ["Sorgun", "Akdağmadeni", "Boğazlıyan", "Çayıralan"]

# ilceler.append("Şefaatli")
# print("Güncel ilçeler:",ilceler)

# ilceler.insert(2, "Yerköy")
# print("Yeni Liste:", ilceler)

# ilceler.remove("Boğazlıyan")
# print("Boğazlıyan çıkarıldı:",ilceler)

# ilceler.sort()
# print("Sıralanmış İlçeler:", ilceler)


# def ogrenci_kayit(ad,soyad):
#     print(f"Öğrenci Kaydedildi: {ad} {soyad}")

# isim = input("Adınızı girin:")
# soyisim = input("Soyadınızı girin: ")

# ogrenci_kayit(isim, soyisim)

# def ortalama_hesapla(vize,final):
#     return (vize * 0.4) + (final*0.6)

# vize_notu = int(input("Vize notunuzu girin:"))
# final_notu = int(input("Final notunuzu girin:"))

# ortalama = ortalama_hesapla(vize_notu, final_notu)
# print(f"Ortalamanız: {ortalama:.2f}")

yozgat_yemekleri = {"arabaşı çorbası", "testi kebabı", "madımak", "tandır kebabı"}

ankara_yemekleri = {"ankara tava", "testi kebabı", "beypazarı güveci", "yoğurtlu çorba"}

ortak = yozgat_yemekleri & ankara_yemekleri
ozel_yozgat = yozgat_yemekleri - ankara_yemekleri
tum_yemekleri = yozgat_yemekleri | ankara_yemekleri

print(f"Ortak yemekler: {ortak}")
print(f"Yozgat'a özgü yemekler: {ozel_yozgat}")
print(f"Her iki şehirdeki yemekler: {tum_yemekleri}")