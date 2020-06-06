# 게으른 초기화
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method call ...")
        else:
            print("instance already created : ", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() # 클래스르 초기화 했지만 객체는 생성 하지 않음
print("object created", Singleton.getInstance()) # 객체생성
s1 = Singleton() # 객체는 이미 생성됐음
