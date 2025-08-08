import os,time,json
directory="./Jason/Newgam.py/"
fileName = f'{directory}userData.json'
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
Profile={'nama':"user1",
         'password':"1234",
         'level':1,
         'last_login':"9/9/9999"}
json.dump(Profile,open(fileName,"w"), indent=4)
oldProfile=json.load(open(fileName))
try:
    with open(fileName, "r") as file:
        userProfile=json.load(file)
except FileNotFoundError:
    print("File tidak ditemukan")

clear()
choice=input("1. Login\n2. Register\n3. Exit\nMasukan Pilihan: ")
if choice=="2":
    lgn=input("Name: ")
    Profile.update(nama=lgn)
    pswd=input("Password: ")
    psd=input("Confirm Password: ")
    if psd==pswd:
            print("Login Success")
            Profile.update(password=pswd)
            time.sleep(1)
            clear()
            print("Selamat datang di game")
            Profile.update(last_login=time.strftime("%d/%m/%Y"))
            time.sleep(1)
    else:
            print("Login Failed")
elif choice=="1":
    print(oldProfile)
    lgn=input("Name: ")
    if lgn==oldProfile['nama']:
        pswd=input("Password: ")
        if pswd==oldProfile['password']:
            print("Login Success")
            time.sleep(1)
            clear()
            print("Selamat datang di game")
            oldProfile.update(last_login=time.strftime("%d/%m/%Y"))
            time.sleep(1)
            data={'coin':0,'life':3}
            with open(f'{directory}gmdata.json','w') as file:
                json.dump(data,file,indent=4)
            if os.path.exists(f"{directory}gmdata.json"):
                os.remove(f"{directory}gmdata.json")





















































            
        else:
            print("Login Failed")
    else :
        print("Login Failed")

elif choice=="3":
    exit()

















#user 
#gmdata