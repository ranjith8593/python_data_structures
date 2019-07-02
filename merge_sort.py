
def merge_sort(ip: list) -> list:
    if len(ip) > 1:
        mid = len(ip) // 2
        l = ip[:mid]
        r = ip[mid:]
        merge_sort(l)
        merge_sort(r)
        i = 0
        j = 0
        k = 0
        while i <= len(l) - 1 and j <= len(r) - 1:
            print("left", l)
            print("right", r)
            if l[i] > r[j]:
                ip[k] = r[j]
                j += 1
            elif l[i] == r[j]:
                ip[k] = l[i]
                i += 1
                j += 1
            else:
                ip[k] = l[i]
                i += 1
            k += 1
        while i < len(l):
            ip[k] = l[i]
            i = i + 1
            k = k + 1

        while j < len(r):
            ip[k] = r[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    ip = [10, 2, 20, 1]
    merge_sort(ip)
    print(ip)
