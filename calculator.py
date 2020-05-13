class numbers:
  def __init__(self, num1,opr ,num2):
    self.number1 = num1
    self.operation = opr
    self.number2 = num2
    

  def printname(self):
    print(self.number1, self.operation ,self.number2)

  def result(self):
    if self.operation == "+":
      
      self.number1 = float(self.number1) + float(self.number2) 
      print(self.number1)
      
      
    elif self.operation == "-":
      print(float(self.number1) - float(self.number2))
    elif self.operation == "*":
      print(float(self.number1) * float(self.number2))
    elif self.operation == "/":
      try:
        print(float(self.number1) / float(self.number2))
      except:
        print("division by zero")
    else:
      return

    x = numbers(self.number1,input("input operation (+, -, *, /) "),input("input second number "))      
    x.printname()

    def repeat():
     
       x.result()
    repeat()

x = numbers(input("input first number "),input("input operation (+, -, *, /) "),input("input second number "))  
x.printname()
x.result()



  
  



    
