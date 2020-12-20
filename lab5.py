class FPN:
# точность дробной части
    exponent = -6 
    
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

#предотвращение ошибок вывода знака и целой части    
    def __str__(self):
        num_str = str(self.number)
        sign = '-' if num_str[0] == '-' else ''
        index = 1 if sign else 0
        int_part = num_str[index:FPN.exponent]
        return f"{sign}{int_part if int_part else 0}.{num_str[FPN.exponent:]}"

f = FPN(10)
g = FPN(1.23)
print(f+g)
print(f-g)
print(f*g)
print(f/g)

