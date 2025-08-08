#========================library========================#

import os
import fungsi as f

#========================variabel========================#

judulnote=[]
directorty='./aplikasinote'

#========================function========================#


#========================main========================#

os.system('cls')
# input(f'welcome to note app')
# input(f'here you can make note and remove note')
# input(f"Lets begin now")

f.startData(directorty, judulnote)
# os.system('cls')
# displayList()
# input(f'to start lets begin by adding note')
# add(input("insert a new note to create: "))
# input(f'now lets remove note')  
# remove(input("Select note to remove: "))
# input(f'now lets edit note')
# edit()
while True:
    if input('do you want to continue? (y/n) ')== 'y':        
        i=input("do you want to add, remove, or edit note? ").lower()
        if  i == 'add':
            f.add(input("Select note to create: "),directorty,judulnote)
        elif i == 'remove':
            f.remove(input("Select note to remove: "),directorty,judulnote)
        elif i == 'edit':
            input(f'now lets edit note')
            f.edit(judulnote,directorty)
        else:
            input("There has been an error! ")
    else:
        break
f.enddata(directorty, judulnote)