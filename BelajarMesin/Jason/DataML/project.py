#=======================Library=======================#

import json, os, time

#=======================File=======================#

direktorti="./Jason/DataML/"

with open(f"{direktorti}/Info.json",'r') as file:
    salesData=json.load(file)

#=======================Function=======================#

def hapus(second):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(second):
        for j in range(4):
            print(f"loading{'.'*j}")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

def userdatadisplay():
    print(f"{CORRECT}Access Granted{ENDC}")
    hapus(0)
    print("#====User Data====#\n")
    i=0
    for data in salesData:
        i+=1
        print(f"ID {i}")
        for key in data:
            print(key,":",data[key])
        print()
    salesamount=0
    for record in salesData:
        salesamount+=record["Amount"]
    print("Total sales:",round(salesamount,2))
def datadisplay(salesData):
    category = set(record["Category"] for record in salesData)
    for corn in sorted(category):
        print(f"-{corn}")
WARNING = '\033[93m'
FAIL = '\033[91m'
CORRECT = "\033[32m"
White = "\033[97m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
LightGray = "\033[37m"
DarkGray = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
LightYellow = "\033[93m"
LightBlue = "\033[94m"
LightMagenta = "\033[95m"
LightCyan = "\033[96m"
ENDC = '\033[0m'

#=======================Main=======================#
hapus(0)
print("Welcome to Handsome Corporation's New\n    User data management system\n")
code=input("Please enter Management authoritations code\n")

if code=='123':

    userdatadisplay()

    cmn=input("1.Filter Products \n2.id Search \n3.Exit \ninsert the next Command: ")
    if cmn=='1':
        hapus(2)
        datadisplay(salesData)
        cmn=input("Inset your Category: ")
        hapus(3)
        for data in salesData:
            if data["Category"]==cmn:
                for key in data:
                    print(key,":",data[key])

    elif cmn=='2':
        hapus(1)
        id=int(input("insert the id: "))
        for data in salesData[id-1]:
            print(data,":",salesData[id-1][data]) 
    else:
        exit("Goodbye")



























else:
    print(f"{FAIL}Access Denied{ENDC}")
    hapus(1)
    exit