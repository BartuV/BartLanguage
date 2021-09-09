import re

class Lexer:
    def __init__(self,code):
        self.code = code

    def tokenize(self):
        self.tokens = []
        tokens = self.tokens
        source_code = self.code.split()
        
        source_index = 0

        while source_index < len(source_code):
            word = source_code[source_index]

            if word == "var": 
                tokens.append(["VAR_DECLERATION",word])

            elif re.match("[a-z]", word) or re.match("[A-Z]", word):
                if word[len(word)-1] == ";":
                    tokens.append(["IDENTIFIER",word[0:len(word)-1]]) 
                elif word == "action":
                    tokens.append(["FUNCTION_STATMENT",word])
                elif word == "end" or word == "END": 
                    tokens.append(["STATMENT_END",word])
                else:
                    tokens.append(["IDENTIFIER",word]) 
            #burada sayıları kontrol ediyoruz
            elif re.match("[0-9]",word):
                if word[len(word)-1] == ";":
                    tokens.append(["INTEGER",word[0:len(word)-1]])
                else:
                    tokens.append(["INTEGER",word])
            elif word in "/*-+=": tokens.append(["OPERATOR",word])

            if word[len(word)-1] == ";":
                tokens.append(["STATMENT_END",";"])
            if word[0:6] == "print(" and word[len(word)-2]==")":
                tokens.append(["PRINT_STATMENT",word[6:len(word)-2]])
            source_index += 1
        return tokens