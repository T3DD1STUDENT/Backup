import json, os, time

directory="./Jason/Projek1/"
def hapus():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

userProfile = {
    "userName": "coder_learner",
    "lastLogin": "2023-10-01T12:00:00Z",
    "preferences": {
        "theme": "dark",
        "notifications": True,
    },
    "recentActivities": ["tutorial_started","excercise_completed","read_docs"]
}

fileName = f'{directory}userData.json'

print(f'Tulis nama file ke {fileName}')

try: 
    with open(fileName, 'w') as file:
        json.dump(userProfile, file, indent=4) #simpan data dengan json.dump kalau convert data json.dumps
        
except FileNotFoundError:
    print('Very handsome')

#open file
with open(fileName, "r") as file:
    userProfile=json.load(file) #convert data json.load kalau convert data json.loads