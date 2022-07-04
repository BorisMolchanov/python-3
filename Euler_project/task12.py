a, b = 1, 1
divisors = set()

while True:
    a += 1
    b += a

    for i in range(1, int(b ** 0.5) + 1):
        if b % i == 0:
            divisors.add(i)
            divisors.add(int(b / i))

    if len(divisors) < 500:
        divisors.clear()
    if len(divisors) >= 500:
        print(f"The triangle number which have over 500 divisors is {b}")
        print(f"The number {b} has {len(divisors)} divisors")
        break
