class Carro:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self) -> str: # toString
        return f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self) -> None:
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount: int):
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= distance:
            self.gas -= distance
            self.km += distance
        else:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0

def main():
    carro = Carro()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            amount = int(args[1])
            carro.fuel(amount)
        elif args[0] == "drive":
            distance = int(args[1])
            carro.drive(distance)
        else:
            print(f"fail: comando inválido")

main()