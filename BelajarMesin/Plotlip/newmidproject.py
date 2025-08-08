import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Membuat Data dengan Pandas
# Data penjualan fiktif untuk beberapa produk selama 4 bulan
data_penjualan = {
    'Bulan':        ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul'],
    'Lemonpee':     [ 120 ,  130 ,  150 ,  140 ,  70  ,  50  ,  20  ],
    'Poison':       [ 80  ,  95  ,  100 ,  110 ,  125 ,  140 ,  156 ],
    "jus babi":     [ 10  ,  70  ,  90  ,  130 ,  200 ,  110 ,  112 ],
    "tembok peres": [ 15  ,  30  ,  100 ,  11  ,  130 ,  110 ,  200 ],
    "Es teh tawar": [ 1   ,  15  ,  40  ,  101 ,  20  ,  11  ,  2   ]
}

Penjualan_minuman = pd.DataFrame(data_penjualan)

print(Penjualan_minuman)

Penjualan_minuman["Total Jual"]=Penjualan_minuman[["Lemonpee","Poison","jus babi","tembok peres","Es teh tawar"]].sum(axis=1)
print(Penjualan_minuman)

ratarata=Penjualan_minuman[["Lemonpee","Poison","jus babi","tembok peres","Es teh tawar"]].mean()
print(ratarata.round(2))

MostValueble=ratarata.idxmax()
MostValueblebutnumber=ratarata.max()
print(MostValueble)
print(MostValueblebutnumber)
plt.figure(figsize=(10, 6))
for product in ["Lemonpee", "Poison", "jus babi", "tembok peres", "Es teh tawar"]:
    plt.plot(data_penjualan["Bulan"], data_penjualan[product], label=product, marker="o")
plt.title("Grafik Penjualan Minuman")
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(data_penjualan["Bulan"], Penjualan_minuman["Total Jual"])
plt.title("Grafik Penjualan Minuman")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(data_penjualan["Bulan"], ratarata)
plt.show()


# 3. Visualisasi Data dengan Matplotlib
# Visualisasi Tren Penjualan Produk Individual (Line Plot)

# Visualisasi Total Penjualan Bulanan (Bar Plot)

# Visualisasi Rata-rata Penjualan per Produk (Bar Plot)