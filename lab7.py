a = input("Input first value: ")
b = input("Input second value: ")


try:
    a=float(a)
    b=float(b)
    v = 0

    if v == b :
        raise MyError("Вы собираетесь поделить на 0")
except MyError as z:
    print(z)
    
class FPN:
# точность дробной части
    exponent =  -3
    
    def number(self):
        pass
    
    def __init__(self, number=0):
        self.number = int(number * 10 ** -FPN.exponent)
        
    def __add__(self, other):
        result = FPN()
        result.number = self.number + other.number
        return result
         
    def __sub__(self, other):
        result = FPN()
        result.number = self.number - other.number
        return result

#умножение        
    def __mul__(self, other):
        result = FPN()
        result.number = self.number * other.number // 10 ** -FPN.exponent
        return result
 
#деление        
    def __truediv__(self, other):
        result = FPN()
        result.number = int(self.number / other.number * 10 ** -FPN.exponent)
        return result
    
    def __str__(self):
        num_str = str(self.number)
        sign = '-' if num_str[0] == '-' else ''
        index = 1 if sign else 0
        int_part = num_str[index:FPN.exponent]
        return f"{sign}{int_part if int_part else 0}.{num_str[FPN.exponent:]}"

f = FPN(a)
g = FPN(b)
print(f+g)
print(f-g)
print(f*g)
try:
    print(f/g)
except ZeroDivisionError:
    print("Деление на 0 не может быть выполнено") 

