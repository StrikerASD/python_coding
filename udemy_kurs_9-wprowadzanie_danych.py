print("Prosty program robiący obliczenia za pomocą danych wejściowych")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Wynik dodania", a, "do", b, "wynosi:", (a + b))

### Program odpytujący

imie = input("Jak masz na imię? ")

print("Hej, cześć", imie)
ileLat = int(input("... Ile masz lat? "))
print("Okey,", imie, "więc za rok będziesz mieć", (ileLat + 1), "lat")


###

# Pobierz imie użytkownika:
name = input("Podaj swoje imię: ")

# pobierz wiek użytkownika:
age = int(input("Podaj swój wiek: "))

# pobierz jego ulubiony kolor:
color = input("Podaj swój ulubiony kolor: ")

# Sformatuj i wypisz wynik na ekran:
print("Hej " + name + ", Twój ulubiony kolor to " + color + ".")
print("Masz ", age, "lat")
print("Za rok będziesz miał:", age + 1, "lat")