def primos(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
        return True

print(primos(45))
print(primos(7))
print(primos(11))
print(primos(10))
