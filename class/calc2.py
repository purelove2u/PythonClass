class Calculator:
    """
    Calculator Class
    Author : ..
    Date : 2020.08.13
    Description : Class 생성 / 인자를 받는 생성자
    """

    def __init__(self, result):
        self.result = result

    def adder(self, num):
        self.result += num
        return self.result


# 객체 생성
cal1 = Calculator(0)
cal2 = Calculator(0)

print("cal1 : {}".format(cal1.adder(10)))
print("cal2 : {}".format(cal2.adder(100)))
