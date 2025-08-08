pesan=[['line1','8\t','line3'],
        ['lines1','7']]

#with open('./tedfile1/data.txt','w') as file:
with open('data.txt','w') as file:
    for line in pesan:
        file.write("\t".join(line)+"\n")
    
with open('data.txt','r') as file:
    data=file.readlines()
    print(data)
