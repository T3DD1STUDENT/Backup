#=============library==================#
import os
#=============varieble==================#
datastaff={
    'staff1':{
        'nama':'Cornilius sebastion decaprio the third',
        'umur':90,
        'jabatan':'ceo'},
    'staff2':{
        'nama':'k',
        'umur':9,
        'jabatan':'cfo'},
    'staff3':{
        'nama':'subi',
        'umur':21,
        'jabatan':'staff'},
    }
list=[]

#=============function==================#
print('#staf of Cornilius sebastion decaprio the third technical center#')
for i in datastaff.keys():
    list.append(i)
    print (i)
for i in range(len(list)):
    print(f'{i+1}.{datastaff[list[i]]['nama']}\n\tumur:{datastaff[list[i]]['umur']}\n\tjabatan:{datastaff[list[i]]['jabatan']}')
    print (i)