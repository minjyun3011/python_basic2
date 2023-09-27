horizontal = int(input("行数を入力してください: "))
vertical = int(input("列数を入力してください: "))

for i in range(1, 10):
    for j in range(1, vertical + 1):
        result = i * j
        print(f'{i} x {j} = {result:2d} |', end=' ')
    print()
