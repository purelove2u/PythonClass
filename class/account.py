class Account:
    """
    은행계좌 클래스
    계좌번호, 이름, 잔액을 받아서 객체를 생성
    입금 / 출금 기능의 메소드 구현
    """
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def deposit(self, money):        
        self.balance += money
        print("{}님 {}원 입금완료. 현재잔액 : {}".format(self.name, money, self.balance))

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print("{}님 {}원 출금완료. 현재잔액 : {}".format(self.name, money, self.balance))
        else:
            print("{}님 {}원 출금요청. 잔액이 부족합니다. 현재잔액 : {}".format(self.name, money, self.balance))

    def __str__(self):  # toString() 기능
        return "{},{},{}".format(
            self.account_num, self.name, self.balance
        )

user1 = Account(1111, '홍길동', 100000)
user2 = Account(2222, '성춘향', 50000)
user3 = Account(3333, '고길동', 200000)

print(user1)
print(user2)
print(user3)

user1.deposit(5000)
user2.withdraw(50000)
user3.withdraw(300000)