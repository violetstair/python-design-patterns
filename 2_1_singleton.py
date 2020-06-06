# 싱글톤 패턴
class Singletone:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print("create instance ...")
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


s = Singletone()
print("object created ", s)

s1 = Singletone()
print("object created ", s1)
