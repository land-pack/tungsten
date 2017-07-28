
from collections import Counter
import random

class RandManage(object):
    """
        We already have std-random, why we need this?
    """

    def by_weight(self, seq, choice=None, percentage=100):
        """
            Input a right weight list, the value should be 0 ~ 1
            Example: [0, 0.1, 0.2, 0.3,0.4]
        """
        if not isinstance(seq, list):
            raise ValueError("Please Input a List as the first param!")
        if abs(sum(seq) - 1) > 0.0001:
            raise ValueError("The sum of percentage did't equal `1`")
        if choice:
            pass
        else:

            weight_area = [int(i * percentage) for i in seq]
            weight_list = {i: weight_area[i] for i in range(len(weight_area))}
            weight_list_area = [[k] * v for k, v in weight_list.items()]
            weight_list_area = sum(weight_list_area, [])
            target = random.choice(weight_list_area)
            return target


if __name__ == '__main__':
	#30,55,60,50,45,110,110,100,100,100,90,50,60,20,21
    rb = RandManage()
    a = [0, 0.03, 0.055, 0.06, 0.05, 0.045, 0.11, 0.11, 0.1, 0.1,0.1,0.09,0.05,0.06, 0.02,0.02]
    lst = []
    for i in range(200):
        d = rb.by_weight(a, percentage=10000)
        lst.append(d)

    print(Counter(lst))
