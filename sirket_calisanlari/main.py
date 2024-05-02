class kimlik:
    def __init__(self,tc,ad,soyad,dogum_tarihi):
        self.tc = tc
        self._ad = ad  #ad değişkenini private yapmak için başına '__' ekledik
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi

class personel(kimlik):
    personel_id_maas_dict = {}
    def __init__(self, tc, ad, soyad, dogum_tarihi, departman, giris_gunu, giris_ayi, giris_yili, maas):
        super().__init__(tc, ad, soyad, dogum_tarihi)
        self.__departman = departman  #departman değişkenini private yapmak için başına '__' ekledik
        self.__giris_gunu = giris_gunu
        self.__giris_ayi = giris_ayi
        self.__giris_yili = giris_yili
        self.__maas = maas #maas değişkenini private yapmak için başına '__' ekledik
        
        self.personel_id_maas_dict[self.id_olustur()] = maas #personellerin personel_id'si ile ilişkilendirilmiş maaş bilgisini sözlüğe ekler
    
    #private değişkenler için get ve set metotlarını kullanıyoruz
    def get_ad(self):  #get metodu belirli bir özelliğin değerini döndürür
        return self._ad
    def set_ad(self,ad):  #set metodu belirli bir özelliğin değerini değiştirir
        self._ad = ad
    
    def get_departman(self):
        return self.__departman
    def set_departman(self,departman):
        self.__departman = departman
        
    def get_giris_tarihi(self):
        giris_tarihi = self.__giris_gunu, self.__giris_ayi, self.__giris_yili #gun,ay,yil değişkenlerini giris_tarihi değişkenine atıyoruz
        return giris_tarihi
    def set_giris_tarihi(self,giris_gunu,giris_ayi,giris_yili):
        self.__giris_gunu = giris_gunu
        self.__giris_ayi = giris_ayi
        self.__giris_yili = giris_yili
    
    def get_maas(self):
        return self.__maas
    def set_maas(self,maas):
        self.__maas = maas
    
    #bilgileri ekrana yazdırır    
    def __str__(self):
        bilgi = f"Ad: {self._ad}, Departman: {self.__departman}, Giriş tarihi: {self.get_giris_tarihi()}, Maaş: {self.__maas}"
        return bilgi
    
    #personel bilgileriyle id oluşturan metot
    def id_olustur(self):
        #adın ilk 2 harfi,departmanın son 2 harfi ve giriş tarihinin günü ve ayını birleştirere bir id oluşturularak personel_id değişkenine atanır
        personel_id = self._ad[:2] + self.__departman[-2:] + f"{self.__giris_gunu}{self.__giris_ayi}" 
        return personel_id

def main():
    personeller = [] #personelleri saklayacak olan liste
    departman_maaslari = {} #departman maaşlarını saklayacak olan sözlük
    toplam_maas = 0
    
    while True: #break ile kırılana kadar devam eden sonsuz bir döngü
        print("\n") #çıktının terminalde daha düzenli durması için
        ad = input("Adınız(Çıkış için 'h/H'): ") 
        if ad == 'h' or ad == 'H': #'h' veya 'H' girildiği zaman döngüyü sonlandırır
            print("\n")
            break 

        soyad = input("Soyadınız: ") 
        tc = input("TC numaranız: ")
        dogum_tarihi = input("Doğum tarihiniz(gün.ay.yıl): ")  
        departman = input("Departmanınız: ")
        giris_gunu, giris_ayi, giris_yili = input("Giriş tarihiniz(gün.ay.yıl): ").split(".") #kullanıcıdan giriş tarihinin gününü,ayını ve yılını alarak "." ile ayırır
        maas = int(input("Maaşınız: ")) 
        
        personel_nesne= personel(tc,ad,soyad,dogum_tarihi,departman,giris_gunu,giris_ayi,giris_yili,maas) #personel nesnesini oluşturur
        personeller.append(personel_nesne) #personel nesnesini personeller listesine ekler
        
        departman_maaslari[departman] = departman_maaslari.get(departman, 0) + maas #belirli bir departmana ait maaş bilgisini günceller
        toplam_maas += maas
        
    print(f"Şirketin toplam maaşı: {toplam_maas}") #toplam maaşı ekrana yazdırır
    print(f"Şirketin ortalama maaşı: {toplam_maas / len(personeller)}\n") #toplam maaşı personel listesinin uzunluğuna bölerek ortalama maaşı ekrana yazdırır
        
    for departman, maas in departman_maaslari.items(): #belirli bir departmana ait maaşlar ile ilgili bir döngü başlatır
        print(f"{departman} Departmanı:")
        print("************************")
        personel_sayisi = sum(1 for personel in personeller if personel.get_departman() == departman) #belirli bir departmana ait personel sayısını hesaplar
        #personel sayısını hesaplarken kullanılan sum ifadesi eğer kişinin departmanı verilen departmana eşit ise 1 değerini döndürür ve döndürülen tüm 1 değerlerini toplayarak kişi sayısını bulur
        en_yuksek = max(personel.get_maas() for personel in personeller if personel.get_departman() == departman) #belirli bir departmana ait en yüksek maaşı hesaplar
        en_dusuk = min(personel.get_maas() for personel in personeller if personel.get_departman() == departman) #belirli bir departmana ait en düşük maaşı hesaplar

        print(f"Toplam Maaş: {maas}")
        print(f"Personel Sayısı: {personel_sayisi}")
        print(f"En Yüksek Maaş: {en_yuksek}")
        print(f"En Düşük Maaş: {en_dusuk}\n")
            
    for personel_nesne in personeller:
        print(personel_nesne) #personeller listesi içerisinde bulunan personel nesnelerini ekrana yazdırır
    
    print("\n")    
    print(personel.personel_id_maas_dict) #personellerin id'si ile ilişkilendirilen maaş bilgilerini ekrana yazdırır

if __name__ == "__main__":
    main()
    
    