def longest_increasing_subsequence(ip_arr):
    len_array = len(ip_arr)
    notes = [1] * (len_array)
    for i in range(1, len_array):
        for j in range(i):
            if ip_arr[j] < ip_arr[i]:
                notes[i] = max(notes[i], notes[j] + 1)
                print(notes)

    max_num = 0
    for val in notes:
        if val > max_num:
            max_num = val
    print(max_num)


if __name__ == "__main__":
    longest_increasing_subsequence([3, 4, 0, -1, 0, 6, 2, 3])
