def pair_sum(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
            seen.remove(target)
    print(len(output))

pair_sum([1,3,2,2,],4)
