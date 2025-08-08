#===================Library===================#
import numpy as np
import os,time,textwrap
#===================Variable===================#
num1=0
num2=0
answer=0
Operator='+'
asn='0'
#===================Function===================#
def clear():
    os.system('cls')
def display(asn):
    clear()
    print('========Calculator========')
    for i in asn:
        print(f'|{i:^24}|')
    print('='*26)
def basicoperator():
    display('0')
    global num1,num2,asn
    try:
        num1=int(input('Masukan angka pertama: '))
        num2=int(input('Masukan angka kedua: '))

    except ValueError:
        input('Please Enter a Number!')
        basicoperator()
    choice=input('1.add\n2.sub\n3.mul\n4.div\n5.advanced choice\nMasukan pilihan anda: ')
    if choice=='add'or choice=='1':
        answer=np.add(num1,num2)
        wraper=textwrap.TextWrapper(width=24)
        asn=wraper.wrap(f"{str(num1)}+{str(num2)}={str(answer)}")
    elif choice=='sub'or choice=='2':
        answer=np.subtract(num1,num2)
        wraper=textwrap.TextWrapper(width=24)
        asn=wraper.wrap(f"{str(num1)}-{str(num2)}={str(answer)}")
    elif choice=='mul'or choice=='3':
        answer=np.multiply(num1,num2)
        wraper=textwrap.TextWrapper(width=24)
        asn=wraper.wrap(f"{str(num1)}X{str(num2)}={str(answer)}")
    elif choice=='div'or choice=='4':
        answer=np.divide(num1,num2)
        wraper=textwrap.TextWrapper(width=24)
        asn=wraper.wrap(f"{str(num1)}:{str(num2)}={str(answer)}")
    elif choice=='advance' or choice=='5':
        answer,asn=AdvancedChoice()
    else:
        input('Eror ')
        basicoperator()
    display(asn)
    input('Press enter to continue ')

    basicoperator()
def AdvancedChoice():
    wraper=textwrap.TextWrapper(width=24)
    choice=input('1.Pwr\n2.sqrt\n3.log \n4.sin\n5.cos\n6.tan\n7.back\nMasukan pilihan anda: ')
    if choice=='pwr' or choice=='1':
        answer=np.power(num1,num2)
        asn=wraper.wrap(f"{str(num1)}^{str(num2)}={str(answer)}")
    elif choice=='sqrt' or choice=='2':
        numpy=input('num1 or num2\n')
        if numpy=='num1':
            answer=np.sqrt(num1)
        elif numpy=='num2':
            num2=num1
            answer=np.sqrt(num1)
        else:
            print('Eror')
            AdvancedChoice()
        asn=wraper.wrap(f"√{str(num1)}={str(answer)}")
    elif choice=='log' or choice=='3':
        numpy=input('num1 or num2\n')
        if numpy=='num1':
            answer=np.log(num1)
        elif numpy=='num2':
            num2=num1
            answer=np.log(num2)
        else:
            print('Eror')
            AdvancedChoice()
        asn=wraper.wrap(f"log{str(num1)}={str(answer)}")
    elif choice=='sin' or choice=='4':
        numpy=input('num1 or num2\n')
        if numpy=='num1':
            answer=np.sin(num1)
        elif numpy=='num2':
            num2=num1
            answer=np.sin(num2)
        else:
            print('Eror')
            AdvancedChoice()
        asn=wraper.wrap(f"sin{str(num1)}={str(answer)}")
    elif choice=='cos' or choice=='5':
        numpy=input('num1 or num2\n')
        if numpy=='num1':
            answer=np.cos(num1)
        elif numpy=='num2':
            num2=num1
            answer=np.cos(num2)
        else:
            print('Eror')
            AdvancedChoice()
        asn=wraper.wrap(f"cos{str(num1)}={str(answer)}")
    elif choice=='tan'or choice=='6':
        numpy=input('num1 or num2\n')
        if numpy=='num1':
            answer=np.tan(num1)
        elif numpy=='num2':
            num2=num1
            answer=np.tan(num2)
        else:
            print('Eror')
            AdvancedChoice()
        asn=wraper.wrap(f"tan{str(num1)}={str(answer)}")
    return(answer,asn)
#===================Main===================#


basicoperator()




