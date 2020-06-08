# 옵서버 패턴 사용 사례
from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class NewsPublisher:

    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def add_news(self, news):
        self.__latest_news = news
    
    def get_news(self):
        return "Got News : ", self.__latest_news


if __name__ == "__main__":
    news_pub = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_pub)
    print("\nSubscribers : ", news_pub.subscribers())

    news_pub.add_news('hello world')
    news_pub.notify_subscribers()

    print("\nDetached: ", type(news_pub.detach()).__name__)
    print("\nSubscribers: ", news_pub.subscribers())

    news_pub.add_news('second news')
    news_pub.notify_subscribers()
