
'''
1 load data
2. cleaning data (kosong, duplikat, transformasi, ubah tipe data)
3. Analisis Data
4. Sort, grouping, agregasi
5. Visualisasi Data (Matplotlib, Seaborn)
'''

#=========================================Library==========================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os, time

#=========================================Variable==========================================
newfile=pd.read_csv("BelajarMesin/KakGel/netflix_titles.csv")


newfile = newfile.dropna() #menghapus data yang kosong
newfile = newfile.drop_duplicates() #menghapus data yang duplikat
newfile = newfile.head(150)
newfile['duration_num'] = newfile['duration'].str.extract('(\d+)').astype(int)
newfile['duration_type'] = newfile['duration'].apply(
    lambda x: 'min' if 'min' in str(x).lower() else 'season'
)
#=========================================Function==========================================

def typeasMovie():
    movie=newfile[newfile['type'] == 'Movie']
    print(movie.head())

def typeasTVShow():
    tvshow=newfile[newfile['type'].str.strip().str.lower() == 'tv show']    
    print(tvshow.head())
def sort_by_date():
    thnpilih=int(input("Masukkan tahun: "))
    year=newfile[newfile['release_year'] == thnpilih]
    print(year)
def sort_by_rating():
    rating=newfile['rating'].value_counts()
    print(rating)
#=========================================Main==========================================
os.system('cls' if os.name == 'nt' else 'clear')

# print(newfile.head()) #ambil 5 data teratas
# print(newfile.info()) #menampilkan informasi data
# print(newfile.describe()) #menampilkan statistik deskriptif
# print(newfile.columns) #menampilkan nama kolom


# print(F"max={newfile["duration"].max()}")
# print(newfile["type"].value_counts())

# print(newfile["country"].value_counts())

# print("\nTahun rilis terbanyak:")
# print(newfile['release_year'].value_counts().head(5))

# print("\nDurasi rata-rata film (menit):")
# print(newfile[newfile['duration_type'] == 'min']['duration_num'].mean())

# print("\nDurasi rata-rata TV Show (season):")
# print(newfile[newfile['duration_type'] == 'season']['duration_num'].mean())

# print(newfile["listed_in"])

# print((newfile[newfile["listed_in"]=="Dramas"]).head(5))


print(newfile["title"].sort_values().head(50))