s, e = [0, 5, 12], [4, 10, 14]
inter = [8, 12]

n = len(s)

ans = list()

for i in range(n):
    """ behind """
    if inter[1] < s[i]:
        ans.append((inter[0], inter[1]))
        for j in range(i, n):
            ans.append((s[i], e[i]))
        break
    elif e[i] < inter[0]:
        ans.append((s[i], e[i]))

    inter[0] = min(inter[0], s[i])
    inter[1] = max(inter[1], e[i])


print(ans)
