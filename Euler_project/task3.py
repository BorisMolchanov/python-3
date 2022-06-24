import sympy

def prime_divisor(a):
    sqrt = int(a**0.5)
    lst=[]
    for i in range(3,sqrt):
        if a%i==0:
            if sympy.isprime(i):
                lst.append(i)
            if sympy.isprime(a//i):
                lst.append(a//i)
    return lst
pd=prime_divisor(600851475143)
print("Простые делители:")
print(pd)
print("")
print("Самый большой простой делитель:")
print(max(pd))
