#!/usr/bin/env python
from collections import deque


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    print('number in last 8', some_int)
    return some_int%100000000

def optimized_fibonacci(f):
    """
    Optimized version of recursive fibonacci
    :param int f: the position of number to be generated
    :rtype: int
    """
    if (f<= 0):
        return 0
    elif (f==1):
        return 1
    else:
        myseq= SummableSequence(0,1)
    return myseq(f)


class SummableSequence(object):
    """
        class that generates sum of previous n numbers as next number

    """
    def __init__(self, *initial):

        self.baselen=len(initial)
        self.q = deque(initial)
        #print('Base sequence',self.q, self.baselen)
        #raise NotImplementedError()

    def __call__(self, i):
        return self.gen_series(i)

        #raise NotImplementedError()

    def gen_series(self,i):
        """
           Optimized version of recursive fibonacci
           :param int i: the position of number to be generated
           :rtype: int
        """
        startseq = self.baselen

        if (i <= startseq):
            return sum(self.q)  #pass
        else:
            queue = deque(self.q)
            for k in (range(startseq, i+1)):

                sumNum = sum(queue)
                queue.append(sumNum)
                queue.popleft()

        return queue[-1]

if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(40)))

    new_seq = SummableSequence(5, 7, 11, 12)


    print("new_seq(100000)[-8:]:", last_8(new_seq(10)))
