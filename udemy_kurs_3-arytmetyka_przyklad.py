# Podatek VAT

cenaNettoJava = 10
cenaNettoAjax = 20

cenaBruttoJava = cenaNettoJava * 1.23 #Stała wartość VAT, trzeba zmieniać wszędzie w kodzie. Nie praktyczne
cenaBruttoAjax = cenaNettoAjax * 1.23

### Lepiej stworzyć zmienną VAT, zmienić trochę metodę obliczania VAT i wtedy wystarczy już zmienić wartość VAT w jednym miejscu

VAT = 23

cenaBruttoJava = cenaNettoJava * (1 + VAT / 100)
cenaBruttoJava = cenaNettoAjax * (1 + VAT / 100)

### Można również obliczenie VAT wstawić do zmiennej

obliczonyVAT = (1 + VAT / 100)

cenaBruttoJava = cenaNettoJava * obliczonyVAT
cenaBruttoAjax = cenaNettoAjax * obliczonyVAT

print (cenaBruttoJava)
print (cenaBruttoAjax)

cenaNettoKomputer = 3499
cenaNettoMonitor4K = 2599
cenaNettoBiurko = 1399

cenaBruttoKomputer = cenaNettoKomputer * obliczonyVAT
print (cenaBruttoKomputer)
cenaBruttoMonitor4K = cenaNettoMonitor4K * obliczonyVAT
print (cenaBruttoMonitor4K)
cenaBruttoBiurko = cenaNettoBiurko * obliczonyVAT
print (cenaBruttoBiurko)