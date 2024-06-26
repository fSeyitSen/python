import sqlite3

# Kullanıcıdan metinleri al
metin1 = input("Birinci metni girin: ")
metin2 = input("İkinci metni girin: ")

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('metinler.db')
c = conn.cursor()

# Metinler tablosunu oluştur
c.execute('''CREATE TABLE IF NOT EXISTS metinler
             (id INTEGER PRIMARY KEY, metin TEXT)''')

# Metinleri veritabanına ekle
c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))

# Veritabanı değişikliklerini kaydet
conn.commit()

# Veritabanı bağlantısını kapat
conn.close()

# Benzerlik hesaplama fonksiyonu
def jaccard_benzerlik(metin1, metin2):
    kume1 = set(metin1.split())
    kume2 = set(metin2.split())
    kesisim = len(kume1.intersection(kume2))
    birlesim = len(kume1.union(kume2))
    return kesisim / birlesim

# Benzerlik hesapla
benzerlik_orani = jaccard_benzerlik(metin1, metin2)

# Benzerlik sonucunu ekrana yazdır
print("Metinler arasindaki benzerlik orani:", benzerlik_orani)

# Benzerlik sonucunu dosyaya yazdır
with open('benzerlik_durumu.txt', 'w') as dosya:
    dosya.write("Metinler arasindaki benzerlik orani: " + str(benzerlik_orani))
    dosya.write("\n")  
