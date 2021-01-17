#!/usr/bin/env python3
import numpy as np


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    return some_int%100000000


def optimized_fibonacci(f):
    if (f<= 0):
        return 0
    elif (f==1):
        return 1
    else:
        myseq= SummableSequence(0,1)
    return myseq(f)


class SummableSequence(object):
    def __init__(self, *initial):

        self.baselen=len(initial)

        self.narr = np.array(initial)
        print('Base sequence',self.narr, self.baselen)
        #raise NotImplementedError()

    def __call__(self, i):
        return self.gen_fibonacci(i)

        #raise NotImplementedError()

    def gen_fibonacci(self,i):
        startseq = self.baselen

        if (i <= startseq):
            return np.sum(self.narr)  #pass
        else:

            circ_start = 0

            for k in (range(startseq, i+1)):
                sumNum = np.sum(self.narr)
                self.narr[circ_start]=sumNum
                circ_start = (circ_start +1) % self.baselen

            print('my result',self.narr.max())
        return self.narr.max()

if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(6)))

    new_seq = SummableSequence(5, 7, 11, 12)

    #print("new_seq(100000)[-8:]:", new_seq(10))

    print("new_seq(100000)[-8:]:", last_8(new_seq(1000000)))
