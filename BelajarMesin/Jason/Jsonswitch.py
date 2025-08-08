import json

DataBarang={
    "ID": "9475",
    "Nama": "esusu",
    "Harga": 10000,
    "Stok": 10,
    "descripsi":"Laptop termurah dengan performance terbaik",
    "spesifikasi":{"prosesor":"Intel Core i11",
        "ram": "10TB",
        "Storage": "12mb",
        "gpu":"Stvs gxo IX pro max"}
}
print(DataBarang)
jsonstuff = json.dumps(DataBarang, indent=4) 
print(jsonstuff)

DataMobil={
    "Nama": "Astaga",
    "Harga": 100,
    "stok": -10,
    "descripsi":"Mobil hybrid Udara Terbaru",
    "spesifikasi":{"Motor":"RGB TRF 2009",
        "kubikasi":"2.5",
        "tipe":"CrashCar"}    
}
print(DataMobil)
jsonderulo = json.dumps(DataMobil, indent=4)
print(jsonderulo)

DataHP={
    'ID':0.0001,
    "Merek": "Airoplain",
    "Harga": 10000,
    "Stok": 11,
    "descripsi":"HP ter",
    "spesifikasi":{"prosesor":"Intel Core i11",
        "ram": "100TB",
        "Storage": "12kb",
        "Storage2": "1b"}
}
print(DataHP)
jsonkun = json.dumps( DataHP, indent=4)
print(jsonkun)
