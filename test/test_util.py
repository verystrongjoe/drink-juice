"""
Using time function
"""

import time

def test_run() :
    t1 = time.time()

    print("check")

    t2 = time.time()

    print("The time taken by print statement is ", t2-t1, " seconds")

if __name__ == "__main__" :
    test_run()