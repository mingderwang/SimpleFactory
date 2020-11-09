from utils.simple_factory import PhoneFactory

class App:
  def main():
    工廠 = PhoneFactory()
    phone1 = 工廠.create_type('samsung')
    phone2 = 工廠.create_type('iphone')
    phone1.show()
    phone2.show()

App.main()