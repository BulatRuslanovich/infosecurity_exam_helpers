def modular_exponentiation(m, d, fn):
    result = 1
    base = m % fn

    step = 1
    while d > 0:
        if d % 2 == 1:
            result = (result * base) % fn
       
        base = (base * base) % fn
        d //= 2
        step += 1

    return result


print("Welcome to the (m^d) mod F(n) computation program!\n")
m = int(input("Enter m: " ))
d = int(input("Enter d: " ))
fn = int(input("Enter F(n): "))

result = modular_exponentiation(m, d, fn)
print(f"\nResult: ({m}^{d}) % {fn} = {result}" )
