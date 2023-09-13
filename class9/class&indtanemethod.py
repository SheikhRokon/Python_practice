
class className:
    def instancemethod(self):
        print("class instance")
        
    @classmethod
    def classmethod(cls):
        print("class method ")
        
x = className()


x.instancemethod() 
# className.instancemethod() kaj kor be na 



x.classmethod()
className.classmethod()
          