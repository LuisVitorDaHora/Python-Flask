# Módulo Operações Matemáticas

def soma (x,y):
    return x+y

def substracao (x,y):
    return x-y

def multiplicacao (x,y):
    return x*y

def divisao (x,y):
    if y != 0:
        return x/y
    else: 
        raise ValueError ("Não é permitido divisão por zero")