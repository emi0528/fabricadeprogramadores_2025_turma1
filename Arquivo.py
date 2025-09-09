"""
try: 
    arquivo=open("números.txt","w")
    for linha in range(1,101):
        arquivo.write(" Emilly%d\n" % linha)
    arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado!'
"""
try:
    arquivo=open("numeros.tx","r")
    for linha in arquivo.readlines():
        print(linha)
        arquivo.close()

    impares=open("impares.txt","w")
    pares=open("pares.txt","w")
    for n in range(0,1000):
        if n % 2 == 0:
            pares.write("%d/n"% n)
    impares.close()
    pares.close()