öğrenci_adı = "Semra"

notlar = {"Handan":90, "Semra": 75, "Kamil": 67}
for i in notlar:
    if i == öğrenci_adı:
        print(notlar[i])
        break
    else:
        print("Bu isimde kayıt bulunamadı.")