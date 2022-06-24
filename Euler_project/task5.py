x = int(input("Enter first number: ")) 
y = int(input("Enter second number: "))
n = 20 # ищем наименьшее общее кратное для всех чисел от 1 до n

def calculate_hcf(x, y): # ищем наибольший общий делитель (НОД)
    if x > y: 
        smaller = y 
    else: 
        smaller = x 
    for i in range(1,smaller + 1): 
        if((x % i == 0) and (y % i == 0)): 
            hcf = i
    return hcf

def calculate_lcm(x,y): # ищем наименьшее общее кратное НОК по формуле НОК(a,b) = a*b/НОД(ab)
    lcm = x*y/calculate_hcf(x,y)
    return lcm

# попарно прогоняем по циклу 1е и 2е число, получаем НОК(1,2) далее НОК(1,2) и 3е число и т д.
while y<n: 
    x = calculate_lcm(x,y)
    y +=1

print(calculate_lcm(x, y))




print("The H.C.F. of", x,"and", y,"is", calculate_hcf(x, y))
print("The L.C.M. of", x,"and", y,"is", calculate_lcm(x, y))
