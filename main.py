import random 
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

try:
    user_length = int(input('Podaj długość hasła: '))
except:
    print('Musisz wpisać liczbę całkowitą')
    quit()


output = ''

for i in range(user_length):
    output += symbols[random.randint(0,len(symbols)-1)]

print(f'Twoje hasło: {output}')