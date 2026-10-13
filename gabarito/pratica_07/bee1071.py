soma = 0

x = int(input('X = '))
y = int(input('Y = '))

if x > y:
    x,y = y,x

for i in range(x+1,y):
    if (i % 2) != 0:
        soma += i
print(soma)