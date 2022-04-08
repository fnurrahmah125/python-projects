import random

print("""Selamat datang!
Kamu punya 3 kesempatan untuk bermain.
""")

# point
score_user = 0
score_comp = 0

for i in range(3):
  # user
  user_choice = input("Masukkan pilihan (batu, gunting, kertas): ").lower()

  # computer
  actions = ["batu", "gunting", "kertas"]
  comp_choice = random.choice(actions)

  if user_choice == comp_choice:
    score_user += 1
    score_comp += 1
    print(f"SERI. Kedua pemain memilih {user_choice}!")
  elif user_choice == "batu":
    if comp_choice == "gunting":
      print("MENANG. Batu mengalahkan gunting.")
      score_user += 1
    else:
      print("KALAH. Kertas mengalahkan batu.")
      score_comp += 1
  elif user_choice == "gunting":
    if comp_choice == "kertas":
      print("MENANG. Gunting mengalahkan kertas.")
      score_user += 1
    else:
      print("KALAH. Kertas mengalahkan batu.")
      score_comp += 1
  else:
    if comp_choice == "batu":
      print("MENANG. Kertas mengalahkan batu.")
      score_user += 1
    else:
      print("KALAH. Gunting mengalahkan kertas.")
      score_comp += 1


if score_user > score_comp:
  print(f"\nKAMU MENANG! \nSkor Akhir User vs Computer {score_user}-{score_comp}")
elif score_user < score_comp:
  print(f"\nKAMU KALAH! \nSkor Akhir User vs Computer {score_user}-{score_comp}")
else:
  print(f"\nSERI! \nSkor Akhir User vs Computer {score_user}-{score_comp}")