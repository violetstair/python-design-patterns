# 메타 클래스
# 메타클래스는 자신의 메타클래스의 인스턴스이다
# 파이썬에서 모든 것은 객체이다 a=5라면 type(a)는 <type 'int'> 즉 a는 int형 변수라는 뜻이다
# 하지만 type(int)는 <type 'type'>을 반환한다
# int의 메타클래스는 type 클래스를 의미한다

class MyInt(type):
    
    def __call__(cls, *args, **kwargs):
        print('***** hear is my int *****', args)
        print('now do whatever you want with these objects ...')
        return type.__call__(cls, *args, **kwargs)
    

class int(metaclass=MyInt):

    def __init__(self, x, y):
        self.x = x
        self.y = y


# int 클래스를 생성하면 int의 메타클래스인 MyInt의 __call__이 호출되는데
# 객체 생성을 메타클래스가 제어한다는 것을 의미한다
i = int(4, 5)


# 메타클래스를 사용한 싱글턴 패턴
class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances
    

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)
