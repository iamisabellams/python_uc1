class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  
        self.modelo = modelo  
        self.ano = ano 
        self.ligado = False 

    def exibir_info(self):
        if self.ligado == True :
            status = "Ligado"
        else:
            status = "Desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}")

    def ligar(self):
        self.ligado = True
        # print(f"O carro está ligado.")

    def desligar(self):
        self.ligado = False
        # print(f"O carro está desligado.")


if __name__ == "__main__":
    print(f"Criando um objeto da classe carros")
    meu_carro = Carro("Toyota", "Corolla", 2020)
    meu_carro.exibir_info()

    meu_carro.ligar()
    meu_carro.exibir_info()