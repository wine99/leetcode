# 多多有一个长度为 n 的字符串, 这个字符串由26个小写字母组成.
# 多多可以对这个字符串进行多次操作, 每次操作可以把该字符串中一段连续的回文子串删除(单个字符也属于回文串), 删除后剩下的串会拼在一起.
# 请问最少需要多少次操作可以将这个字符串删光.

# 第一行, 包含一个正整数 T( 1 \leq T \leq 20) 代表测试数据的组数.
# 对于每组测试数据, 仅有一行, 代表这个字符串.
# ( 1 \leq n \leq 500)
# 保证 \sumn 不超过 3000

from functools import cache


@cache
def min_del(s):
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    ans = len(s)
    for i in range(len(s)):
        j = len(s)
        while j > i + 1:
            if s[i:j] == s[i:j][::-1]:
                break
            j -= 1
        print(s, i, j, s[:i] + s[j:])
        tmp = min_del(s[:i] + s[j:]) + 1
        ans = min(ans, tmp)
    return ans


T = int(input())
for _ in range(T):
    s = input()
    print(min_del(s))
    min_del.cache_clear()


# 超时，通过0%
