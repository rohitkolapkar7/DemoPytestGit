

class Test_Py:
    def test_sum_001(self):
        a= 3
        b= 5
        sum= a+b
        print(sum)

        if sum ==8:
            print("test_sum_001 is   Passed")
        else:
            print("test_sum_001 is Failed")

    def test_mul_001(self):
        a= 3
        b= 5
        mul=a*b
        print(mul)

        if mul ==12:
            print("test_mul_001 is Passed")
        else:
            print("test_mul_001 is Failed")

