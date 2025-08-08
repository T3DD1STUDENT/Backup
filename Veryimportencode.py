import time
import os

def hapus(text,second):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(second):
        for j in range(4):
            print(f"{text}{'.'*j}")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')


