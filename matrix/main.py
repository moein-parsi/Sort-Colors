class Solution(object):
    def __init__(self, num):
        self.num = num

    def sortColors(self):
        zero = 0
        one = 0
        two = 0
        for i in self.num:
            if i == "0":
                zero += 1
            elif i == "1":
                one += 1
            elif i == "2":
                two += 1

        sort_list = []
        while zero > 0:
            sort_list.append(0)
            zero -= 1
        while one > 0:
            sort_list.append(1)
            one -= 1
        while two > 0:
            sort_list.append(2)
            two -= 1

        print(sort_list)

m = input(">> ")
# m = int(m)
c = Solution(m)
c.sortColors()