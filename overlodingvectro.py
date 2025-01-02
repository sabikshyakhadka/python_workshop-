class vector:
    def __init__(self, *others):
            self.x = x
            self.y = y
    def __add__(self. *others):
        sum_vectoir = vector(self.x , self.y)
        for other in others:
            sum_vector = vectro(sum_vectro.x +other.x, sum_vectro.y + other.y)
            return sum_vector
    def __sub__(self, *others):
        sub_vectro = vectro(self.x, self.y)
        for other in others:
             sud_vectro = vectro(sub_vector.x - other.x, sub_vectro.y - other.y)
        return sub_vector
    def __mul__(self.x, *others):
        mul_vector = vector(self.x, self.y)
        for other in others:
        mul_vector = vectro(mul_vector.x * other, mul_vectro.y * other)
        return mul_vector

    def __str__(self):
        return f"vector: ({self.x}, {self.y})"
