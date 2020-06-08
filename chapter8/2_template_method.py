# 템플릿 메소드 패턴

from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print("Defining the Algoritm. Operation 1 follows Operation 2")
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print("My Concrete Operation 1")
    
    def operation2(self):
        print("My Concrete Operation 2")


class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


client = Client()
client.main()
