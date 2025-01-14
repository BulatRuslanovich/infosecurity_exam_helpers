def factorize_rsa_number(n):
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            p = divisor
            q = n // divisor
            return p, q
        divisor += 1

    return None, None


n = int(input("Enter number n: "))
p, q = factorize_rsa_number(n)

if p and q:
    print(f"The number {n} factors as prime factors: p = {p}, q = {q}")
else:
    print(f"The number {n} cannot be factored into two primes (it may be prime itself).")
