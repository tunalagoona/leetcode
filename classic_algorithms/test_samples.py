from random import randint

import time

from classic_algorithms.three_way_quicksort import quicksort as qsort_3way
from classic_algorithms.quicksort import quicksort as qsort_std


class TestClass:
    def test_basic(self):
        arr = [3, 6, 1, 9, 22, 6, 3, 90]
        for sort in [qsort_3way, qsort_std]:
            sort(arr)
            assert arr == sorted(arr)

    def test_already_sorted(self):
        x = []
        length = 1000
        for i in range(0, length):
            x.append(randint(-(2 ** 30), 2 ** 30))
        x.sort()
        for sort in [qsort_3way, qsort_std]:
            start = time.time()
            sort(x)
            stop = time.time()
            ex_time = stop - start
            assert ex_time < 0.08

    def test_equal_elements(self):
        x = []
        length = randint(1, 1000)
        for i in range(0, length):
            x.append(5)
        for sort in [qsort_3way, qsort_std]:
            start = time.time()
            sort(x)
            stop = time.time()
            ex_time = stop - start
            assert ex_time < 0.1

    def test_large_input(self):
        x = []
        length = 10000
        for i in range(0, length):
            x.append(randint(0, 100))
        for sort in [qsort_3way, qsort_std]:
            start = time.time()
            sort(x)
            stop = time.time()
            ex_time = stop - start
            assert ex_time < 2

    def test_zero(self):
        x = []
        for sort in [qsort_3way, qsort_std]:
            start = time.time()
            sort(x)
            stop = time.time()
            ex_time = stop - start
            assert ex_time < 0.05


s = TestClass()
s.test_basic()
s.test_already_sorted()
s.test_equal_elements()
s.test_large_input()
s.test_zero()
