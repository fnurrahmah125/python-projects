import random

print("Tebak angka dari 1-10, kamu punya 5 kesempatan!\n")

comp = random.randint(1,10)

i = 0
while i < 5:
  user = int(input("Masukkan angka: "))
  
  if i < 4:
    if user == comp:
      print(f"\tBENAR. Angka yang dicari adalah {comp}.")
      i = 5
    elif user < comp:
      if user == comp-1:
        print("\tSALAH. Ayo sedikit lebih tinggi!")
        i += 1
      else:
        print("\tSALAH. Angka terlalu rendah. Coba lagi!")
        i += 1
    else:
      if user == comp+1:
        print("\tSALAH. Ayo sedikit lebih rendah!")
        i += 1
      else:
        print("\tSALAH. Angka terlalu tinggi. Coba lagi!")
        i += 1
  else:
    if user == comp:
      print(f"\tBENAR. Angka yang dicari adalah {comp}.")
      i += 1
    else:
      print(f"\tGAGAL. Jawaban yang benar adalah {comp}.")
      i += 1
    
print("\nPermainan selesai. Terima kasih!")