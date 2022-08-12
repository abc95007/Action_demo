#%%
import function
import numpy as np
from raydium import driver

def test_Allen_fun():
    assert function.Allen_add(1, 2) == 3

def test_YC_fun():
    assert function.YC_checksum(np.arange(10)) == 45

