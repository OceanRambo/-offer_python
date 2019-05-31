class Solution:
    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
    def reOrder(self, array, func):
        if not array:
            return
        if len(array) == 1:
            return array

        begin = 0
        end = len(array) - 1
        while begin < end:
            if begin < end and func(array[begin]):
                begin += 1
            if begin < end and not func(array[end]):
                end -= 1

            if begin < end:
                array[begin], array[end] = array[end], array[begin]

        return array

    def isEven(self, n):
        return n & 0x1

    def isNegtive(self, n):
        return n < 0

    def reOrderArray(self, array):
        # return self.reOrder(array, func=self.isEven)

        return self.reOrder(array, func=self.isNegtive)


s = Solution()
print(s.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))


print(s.reOrderArray([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))