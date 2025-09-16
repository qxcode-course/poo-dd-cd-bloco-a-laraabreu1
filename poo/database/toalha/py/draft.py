class Towel:
    def __init__(self, color: str, size: str): #construtor
        self.color = "red" #atributos
        self.size = "p"
        self.wetness = 0

    def __str__(self) :
        return f"color: {self.color}, tam:{self.size}, umi:{self.wetness}"

#variavel ou referencia
toalha = Towel("green", "g") #objetos
toalha = Towel("red", "p")
outra = toalha
print(toalha.color)
toalha.color = "white"
outra.color = "blue"
print(toalha.color)
print(toalha.size)
print(toalha.wetness)

#https://classroom.github.com/a/G161n2yI