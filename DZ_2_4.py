line = input('Введите текст разделенный пробелами: ')
line = line.split()
count = len(line)
i = 0
while i < count:
    print(f'{i+1}: {line[i][0:10] }')
    i += 1
