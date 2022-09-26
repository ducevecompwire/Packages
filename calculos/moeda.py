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

def moeda(p=0, moeda= 'R$'):
    return f'{moeda}{p}'.replace('.', ',')