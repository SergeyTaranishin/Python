n = input('Введите целое положительное число: ')
i = 1
cifra_max = 0
while i < 10:
    if str(i) in n:
        if i > cifra_max:
            cifra_max = i
    i = i + 1

print('самая большая цифра в числе:', cifra_max)