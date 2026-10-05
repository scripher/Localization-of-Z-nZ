# 用Z/nZ中的x生成一个乘性子集
def mult_set_gen(n, x):
    if (x == 0):
        print("Nilpotent Error!")
        return -1
    ans = [1, x]
    temp = (x * x) % n
    while (temp not in ans):
        if (temp == 0):
            print("Nilpotent Error!")
            return -1
        else:
            ans.append(temp)
            temp = (temp * x) % n
    return ans

# 获取零因子
def get_zero_div(n, mult):
    ans = [0]
    size = len(mult)
    for i in range(1, n):
        for j in range(0, size):
            if ((i * mult[j]) % n == 0):
                ans.append(i)
                break
    return ans

# 比较x和y两个分数是否相等，中间加一个n^2是为了让整体变正，防止取余出问题
def compare(n, x, y, zero):
    if (((x[0] * y[1] + n * n - x[1] * y[0]) % n) in zero):
        return True
    else:
        return False

# 计算Z/nZ在x生成的乘性子集下的局部化有哪些等价类
def cal_equiv(n, x): 
    mult = mult_set_gen(n, x)
    if (mult == -1):
        return -1
    else:
        zero = get_zero_div(n, mult)
        mult_num = len(mult)
        
        ans = [[[0, mult[i]] for i in range(0, mult_num)]]  # 先添加所有分子为0的，他们一定属于同一个等价类
        equiv_num = len(ans)    # ans的大小，或者说等价类的个数，后面会动态更新

        # i是分子，j是分母
        for i in range(1, n):
            for j in range(0, mult_num):
                flag = 0    # 0表示没有已有的等价类跟他一样，所以要新建一个等价类；1则表示已经添加到已有的等价类中
                for x in range(0, equiv_num):
                    if (compare(n, [i, mult[j]], ans[x][0], zero)):
                        ans[x].append([i, mult[j]])
                        flag = 1
                        break
                if (flag == 0):
                    ans.append([[i, mult[j]]])
                    equiv_num += 1
        return ans

# 格式化输出等价类
def print_equiv(eq, vformat = "console"):
    equiv_num = len(eq)
    if (vformat == "console"):
        for x in range(0, equiv_num):
            ele_num = len(eq[x])
            print(f"equiv_{x} ({ele_num} elements): ", end = "")
            for i in range(0, ele_num):
                print(f"  {eq[x][i][0]}/{eq[x][i][1]} ", end = "")
            print()
    return

n = 6
x = 2
ans = cal_equiv(n, x)
if (ans != -1):
    print_equiv(ans)
