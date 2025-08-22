
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
import seaborn as sns
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

def hapus(text,second):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(second):
        for j in range(4):
            print(f"{text}{'.'*j}")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

def typeasMovie():
    movie=newfile[newfile['type'] == 'Movie']
    print(movie.head())

def typeasTVShow():
    tvshow=newfile[newfile['type'].str.strip().str.lower() == 'tv show']    
    print(tvshow.head())

def search_by_date():
    thnpilih=int(input("Masukkan tahun: "))
    year=newfile[newfile['release_year'] == thnpilih]
    print(year)

def sort_by_rating():
    rating=newfile['rating'].value_counts()
    print(rating)

def search_by_title():
    title=input("Masukkan judul: ")
    judul=newfile[newfile['title'] == title]
    print(judul)
def sort_by_title():
    print(newfile["title"].sort_values().head(50))

def search_by_rating():
    rating=input("Masukkan rating: ")
    rate=newfile[newfile['rating'] == rating]
    print(rate)

def chart_of_shows():
    plt.figure(figsize=(8,5))
    sns.countplot(data=newfile, x='type', palette='viridis')
    plt.title('Jumlah Konten per Tipe')
    plt.show()
def chart_of_rating():
    plt.figure(figsize=(10,6))
    sns.barplot(x=contetbruh.index, y=contet_rating.index, palette='coolwarm')
    plt.title('Jumlah rating per konten')
    plt.xlabel('Tipe rating')
    plt.ylabel('Jumlah Konten')
    plt.show()
def chart_of_Country():
    plt.figure(figsize=(10,6))
    plt.plot( top_country.index ,top_country.values.astype,color="LemonChiffon")
    plt.title('Top 10 Negara dengan Konten Terbanyak')
    plt.xlabel('Jumlah Konten')
    plt.ylabel('Negara')
    plt.show()

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
top_country = newfile['country'].value_counts().head(10)
contetbruh =rating=newfile['rating'].value_counts()
# Konten terbanyak per tahun
content_per_year = newfile.groupby('release_year')['show_id'].count().reset_index()
content_per_year = content_per_year.sort_values(by='show_id', ascending=False)

contet_rating = newfile.groupby('rating')['show_id'].count().reset_index()
contet_rating = contet_rating.sort_values(by='show_id', ascending=False)



# plt.figure(figsize=(8,5))
# sns.countplot(data=newfile, x='type', palette='viridis')
# plt.title('Jumlah Konten per Tipe')
# plt.show()

# plt.figure(figsize=(10,6))
# sns.barplot(x=top_country.values, y=top_country.index, palette='coolwarm')
# plt.title('Top 10 Negara dengan Konten Terbanyak')
# plt.xlabel('Jumlah Konten')
# plt.ylabel('Negara')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.lineplot(data=content_per_year, x='release_year', y='show_id', marker='o')
# plt.title('Jumlah Konten per Tahun')
# plt.xlabel('Tahun Rilis')
# plt.ylabel('Jumlah Konten')
# plt.show()

print("Welcome to KakGel Moives and TV Show Data Analysis")
print("Here we have top shows from around the world for you to watch")

c=input("1. Sign Up\n2. Sign In\n3. no account\nEnter your Pilihan: ")

if c == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    input("user name: ")
    while True:
        k=input("password: ")
        j=input("confirm password: ")
        if j != k:
            print("Password not match")
            time.sleep(1)
        elif j == k:
            break
    input("Email: ")
    input("Phone Number: ")
    input("Address: ")
    input("date of birth: ")
    input("gender: ")
    input("Ocupation: ")
    input("Reason for joining: ")

    print("Sign Up Success")
    time.sleep(1)
    print("Success")


elif c == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sign In")
    time.sleep(1)
    print("Success")

else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("No Account")
    time.sleep(1)
    print("Success")

sort_by_title()

while True:
    print("===============================================================")
    print('''
    1.Sort
    2.Search
    3.Chart
    4.Exit
    ''')

    pilihan=input("Enter your Pilihan: ")

    # hapus("Waiting for no reason",3)

    if pilihan == "1":
        print('''
        1.Sort by Movie
        2.Sort by TV Show
        3.Sort by Rating
        4.Sort by Title
        ''')
        pilihan=input("Enter your Pilihan: ")
        if pilihan == "1":
            typeasMovie()

        elif pilihan == "2":
            typeasTVShow()

        elif pilihan == "3":
            sort_by_rating()

        elif pilihan == "4":
            sort_by_title()
        
        else :
            pass

    elif pilihan == "2":
        print('''
        1.Search by Date
        2.Search by Title
        3.Search by Rating
        ''')
        pilihan=input("Enter your Pilihan: ")
        if pilihan == "2":
            search_by_title()
        elif pilihan == "1":
            search_by_date()
        elif pilihan == "3":
            search_by_rating()
        else :
            pass
    elif pilihan == "3":
        print('''
        1.Chart of shows
        2.Chart of ratings
        3.Chart of countries
        4.Chart of years
        ''')
        pilihan=input("Enter your Pilihan: ")
        if pilihan == "1":
            chart_of_shows()
        elif pilihan == "2":
            chart_of_rating()
        elif pilihan == "3":
            chart_of_Country()
        else :
            pass

    else :
        break

print ("Thank you for using this program")