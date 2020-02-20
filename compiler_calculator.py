#...............
#...............
#...............
#@Alireza_sarami
#@9521170016
#@Compiler_Calculator
#...............
#...............
#...............
from enum import Enum
from collections import namedtuple

class Type(Enum):
    ID = 1
    EQUAL = 2 #=
    number = 3
    LPAR = 4 #(
    RPAR = 5 #)
    STAR = 6 #*
    PLUS = 7 #+
    MINUS = 8 # -
    DIVIDE = 9 #/
    SPACE = 10
    NEWLINE = 11 #/n \n is syntax in string and i can't to programming on it and i replaced it with /n
# class Token :
#     def __init__(self,Type,Value):
#         self.Type = Type
#         self.Value = Value

buffer = ['c','a','b','/n','1','.','2','(','1',')','+','*','-','/','d','$']
# buffer = ['/n']
index = 0
lToken = []
def getToken(buffer):
    Token = namedtuple("Token", "Type Value")
    i = index
    j = 0
    state = 0
    alpha=""
    digit=""
    while i < len(buffer):
        flag = 0
        if(state==0):
            if(buffer[i].isalpha()):
                state = 10

            elif(buffer[i].isdigit()):
                state = 20

            elif(buffer[i]==')'):
                state = 30

            elif(buffer[i] == '('):
                state = 40

            elif(buffer[i] == '*'):
                state = 50

            elif (buffer[i] == '+'):
                state = 60

            elif (buffer[i] == '-'):
                state = 70

            elif (buffer[i] == '/'):
                state = 80

            elif (buffer[i] == '='):
                state = 90

            elif(buffer[i] == '/n'):
                state = 100

            else:
                state = 0
                print("state 0 = error in input")

            if(buffer[i] == '$'):
                print("Completed :)")
                i = len(buffer)

        elif(state==10):
            if(buffer[i].isalpha()):
                state = 10
                alpha += buffer[i]
                i += 1

            elif(buffer[i].isdigit()):
                state = 10
                alpha += buffer[i]
                i += 1
            elif(buffer[i]=='_'):
                state = 10
                alpha += buffer[i]
                i += 1
            else:
                print("Token alpha created!")
                t = Token(Type.ID, alpha)
                flag = 1
                state = 0
                alpha = ""
                print("state 10 = Is Error or go to State 0")
        elif(state==20):
            if(buffer[i].isdigit()):
                state = 20
                digit += buffer[i]
                i += 1
            elif(buffer[i]=='.'):
                state = 21
                digit += buffer[i]
                i += 1
                print('.')
            else:
                print("Token number created!")
                t = Token(Type.number,digit)
                flag = 1
                state = 0
                digit = ""
                print("state 20 = Is Error or go to State 0")

        elif(state==21):
            if (buffer[i].isdigit()):
                state = 22
                digit += buffer[i]
                i += 1
            else:
                print("Token number created!")
                t = Token(Type.number, digit)
                flag = 1
                state = 0
                digit = ""
                print("state 21 = Is Error or go to State 0")

        elif(state==22):
            if(buffer[i].isdigit()):
                state = 22
                digit += buffer[i]
                i += 1
            else:
                print("Token number created!")
                t = Token(Type.number, digit)
                flag = 1
                state = 0
                digit = ""
                print("state 22 = Is Error or go to State 0")

        elif(state==30):
            if(buffer[i]==')'):
                state = 30
                i += 1
                print("Token RPAR created!")
                t = Token(Type.RPAR,"")
                flag = 1
            else:
                state = 0
                print("state 30 = Is Error or go to State 0")

        elif (state == 40):
            if (buffer[i] == '('):
                state = 40
                i += 1
                print("Token LPAR created!")
                t = Token(Type.LPAR, "")
                flag = 1
            else:
                state = 0
                print("state 40 = Is Error or go to State 0")

        elif (state == 50):
            if (buffer[i] == '*'):
                state = 50
                i += 1
                print("Token STAR created!")
                t = Token(Type.STAR, "")
                flag = 1
            else:
                state = 0
                print("state 50 = Is Error or go to State 0")

        elif (state == 60):
            if (buffer[i] == '+'):
                state = 60
                i += 1
                print("Token PLUS created!")
                t = Token(Type.PLUS, "")
                flag = 1
            else:
                state = 0
                print("state 60 = Is Error or go to State 0")

        elif (state == 70):
            if (buffer[i] == '-'):
                state = 70
                i += 1
                print("Token MINUS created!")
                t = Token(Type.MINUS, "")
                flag = 1
            else:
                state = 0
                print("state 70 = Is Error or go to State 0")

        elif (state == 80):
            if (buffer[i] == '/'):
                state = 80
                i += 1
                print("Token DIVIDE created!")
                t = Token(Type.DIVIDE, "")
                flag = 1
            else:
                state = 0
                print("state 80 = Is Error or go to State 0")

        elif (buffer[i].isspace()):
            print("Token SPACE created!")
            t = Token(Type.SPACE,"")
            flag = 1
            i += 1

        elif (state == 90):
            if(buffer[i]=='='):
                state = 90
                i += 1
                print("Token EQUAL created!")
                t = Token(Type.EQUAL, "")
                flag = 1
            else:
                state = 0

        elif(state == 100):
            if (buffer[i] == '/n'):
                print("Token NEWLINE created!")
                t = Token(Type.NEWLINE, "")
                flag = 1
                state = 0
                i += 1
                state = 100
            else:
                state = 0

        else:
            state = 0
            print("Is Error or go to State 0")


        if(flag==1):
            # print(t.Type._name_)
            lToken.append(t.Type._name_)
            lToken.append(t.Value)
try:
    getToken(buffer)

    while(index<len(lToken)):
        print('---------')
        print(f"|{lToken[index]}|")
        print('---------')
        index += 1
        print(f"{lToken[index]}")
        index += 1
        print('\t')
except:
    print('Error')