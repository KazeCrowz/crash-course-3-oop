from geometry.bangunruang import BangunRuang
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(f'hasil dari luasnya adalah {p1.hitung_luas()}')

s1 = Segitiga(5, 8)
print(s1.info())
print(f'hasil dari luas segitiga adalah {s1.hitung_luas()}')

print('\nMencoba membuat object dari Bangunruang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism : Kemampuan object merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for BangunRuang in daftar_bangun_ruang:
    print(BangunRuang.info())