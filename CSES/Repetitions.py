def solve(s: str):
    count = 1
    res = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1

        res = max(res, count)

    print(res)


s = input().strip()
solve(s)