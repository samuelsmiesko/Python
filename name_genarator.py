import random 

vowels = ['e','u','i','o','a','y']
consonants = ['q','w','r','t','z','p','s','d','f','g','h','j','k','l','x','c','v','b','n','m']
name = []

class names:
    def __init__(self, letter,lenght,sufix):
        self.letter = letter
        self.lenght = lenght
        self.sufix = sufix



    def result(self):
        x = range(20)
        for n in x:
        
          name.append(self.letter)
          x = range((self.lenght)-1-(len(self.sufix)))
          for n in x:
          
              if name[-1] in vowels:
                  a = random.choice(consonants)
                  name.append(a)
                                          
              elif name[-1] in consonants:
                  
                  a=random.choice(vowels)
                  name.append(a)              

              else:
                  print("only letters are allowed")

          final = ''
          a = final.join(name)
          if len(self.sufix) < 1:
              print(a)
          else:    
              b = str(a + self.sufix)
              print(b)
          
          name.clear() 
        
                 
if __name__ == "__main__":        
  
    x = names(input("input first letter "),int(input("input leght of the word ")),input("Input optional -sufix "))
    x.result()

