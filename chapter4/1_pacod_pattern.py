# 퍼사드 패턴
# 클라이언트 : 결혹식 전까지 모든 준비를 마쳐야 하는 사용자, 하객들이 만족할 만한 최고 수준으로 준비해야 한다
# 퍼사드 : 음식과 꽃 장식 등을 준비하는 업체와의 조율을 담당하는 웨딩플래너
# 서브시스템 : 음식과 호텔 예약, 꽃 장식 등을 담당하는 업체

class EventManager(object):

    def __init__(self):
        print("Event Manager :: Let me talk to the fork\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):

    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    
    def __is_available(self):
        print("Is the Hotel free for the event on given day?")
        return True
    
    def book_hotel(self):
        print("Registered the booking\n\n")
        

class Florist(object):

    def __init__(self):
        print("Flower Decorations for the Event? --")

    def set_flower_requirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")

class Caterer(object):

    def __init__(self):
        print("Food arrangements for the event --")

    def set_cuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")

class Musician(object):

    def __init__(self):
        print("Musical arrangements for the Marriage --")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


class You(object):

    def __init__(self):
        print("YOU :: Whoa! Marriage Arrangements???!!!")
    
    def ask_event_manager(self):
        print("YOU :: let's contact the event manager\n\n")
        em = EventManager()
        em.arrange()
    
    def __del__(self):
        print("YOU :: Tanks to Event Manager, all preparations done! Phew!")

you = You()
you.ask_event_manager()

# EventManager는 You 클래스를 위해 인터페이스를 간소화 해주는 퍼사드이다
# EventManager는 컴포지션을 통해 Hotelier와 Caterer 등의 서브 시스템 객체를 생성한다
