#===================Library===================#
import numpy as np
import pandas as pd
import os,time

#===================Variable===================#

Datasales=np.array([
    [ 212 , 11 , 2.0],
    [ 213 , 2 , 500.0],
    [ 214 , 3 , 21.0],
    [213 , 7 , 500.0],
    [212 , 1 , 2.0],
    [214 , 2 , 21.0],])

df_Sarles = pd.DataFrame(Datasales, columns=["productID","QUANTITY","PRICE"])

df_Sarles['productID']=df_Sarles['productID'].astype(int)
df_Sarles['QUANTITY']=df_Sarles['QUANTITY'].astype(int)

df_Sarles["TotalSalesAmount"]=df_Sarles["QUANTITY"]*df_Sarles["PRICE"]

TotalSaLES=df_Sarles["TotalSalesAmount"].sum()
AvarageSales=df_Sarles["TotalSalesAmount"].mean()

ProducQuantity_sold=df_Sarles.groupby("productID")["QUANTITY"].sum().sort_values(ascending=True)
Producreaveanu=df_Sarles.groupby("productID")["TotalSalesAmount"].sum().sort_values(ascending=True)

NumofUniqueProducts=df_Sarles["productID"].nunique()

Product_212Sales=df_Sarles[df_Sarles["productID"] == 212]

HighValueSales=df_Sarles[df_Sarles["TotalSalesAmount"] > 100]
LowValueSales=df_Sarles[df_Sarles["TotalSalesAmount"] < 50]
#===================Function===================#

def hapus(text,second):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(second):
        for j in range(4):
            print(f"{text}{'.'*j}")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

def Main_menu():
    print(f"\nNumber of Unique Products Sold: {NumofUniqueProducts}")
    print(df_Sarles)
    print(F"Total Sales: {TotalSaLES}")
    print(F"Avarage Sales: {AvarageSales}")

def Sales_Transactions(ID):
    Product_212Sales=df_Sarles[df_Sarles["productID"] == ID]
    print(f"\nSales Transactions for Product ID {ID}:")
    print(Product_212Sales)

def Product_by_Quantity():
    print (ProducQuantity_sold)
    print(F"Top Selling Product by Quantity: Product ID {ProducQuantity_sold.index[-1]}({ProducQuantity_sold.iloc[-1]}) units")
    print(Producreaveanu)

def Product_by_Revenue():
    print(Producreaveanu)
    print(F"Top Earning Product by Revenue: Product ID {Producreaveanu.index[-1]} (${Producreaveanu.iloc[-1]:.2f})")
def Sales_by_Value():
    Valueses=input("1. High Value Sales\n2. Low Value Sales\n Wich data would you like to see: ")
    if Valueses == 1:
        print("\nHigh-Value Sales Transactions (TotalSaleAmount > $100):")
        print(HighValueSales)
    elif Valueses == 2:
        print("\nHigh-Value Sales Transactions (TotalSaleAmount < $50):")
        print(LowValueSales)
#===================Main===================#
hapus("Waiting for no reason",1)
print("Welcome to World Best Sales Analysis of Handsome company")
print("Here we provide the best sales analysis")
input("Enter to continue! ")
hapus("Preparing resources",3)
Main_menu()
while True:
    Choice=int(input("\n1.Transactions by sales ID\n2. Product by Quantity\n3. Product by Revenue\n4. Sales by Value\n5. Back\nWitch data would you like to see: "))
    hapus("Analyzing Data",1)
    if Choice == 1:
        it=int(input("Enter Product ID: "))
        Sales_Transactions(it)
    elif Choice == 2:
        Product_by_Quantity()
    elif Choice == 3:
        Product_by_Revenue()
    elif Choice == 4:
        Sales_by_Value()
    else:
        Main_menu()







