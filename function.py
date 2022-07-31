def Allen_add(a:int, b:int) -> int:
    return a + b

def YC_checksum(data:list) -> int:
    value = 0
    for i in data:
        value = Allen_add(value, i)
    return value

