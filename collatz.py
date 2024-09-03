import matplotlib.pyplot as plt
from math import log
plt.style.use('dark_background')
plt.rc('figure', figsize=(12, 8))
plt.rcParams['figure.dpi']= 100


def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
        sequence.append(n)
    return sequence[::-1]


n_range = int(input('Enter a range to generate a bunch os sequences: '))

for N in range(1, n_range + 1):
    Y = collatz(N)
    Y_log = [log(y) for y in Y]
    X = [i for i in range(1, len(collatz(N)) + 1)]
    X_log = [log(x) for x in X]

    plt.plot(X_log, Y_log, alpha=0.2, color='deeppink', linewidth=0.5)
plt.grid(alpha=0.2)
plt.title(f'Log of Collatz Sequences from 1 to {n_range}')
plt.xlabel('Steps (log)')
plt.ylabel('Collatz value (log)')
plt.savefig(f'bunch_of_collatz_between_1_to_{n_range}.png')
plt.show()
