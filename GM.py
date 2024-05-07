from cool_guys import legandr


c = [ 218, 34, 194, 164, 220, 50, 237, 77,68, 151, 135, 21, 101, 167, 196, 98,196, 219, 89, 241, 16, 134, 240, 43,36, 193, 37, 17, 184, 61, 81, 41, 81, 148, 18, 172, 193, 37, 203, 233,244, 145, 18, 1, 121, 46, 18, 193 ]

y, n = 109, 247
p, q = 13, 19

tmp=''

for elem in c:
    tmp += str(int(legandr(elem, p) < 0 or legandr(elem, q) < 0))

tmp = [chr(int(tmp[i:i+8], 2)) for i in range (0, len(tmp), 8)]

print(*tmp, sep='')