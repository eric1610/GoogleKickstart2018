
test_case = int(input())
for i in range(1, test_case + 1):
    size = int(input())
    num = list(map(int, input().split()))
    num.sort()
    counter = 0
    zero_counter = 0

        
        
    bucket = {}
    bucket[str(num[size - 1])] = 1

    for a in range(size - 2, -1, -1):
        if num[a] == 0:
            zero_counter += 1
        else:
            for b in range(a - 1, -1, -1):
                if num[b] > 0:
                    if str(num[a] * num[b]) in bucket:
                        counter += bucket[str(num[a] * num[b])]
            if str(num[a]) in bucket:
                bucket[str(num[a])] += 1
            else:
                bucket[str(num[a])] = 1

    counter = counter + (((zero_counter) * (zero_counter - 1) * (zero_counter - 2)) / 6) + (((zero_counter) * (zero_counter - 1)) / 2 * (size - zero_counter))
    print ("Case #" + str(i) + ": " + str(int(counter))) 
    