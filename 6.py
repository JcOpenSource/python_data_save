file = open('1.txt', 'r')

while True:
    line = file.readline()
    if line == '':
        break
    print(line)
