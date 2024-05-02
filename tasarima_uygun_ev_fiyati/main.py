from dis_cephe import * #dis_cephe.py modülü koda dahil edilir
from ic_cephe import *  #ic_cephe.py modülü koda dahil edilir

def main():
    gecmis_hesaplamalar=[]  #ortalama ev fiyatını bulmak için geçmişte hesaplanan ev fiyatlarını tutan bir dizi oluşturulur
    while True: #break ile kırılana kadar devam eden sonsuz bir döngü oluşturulur
        
        dis_cephe_tasarimi = input("Dış cephe tasarımını seçmek için modern(m/M), geleneksel(g/G), eski(e/E) harflerinden birini giriniz (çıkış yapmak için (h/H)): ")
        if dis_cephe_tasarimi=='h' or dis_cephe_tasarimi=='H':
            break
        if dis_cephe_tasarimi=='m' or dis_cephe_tasarimi=='M':
            kullanici_puani = float(input("Modern dış cephe tasarımını puanlayın:"))
            puanlama = modern(kullanici_puani)
        elif dis_cephe_tasarimi=='g' or dis_cephe_tasarimi=='G':
            kullanici_puani = float(input("Geleneksel dış cephe tasarımını puanlayın:"))
            puanlama = geleneksel(kullanici_puani)
        elif dis_cephe_tasarimi=='e' or dis_cephe_tasarimi=='E':
            kullanici_puani = float(input("Eski dış cephe tasarımını puanlayın:"))
            puanlama = eski(kullanici_puani)
        else:
            print("Yanlış seçimde bulundunuz.")
            continue
        
        
        mekan_secimi = input("Evin bulunacağı alanı seçmek için deniz kenarı(d/D), şehir merkezi(s/S), kırsal(k/K) harflerinden birini giriniz: ")
        if mekan_secimi=='d' or mekan_secimi=='D':
            bolge_katsayisi = deniz_kenari_ks
        elif mekan_secimi=='s' or mekan_secimi=='S':
            bolge_katsayisi = sehir_merkezi_ks
        elif mekan_secimi=='k' or mekan_secimi=='K':
            bolge_katsayisi = kirsal_ks
        else:
            print("Yanlış seçimde bulundunuz.")
            continue
        
        
        en = float(input("İç cephenin enini giriniz:"))
        boy = float(input("İç cephenin boyunu giriniz:"))
        
        metreKare = metre_kare(en,boy) #evin metrekaresi hesaplanır
        
        
        ic_tasarim_degerlendirme = input("İç cephe tasarımını yorumlamak için lüks(l/L), güzel(g/G), idare eder(ı/I) harflerinden birini giriniz: ")
        if ic_tasarim_degerlendirme=='l' or ic_tasarim_degerlendirme=='L':
            duzenleme_katsayisi = LUKS
        elif ic_tasarim_degerlendirme=='g' or ic_tasarim_degerlendirme=='G':
            duzenleme_katsayisi = GUZEL
        elif ic_tasarim_degerlendirme=='ı' or ic_tasarim_degerlendirme=='I':
            duzenleme_katsayisi = IDARE_EDER
        else:
            print("Yanlış seçimde bulundunuz.")
            continue
        
        dis_fiyati = dis_cephenin_fiyati(bolge_katsayisi, puanlama)
        ic_fiyati = ic_cephenin_fiyati(metreKare , duzenleme_katsayisi)
        
        genel_fiyat = dis_fiyati*40 + ic_fiyati*60
        gecmis_hesaplamalar.append(genel_fiyat)
        print(f"Evin toplam fiyatı:{genel_fiyat: .2f}")
        
        if len(gecmis_hesaplamalar) > 0:
            #gecmis_hesaplamalar dizisindeki değerler toplanarak gecmis_hesaplamalar dizisinin uzunluğuna bölünerek ortalama hesaplanır
            ortalama_fiyat = sum(gecmis_hesaplamalar) / len(gecmis_hesaplamalar)
            print(f"Evin ortalama fiyatı: {ortalama_fiyat: .2f}")

if __name__ == "__main__":
    main()
    