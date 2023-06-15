class MyClass:
  def __init__(self, value):
      self._value = value
  
  
  def show(self):
     print(f"value is {self._value}")

  @property                      #getter - to get the value
  def ten_value(self):           
     
     
     return self._value * 10
  
  @ten_value.setter             #setter - to set the value
  def ten_value(self,new_value):
     self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67              #setter
print(obj.ten_value)            #getter
obj.show()

     
    

         