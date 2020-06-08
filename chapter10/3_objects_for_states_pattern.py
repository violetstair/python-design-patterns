# 상태 디자인 패턴

class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current: ', self, ' => switched to new state ', state.name)
            self.__class__ = state
        else:
            print('Current: ', self, ' => switched to ', state.name, ' not posible')
    
    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ["on"]


class On(ComputerState):
    name = "on"
    allowed = ["off", "suspend", "hibernate"]


class Suspend(ComputerState):
    name = "suspend"
    allowed = ["on"]


class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ["on"]


class Computer:

    def __init__(self, model='Apple'):
        self.model = model
        self.state = Off()
    
    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    c = Computer()

    # 전원을 켠다
    c.change(On)

    # 전원을 끈다
    c.change(Off)

    # 전원을 켠다
    c.change(On)

    # 일시 중지
    c.change(Suspend)

    # 절전 모드로 변경 시도
    c.change(Hibernate) # 실패

    # 전원을 켠다
    c.change(On)

    # 전원을 끈다
    c.change(Off)
