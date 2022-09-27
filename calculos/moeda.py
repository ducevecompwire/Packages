def metade(p, format=False):
    met = p / 2
    return met if format is False else moeda(met)
    
def dobro(p, format=False):
    dob = p * 2
    return dob if format is False else moeda(dob)
    
def aumentar(p, taxa, format=False):
    b = (p * taxa) / 100
    c = p + b
    return c if format is False else moeda(c)
   
def reduzir(p, taxa, format=False):
    b = p * taxa / 100
    c = p - b
    return c if format is False else moeda(c)

def moeda(p, moeda= 'R$'):
    return f'{moeda}{p}'.replace('.', ',')

def resumo(p):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(p)}')
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')
    print(f'Aumento de 10%: {aumentar(p, 10, True)}')
    print(f'O preço reduzido em 13% é: {reduzir(p, 13, True)}')
    print('-' * 30)
    
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
            válido = True
            return float(entrada)