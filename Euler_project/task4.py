import math

r = 999*999
s = (str(r))
sqrt = math.ceil(r**0.5)
lst = []

def func():
	for i in range(r,0, -1):
		if str(i) == str(i)[::-1]:
			for n in range(100, sqrt):
				if i%n == 0:
					for a in range(100, sqrt):
						if a == i/n:
							lst.append(i)
							lst.append(a)
							lst.append(n)
							return lst
func()
print("Наибольший палиндром и трёхзначные множители: ", lst[0], "= ", lst[1], "*", lst[2])
