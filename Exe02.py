# Crie uma hierarquia de classes que represente veículos.
# Comece com uma classe base "Veículo" e, em seguida, crie classes derivadas como "Carro" e "Bicicleta." 
# Adicione métodos para definir atributos, como "cor" e "modelo" epermita a chamada de métodos em cadeia 
# para configurar esses atributos.

# Criando a classe Veículo
class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def definir_cor(self, cor): # Método 
        self.cor = cor
        return self
    
    def definir_modelo(self, modelo): # Método 
        self.modelo = modelo
        return self
    
class Carro(Veiculo): # Classe derivada
    def __init__(self):
        super().__init__()
        self.tipo = 'Carro'

class Bicicleta(Veiculo): # Classe derivada
    def __init__(self):
        super().__init__()
        self.tipo = 'Bicicleta'

# Uso das classes:
carro = Carro().definir_cor('Cinza Fosco').definir_modelo('Sedan')
print(f'Carro: cor {carro.cor}, modelo {carro.modelo}')

bicicleta = Bicicleta().definir_cor('Preto Fosco').definir_modelo('Speed')
print(f'Bicicleta: cor {bicicleta.cor}, modelo {bicicleta.modelo}')