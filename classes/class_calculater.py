
class simple_oper:
    def __init__(self):
        pass
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        return num1 / num2
def get_int(input_message, tm):
    num = input(input_message)
    try:
        return int(num)
    except:
        return get_int(tm, tm)

num1 = get_int("Please enter the first number : ", "Please enter the correct number : ")
l = ["+", "-", "*", "/"]
c = simple_oper
while True:
    oper = str(input("Please enter the operand to do : "))
    if oper == "=":
        print("You typed = print result")
        break
    elif oper not in l:
        print("Ypu typed incorrect operand. aborting and printing result")
        break
    num2 = get_int("please enter the number : ", "please enter the correct number")
    if oper == "+":
        num1 = simple_oper.add(c, num1, num2)
    if oper == "-":
        num1 = simple_oper.subtract(c, num1, num2)
    if oper == "*":
        num1 = simple_oper.mul(c, num1, num2)
    if oper == "/":
        num1 = simple_oper.div(c, num1, num2)
print(num1)
