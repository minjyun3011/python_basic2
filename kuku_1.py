horizonal = int(input("行数を入力してください: "))
vertical = int(input("列数を入力してください: "))

for a in range(1, horizonal + 1):
    for b in range(1, vertical + 1):

        result = a * b
         
        print(result, end=' ')
    print()  # 行末で改行

