class Menu:
    """fill in class definition here"""
    def _init_(self):
        self.d=dict()
        
    def add(self,value,number):
        self.d[value] =number          
    def show(self):
        for i in self.d:
            print(i,self.d[i])
        

m = Menu()     # Menu is a class
m.add("idly", 10) 
m.add("vada", 20)
m.show()