def gcd(a, b):
    if ( b == 0):
        return a
    return gcd(b, a%b)


def extended_Euclid_alg(a, b):
    if ( b == 0):
        return [a, 1, 0]
    tmp = extended_Euclid_alg(b, a%b)
    return [tmp[0], tmp[2], tmp[1] - tmp[2]*(a//b)]


def legandr(a, p):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0:
        return legandr(a//2, p) * (-1)**((p**2-1)//8)
    return legandr(p % a, a) * (-1)**((a-1)*(p-1)//4)


def jacobi(a, n):
    if a==0:
        return 0
    if a == 1:
        return 1
    if a >= n:
        return jacobi(a % n, n)
    if a == 2:
        return (-1)**((n**2-1)//8 % 2)
    if (gcd(a, n) == 1):
        if a % 2 == 0:
            return jacobi(2, n) * jacobi(a//2, n)
        if n % 2 == 0:
            return jacobi(a, 2) * jacobi(a, n//2)
        return (-1)**((a-1)*(n-1)//4) * jacobi(n, a)
    else:
        return jacobi(a, n//gcd(a, n)) * jacobi(a, gcd(a, n))