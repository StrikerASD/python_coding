warunek = int(input("Podaj liczbę z zakresu od 1 do 10: "))
if(warunek >= 1 and warunek <= 10):
    print("Podana liczba jest z zakresu od 1 do 10.")
    print("Wpisałeś ", warunek)
else:
    print("Liczba poza uzgodnionym zakresem: ", warunek)