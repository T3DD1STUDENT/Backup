import os
def startData(directorty, judulnote):
    with open(f'{directorty}/dataNote.txt', 'r') as file:
        for line in file:
            judulnote.append(line.strip())
def add(note, directorty, judulnote):
    os.system('cls')
    try:    
        with open(f'{directorty}/{note}.txt', 'x') as file:
            file.write(input("Enter your note: "))
            judulnote.append(note)
            enddata(directorty, judulnote)
    except FileExistsError:
        input("This item is already in the list! ")
    else:
        os.system('cls')
        displayList(judulnote)

def remove(note, directorty, judulnote):
    os.system('cls')
    displayList(judulnote)
    try:
        judulnote.remove(note)
        os.remove(f'{directorty}/{note}.txt')
    except ValueError:
        print("This item is not in the list! ")
    except FileNotFoundError:
        print(f'your note {note} does not exist! ')
    else:
        input(f'your note {note} has been deleted! ')
    os.system('cls')
    displayList(judulnote)


def displayList(judulnote):
    print('====**NOTE**====')
    for i in range(len(judulnote)):
        print( i+1 , judulnote[i] )

def enddata(directorty, judulnote):
    with open(f'{directorty}/dataNote.txt', 'w') as file:
        for line in judulnote:
            # print(line)
            file.write(line + '\n')
def edit(judulnote,directorty):
    os.system('cls')
    displayList(judulnote)
    print(judulnote)
    try:
        note=(judulnote[int(input(f"Select note to edit: "))-1])
    except ValueError: 
        input("There has been an error! ")
        edit()
    except IndexError:
        input("There has been an error!  ")
        edit()
    else:
        with open(f'{directorty}/{note}.txt', 'w') as file:
         file.write(input(f"insert your new note for {note}: "))
