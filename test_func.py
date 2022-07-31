#%%
import function

def test_fun():
    assert function.Allen_add(1, 2) == 3

def test_fun2():
    assert function.YC_checksum([1, 2, 3]) == 6

if __name__ == '__main__':
    test_fun()
    test_fun2()
    print('All tests passed!')
