def dd(prices): 
    cur_max = 0
    cur_min = -100
    dds = []
    predd = 0
    
    for idx,p in enumerate(prices):
        # print()
        # print(f"current price {p}")
        # print(f"pre price {pre_p}")
        if p >= cur_max:
            cur_max = p
            predd = 0
        elif p < cur_max:
            cur_min = p
            
        # print(f"current max {cur_max}")
        # print(f"current min {cur_min}")
        if p >= cur_min and p < cur_max:
            dd = cur_max - cur_min
            # print(f" in dd {cur_max - cur_min} predd {predd}")
            if dd > predd:
                # print(f"add dd {dd}")
                dds.append(dd)
                predd = dd
            else: 
                predd = dd
                dds.append(0)
        else:
            dds.append(0)
    
    return dds
        

def find_idx(dds):
    # find idx followed by a 0
    cur = -1
    next = -1
    idx = []
    for i in range(len(dds)-1):
        cur = dds[i]
        next = dds[i+1] 
        if next == 0 and cur != 0: 
            idx.append(cur)
        
    if dds[-1] != 0:
        idx.append(dds[-1])

    return idx

# Test
prices = [1, 2, 3, 4, 3, 2, 1, 2, 4, 3, 1]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)

prices = [1, 2, 3]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)

prices = [1, 2, 3, 2]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)

prices = [4,3,2,1,2,3,2]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)


prices = [4,3,2,1, 2, 3, 2, 1]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)


prices = [-1, 0, 1]
print("prices: ", prices)
res = dd(prices)
idx = find_idx(res)
print("Rolling dd: ", res)
print("DD:", idx)