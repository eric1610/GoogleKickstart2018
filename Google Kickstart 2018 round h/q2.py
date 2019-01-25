if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        num, arr = int(input()), input()
        amount = num
        if num % 2 == 1:
            amount += 1 
        amount = amount // 2
        arr_int = [int(x) for x in arr]
        max_amount = sum(arr_int[:amount])
        curr_max = max_amount
        for index in range(amount, num):
            curr_max = curr_max - arr_int[index - amount] + arr_int[index]
            if curr_max > max_amount:
                max_amount = curr_max
        print(f'Case #{i}: {max_amount}')