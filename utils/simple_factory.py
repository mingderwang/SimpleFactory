from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def show(self):
        pass

class Samsung(Phone):
    def show(self):
        print(f"This is a Samsung phone with ID: {id(self)}")
        

class AppleIPhone(Phone):
    def show(self):
        print(f"This is an Apple iphone with ID: {id(self)}")

class PhoneFactory:
    @classmethod
    def create_type(self, type):
        return {
          'iphone': AppleIPhone(),
          'samsung': Samsung(),
        }[type]