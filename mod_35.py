from cool_guys import legandr, jacobi


n = 35
a = [i for i in range(n)]
for elem in a:
    print(f"{elem}: (a/5) = {legandr(elem, 5)}, (a/7) = {legandr(elem, 7)}, (a/35) = {jacobi(elem, 35)}, Quadratic: {legandr(elem, 5) >=0 and legandr(elem, 7) >=0}")

print("Special cases: ", end='')
for elem in a:
    if not (legandr(elem, 5) >=0 and legandr(elem, 7) >=0) and (jacobi(elem, 35) > -1):
        print(elem, end = ' ')