import numpy as np

def test_print_numpy() :
    print(np.array([(2,3,4),(5,6,7)]))
    print(np.empty((5,4,3)))
    print(np.ones((5,4), dtype= int))
    print(np.random.random((5,4)))
    print( np.random.normal(size=(2,3) ) )

    np.random.seed(693)

    a = np.random.randint(0,10, size=(5,4))
    print("Array: \n" , a)

    # Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns, to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics : min, max, mean ( across rows, cols, and overall )
    print("Minimum of each column : \n" , a.min(axis=0))
    print("Minimum of each row : \n", a.min(axis=1))
    print("Maximum of each column : \n" , a.max(axis=0))
    print("Maximum of each row : \n", a.max(axis=1))
    print("Mean of all elements : \n", a.mean())

def test_run() :

    a = np.random.rand(5,4)
    print("Array:\n", a)

    # Slicing
    # Note : Slice n:m:t specifies a range that starts at n, and stops before m, in
    print(a[:, 0:3:2]) # will select columns 0, 2 for every row


def test_run2() :
    a = np.random.rand(5)
    print(a)
    # accessing using list of indices
    indices = np.array([1,1,2,3])
    print(a[indices])

def test_run3() :
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print(a)

    # calculating mean
    mean = a.mean()
    print("mean: ", mean)
    a[a < mean]= mean
    print(a)

def test():
        x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
        z = np.polyfit(x, y, 3)
        print(z)


        # a = np.array([0,0.5,1.0,1.5,2.0])
        #
        # print(type(a))
        # print(a[:2])
        # print(a.sum())
        # print(a.std())
        # print(a.cumsum())
        # print(a * 2)
        # print(a ** 2)
        # print(np.sqrt(a))
        #
        # b = np.array([a,a*2])
        # print(b)
        # print(b[0])
        # print(b[0,2])
        # print(b.sum())
        # print(b.sum(axis=0))
        # print(b.sum(axis=1))


if __name__ == "__main__" :
    test()
