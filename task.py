with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    f1 = []
    f2 = []
    f3 = []
    for l in file1:
        f1.append(int(l))
    # print(f1)
    for i in file2:
        f2.append(int(i))
    # print(f2)

    # intersection = set(f1) & set(f2)
    # f3 = list(intersection)
    # print(f3)

    for l in f1:
        for i in f2:
            if l == i:
                f3.append(l)
    print(f3)


with open('file1.txt') as file1, open('file2.txt') as file2:
    f1 = [int(line) for line in file1]
    f2 = [int(line) for line in file2]

    f3 = [x for x in f1 for y in f2 if x == y]

    print(f3)
    
# 'как еще можно открывать файлы'
# with open("file1.txt") as f1, open("file2.txt") as f2: # Если нужно читать строки параллельно:
#     for line1, line2 in zip(f1, f2):
#         print(line1.strip(), line2.strip())

# with open("input.txt", "r") as inp, open("output.txt", "w") as out: # Можно открывать файлы в разных режимах
#     out.write(inp.read())

