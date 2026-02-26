import os

# Parol endi kod ichida emas, xavfsiz "seyf"dan olinadi
password = os.getenv("MY_PASSWORD")

if password:
    print("Tizim xavfsiz ulandi.")
else:
    print("Xato: Parol topilmadi!")
