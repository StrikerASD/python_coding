"""
Oblicz wartość bezwzględną z liczby tzn. spraw, aby liczba ujemna stała się dodatnią.

Wartość bezwzględna usuwa 'minus' liczbie ujemnej. Wartość dodatnią i zerową pozostawia bez zmian.

Tzn. liczba:

-5 ma stać się 5.

4 ma zostać 4.

-1 ma stać się 1.

0 ma zostać 0.

1) Pobierz od użytkownika wartość i zapisz ją do zmiennej

2) Jeśli liczba jest ujemna to zmień wartość zmiennej tak, aby była dodatnia. Wypisz wynik.

"""

print("Podaj liczbę: ")

wynik = int(input())

print(abs(wynik))

# Pobierz wartość od użytkownika i zapisz ją do zmiennej
x = int(input("Podaj liczbę: "))

# Sprawdź, czy x jest ujemne
if x < 0:
    # Jeśli x jest ujemne, to zmień jego wartość na dodatnią
    x = -x

# Wypisz wartość bezwzględną z liczby x
print(x)