# @author dono/ozkan0
# tr, basit parola oluşturucu
# en, basic password generator
import random

charsTR="abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@£$%^&*().,?0123456789"

uzunluk = int(input("Parola uzunluğunu belirleyin: "))
adet = int(input("Kaç adet parola oluşturulsun?: "))

for a in range(adet):
    password=""
    for b in range(uzunluk):
        password += random.choice(charsTR)
    print(password)
print("\nParola oluşturuldu")