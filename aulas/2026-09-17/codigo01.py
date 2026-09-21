num = int(input('Número: '))

if num <= 0:
    print('Errado')
    num = int(input('Número: '))
    if num <= 0:
        print('Errado')
        num = int(input('Número: '))
        if num <= 0:
            print('Errado')
            num = int(input('Número: '))
            if num <= 0:
                print('Errado')
                num = int(input('Número: '))
            else:
                print('ok')
        else:
            print('ok')
    else:
        print('ok')
else:
    print('ok')
