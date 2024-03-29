# 伊文有两个由0和1组成的字符串，A和B，长度分别为m和n(m>=n)。伊文希望取出A的连续子串与B异或构造出新的长度为n的S串，使得S中的各位异或的结果为0。请问伊文有多少种取法？

# 输入有三行，第一行2个数m和n，为A和B的长度；
# m,n\ \ (0<n\leq m\leq 5\times10^3)
# 第二行为长度为的A串
# 第三行为长度为的B串，A和B仅由'0'和'1'组成


def xor1count(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c


m, n = map(int, input().split())
A = input()
B = input()
s = set()
ans = 0
for i in range(m - n + 1):
    sub_A = A[i : i + n]
    if sub_A not in s:
        s.add(sub_A)
        if xor1count(sub_A, B) % 2 == 0:
            ans += 1
print(ans)


# 通过

# 3
# mwapd
# tvuvv
# yxxmi

# 5
# 3
# 4
