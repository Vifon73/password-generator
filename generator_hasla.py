import secrets
import string

print("Generator hasla.")

while True:
    print('''Wybierz ponizej opcje:\n
        Same cyfry ---> 1
        Same litery ---> 2
        Pomieszane haslo ---> 3''')
    wybor = int(input("\nWpisz 1 lub 2 lub 3: --> "))
    
    if (wybor == 1):
        dlugosc_hasla = int(input("Podaj dlugosc hasla:"))
        znaki = string.digits
        haslo = "".join(secrets.choice(znaki) for i in range(dlugosc_hasla))
        print(haslo)
        input("Aby zakonczyc kliknij ENTER!")
        break

    elif (wybor == 2):
        dlugosc_hasla = int(input("Podaj dlugosc hasla:"))
        znaki = string.ascii_letters
        haslo = "".join(secrets.choice(znaki) for i in range(dlugosc_hasla))
        print(haslo)
        input("Aby zakonczyc kliknij ENTER!")
        break

    elif (wybor == 3):
        dlugosc_hasla = int(input("Podaj dlugosc hasla:"))
        znaki = string.digits + string.ascii_letters
        haslo = "".join(secrets.choice(znaki) for i in range(dlugosc_hasla))
        print(haslo)
        input("Aby zakonczyc kliknij ENTER!")
        break
        
    else:
        print("Blad w wyborze!")


    