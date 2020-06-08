# 프록시 디자인 패턴
# 복잡한 시스템을 간단하게 표현할 수 있다
# 객체에 대한 보안을 제공한다
# 다른 서버에 존재하는 외부 객체에 대한 로컬 인터페이스를 제공한다
# 메모리 사용량이 높은 객체를 다루는 개벼운 핸들러 역할을 한다

class Actor(object):

    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie") # 다른 영화 촬영 중
    
    def available(self):
        self.is_busy =  False
        print(type(self).__name__, "is free for movie") # 출연 가능

    def get_status(self):
        return self.is_busy


class Agent(object):

    def __init__(self):
        self.pricipal = None
    
    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == "__main__":
    r = Agent()
    r.work()
