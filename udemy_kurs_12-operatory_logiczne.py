warunek = int(input("Podaj liczbę z zakresu od 1 do 10: "))
# if(warunek >= 1 and warunek <= 10):
#     print("Podana liczba jest z zakresu od 1 do 10.")
#     print("Wpisałeś ", warunek)
# else:
#     print("Liczba poza uzgodnionym zakresem: ", warunek)
#
# if(warunek >= 1 or warunek <= 10):
#     print("Jedna z podanych liczb jest z zakresu od 1 do 10 lub wyżej.")
#     print("Wpisałeś ", warunek)

if(not(warunek >= 1 and warunek <= 10)):
    print("Wpisana liczba jest... ", warunek)
else:
    print("Wpisana liczba jest spoza zakresu...")