tc = [0] * 7
tf = [0] * 7

for i in range(len(tc)):
    tc[i] = float(input('TC: '))

for i in range(len(tc)):
    tf[i] = (tc[i] * 9) / 5 + 32

for i in range(len(tc)):
    print(tc[i], tf[i])
