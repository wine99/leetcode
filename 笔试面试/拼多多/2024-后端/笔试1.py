# 这里有 n 个正整数，a_1, ..., a_n
# Alice 会先去掉其中最多 d 个数
# Bob 接下来会将剩余的数中最多 m 个数乘以 -k
# Alice 想要剩余数之和尽可能大，Bob 想要剩余数之和尽可能小。假设 Alice 和 Bob 都足够聪明，请问最后剩余数之和是多少。

# 输入T组数据
# 输出T行结果

T = int(input())

for i in range(T):
    n, m, k, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = float("-inf")
    for j in range(d + 1):
        rest_arr = arr[j:]
        tmp = sum(rest_arr[:m]) * -k + sum(rest_arr[m:])
        ans = max(tmp, ans)
    print(ans)


# 超时，通过60%

# 1
# 3 1 1 1
# 4 1 1

# 1


# 1
# 3 1 1 1
# 4 3 2

# 1


# 2
# 5 4 2 0
# 3 5 1 4 1
# 10 4 1 6
# 1 8 2 9 3 3 4 5 3 200

# -25
# -9
