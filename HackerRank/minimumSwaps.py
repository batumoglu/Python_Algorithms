def minimumSwaps2(arr):
    distance = {}
    changes = 0

    for pos, value in enumerate(arr):
        distance[pos] = value - pos - 1
    
    while sum([abs(x) for x in distance.values()]) != 0:
        pos1 = max(distance, key=distance.get)
        pos2 = min(distance, key=distance.get)

        val1 = distance[pos1] + pos1 + 1
        val2 = distance[pos2] + pos2 + 1

        distance[pos1] = val2 - pos1 - 1
        distance[pos2] = val1 - pos2 - 1

        changes += 1
    else:
        print(changes)

def minimumSwaps(arr):
    changes = 0
    arr = [value-1 for value in arr]
    value_idx = {value:pos for pos, value in enumerate(arr)}

    for pos, value in enumerate(arr):
        if pos != value:
            to_swap_idx = value_idx[pos]
            arr[pos], arr[to_swap_idx] = pos, value
            value_idx[pos] = pos
            value_idx[value] = to_swap_idx
            changes += 1
    return changes



if __name__ == '__main__':
    #minimumSwaps([4,2,1,3])
    print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
