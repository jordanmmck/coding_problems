##############################
# dicts
##############################

d = {'a': 1, 'b': 2, 'c': 3}

# dict keys
keys_list = list(d)
keys_iterator = d.keys()

# iterator of key-value tuples
key_val_pairs = d.items()

##############################
# lists
##############################

l1 = ['x', 'y', 'z']
l2 = [2, 3, 5, 7]

# combine lists into iterator of tuples
l1_l2_pairs = zip(l1, l2)

# get l1 reversed
l1_reversed = l1[::-1]
