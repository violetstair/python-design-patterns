# 싱글톤 패턴
# 글로벌하게 접근 가능한 단 한 개의 객체만을 허용하는 패턴
# 로깅이나 데이터베이스, 프린터 스풀러 등의 작업에 주로 사용된다

class Singletone:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print("create instance ...")
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


s = Singletone()
s1 = Singletone()

print("object created ", s)
print("object created ", s1) # s와 s1 두객체는 같은 객체 인스턴스를 갇는다
