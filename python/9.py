class calculator:
    def __init__ (self,name,price,hight,width,weigth):
        self.name = name
        self.price = price
        self.hight = hight
        self.width = width
        self.weigth = weigth
    def add(self,x,y):
        print(x+y)
    def minus(self,x,y):
        print(x-y)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)