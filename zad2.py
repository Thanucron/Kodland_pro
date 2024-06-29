# Funkcja sprawdzająca obecność podłańcucha
# Zadanie: Napisać funkcję contains_substring, która przyjmuje dwa ciągi znaków: ciąg główny i podciąg, i zwraca True, jeśli podciąg jest zawarty w ciągu głównym, a False w przeciwnym razie.

def contains_substring(ciąg_główny=input('Podaj ciąg główny: '), podciąg=input('Podaj podciąg: ')):
    return podciąg in ciąg_główny

print(contains_substring())