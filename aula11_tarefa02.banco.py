class Conta:
    def __init__ (self, numero, titular, limite):
        self.numero=numero
        self.titular=titular
        self.limite=limite
        self.saldo= 0

    def depositar(self, valor):
        print(f"Seu saldo inicial é de : {self.saldo}")
        self.saldo += valor
        print(f"Seu saldo final é de : {self.saldo}")

    def saque(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Seu saque foi de : R$ {valor} ")
            print(f"Seu saldo final é :  R${self.saldo}")

    def info(self):
        print(f"Conta : {self.numero}\n \nTitular : {self.titular}\n \nLimite: {self.limite}\n")

class Banco:
    def __init__(self):
        self.contas={}

if __name__ == "__main__":
    print(f"Criando a primeira conta")
    cc1= Conta ("00001", "Isabella", 2000.00)
    cc1.info()
    cc1.depositar(1000.00)
    cc1.saque(2000.01)