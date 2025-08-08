#=========================================library==========================================

import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np

import pandas as pd

import os,time
#=========================================Variable==========================================

Directorti = 'BelajarMesin/Plotlip/'

Filminfo = pd.read_csv(f"{Directorti}/filmbaru2050.csv" )

#=========================================Function==========================================

def hapus(text,second):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(second):
        for j in range(4):
            print(f"{text}{'.'*j}")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

print("--- Data Penjualan Komponen Komputer ---")
print("\nDataFrame:")
print(Filminfo)

fiRlm_plot=Filminfo.set_index("bulan")
totalfilmjual =fiRlm_plot.sum()
def show_line_chart():
    """Menampilkan Kehidupan"""
    fig, ax = plt.subplots(num="Figur1", figsize=(10, 6))
    ax.set_title('Tren Penjualan Produk per Bulan', fontsize=32)
    fiRlm_plot.plot(kind='line', ax=ax, marker='o')
    ax.set_xlabel('Bulan', fontsize=16)
    ax.set_ylabel('Jumlah Penjualan', fontsize=16)
    plt.tight_layout()
    plt.show()
 
"""Manampilkan Kehidupan
Part 2 diagram Batang """
def show_bar_chart():
    fig, Lmao = plt.subplots(num="Diagram Batang", figsize=(10, 6)) 
    Lmao.set_title('Total Penjualan per Produk (Selama 12 Bulan)', fontsize=32)
    totalfilmjual.plot(kind="bar", ax=Lmao, color=['skyblue', 'salmon', 'lightgreen', 'orange'])
    Lmao.set_xlabel('Produk', fontsize=16)
    Lmao.set_ylabel('Total Penjualan', fontsize=16)
    Lmao.tick_params(axis='x', rotation=0)
    plt.tight_layout()
    plt.show()

produk_terlaris = totalfilmjual.idxmax()
jumlah_telalis = totalfilmjual.max()
print(f"Produk Terlaris: {produk_terlaris} with total sales: {jumlah_telalis}")

Filminfo['Total_Penjualan_Bulanan'] = Filminfo[['GogOPOWERANGER', 'Woolkong', 'Averager', 'Princesrubansel','Doctornormal', 'Whirelies']].sum(axis=1)
bulan_terlaris = Filminfo.loc[Filminfo['Total_Penjualan_Bulanan'].idxmax()]["bulan"]
total_penjualan_bulan_terlaris = Filminfo['Total_Penjualan_Bulanan'].max()
print(f"Bulan dengan total penjualan paling tinggi adalah '{bulan_terlaris}' dengan total: {total_penjualan_bulan_terlaris}")

rootbeer = tk.Tk()
rootbeer.title("Aplikasi Visualisasi Info Film")
rootbeer.geometry("400x200") 

frame = ttk.Frame(rootbeer, padding="20")
frame.pack(expand=True, fill='both')

label_title = ttk.Label(frame, text="Pilih Visualisasi yang Ingin Ditampilkan:", font=("Helvetica", 14, "bold"))
label_title.pack(pady=10)

button_line = ttk.Button(frame, text="Tampilkan Tren Penjualan", command=show_line_chart)
button_line.pack(pady=5, ipadx=10, ipady=5)

button_bar = ttk.Button(frame, text="Tampilkan Total Penjualan", command=show_bar_chart)
button_bar.pack(pady=5, ipadx=10, ipady=5)

rootbeer.mainloop()

# print(Filminfo.info())




# print("\nStatistik Deskriptif:")
# print(Filminfo.describe())


