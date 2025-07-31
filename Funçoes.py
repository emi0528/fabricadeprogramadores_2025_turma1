"""nome = input("insira seu nome")
saudacao  = "ola" +nome 
print(saudacao)

numero_string = input("insira 1numero: ")
numero_inteiro = int( numero_string )
subtracao = numero_inteiro - 2
print(subtracao)
"""

def quadrado(lado):
    area = lado ** 2
    return area
print(quadrado(30))


def reajuste(salario):
    novo_salario = salario + salario * 15/100
    return novo_salario
print(reajuste(1000)) 


def triangulo(base, altura):
    resultado = ( altura * base)/2
    return resultado
print(triangulo(2,4))

def temperatura(celcius):
    resposta = ( 9*celcius+160)/5
    return resposta
print(temperatura(100))

def troca(x,y):
    x = y
    y = x
    z = y
    return x,y
print(troca(4,9))        