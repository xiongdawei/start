

import unittest

import random
import numpy as np

import itertools


# Given a string (e.g. "What the hell?"), returns a list of the following pattern

# ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',

#  'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']

def input_nput_put_ut_t(a) :
    b = len(a)
    c=[]
    for i in range(b, 2, -1):
        c.append(a[0:i])
    return c
    raise NotImplementedError()


# add two vectors

def vector_addition(a, b):
    return np.add(a,b)
    raise NotImplementedError()


# given two lists of integers, find a slice in list 1 and a slice in list 2 whose sums are equal

# using enumeration is fine

def find_equal_sum_slice(a, b):
    for i in range(1, len(a) + 1):
        for j in range(0, len(a) - i + 1):
            p = 0
            for k in range(j, j + i):
                p = p + a[k]
            # print(j+1,j+i)
            for l in range(1, len(b) + 1):
                for m in range(0, len(b) - l + 1):
                    q = 0
                    for n in range(m, m + l):
                        q = q + b[n]
                    if p == q:
                        return(j + 1, j + i, m + 1, m + l)


raise NotImplementedError()

# use a sorting algorithm (your choice) to sort a list of ten unsorted integers. Do not use the python 
 
# sort function.


def basic_sort(c):
    d = []
    for i in range(0, len(c)):
        d.append(eval(c[i]))
    for i in range(0, len(d)):
        for j in range(0, i):
            if (d[i] < d[j]):
                d[i], d[j] = d[j], d[i]
    print(d)
raise NotImplementedError()
	


# A well-known NP-complete problem

# Given a set of integers, find a non-empty subset (if exists) summing to a given number k

# Note: make use of itertools.combinations. See python documentation online

def subset_sum(a, b):
    import itertools
    for i in range(1, len(a) + 1):
        j = [x for x in itertools.combinations(a, i)]
        for k in j:
            r = 0
            for l in k:
                r = r + l
            if (r == b):
                return(k)
    raise NotImplementedError()


class UnitTest(unittest.TestCase):

    def test_input(self):

        self.assertEqual(input_nput_put_ut_t("What the hell?"),

                         ['What the hell?', 'What the hell', 'What the hel', 'What the he', 'What the h', 'What the ',

                          'What the', 'What th', 'What t', 'What ', 'What', 'Wha', 'Wh', 'W']

                         )


    def test_eq_sum_slice(self):

        for i in range(10):

            list1 = [random.randint(0, 150) for i in range(150)]

            list2 = [random.randint(0, 60) for i in range(75)]



            a, b, c, d = find_equal_sum_slice(list1, list2)

            s1, s2 = sum(list1[a:b + 1]), sum(list2[c:d + 1])

            self.assertEqual(s1, s2)


    def test_add_vectors(self):

        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])

        self.assertEqual(vector_addition([1], [-1]), [0])

    def test_basic_sort(self):
	
		    self.assertEqual([1,3,5,7,9,11,13,15,17,10000], basic_sort([3,1,5,7,9,11,15,17,10000,13]))
		

    def test_subset_sum(self):

        s = {random.randint(-200, 200) for i in range(random.randint(100))}

        k = random.randint(-50, 50)

        subset = subset_sum(s, k)

        self.assertTrue(set(subset).issubset(s))

        self.assertEqual(sum(subset), k)


if __name__ == "__main__":

    unittest.main()



