from Objects.varObj import VariableObject
from Objects.actionObj import Function

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.token_index = 0
        self.tranpiled_code = ""
        self.functionnums = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type  = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == "FUNCTION_STATMENT" and token_value == "action":
                if self.functionnums < 1:
                    self.functionnums += 1
                    ind = self.tokens.index(["FUNCTION_STATMENT",token_value])
                    name = self.tokens[ind+1][1]
                    self.tokens[ind][1] = name
                    actionobj = Function(self.tokens)
                    actionobj.run()
                else:
                    return

            if token_type == "PRINT_STATMENT":
                print("print")
                if token_value in self.tranpiled_code.split():
                    index = self.tranpiled_code.split().index(token_value)
                    print(self.tranpiled_code.split()[index + 2])
                else:
                    print(token_value)

            if token_type == "VAR_DECLERATION" and token_value == "var":
                self.parse_variable_decleration(self.tokens[self.token_index:len(self.tokens)])

            self.token_index += 1
    
    def parse_variable_decleration(self,token_stream):
        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        for token in range(0,len(token_stream)):
            token_type  = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if token == 4 and token_type == "STATMENT_END": break

            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: Invalid Variable Name '"+token_value+"'")
                quit()
            elif token == 2 and token_type == "OPERATOR":
                operator = token_value
            elif token == 1 and token_type != "OPERATOR":
                print("Assignment Opearator is missing or invalid. it should be '='")
            elif token == 3 and token_type in ["STRING","INTEGER","IDENTIFIER"]:
                value = token_value
            elif token == 3 and token_type not in ["STRING","INTEGER","IDENTIFIER"]:
                print("Invalid Variable assignment value'" + token_value+"'")
                quit()

            tokens_checked += 1
        
        varobj = VariableObject()
        self.tranpiled_code += varobj.transpile(name, operator, value)
        self.token_index += tokens_checked