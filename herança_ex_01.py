class Personagem:
    def __init__(self,Arthas, nivel, vida, força, mago):
        
        self.nome =  Arthas
        self.nivel = 10
        self.vida = 20
        self.força = força 
        self.magico = mago
def apresentar(self):
    print(f"Ola, eu sou {self.nome},nivel{self.nivel}!")

def atacar(self):
    if self.magico:
        print(f"{self.nome} lançou um feitiço poderoso!")
    else:
        print(f"{self.nome} desferiu um golpe com força{self.força}!")

        def receber_dano(self, dano):
            self.vida -= dano
            print(f"{self.nome}se curou em {self.valor}. Vida atual: {self.vida}")

            def curar(self, valor):
                self.vida += valor
                print(f"{self.nome} se curou em {valor}. Vida ayual: {self.vida}")
        
            def subir_nivel(self):
                self.nivel += 1
                self.força += 5
                print(f"{self.nomr} subiu para o nivel {self.nivel}!")