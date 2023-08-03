# @author dono/ozkan0
# tr, basit ürün stok yönetim arayüzü
stok={}
satilanlar=[]
def stok_ekle():
    while True:
        urun_adi=input("Ürünün adını girin: ").lower()
        urun_adeti=int(input("Ürünün adetini girin: "))
        kategori=input("Ürün kategorisi: ")
        stok[urun_adi]=[urun_adeti,kategori]
        durum=input("Başka ürün eklemek ister misiniz? (e/h): ")
        if durum=="h":
            break
def urun_sat():
    while True:
        sat=[]
        urun = input("Satılan ürün adını girin: ").lower()
        for urunler in stok:
            if urunler == urun:
                adet_sat = int(input("Satılan adet: "))
                urun_fiyati=float(input("Ürünün fiyatı: "))
                gelir = adet_sat*urun_fiyati
                sat.extend([urunler,gelir,adet_sat])
                satilanlar.append(sat)
            else:
                print("Böyle bir ürün bulunamadı.")
                break
        durum = input("Satış girmeye devam etmek istiyor musunuz? (e/h): ")
        if durum == "h":
            break
def gun_sonu():
    while True:
        print(f'Bugün satılanlar:')
        for i in satilanlar:
            print(f'{i[0].capitalize()} adlı üründen {i[2]} adet satılmış ve {i[1]}tl elde edilmiş')
        break
    
def menu():
    while True:
        secim = input("\Stok yönetim sistemine hoşgeldiniz.\n1: Stok girişi yap\n2: Ürün satışı gir\n3: Günün özetini al\nq: Çıkış yap\n")
        if secim == "1":
            stok_ekle()
        elif secim == "2":
            urun_sat()
        elif secim == "3":
            gun_sonu()
        elif secim == "q":
            break
        else:
            print("Lütfen geçerli bir seçim yapınız")
menu()