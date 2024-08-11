print("Instrukcje warunkowe")
print("")

print("Wybierz jedną z poniższych opcji:")
print("Mnożenie - 1 Dzielenie - 2 Dodawanie - 3 Odejmowanie - 4:")
wybor = int(input())

a = int(input("Wybierz pierwszą liczbę: "))
b = int(input("Wybierz drugą liczbę: "))

if (wybor == 1):
    print("Wynik mnożenia: ", a, "*", b, "=", (a * b))
elif (wybor == 2):
    if (b == 0):
        print("Cholero, nie dziel przez zero!")
    else:
        print("Wynik dzielenia: ", a, "/", b, "=", (a / b))

elif (wybor == 3):
    print("Wynik dodawania: ",a, "+", b, "=", (a + b))

elif (wybor == 4):
    print("Wynik odejmowania: ",a, "-", b, "=", (a - b))
