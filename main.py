from factory import Factory

class App:
  def main():
    工廠 = Factory()
    iphone1 = 工廠.create_type('iphone')
    iphone2 = 工廠.create_type('iphone')
    if (iphone1 == iphone2):
      print('same phone')
    else:
      print("different ones")


App.main()