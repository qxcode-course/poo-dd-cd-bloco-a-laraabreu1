class Calculadora:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str: # toString
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def useBattery(self) -> bool:
        if self.battery > 0:
            self.battery -= 1
            return True
        else:
            print("fail: bateria insuficiente")
            return False
        
    def sum(self, a: float, b: float):
        if not self.useBattery():
            return
        self.display = a + b
    
    def div(self, a: float, b: float):
        if not self.useBattery():
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b
    

def main():
    calc = None
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calc = Calculadora(batteryMax)
        elif args[0] == "show":
            if calc is not None:
                print(calc)
            else:
                print("fail: calc nao inicializada")
        elif args[0] == "charge":
            increment = int(args[1])
            calc.charge(increment)
        elif args[0] == "sum":
            a = float(args[1])
            b = float(args[2])
            calc.sum(a, b)
        elif args[0] == "div":
            a = float(args[1])
            b = float(args[2])
            calc.div(a, b)
        else:
            print(f"fail: comando inválido")

main()