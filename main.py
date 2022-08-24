# Mine
def positive_sum(arr):
    result = 0
    positive_arr = filter(lambda x: x > 0, arr)
    return sum(positive_arr)

#Best
def positive_sum_b(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum([1,2,3,4,5]))