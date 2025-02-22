class uk ():
    def Capital(self):
        print("London is the capital of England")
    def language(self):
        print("English is the most widely spoken language")
    def type (self):
        print("Uk is a high income country")

class Usa ():
    def Capital(self):
        print("Washington DC is the capital of England")
    def language(self):
        print("English is the primary spoken language")
    def type (self):
        print("Usa is a developed country")
obj1 = uk()
obj2 = Usa()
for c in (obj1,obj2):
    c.Capital()
    c.language()
    c.type()