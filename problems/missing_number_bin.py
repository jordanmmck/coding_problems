# each integer is 32 bits
def missing_number_bin(A):

    nums = []

    for idx, value in enumerate(A):
        bit_str = []
        for bit in value[2::]:
            bit_str.append(bit)
            print(bit)
        nums.append("".join(["0b"] + bit_str))

    print("VALUES", bin(nums[2]))

    for i in range(0, len(A)):
        print(nums)


missing_number_bin([bin(0), bin(1), bin(2), bin(3), bin(
    4), bin(5), bin(6), bin(8), bin(9), bin(10)])
