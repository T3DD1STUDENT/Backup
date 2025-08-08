import json, os

direktorti="./Jason/DataML/"
def hapus():
    os.system('cls' if os.name == 'nt' else 'clear')

with open(f"{direktorti}/Info.json",'r') as file:
    salesData=json.load(file)

hapus()
print("---Basic data Exploration---")
print(f'Total Records: {len(salesData)}')

#1. Hitung jumlah penjualan berdasarkan kategori
Category_Count={}
for record in salesData:
    category=record["Category"]
    Category_Count[category]= Category_Count.get(category, 0) + record["Quantity"]
print("\nSales by category:")
for category, count in Category_Count.items():
    print(f"{category}: {count} sales")

City_Count={}
for record in salesData:
    city=record["City"]
    City_Count[city]= City_Count.get(city, 0) + 1
print("\nCities with sales:")
for city, count in City_Count.items():
    print(f"{city}: {count} sales")

salesamount=0
for record in salesData:
    salesamount+=record["Quantity"]
print("\nTotal sales amount:",salesamount)

Category_Quantity={}
for record in salesData:
    category=record["Category"]
    Category_Quantity[category]= Category_Quantity.get(category, 0) + record["Quantity"]
print("\npurchuses by category:")
for category, count in Category_Quantity.items():
    print(f"{category}: {count} sales")