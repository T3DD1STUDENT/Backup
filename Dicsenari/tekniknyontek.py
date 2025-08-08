import os

Tokotas={'tas1':{"Merek":"Juiviton",'warna':'Jeruk','Harga':5000},
    'tas2':{"Merek":"Buci","warna":'nasi putih','Harga':10000},
    'tas3':{'Merek':"Berada","warna":"Hijau",'Harga':2000}}
Cash=0

def Tasshower(tes):
    print(f"#{'='*20}#")
    print('Merek: ',Tokotas[tes]['Merek'])
    print('Merek: ',Tokotas[tes]['warna'])
    print(f'Merek: Rp.{Tokotas[tes]['Harga']}')
    print(f"#{'='*20}#")

def alltas():
    print(Cash)
    print(f"#{'='*20}#")
    for Tas in Tokotas:
        print(f"{Tas}:")
        print(' Merek: ',Tokotas[Tas]['Merek'])
        print(' Merek: ',Tokotas[Tas]['warna'])
        print(' Merek: ',Tokotas[Tas]['Harga'])
        print(f"#{'='*20}#")

def Topup():
    os.system('cls')
    tu=int(input("How much would you like to top up? "))
    confirme=input(f"YOU are going to top up for {tu} are you sure? (y/n) ")
    
    if confirme=='y':
        print("Top up successful")
        Cash+=tu
    elif confirme=='n':
        print("Top up canceled")

    return Cash
os.system('cls')
input("Welcome to Toko Tas branded")
os.system('cls')
while True:
    alltas()

    task=input(" 1. View Bag\n 2. Top up\n 3. Exit\nWhat would you like to do? ")

    if task=='1':
        
        Tas=input("What Tas would you like to View? ")
        os.system('cls')
        Tasshower(Tas)
        
        tas=input(" 1. Buy\n 2. Back\nWhat would you like to do? ")

        if tas=='1':
            if Cash>=Tokotas[Tas]['Harga']:
                print("Pembelian Berhasil")
            else:
                task=input("You have Insufficient cash to make this purchase. Do you want to top up? (y/n) ")
                if task=='y':
                    Cash=Topup()
                elif task=='n':
                    continue

    elif task=='2':
        
        Cash=Topup()

    elif task=='3':
        
        exit('Have a nice day!')

