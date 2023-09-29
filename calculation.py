def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_max(numbers):
    max_value = float('-inf')
    for i in numbers:
        if i > max_value:
            max_value = i
    return max_value


def calculate_min(numbers):
    min_value = float('inf')
    for i in numbers:
        if i < min_value:
            min_value = i
    return min_value


def calculate_av(numbers):
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def main():
    input_data = input("データを入力してください(スペース区切り) > ")
    input_numbers = [int(x) for x in input_data.split()]
    
    if len(input_numbers) == 0:
        print("データがありません。")
        return

    # 統計量の計算と表示
    print(f"合計値: {calculate_sum(input_numbers)}")
    print(f"最大値: {calculate_max(input_numbers)}")
    print(f"最小値: {calculate_min(input_numbers)}")
    print(f"平均値: {calculate_av(input_numbers):.2f}")

if __name__ == "__main__":
    main()
