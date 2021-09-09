class VariableObject(object):
    def __init__(self):
        self.exec_string = ""

    def transpile(self,name,Opearator,value):
        self.exec_string += name + " " + Opearator + " " + value + "\n"
        return self.exec_string