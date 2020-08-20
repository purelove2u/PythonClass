class Audio:
    """
    power, volume 을 가진 클래스
    power => True,False
    volume => 정수

    switch() => power 값을 변경
    tune() => power 켜 있으면 음악 재생되고, power 꺼진 상태면
              power 켜라는 메세지 출력
    volume() => volume 값을 변경
    """
    def __init__(self, power = False, volume = 0):
        self.power = power
        self.volume = volume
    
    def switch(self):
        if self.power:
            self.power = False
        else :
            self.power = True
    
    def tune(self):
        if self.power:
            print("음악 재생 중")
        else:
            print("전원을 켜세요")

    def set_volume(self, value):
        if self.power:
            self.volume = value
            print("현재 음악 재생 중 볼륨 : {}".format(self.volume))
        else:
            print("전원을 켜세요")

sony = Audio()
sony.tune()
sony.switch()
sony.tune()
sony.set_volume(20)
sony.switch()
sony.set_volume(10)
 

