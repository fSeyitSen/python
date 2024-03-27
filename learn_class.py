class Personel:
    def __init__(self, ad, departman, calismaYili, maas):
        self.ad = ad
        self.departman = departman
        self.calismaYili = calismaYili
        self.maas = maas

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel_nesnesi):
        self.personel_listesi.append(personel_nesnesi)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.ad)
            print("Departmanı:", personel.departman)
            print("Çalışma Yılı:", personel.calismaYili)
            print("Maaşı:", personel.maas)
            print("")

    def maasZammi(self, personel_nesnesi, zam_orani):
        personel_nesnesi.maas *= (1 + zam_orani / 100)

    def personel_cikart(self, personel_nesnesi):
        self.personel_listesi.remove(personel_nesnesi)


# Personel nesneleri oluşturma
personel1 = Personel("Ahmet", "Yazılım", 2023, 50000)
personel2 = Personel("Elif", "Bilişim Teknolojileri", 2024, 45000)
personel3 = Personel("Kerem", "Pazarlama", 2020, 32000)
# personel4 = Personel("Nisa", "Yazılım", 4, 65000)

# Firma nesnesi oluşturma
firmaa= Firma()

# Personel ekleme
firmaa.personel_ekle(personel1)
firmaa.personel_ekle(personel2)
firmaa.personel_ekle(personel3)

# Personel listeleme
print("Firmanın Personel Listesi:")
print("")
firmaa.personel_listele()

# Maaş zammı
firmaa.maasZammi(personel1, 50)
print("Ahmet'in yeni maaşı:", personel1.maas)

# Personel çıkartma
firmaa.personel_cikart(personel3)

print("*"*40)
print("")
print("Firmanın güncellenmiş Personel Listesi:")

firmaa.personel_listele()
#firmaa.personel_listele()


