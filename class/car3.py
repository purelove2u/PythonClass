class Car:
    """
    Car class
    Author : Park
    Date : 2020.08.13
    Description : Class 작성법 / 생성자
    """

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


# 객체 생성
myCar1 = Car('red', 0)
myCar2 = Car('blue', 0)
myCar3 = Car('yellow', 0)

myCar1.upSpeed(20)
print("자동차1의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar1.color, myCar1.speed))

myCar2.upSpeed(30)
print("자동차2의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar2.color, myCar2.speed))


myCar3.upSpeed(40)
print("자동차3의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar3.color, myCar3.speed))


print()
print("myCar1 주소 : ", id(myCar1))
print("myCar2 주소 : ", id(myCar2))
print("myCar3 주소 : ", id(myCar3))

print()
print(Car.__doc__)