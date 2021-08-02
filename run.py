import pytest


def print_hi():
    pass


if __name__ == '__main__':
    pytest.main(["-v", '-s', 'testcase/test_LeverTotal.py', 'testcase/test_LeverTotal1.py'])
