# 템플릿 메소드 패턴 사용 사례

from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):

    @abstractmethod
    def set_transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    def itinerary(self):
        self.set_transport()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


class VeniceTrip(Trip):
    def set_transport(self):
        print("Take a boat and find your way in the Grand Canal")

    def day1(self):
        print("Visit St.Mark's Basilica in St.Mark's Square")

    def day2(self):
        print("Appreciate Doge's Place")

    def day3(self):
        print("Enjoy the food near the Rialto Bridge")

    def return_home(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    def set_transport(self):
        print("On foot, on any island")

    def day1(self):
        print("Enjoy the marine life of Banana Reef")

    def day2(self):
        print("Go for the water sports and snorkelling")

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def return_home(self):
        print("Don't fell like leaving the beach ... ")


class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        elif choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()
    

TravelAgency().arrange_trip()
