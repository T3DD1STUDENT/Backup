import os
import datetime
ord=[]
def startData():
        with open(f'./ord.txt','w') as file:
            file.write(f'Order:\n')
order=[]
def orderof(order):
    os.system('cls')
    ct=input("Do u want to make your on coffe?(y/n)\n")
    if ct=='y':
        ct=input("Do u want to at milk?(y/n)\n")
        if ct=='y':
            ct=input("Do u own an expreso machine?(y/n)\n")
            if ct=='y':
                ct=input("DO YOU DREAM OF YOUR SEMESTER ABROAD IN AUSTRALIA OR NEW ZEALAND?(y/n)\n")
                if ct=='y':
                    order.append("Flat White")
                elif ct=='n':
                    ct=input("Do u want a lot of milk?(y/n)\n")
                    if ct=='y':
                        order.append('Late')
                    elif ct=='n':
                        order.append("Capuccino")
            elif ct=='n':
                order.append('Bialetti') 
        elif ct=='n':
            ct=input("Do u get creative with recipes?(y/n)\n")
            if ct=='y':
                order.append("French press")
            elif ct=='n':
                order.append("clever Driper")
            elif ct=='no':
                ct=input("Are u a science geek?(y/n)\n")
                if ct=='y':
                    ct=input("DO YOU WANT YOUR COFFEE BREWING TO BE DRAMATIC?(y/n)\n")
                    if ct=='y':
                        order.append("Siphon Coffee")
                    if ct=='n':
                        order.append("Chemex")
                elif ct=='n':
                    order.append("clever Driper")
    elif ct=='n':
        order.append('black coffee')
    print('your order is:')
    for i in range(len(order)):
        print(f'{i+1}. {order[i]}')
    cn=input("Whould u like to add another item?(y/n)\n")
    if cn=='y':
        orderof(order)
    elif cn=='n':
        print('Thank you for your order')
def endata(order):
    with open(f'./ord.txt','a') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')+'\n')
        for fd in order:
            #file.write('|'.join(fd) + '\n')
            file.write(fd + '\n')

startData()
orderof(order)
endata(order)
