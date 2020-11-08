from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class Samgsung(Base):
    def create(self):
        print(f"this is a Samgsung phone. {id(self)}")
        return self

class AppleIPhone(Base):
    def create(self):
        print(f"this is an Apple iphone. {id(self)}")
        return self

class Factory:
    def create_type(self, type):
        return {
          'iphone': AppleIPhone(),
          'samgsung': Samgsung(),
        }[type].create()