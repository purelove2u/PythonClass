# 클래스 상속
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__호출")
    
    def test(self):
        print("Parent 클래스의 test() 호출")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init() 호출")

child = Child()
child.test()
print(child.value)