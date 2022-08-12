#%%
import numpy as np
def Allen_add(a:int, b:int) -> int:
    return a + b 

def YC_checksum(data:np.ndarray) -> int:
    value = 0
    for i in data:
        value = Allen_add(value, i)
    return value

if __name__ == '__main__':
    data = np.arange(10)
    checksum = YC_checksum(data)
    print("checksum:", checksum)  # checksum: 55

