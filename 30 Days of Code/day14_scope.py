# Day 14: Scope

class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here
    def computeDifference(self):
        max_value = max(self.__elements)
        min_value = min(self.__elements)

        self.maximumDifference = max_value - min_value


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)