# 这里有 n 个正整数，a_1, ..., a_n
# Alice 会先去掉其中最多 d 个数
# Bob 接下来会将剩余的数中最多 m 个数乘以 -k
# Alice 想要剩余数之和尽可能大，Bob 想要剩余数之和尽可能小。假设 Alice 和 Bob 都足够聪明，请问最后剩余数之和是多少。

# 输入T组数据, 每组数据第一行四个整数 n, m, k, d
# 输出T行结果


T = int(input())

for i in range(T):
    n, m, k, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = float("-inf")
    bob_neg = sum(arr[:m]) * -k
    bob_pos = sum(arr[m:])
    for j in range(d + 1):
        tmp = bob_neg + bob_pos
        ans = max(tmp, ans)
        bob_neg -= arr[j] * -k
        if j + m < n:
            bob_neg += arr[j + m] * -k
            bob_pos -= arr[j + m]
    print(ans)


# 1
# 3 1 1 1
# 4 1 1

# 0


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
