import os
def IfFunc(inputvar, ifstatement, functionzz):
    """
    If Var1 == Var2 run function Var3
    """
    if inputvar == ifstatement:
        functionzz()

def clear():
    """
    Just runs os.system('clear'). Fast doe
    """
    os.system('clear')

def IfNotFunc(inputvar, ifstatement, function):
    """
    if Var1 != Var2 run function Var3()
    """
    if inputvar != (ifstatement):
        function()
