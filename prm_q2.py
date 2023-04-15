class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate_triangle(self):
        
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            return "Valid Triangle"
        else:
            return "Invalid triangle"
            
        
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def validate_rectangle(self):
        
        if self.l == self.b:
            return "Invalid rectangle"
        elif self.l > self.b:
            if self.l == 2*self.b:
                return "Valid Rectangle"
            else:
                return "Invalid rectangle"
        else:
            if self.b == 2*self.l:
                return "Valid Rectangle"
            else:
                return "Invalid rectangle"
