#1
harf = input("harf:")
print(harf * 5)
#2
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

yigindi = son1 + son2
ayirma = son1 - son2
kopaytma = son1 * son2
bolinma = son1 / son2
butun_qism = son1 // son2
daraja = son1 ** son2


print ("Yig'indisi: ", yigindi)
print ("Ayirmasi: ", ayirma)
print ("Ko'paytmasi: ", kopaytma)
print ("Bo'linmasi: ", bolinma)
print ("Darajaga oshirish: ", daraja)
print ("Butun qismi: ", butun_qism)

import math

#3
son3 = float(input("Birinchi sonni kiriting (katta son): "))
son4 = float(input("Ikkinchi sonni kiriting (kichik son): "))


bolinma = son3 / son4


floor_qiymat = math.floor(bolinma)
ceil_qiymat = math.ceil(bolinma)

print ("Kattasini kichikka bo'lish: ", bolinma)
print ("Floor qiymati: ", floor_qiymat)
print ("Ceil qiymati: ", ceil_qiymat)

#4 

son5 = float(input("Birinchi sonni kiriting: "))
son6 = float(input("Ikkinchi sonni kiriting: "))


pow_qiymat = math.pow(son5, son6)
sqrt_qiymat1 = math.sqrt(son5)
sqrt_qiymat2 = math.sqrt(son6)
abs_qiymat1 = abs(son5)
abs_qiymat2 = abs(son6)

print ("Pow qiymati: ", pow_qiymat)
print ("Abs qiymati: ", abs_qiymat1)
print ("Abs qiymati: ", abs_qiymat2)
print ("Sqrt qiymati: ", sqrt_qiymat1)
print ("Sqrt qiymati: ", sqrt_qiymat2)
