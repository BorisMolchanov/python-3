x = int(input("Enter first number: ")) 
y = x+1
n = int(input("Enter last number: ")) # ищем наименьшее общее кратное для всех чисел от 1 до n

def calculate_hcf(x, y):
    if x > y: 
        smaller = y 
    else: 
        smaller = x 
    for i in range(1,smaller + 1): 
        if((x % i == 0) and (y % i == 0)): 
            hcf = i
    return hcf

def calculate_lcm(x,y):
    lcm = x*y//calculate_hcf(x,y)
    return lcm


while y<n:
    x = calculate_lcm(x,y)
    y +=1

print("The L.C.M. is", calculate_lcm(x, y))
