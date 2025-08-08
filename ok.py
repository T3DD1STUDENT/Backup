import getpass

password = getpass.getpass("Masukkan password Anda: ")

print("Password Anda:", "*" * len(password))  # Menampilkan * sejumlah panjang password