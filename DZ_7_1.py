# Пытался потом сделать с использованием Numpy, но не хватило времени разобраться (((
# Надеюсь, покажите как его можно было тут использовать

class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        new_array = []
        tmp_array = []
        for line, value in enumerate(self.array):
            for i, v in enumerate(value):
                tmp_array.append(self.array[line][i] + other.array[line][i])
            new_array.append(tmp_array.copy())
            tmp_array.clear()
        return new_array

    def __str__(self):
        for el in self.array:
            print(el)
        return ''
        # Вот тут не совсем понятно.
        # Требует возврата строки же?
        # А если я не хочу ничего возвращать, то как быть?


obj_matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
obj_matrix_2 = Matrix([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

obj_matrix_3 = Matrix(obj_matrix_1 + obj_matrix_2)

print('Матрица 1:')
print(obj_matrix_1)

print('Матрица 2:')
print(obj_matrix_2)

print('Матрица 1 + Матрица 2 = Матрица 3:')
print(obj_matrix_3)
