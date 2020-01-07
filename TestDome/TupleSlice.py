def tuple_slice(startIndex, endIndex, tup):
    value = tup[startIndex:endIndex]
    return ",".join([str(item) for item in value])

print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))