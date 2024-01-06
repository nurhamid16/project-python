import json
import random

file_surah = open("surah.json", encoding="utf8")
surah = json.load(file_surah)

file_surah_terjemah = open("surah-translit-id.json", encoding="utf8")
surah_terjemah = json.load(file_surah_terjemah)

for k in surah:
    s = surah[k]
    s["nama"] = surah_terjemah[k]["nama"]
    s["arti_nama"] = surah_terjemah[k]["nama"]


surah = list(surah.values())
surah_10 = random.sample(surah, k =10)

#siapkan kandidat pilihan salah
pilihan_salah = []
for s in surah:
    pilihan_salah.append(s["arti_nama"])


#memulai permainan
skor = 0
for s in surah_10:
    print(f"arti nama surah {s['nama']} adalah")#cetak pertanyaan
    jawaban_benar = s["arti_nama"]   
    jawaban_user = input("")
    #minta jawabn
    pilihan = random.sample(pilihan_salah, k = 2)# jawaban salah
    random.shuffle(pilihan)# ajak pilihan
    peta_jawaban = {
        "a" : pilihan[0], "b": pilihan[1], "c": pilihan[2]
    }
    print(f"a.{pilihan[0]} b. {pilihan[1]} c.{pilihan[2]}")#cetak pilihan
    pilihan_user = input("a/b/c?:")# meminta jawaban user
    jawaban_user = peta_jawaban[pilihan_user]
    if jawaban_user == jawaban_benar :
        skor += 1
        print(f"Benar! skor anda: {skor}")
    else:
        print(f"salah! jawaban yang benar adalah: {jawaban_benar}")

    print(f"permainan selesai, skor akhir anda: {skor}")