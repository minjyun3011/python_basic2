horizontal = int(input("行数を入力してください: "))
vertical = int(input("列数を入力してください: "))

# 九九の表を生成する際の最大値を計算
max_value = horizontal * vertical

# 九九の表の最大値の桁数を計算
max_digits = len(str(max_value))

for i in range(1, horizontal + 1):
    for j in range(1, vertical + 1):
        result = i * j
        spacing = 3 - max_digits
        # 空白を使って均等な間隔で表示
        print(f'{result:{max_digits}}', end=' '*spacing)
    print()  # 行末で改行
