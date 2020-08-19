class calculator():

    def __init__(self):
        self.result =0

    def add(self,x):
        self.result +=x
        return self
    def substract(self,x):
        self.result -=x
        return self
    def out(self):
        return self.result

result = calculator().add(4).add(5).substract(3).out()
print(result)

