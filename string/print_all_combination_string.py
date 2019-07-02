def permute(input, p, result):
    for i in input:
        if len(p) < len(input):
            permute(input, p, result)
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    path, result = [], []
    print(permute([1, 2, 3], path, result))
