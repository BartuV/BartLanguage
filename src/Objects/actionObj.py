class Function(object):
    def __init__(self,tokens):
        self.tokens = tokens
        self.funcnames = []
    
    def run(self):
        for i in self.tokens:
            if i[0] == "FUNCTION_STATMENT":
                name = i[1]
                variables =[]
                namelist = []
                while True:
                    if name[len(name)-1] == ")":
                        for v in name:
                            namelist.append(v)
                    if "(" in namelist:
                        varstartindex = namelist.index("(")
                        num = 1
                        a = namelist[varstartindex+num]
                        num = num + 1
                        print(a)
                    quit() 