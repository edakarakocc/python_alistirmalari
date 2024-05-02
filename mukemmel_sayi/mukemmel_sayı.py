mukemmel_adedi=0 #kullanıcının girmiş olduğu mükemmel sayı adedini tutan değişken
genel_toplam=0   #girilen mükemmel sayıların toplamını tutan ifade

while True:   #break ifadesi ile kırılmadığı sürece çalışan sonsuz bir döngü oluşturur
    toplam=0  #girilen sayının bölenlerinin toplamını tutan ifade
    sayi=int(input("Sayı giriniz (çıkış yapmak için 0'a basınız):")) #kullanıcıdan integer sayı alır
    
    if sayi==0: #kullanıcı sıfır girdiği anda programı sonlandırır
        break
    for i in range(1,sayi):
        if sayi % i == 0: #girilen sayının kendisinden başka bölenlerini bulur
            toplam += i #bölenlerin toplamını alır
    if sayi == toplam:
        print("Girmiş olduğunuz sayı mükemmel sayıdır.")
        mukemmel_adedi += 1  #girilen mükemmel sayı adedini arttırır
        genel_toplam += sayi 
    else:
        print("Girmiş olduğunuz sayı mükemmel sayı değildir.")

print("Girmiş olduğunuz mükemmel sayı adedi:",mukemmel_adedi)
if mukemmel_adedi>0: #bölme işleminde paydanın 0 olması tanımsızlık oluşur bunu önlemek için kullanılan bir ifadedir
    print("Girmiş olduğunuz mükemmel sayıların ortalaması:",genel_toplam/mukemmel_adedi)
            