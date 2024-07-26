# https://mindyourdecisions.com/blog/2024/06/30/scientists-just-discovered-a-new-formula-for-pi-accidentally/
from math import factorial, gamma, pi


def calculatePI(_lambda, iterations):
    _sum = 0

    for N in range(iterations):
        first = 1 / factorial(N)
        second = (1 / (N + _lambda)) - (4 / (2 * N + 1))
        a = ((2 * N + 1) ** 2 / (4 * (N + _lambda))) - N
        b = N - 1
        _gamma = gamma(a + b) / gamma(a)
        product = first * second * _gamma

        _sum += product
    
    return _sum


# For testing
lambda_ = 10
iterats = 30

real_value = pi
estimated = calculatePI(lambda_, iterats)
error = real_value - estimated

print(f'PI (real) ---> {real_value}\nPI (est.) ---> {estimated}\nError ---> {error}')
