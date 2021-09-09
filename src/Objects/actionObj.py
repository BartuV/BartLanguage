class Function(object):
    def __init__(self,tokens):
        self.tokens = tokens
    
    def run(self):
        for i in self.tokens:
            if i[0] == "FUNCTION_STATMENT":
                name = i[1]
                print(name)