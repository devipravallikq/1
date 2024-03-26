class F15:
    def light(self):
        print("ok switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
chandu=F15()
chandu.light()
chandu.fan(5)
chandu.cpu()


class shopping(F15):
    def __init__(self,place):
        self.place=place
        print("welcome to shopping at",place)
    def dresstype(self,type):
        self.t=type 
    def price(self,pr):
        self.p=pr
    def size(self,si):
        self.s=si 
    def dispaly(self,):
        print("the dress is",self.t)
        print("the price is",self.p)
        print("the size is",self.s)
john=shopping("srmt")
john.dresstype("shirt")
john.price(2500)
john.size("XL")
john.dispaly()
john.light()
john.fan(5)
john.cpu()
