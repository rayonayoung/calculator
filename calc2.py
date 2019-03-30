#!C:/Users/young/AppData/Local/Programs/Python/Python37-32/python.exe
import cgi
print("Content-Type: text/html\n")
print("Rayona Young<br>Assignment 5: Calc.py<br><br>")
def getInput():
    f = cgi.FieldStorage()
    num1 = int(f.getvalue('num1', default='0'))
    num2 = int(f.getvalue('num2', default='0'))
    op = f.getvalue('op', default='add')

    return num1, num2, op

num1, num2, op = getInput()

def calcResults (num1,num2,op):

    if op == 'add':

        res = num1 + num2

    elif op == 'subtract':

        res = num1 - num2

    elif op == 'multiply':

        res = num1 * num2

    elif op == 'divide':

        res = num1 / num2

    else:

        raise Exception ("Invalid operation")

    return res

res = calcResults(num1,num2,op)

out = '''
Number1: {} <br>
Number2: {} <br>
Operation: {} <br>
Result: {} <br>
'''.format(num1, num2, op, res)
print(out)






