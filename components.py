class Component():
    def __init__(self,name):
        self.name = name
        self.value = 0 
        self.unit = ""

        self.high = None
        self.low = None

    def __str__(self):
        return f"{self.value} {self.unit}"
#-------------------------------------------------
class Resistance(Component):
    def __init__(self,value):
        self.name = "resistance"
        self.value = value 
        self.unit = "ohm"


        self.positive_voltage = 0
        self.negative_voltage = 0


    def calculate_voltage(self,current):
        self.positive_voltage = self.high.voltage
        self.negative_voltage = self.positive_voltage - current * self.value
#-------------------------------------------------
class Point():
    def __init__(self,label):
        self.connects = []
        self.voltage = 0
        self.label = label

    def conncet_to(self,component,where):
        self.connects.append(component)
        if(where):
            component.high = self
        else:
            component.low = self  

    def calculate_voltage(self):
        for component in self.connects:
            if(component.name == "source" and component.high.label == self.label): 
                self.voltage = component.value
                return
            if(component.name == "resistance" and component.low.label == self.label):
                self.voltage = component.negative_voltage

    def __str__(self):
        return f"{self.label}"
#-------------------------------------------------
class VoltageSource(Component):
    def __init__(self,value):
        self.name = "source"
        self.value = value 
        self.unit = "voltage"
#-------------------------------------------------
class Circuit():
    def __init__(self):
        self.components = []
#-------------------------------------------------
my_res = Resistance(2)
my_source = VoltageSource(10)

point1 = Point("p1")
point1.conncet_to(my_source,True)
point1.conncet_to(my_res,True)

point2 = Point("p2")
point2.conncet_to(my_source,False)
point2.conncet_to(my_res,False)


point1.calculate_voltage()
my_res.calculate_voltage(5)
point2.calculate_voltage()
print(point1.voltage)
print(point2.voltage)

# print(my_res)
# print(my_source)