import math
deniz_kenari_ks=2
sehir_merkezi_ks=1.5
kirsal_ks=0.75

def modern(girilen_deger):
    return girilen_deger*girilen_deger
def geleneksel(girilen_deger):
    return girilen_deger * math.pi
def eski(girilen_deger):
    return girilen_deger * math.e
def dis_cephenin_fiyati(bolge_katsayisi,puanlama):
    return bolge_katsayisi * puanlama * 500