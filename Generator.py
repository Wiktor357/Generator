import random

znaki = "1234567890qwetyuioplkjhgfdsazxcvbnm<>!@#$%^&*()"
dlugosc_hasla = int(input("Z ilu znaków ma się składać twoje hasło?"))
haslo = ''

for i in range(0, dlugosc_hasla):   
    haslo += random.choice(znaki)
print("Twoje haslo to:", haslo)
