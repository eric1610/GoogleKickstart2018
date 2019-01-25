if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        size, p = map(int, input().split())
        blacklist = set()
        p_set = set()
        for _ in range(p):
            p_set.add(input())
        res = 1 << size
        for a in p_set:
            for b in p_set:
                if a == b: 
                    continue
                elif len(a) <= len(b) and a == b[:len(a)]:
                    blacklist.add(b)
        p_set = p_set - blacklist
        for x in p_set:
            i_size = len(x)
            res -= 1 if i_size == size else 1 << (size - i_size)
        if res < 0:
            res = 0
        print('Case #{0}: {1}'.format(str(i), str(res)))