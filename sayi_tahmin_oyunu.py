
import random

def tahmin_oyunu():
    sayi1 = random.randint(1,1000)
    deneme_sayisi=0
  
    while True:
        try:
            sayi2=int(input("Bir sayı tahmin ediniz:"))
            deneme_sayisi +=1
        except ValueError:
            print("Lütfen geçerli sayı giriniz:")
            continue
        
        if sayi1> sayi2:
            print("Daha Büyük Sayi Giriniz !!")
        elif sayi1 <sayi2:
            print("Daha küçük bir sayı giriniz!!")
        else:
            print("******************TEBRİKLER********************")
            break
    oyunu_tekrar_oyna= input("Tekrar oynamak istermisin (e/h): ")
    if oyunu_tekrar_oyna.lower()== "e":
        tahmin_oyunu()
    
tahmin_oyunu()