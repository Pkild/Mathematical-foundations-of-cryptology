from cool_guys import extended_Euclid_alg

n = int(input("Number of equasions:"))
a, m = int(input("a = ")), int(input("m = "))
for i in range(n-1):
    tmp_a, tmp_m = int(input("a = ")), int(input("m = "))
    a, m = m * extended_Euclid_alg(m, tmp_m)[1] * (tmp_a - a) + a, m * tmp_m 
print(a)