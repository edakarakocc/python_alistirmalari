import random #rastgele sayı kütüphanesi eklendi

MIN_SAYI=50
MAX_SAYI=250
MAX_TAHMIN=10
basarili_tahminler=[] #oyun birden fazla kez oynandığında en başarılı tahminin bulunması için oluşturulan dizi

while True: #break ifadesi ile durdurulana kadar sonsuz bir döngü oluşturur
    rastgele_sayi = random.randint(MIN_SAYI,MAX_SAYI) #minimum ve maksimum değerler arasından rastgele bir sayı seçilmesini sağlar
    tahmin_sayisi=0 #her oyun başladığında tahmin sayısını sıfırlar
    tahminler=[] #önceden tahmin edilen sayıların tutulması için oluşturulan dizi
    print(rastgele_sayi)
    while tahmin_sayisi<MAX_TAHMIN:
        tahmin=int(input("Sayı tahmin ediniz:"))
        
        if tahmin<MIN_SAYI or tahmin>MAX_SAYI:
            print("Lütfen 50-250 aralığından bir sayı seçiniz.")
            continue
        tahmin_sayisi+=1
        tahminler.append(tahmin) #tahmin edilen değerleri tahminler dizisinin içine ekler
        
        if tahmin<rastgele_sayi:
            print("Daha büyük sayı tahmin ediniz.")
        elif tahmin>rastgele_sayi:
            print("Daha küçük sayı tahmin ediniz.")
        else:
            print(f"{rastgele_sayi} sayısını tahmin ederek doğru tahminde bulundunuz.")
            print(f"Doğru sayıyı {tahmin_sayisi}. tahminde buldunuz.")
            print("Önceki tahminleriniz:",tahminler)
            basarili_tahminler.append(tahmin_sayisi) #en başarılı tahmini bulmak için tahmin sayılarını basarili_tahminler dizisinin içine ekler
            break
    if tahmin_sayisi == MAX_TAHMIN:
        print("Tahmin hakkınız bitti. Doğru sayı:",rastgele_sayi)
    
    mod=input("Tekrar oynamak ister misiniz? (Evet için e/E, hayır için h/H):")
    if mod.lower() != "e": #e harfinden başka bir harf girildiğinde döngüyü kırarak programı sonlandırır
        break
if basarili_tahminler: #en az bir doğru tahmin yapılmışsa en başarılı tahmini buluyoruz
    en_basarili_tahmin = min(basarili_tahminler) #basarili_tahminler dizisi içerisindeki en az tahmin sayısını bulur
    print(f"En başarılı tahmin: {en_basarili_tahmin} tahminde.")
else:
    print("Henüz başarılı tahmin yapılmadı.")
