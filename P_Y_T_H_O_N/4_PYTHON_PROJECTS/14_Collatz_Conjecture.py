#  Collatz Conjecture  -  The Collatz conjecture is a conjecture that a particular sequence always reaches 1. The sequence is defined as: start with a number n. The next number in the sequence is n/2 if n is even and 3n + 1 if n is odd.


n = int(input("Enter any no. : "))

while (n > 1):
    print(n)
    if (n % 2 == 0):
        n = n/2
    else:
        n = (3*n) + 1

print(1)
