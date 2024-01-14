import pytest

from calculator2 import square

def main():
    test_square()


def test_square():
    for i in [-2,-1,0,1,2]:
        try:
            assert square(i) == i * i
        except AssertionError:
            print(i,"does not equal", i * i)


if __name__ == '__main__':
    main()                  

def test_str():
    pytest.raises                                          
    

