# 추상 팩토리(abstract factory) 구현
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndiaPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, NonVegPizza):
        pass


class DeluxVeggiePizza(VegPizza):

    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):

    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chcken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):

    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:

    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndiaPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.createNonVegPizza()
            self.veg_pizza = self.factory.createVegPizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


pizza = PizzaStore()
pizza.makePizzas()
