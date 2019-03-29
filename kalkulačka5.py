from tkinter import *


cislo = []
cisla = [0]

znamienko = []
class Calculator:

         
    def n1(self):
        
        cislo.append(str(1))                      
        self.screen.insert(END,1)
        
    def n2(self):
        
        cislo.append(str(2))                      
        self.screen.insert(END,2)
        
    def n3(self):
        
        cislo.append(str(3))                      
        self.screen.insert(END,3)
        
    def n4(self):
        
        cislo.append(str(4))                     
        self.screen.insert(END,4)

    def n5(self):
        
        cislo.append(str(5))                   
        self.screen.insert(END,5)

    def n6(self):
        
        cislo.append(str(6))                    
        self.screen.insert(END,6)

    def n7(self):
        
        cislo.append(str(7))                       
        self.screen.insert(END,7)

    def n8(self):
        
        cislo.append(str(8))                       
        self.screen.insert(END,8)
        
    def n9(self):
        
        cislo.append(str(9))                       
        self.screen.insert(END,9)

    def n0(self):
        
        cislo.append(str(0))                       
        self.screen.insert(END,0)

    def ndot(self):
        
        cislo.append(str("."))                       
        self.screen.insert(END,".")

    def minus(self):
        if len(cislo) < 1:
                     
            
            cislo.append(("-"))
                                      
            self.screen.insert(END, " - ")
            znamienko.append("-")

        else:
            b = "".join(cislo)        
            del cislo[:]            
            result1=(self.screen.get("1.0",END))               
            a = (result1.replace("x","*")).replace(" ","")
            result = eval(a)
            self.screen1.delete('1.0', END)
            self.screen1.insert(END, result)
            cislo.append(("-"))
            cisla.append(float(b))                           
            self.screen.insert(END, " - ")
            znamienko.append("-")
                       
    def plus(self):
           
            b = "".join(cislo)
            
            del cislo[:]
            result=(self.screen.get("1.0",END))               
            a = (result.replace("x","*")).replace(" ","")
            result = eval(a)
            self.screen1.delete('1.0', END)
            self.screen1.insert(END, result)
            cisla.append(float(b))                           
            self.screen.insert(END, " + ")
            

    def krat(self):

        
            b = "".join(cislo)
            
            del cislo[:]            
            result=(self.screen.get("1.0",END))               
            a = (result.replace("x","*")).replace(" ","")        
            self.screen1.delete('1.0', END)
            self.screen1.insert(END, b)
            cisla.append(float(b))                           
            self.screen.insert(END, " x ")
                   

    def clear(self):
                               
            del cislo[:]
            del cisla[:]
            self.screen1.delete('1.0', END)
            self.screen.delete('1.0', END)

    def rovna(self):

           result=(self.screen.get("1.0",END))               
           a = (result.replace("x","*")).replace(" ","")
           b = eval(a)
           self.screen1.delete('1.0', END)
           self.screen1.insert(END, b)
            
        
    def __init__(self, master=None):
        self.master = master
        master.title("Kalkulačka")

        self.l1=Label(master, text="Čísla",font=("Arial Bold", 15),padx=15, pady=5)
        self.l1.grid(row=0,column=0)
        self.l2=Label(master, text="Výsledok",font=("Arial Bold", 15),padx=15, pady=5)
        self.l2.grid(row=1,column=0)
  
        self.screen = Text(master, state='disabled', width=25, height=2,background="white", foreground="blue",font=("Helvetica", 15))
        self.screen.grid(row=0,column=1,columnspan=4,padx=5,pady=5)
        self.screen1 = Text(master, state='disabled', width=25, height=2,background="white", foreground="blue",font=("Helvetica", 15))
        self.screen1.grid(row=1,column=1,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')
        self.screen1.configure(state='normal')
        self.b1 =Button(master, text=" 1", command = self.n1,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )        
        self.b1.grid(row=3,column=1,padx=5,pady=5)
       
        self.b2 =Button(master, text=" 2", command = self.n2,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b2.grid(row=3,column=2,padx=5,pady=5)
        self.b3 =Button(master, text=" 3", command = self.n3,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b3.grid(row=3,column=3,padx=5,pady=5)
        self.b4 =Button(master, text=" 4", command = self.n4,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b4.grid(row=4,column=1,padx=5,pady=5)
        self.b5 =Button(master, text=" 5", command = self.n5,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b5.grid(row=4,column=2,padx=5,pady=5)
        self.b6 =Button(master, text=" 6", command = self.n6,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b6.grid(row=4,column=3,padx=5,pady=5)
        self.b7 =Button(master, text=" 7", command = self.n7,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b7.grid(row=5,column=1,padx=5,pady=5)
        self.b8 =Button(master, text=" 8", command = self.n8,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b8.grid(row=5,column=2,padx=5,pady=5)
        self.b9 =Button(master, text=" 9", command = self.n9,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b9.grid(row=5,column=3,padx=5,pady=5)
        self.b0 =Button(master, text=" 0", command = self.n0,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b0.grid(row=6,column=2,padx=5,pady=5)
        self.b0 =Button(master, text=" =", command = self.rovna,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.b0.grid(row=6,column=3,padx=5,pady=5)
        self.bdot =Button(master, text=" .", command = self.ndot,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.bdot.grid(row=6,column=1,padx=5,pady=5)
        self.bplus =Button(master, text=" +", command = self.plus,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.bplus.grid(row=5,column=4,padx=5,pady=5)
        self.bminus =Button(master, text=" -", command = self.minus,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.bminus.grid(row=4,column=4,padx=5,pady=5)
        self.bkrat =Button(master, text=" *", command = self.krat,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.bkrat.grid(row=3,column=4,padx=5,pady=5)
        self.bc =Button(master, text=" C", command = self.clear,  borderwidth=4, font="helvetica 12", padx=15, pady=15 )
        self.bc.grid(row=6,column=4,padx=5,pady=5)
        
        self.equation = ''

        self.b1.bind('<Button-1>', lambda n1: n1)

def main():
    root = Tk()
    my_gui = Calculator(root)
    
    root.mainloop()
           

if __name__ == '__main__':
    main()
