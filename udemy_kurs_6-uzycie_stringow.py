imie = "Robert"

nazwisko = "Wasilewski"

imieNazwisko = imie + " " + nazwisko

print(imieNazwisko)

# Jak widać w poniższym przykładzie, jest różnica w wyświetlaniu tekstu w zależności jakie znaki do przetwarzania tekstu wybierzemy

dlugiString = """Jakis tekst który jest bardzo dłuugi i tak w kółko.
               Jakis tekst który jest bardzo dłuugi i tak w kółko.
               Jakis tekst który jest bardzo dłuugi i tak w kółko.
               Jakis tekst który jest bardzo dłuugi i tak w kółko.
               Jakis tekst który jest bardzo dłuugi i tak w kółko."""

print(dlugiString)

dlugiStringDrugi = "Jakis tekst który jest bardzo dłuugi i tak w kółko.\
               Jakis tekst który jest bardzo dłuugi i tak w kółko.\
               Jakis tekst który jest bardzo dłuugi i tak w kółko.\
               Jakis tekst który jest bardzo dłuugi i tak w kółko.\
               Jakis tekst który jest bardzo dłuugi i tak w kółko."

print(dlugiStringDrugi)

"""
Poniżej stosujemy wyświetlanie tylko jakiegoś zakresu danego stringa. Należy pamiętać,
 że gdy chcemy pobrać zakres stringa, to ostatnia wartość nie będzie wyświetlana 
 tak jak w przykładzie: print(nazwisko[0:4]) zostaną wyświetlone pierwsze cztery znaki a nie pięć
 """

print(imie[:3])

print(nazwisko[:-1])

print(nazwisko[0:4])

