import pandas as pd
import os
Directorti = "BelajarMesin/Numpystuff/NumpyPanda"

csv_content = """
Name,Matematika,Science,English
Alice,90,85,88
Bob,75,40,35
Charlie,92,30,32
David,40,50,45
Eve,60,70,80
"""
csv_content2 ='''
Name;Matematika;Science;English
Alice;90;85;88
Bob;75;40;35
Charlie;92;30;32
David;40;45;50
Eve;60;75;80
'''
with open(f"{Directorti}/data.csv", "w") as file:
    file.write(csv_content.strip())


df = pd.read_csv(f"{Directorti}/data.csv")
print(df)

df2=pd.DataFrame(csv_content2)
df2.to_csv(f"{Directorti}/data2.csv")
print('done')