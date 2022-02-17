# Başla

gelir = int(input('Gelirinizi yazınız: '))
gider = int(input('Giderinizi yazınız: '))
if gelir >= gider:
    x = gelir-gider
    print(f'Kalan Paranız: {x}')
else:
    y = gider-gelir
    print(y)
x = gelir-gider
kalan = (int(x))
meyve = int(input("Meyveye ödenecek tutar: "))
sebze = int(input("Sebzeye ödenecek tutar: "))
result = meyve+sebze

if x >= result:
    print(f"Ürünleri alabildiniz. Meyve için harcanan tutar: {meyve}, sebze için harcanan tutar: {sebze}")
else:
    print(f"Paranız yeterli değil. Meyve için harcanan tutar: {meyve}, sebze için harcanan tutar: {sebze}")
para = kalan-result
print(f"Geriye kalan para: {para}TL")

# Tarih: 16.02.2022
# Geriye kalan parayı ekrana yazdırmaya çalışıyoruz
# Tarih: 17.02.2022
# Sorun çözüldü, "x" değişkeni atadık ve "kalan" değişkenini "str" ifadeyken "int" ifadeye çevirdik