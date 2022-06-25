i = 0
sum_sq = 0
while i < 100:
	sum_sq += (i + 1)**2
	i += 1
print("The sum of the squares is: ", sum_sq)

j = 1
sq_sum = 0
lst = []
while j <= 100:
	lst.append(j)
	j += 1
sq_sum = (sum(lst))**2
print("The square of the sum is: ", sq_sum)

answer = sq_sum - sum_sq
print("The difference between the sum of the squares and the square of the sum is: ", answer)



#a simpler solution
x = sum([i**2 for i in range(1,101)])
y = sum([i for i in range(1,101)])**2
answer = y - x
print(answer)
