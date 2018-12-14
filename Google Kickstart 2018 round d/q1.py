import sys

if __name__ == '__main__':
    tests = int(input().rstrip())
    for i in range(1, tests + 1):
        num_candies, odd, level = map(int, input().rstrip().split())
        x1, x2, A, B, C, M, L = map(int, input().rstrip().split())
        x_num = []
        x_num.append(x1)
        x_num.append(x2)
        candies = []
        for a in range(num_candies):
            if a >= 2:
                x_num.append((x_num[a - 1] * A + x_num[a-2] * B + C) % M)
            candies.append(x_num[a] + L)
        r_index = 0
        result = None
        for a in range(num_candies):   
            if a >= r_index:
                r_index = a
                odd_counter = 0 if candies[r_index] % 2 == 0 else 1
                count = candies[r_index]
            else:
                if a > 0:
                    if candies[a - 1] % 2 == 1:
                        odd_counter -= 1
                    count -= candies[a - 1]
            if count <= level and odd_counter <= odd:
                if result is not None:
                    result = max(count, result)
                else:
                    result = count
            while r_index + 1 < num_candies:
                res_odd = candies[r_index + 1] % 2
                res_count = candies[r_index + 1]
                if odd_counter + res_odd <= odd and count + res_count <= level:
                    r_index += 1
                    count += res_count
                    odd_counter += res_odd
                    if result is not None:
                        result = max(result, count)
                    else:
                        result = count
                else:
                    break
        if result is None:
            result = 'IMPOSSIBLE'
        print('Case #{0}: {1}'.format(i, result))


            
            