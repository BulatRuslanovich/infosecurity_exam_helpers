def modular_exponentiation(x, y, z):
    result = 1
    base = x % z

    step = 1
    while y > 0:
        if y % 2 == 1:
            result = (result * base) % z
       
        base = (base * base) % z
        y //= 2
        step += 1

    return result


print("Welcome to the (x^y) mod z computation program!\n")
x = int(input("Enter x: " ))
y = int(input("Enter y: " ))
z = int(input("Enter z: "))

result = modular_exponentiation(x, y, z)
print(f"\nResult: ({x}^{y}) % {z} = {result}" )
