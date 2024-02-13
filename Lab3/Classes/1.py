class STRR:
    def __init__(self):
        self.instr = ""

    def getString(self):
        self.instr = input()

    def printString(self):
        print(self.instr.upper())   



x = STRR()
x.getString()
x.printString()
