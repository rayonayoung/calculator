#!C:/Users/young/AppData/Local/Programs/Python/Python37-32/python.exe
import cgi
print("Content-Type: text/html\n")

print("Rayona Young<br>Assignment 5: Calc.py<br><br>")



def dispForm():
    print('''
        <form action='calc2.py' method='get'>
        Number1 <input type='text' name='num1'><br>
        Number2 <input type='text' name='num2'><br>
        Available Operations:<br>
        <input type='radio' name='op' value='add' checked='true' />Add
        <input type='radio' name='op' value='subtract' />Sub
        <input type='radio' name='op' value='multiply' />Mult
        <input type='radio' name='op' value='divide' />Div<br><br>
        <input type='submit' name='submit' value='Submit'><br><br>
        </form>             
        ''')
dispForm()


