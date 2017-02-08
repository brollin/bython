# Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.
# 
# Toeplitz Matrix
# 7 3 5 1 
# 2 7 3 5 
# 1 2 7 3 
# 4 1 2 7

def is_toeplitz_matrix(matrix):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    
    vals = [None] * (rows + cols - 1)

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            index = (rows-i-1) + (j)
            if vals[index] is not None:
                if val is not vals[index]:
                    return False
            else:
                vals[index] = val
    
    return True


# Given coins
# [1,5,5]
# 
# Produce the amounts that can be made
# from these coins:
# 0, 1, 5, 6, 10, 11

def sum_of_coins(coins_list, memo, sums_set):
    n = len(coins_list)
    sum_of_coins(coins_list[0:n-1], memo, sums_set)
    memo[coins_list[0:n-1]]
    sum_of_coins(coins_list[1:n], memo, sums_set)
    


