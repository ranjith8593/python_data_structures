def permute(ip):
    ans = []
    temp = []

    def perm(ip_a, temp):

        if len(ip_a) == 0:
            ans.append(temp[:])

        for i, c in enumerate(ip_a):
            temp.append(c)
            del ip_a[i]
            perm(ip_a, temp)
            ip_a.insert(i, c)
            del temp[-1]

    perm(ip, temp)
    return ans


if __name__ == "__main__":
    print(permute([1, 2, 3]))
