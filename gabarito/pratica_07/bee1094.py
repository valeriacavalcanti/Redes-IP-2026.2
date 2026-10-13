qtd_coelhos = 0
qtd_sapos = 0
qtd_ratos = 0

casos_teste = int(input('Informe a quantidade de casos de teste: '))

for i in range(casos_teste):
    qtd = int(input('Quant. Cobaias: '))
    tipo = input('Tipo de cobaia (C, R ou S): ')
    if tipo == 'C':
        qtd_coelhos += qtd
    elif tipo == 'R':
        qtd_ratos += qtd
    else:
        qtd_sapos += qtd
        
total = qtd_coelhos + qtd_sapos + qtd_ratos

perc_coelhos = (qtd_coelhos * 100) / total
perc_ratos = (qtd_ratos * 100) / total
perc_sapos = (qtd_sapos * 100) / total

print (f'Total: {total} cobaias')
print (f'Total de coelhos: {qtd_coelhos}')
print (f'Total de ratos: {qtd_ratos}')
print (f'Total de sapos: {qtd_sapos}')
print (f'Percentual de coelhos: {perc_coelhos:.2f} %')
print (f'Percentual de ratos: {perc_ratos:.2f} %')    
print (f'Percentual de sapos: {perc_sapos:.2f} %')