qtd_paginas = int(input('Quantidade de páginas: '))

qtd_copias = 1000 // qtd_paginas

qtd_sobra = 1000 % qtd_paginas

print(qtd_copias, 'cópias')
print(qtd_sobra, 'folhas')
