import sympy

lst = []
x = 2
while len(lst) < 10001:
	if sympy.isprime(x):
		lst.append(x)
	x+=1
print(max(lst))


#without using libs:
def is_prime(x):
	f = True
	for i in range(2, round(x**0.5)+1):
		if x%i == 0:
			f = False
			break
	return f

lst = []
x = 2
while len(lst) < 10001:
	if is_prime(x):
		lst.append(x)
	x+=1
print(max(lst))
