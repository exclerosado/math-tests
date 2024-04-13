''''
Teste simples utilizando o conceito da multiplicação de dois números primos utilizado no algoritmo RSA.
Autor: Alef Matias @exclerosado
'''

from random import choice


def isPrime(number):
    if number <= 1:
        return False
    
    root = int(number ** (1 / 2))
    for divisor in range(2, root + 1):
        if number % divisor == 0:
            return False
    return True


primesList = []
quantity = int(input('Enter the range of prime numbers to generate the list: '))

for _ in range(quantity):
    if isPrime(_):
        primesList.append(_)

print(f'Prime numbers generated: {primesList}\n')

number1, number2 = choice(primesList), choice(primesList)

while True:
    if number1 != number2:
        result = number1 * number2

        print(f'The given number is ---> {result}\n')
        
        guess1 = int(input('Enter the first guess: '))
        guess2 = int(input('Enter the second guess: '))

        if result == (guess1 * guess2):
            print('Correct!\n')
            break
        else:
            print('Incorrect! Try again...\n')
                 