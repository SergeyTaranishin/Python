class Complex_num:
    def __init__(self, a, b):
        self.volue = complex(a, b)

    def __add__(self, other):
        num_tmp = Complex_num(self.volue.real + other.volue.real, self.volue.imag + other.volue.imag)
        return num_tmp.volue

    def __mul__(self, other):
        num_tmp = Complex_num(self.volue.real * other.volue.real - self.volue.imag * other.volue.imag,
                             self.volue.imag * other.volue.real + self.volue.real * other.volue.imag)
        return num_tmp.volue


num1 = Complex_num(-5, 3)
num2 = Complex_num(4, 2)

print(f'A = {num1.volue}')
print(f'B = {num2.volue}')
print()
print(f'A + B = {num1 + num2}')
print(f'A * B = {num1 * num2}')
