import os,time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

shop = [
    ["tedphone1",0,500000],
    ["tedphone1pro",0,650000],
    ["tedphonepromax",0,1000000]]
    
storage = [
    ["tedphone1",100,500000],
    ["tedphone1pro",100,650000],
    ["tedphonepromax",50,1000000]]
    
def main():
    clear()
    print('='*58)
    print('='*58)
    print(f'{"tedvis":^58}')
    print('='*58)
    print(f'{"seeInventory(1)":^58}')
    print(f'{"Move from shop to storage(2)":^58}')
    print(f'{"Move from storage to shop(3)":^58}')
    print(f'{"add newproduc(4)":^58}')
    print(f'{"remove produc(5)":^58}')
    print(f'{"Exit(6)":^58}')
    print('='*58)
    x=int(input(''))
    if x==1:
        listStock()
    elif x==2:
        sh2st()
    elif x==3:
        st2sh()
    elif x==4:
        newproduc()
    elif x==5:
        elminate()
    elif x==6:
        exit("Thank you for using this program")
    else:
        print('Eror')
        
def displayListbarang():
    print('List barang: ')
    for i in range(len(storage)):
        print(f'{i+1}. {storage[i][0]:<18}')
    
        
def storagi():
    print('='*58)
    print(f'{"storage":^58}')
    print('='*58)
    for i in range(len(storage)):
        print('|',end="")
        for j in range(len(storage[i])):
            print(f'{storage[i][j]:^18}',end='|')
        print('')
    print('='*58)

def shopi():
    print('='*58)
    print(f'{"tedshop":^58}')
    print('='*58)
    for i in range(len(shop)):
        print('|',end="")
        for j in range(len(shop[i])):
            print(f'{shop[i][j]:^18}',end='|')
        print('')
    print('='*58)

def listStock():
    clear()
    shopi()
    print(f'{"||":^58}')
    storagi()

def newproduc():
    print(f'{"add newproduc":^58}')
    listStock()
    a=input(f"Product name: ")
    b=int(input(f"seleck amount of {a}:"))
    c=int(input(f"Select price for {a}:"))
    storage.append([a,b,c])
    shop.append([a,0,c])
    clear()
    listStock()
 
def st2sh():  
    print(f'{"Storage to Shop":^58}')
    listStock()
    displayListbarang()
    a=int(input('seleck produc to move:'))
    b=int(input(f"seleck amount for {a} to move: "))
    if b>storage[a-1][1]:
        print("Not enough stock!")
    elif b<0:
        input("Error")
    else:
        storage[a-1][1]-=b
        shop[a-1][1]+=b
        clear()
        listStock()
        print('Data berhasil di pindahkan')
def sh2st():
    print(f'{"shop to Storage ":^58}')
    listStock()
    a=int(input('seleck produc to move:'))
    b=int(input(f"seleck amount for {a} to move: "))
    if b>shop[a-1][1]:
        print("Not enough stock!")
    elif b<0:
        input("Error")
    else:
        shop[a-1][1]-=b
        storage[a-1][1]+=b
        clear()
        listStock()
        print('Data berhasil di pindahkan')

def elminate():
    print(f'{"Remove produc":^58}')
    listStock()
    displayListbarang()
    a=int(input('Seleck item to throw: '))
    storage.pop(a-1)
    shop.pop(a-1)
    clear()
    listStock()
    print('Data berhasil di Hapus')
print('Welcome to ted storage managment.')
print('Here u will be managing teds produc')
q=input("R u ready?y/n")
if q=='y':
    print('great lets star')
elif q=='n':
    print('Oh well your stuck here')
else:
    print('il take that as a yes')
clear()
while True:
    input('Enter to continue! ')
    main()