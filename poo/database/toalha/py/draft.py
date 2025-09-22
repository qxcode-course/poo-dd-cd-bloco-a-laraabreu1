


class Towel:
    def __init__(self, color: str, size: str): #construtor: padrao para definir que aquele metodo eh o construtor
        self.color = "red" #atributos
        self.size = "p"
        self.wetness: int = 0

    def dry(self, amount:int) -> None:  #amount: quantidade de agua
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def __str__(self) :  #transforma em texto, equivalente ao "toString"
        return f"color: {self.color}, tam:{self.size}, umidade:{self.wetness}"  #return: devolve para quem solicitou

#variavel ou referencia
minha: Towel = Towel("red", "M")
toalha = Towel("green", "g") #objetos
toalha = Towel("red", "p")
outra = toalha
print(toalha.color)
toalha.color = "white"
outra.color = "blue"
print(toalha.color)
print(toalha.size)
print(toalha.wetness)

doguito = Towel("velha", "M")  #toalha foi criada aqui
print(doguito)
doguito.dry(3)
print(doguito)
doguito.dry(15)
doguito.dry(10)
print(doguito)



#https://classroom.github.com/a/G161n2yI