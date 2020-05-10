class calculator:
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
        def get_int(self, input_message, tm):
            num = input(input_message)
            try:
                return int(num)
            except:
                return get_int(c, self, input_message, tm)
    l = ["+", "*", "/", "-"]
    c = simple_oper
    n1 = simple_oper.get_int(c, "Please the first number to start the calculation", "Please enter the correct number")
    
