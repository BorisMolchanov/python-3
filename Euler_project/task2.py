fibo1 = 1
fibo2 = 1
fibo_even_sum = 0
fibo_sum = 0

while fibo_sum <= 4000000:
	fibo_sum = fibo1 + fibo2
	fibo1 = fibo2
	fibo2 = fibo_sum
	if fibo_sum % 2 == 0:
		fibo_even_sum += fibo_sum

print(fibo_sum)
print(fibo_even_sum)

f1, f2, s = 0, 1, 0                            # более короткая запись
while f2 <= 4000000:
    s = s + f2 if f2 % 2 == 0 else s
    f1, f2 = f2, f1 + f2
print(s)
