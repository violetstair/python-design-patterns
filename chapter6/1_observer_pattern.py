# 옵서버 디자인 패턴
# 옵서버 패턴이 적합한 상황
# * 분산 시스템의 이벤트 서비스를 구현할 때
# * 뉴스 에이전시 프레임워크
# * 주식 시장 모델

class Subject:

    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
    
    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:

    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, " :: Got ", args, " From ", subject)


class Observer2:

    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, " :: Got ", args, " From ", subject)


sb = Subject()
ob1 = Observer1(sb)
ob2 = Observer2(sb)
sb.notify_all('notification')
