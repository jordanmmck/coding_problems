def majority_element(nums):

    h = {}

    # count occurences of each value
    for idx, val in enumerate(nums):
        if h.get(val) is None:
            h[val] = 1
        else:
            h[val] += 1

    # get max count
    max_count = [0, ""]
    for key in h.keys():
        if h[key] > max_count[0]:
            max_count[0] = h[key]
            max_count[1] = key

    # check if majority
    if max_count[0] > (len(nums)/2):
        return max_count[1]
    else:
        return -1


maj = majority_element([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

print(maj)
