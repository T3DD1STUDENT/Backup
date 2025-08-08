#================library==================#
import os,time,datetime
#================varieble==================#
feedback=[]
directorti='./HandsomeCafe'
Feedback=[]
Feddback=''
#================function==================#
def startdata():
    try:
        with open(f'{directorti}/log.txt','r') as file:
            for fb in file:
                feedback.append(fb.strip())
    except FileNotFoundError:
        with open(f'{directorti}/log.txt','w') as file:
            for fb in file:
                feedback.append(fb.strip())
def enddata(Feedback):
    with open(f'{directorti}/log.txt','a') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M') + '\n')
        for fd in Feedback:
            #file.write('|'.join(fd) + '\n')
            file.write(fd + '\n')

#================main==================#
while True:
    startdata()
    os.system('cls')
    print("Welcome to Handsome Cafe's Feedback page.")
    print('In here u will be able to give us your feed back')
    time.sleep(1.5)
    os.system('cls')
    print('='*55)
    name=input("Please enter your Name\nName: ")
    if not name:
        name='Anonymous'
    Feedback.append('nama: '+name)
    while not Feddback:
        Feddback=input("Please enter your feedback\nFeedback: ")
        print('Please enter a feedback')
        time.sleep(1)
        os.system('cls')
        print('='*55)
    Feedback.append(Feddback)
    if name=='Cornilius Sebastion Decaprio the Third':
        print('Thank You mr ceo for the feed back')
    else:
        print('Thank You for the feed back')
    enddata(Feedback)