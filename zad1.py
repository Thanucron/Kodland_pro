# Funkcja do obliczania reszty z dzielenia dwóch liczb
# Zadanie: Napisz funkcję remainder(a, b), która przyjmuje dwa argumenty i zwraca resztę z ich dzielenia. Jeśli drugi argument jest równy zero, funkcja powinna zwrócić napis "Dzielenie przez zero jest niemożliwe".

def remainder(a, b):
    try:
        reszta = a % b
    except ValueError:
        print("Dzielenie przez zero jest niemożliwe")
        quit()
    return reszta

jaka_reszta = remainder(int(input('Podaj 1 liczbę całkowitą: ')), int(input('Podaj 2 liczbę całkowitą: ')))

if jaka_reszta == 0:
    print('wynik nie ma reszty')
else:
    print(f'reszta jest równa {jaka_reszta}')
