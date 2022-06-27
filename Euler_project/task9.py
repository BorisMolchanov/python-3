def search():
	for c in range(997, 1, -1):
		for b in range(2, 1001-c):
			for a in range(1, 1001-c-b):
				if a+b+c == 1000:
					if a**2 + b**2 == c**2:
						if a<b<c:
							return a, b, c
result = search()
prod = result[0]*result[1]*result[2]
print("a, b, c =", result, ", their product is equal:", prod)
