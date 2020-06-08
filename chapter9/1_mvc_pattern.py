# 모델-뷰-컨트롤러 패턴
# 모델: 데이터를 저장하고 조직하는 클래스
# 뷰: 유저 인터페이스와 데이터의 시각적 표현을 담당하는 클래스
# 컨트롤러: 모델과 뷰를 연결하는 클래스
# 클라이언트: 목적에 따라 정보를 요청하는 클래스
# MVC 패턴이 적합한 상황
# * 비지니스 로직을 건드리지 않고 표현 계층만 수정해야 하는 경우
# * 유저 인터페이스를 수정하는 데 다수의 컨트롤러와 뷰가 사용될 수 있다
# * 모델은 뷰를 수정하지 않아도 변경될 수 있으므로 독립적이다
# MVC 패턴의 목적
# * 데이터 조작과 표현의 분리
# * 쉬운 유지보수와 구현
# * 유연한 데이터 저장과 표현방식의 수정, 서로 독립적이므로 쉽게 수정할 수 있다

class Model:

    services = {
        'email': {'number': 1000, 'price': 2, },
        'sms': {'number': 1000, 'price': 10, },
        'voice': {'number': 1000, 'price': 15, },
    }


class View:

    def list_services(self, services):
        for svc in services:
            print(svc, ' ')
    
    def list_pricing(self, services):
        for svc in services:
            print("For ", Model.services[svc]['number'], svc, " message you pay $", Model.services[svc]['price'])


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    

if __name__ == "__main__":
    controller = Controller()
    print("Services Provided: ")
    controller.get_services()
    print("Pricing for Services: ")
    controller.get_pricing()
