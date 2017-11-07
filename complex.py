
class Complex:

    #Konstruktor
    def __init__(self,r,i):
        self.real=r
        self.imag=i
        
    #Sprzezenie
    def conjugate(self):
        self.imag=-self.imag
    
    def printComplex(self):
        print(self.real," ",self.imag,"*j")
    
    def __add__(self,rhs):
        return Complex(self.real+rhs.real, self.imag+rhs.imag)

    def __sub__(self,rhs):
        return Complex(self.real-rhs.real,self.imag-rhs.imag)
    
    def __mul__(self,rhs):
        return Complex(self.real*rhs.real-self.imag*rhs.imag,self.real*rhs.imag+self.imag*rhs.real)

    def __div__(self,rhs):
        return Complex((self.real*rhs.real+self.imag*rhs.imag)/(rhs.real*rhs.real+rhs.imag*rhs.imag),(self.imag*rhs.real-self.real*rhs.imag)/(rhs.real*rhs.real+rhs.imag*rhs.imag))
    
    #Modul liczby zespolonej
    def mod(self):
        self.real=pow(self.real*self.real,0.5)
        self.imag=pow(self.imag*self.imag,0.5)




    

zespolona1=Complex(2,3)
zespolona1.printComplex()
zespolona1.conjugate()
zespolona1.printComplex()
zespolona2=Complex(4,-7)
zespolona1=zespolona1*zespolona2
zespolona1.printComplex()
zespolona1.mod()
zespolona1.printComplex()
