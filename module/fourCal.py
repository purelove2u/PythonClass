class FourCal:
    def __init__(self):
        super().__init__()

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 // num2

if __name__ == "__main__":
    fourcal = FourCal()
    print(fourcal.sum(5,6))
    print(fourcal.sub(5,6))
    print(fourcal.mul(5,6))
    print(fourcal.div(5,6))