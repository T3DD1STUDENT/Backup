#-----------Library------------#
import os

#-----------Variable------------#
menu={'Nasi Goreng':10000,
    'Ayam Goreng':15000,
    'Mie Goreng':15000,
    'Bakso':10000}


#-----------Function------------#
def clear():
    os.system('cls')

#-----------Main---------------#
clear()
for i in menu:
    print(f'{i} {menu[i]}')

# for i in range(len(menu)):
#      print{menu[i+1]}')

# print(menu)
# print(menu.values)
#-----------End---------------#