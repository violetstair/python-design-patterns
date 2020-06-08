# 상태 디자인 패턴
# 상태 디자인 패턴은 유한 상태 머신(finite state machine)을 개발하거나 트랜젝션을 구현할 때 적합하다
# 상태 디자인 패턴의 구성 요소
# * State: 객체의 행위를 캡슐화하는 인터페이스, 행위는 객체의 상태에 따라 변한다
# * ConcreteState: 인터페이스를 구현하는 서브클래스, 특정 상태의 객체의 행위를 구현한다
# * Context: 사용자가 선택한 인터페이스를 정의, 특정 상태의 객체를 구현한 ConcreteState 서브클래스의 인스턴스를 가지고 있다

from abc import ABCMeta, abstractmethod


# Handle() 추상 메소드를 정의하는 인터페이스, 이 메소드는 ConcreteState가 구현한다
class State(metaclass=ABCMeta):

    @abstractmethod
    def Handle(self):
        pass


# ConcreteState: State 설정에 따라 실행될 각자의 Handle() 메소드를 구현한다
class ConcreteStateB(State):

    def Handle(self):
        print("ConcreteStateB")


class ConcreteStateA(State):

    def Handle(self):
        print("ConcreteStateA")


# Context: 사용자의 요청을 넘겨받는 클래스, 객체의 현재 상태를 저장하고 요청에 맞는 메소드를 호출한다
class Context(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def Handle(self):
        self.state.Handle()


context = Context()
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context.set_state(state_a)
context.Handle()
