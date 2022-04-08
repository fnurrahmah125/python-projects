print("""Temperature Converter
      
Masukkan satuan suhu:
  1. C untuk Celcius
  2. F untuk Fahrenheit 
  3. K untuk Kelvin
""")

active = True
degree_sign = u"\N{DEGREE SIGN}"

def celcius(suhu):
  nilai_celcius = suhu
  nilai_fahrenheit = (nilai_celcius * (9/5)) + 32
  nilai_kelvin = nilai_celcius + 273.15
  
  print(f"\nCelcius = {nilai_celcius}{degree_sign}C")
  print(f"Fahrenheit = {nilai_fahrenheit}{degree_sign}F")
  print(f"Kelvin = {nilai_kelvin} K")

def fahrenheit(suhu):
  nilai_fahrenheit = suhu
  nilai_celcius = round((nilai_fahrenheit-32)*(5/9))
  nilai_kelvin = nilai_celcius + 273.15
  
  print(f"\nFahrenheit = {nilai_fahrenheit}{degree_sign}F")
  print(f"Celcius = {nilai_celcius}{degree_sign}C")
  print(f"Kelvin = {nilai_kelvin} K")

def kelvin(suhu):
  nilai_kelvin = suhu
  nilai_celcius = nilai_kelvin - 273.15
  nilai_fahrenheit = (nilai_celcius*(9/5)) + 32
  
  print(f"\nKelvin = {nilai_kelvin} K")
  print(f"Celcius = {nilai_celcius}{degree_sign}C")
  print(f"Fahrenheit = {nilai_fahrenheit}{degree_sign}F")
   

while active == True:
  satuan_suhu = input("Satuan suhu: ").lower()
  
  if satuan_suhu == "c":
    celcius(float(input("Nilai suhu: ")))
    active = False
  elif satuan_suhu == "f":
    fahrenheit(float(input("Nilai suhu: ")))
    active = False
  elif satuan_suhu == "k":
    kelvin(float(input("Nilai suhu: ")))
    active = False
  else:
    print("Satuan yang anda masukkan salah.")
   