import utils


def main():
  arr = utils.get_array()
  len_arr = len(arr)
  for j in range(1, len_arr):
    i = j - 1
    key = arr[j]
    while i >= 0 and arr[i] > key:
      arr[i + 1] = arr[i]
      i = i - 1
    arr[i + 1] = key
  print(arr)


if __name__ == "__main__":
  main()
