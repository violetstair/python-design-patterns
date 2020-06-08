# 모노스테이트 싱글톤
# 모든 객체가 같은 상태를 공유하는 패턴

class Borg:
    
    __shared_state = {"1": "2"}
    
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1) # b와 b1은 다른 객체이다
print("Object State 'b': ", b.__dict__)
print("Object State 'b1': ", b1.__dict__) # b와 b1은 상태를 공유 한다


# __new__ 를 이요한 모노스테이트 싱글톤
class Borg2(object):
    
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

b = Borg2()
b1 = Borg2()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)
print("Object State 'b1': ", b1.__dict__)
