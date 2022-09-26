from calculos import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar10(p)}')
print(f'Reduzindo 13% de {p}, temos {moeda.reduzir13(p)}. ')
