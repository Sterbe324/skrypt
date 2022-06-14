import random

def SzukLid(A):
    i, kand, ile = 0, 0, 0
    for i in range(len(A)):
        if ile == 0:
            ile = 1
            kand = A[i]
        elif A[i] == kand:
            ile += 1
        else:
            ile -= 1
    if ile == 0:
        return 0
    ile = 0
    for i in range(len(A)):
        if A[i] == kand:
            ile += 1
    if ile > len(A) / 2:
        return kand
    else:
        print("brak Lidera")
    return 0


x = random.randint(0, 100)
N = int(input("wpisz dlugosc listy:"))
A = [0] * N
for i in range(N):
    if random.randint(0, 1) == 0:
        A[i] = random.randint(0, 100)
    else:
        A[i] = x
for i in range(N):
    print(A[i], end=" ")
b = SzukLid(A)
print()
print("Lider ", b)
