class TV:
    """
    power, volume, size 프로퍼티를 가진 클래스
    생성자를 통해 초기화
    switch() : power의 on / off 변환
    set_volume() : volume 조절
    watch() : power 여부에 따라 on 상태이면 "tv 보는 중.." 메시지 보여주기
                              off 상태이면 "tv 켜세요" 메시지 보여주기
    """
    def __init__(self, power, volume, size):
        self.power = power
        self.volume = volume
        self.size = size
    
    def switch(self):
        if self.power:
            self.power = False
            print("TV 종료")
        else :
            self.power = True
            print("TV 켬")

    def set_volume(self, value):
        self.volume = value
        print("볼륨 {}".format(self.volume))

    def watch(self):
        if self.power:
            print("TV 시청 중")
        else :
            print("TV를 켜세요")

lgTV = TV(False, 0, 50)
lgTV.watch()
lgTV.switch()
lgTV.set_volume(20)
lgTV.watch()
lgTV.switch()

    