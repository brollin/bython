
# regular expression for email address:
# \s*\@\s*\.\s*

def find_min(list_):
    # [21, 25, 33, 1, 3, 7, 13, 15]
    # [21, 25, 1, 3]

    print find_min_recurse(list_, 0, len(list_)-1)

def find_min_recurse(list_, lo, hi):

    if lo == hi:
        return list_[lo]

    if lo == hi - 1:
        return min(list_[lo:(hi+1)])

    mid = (hi + lo) / 2

    if list_[mid] < list_[hi]:
        return find_min_recurse(list_, lo, mid)
    else:
        return find_min_recurse(list_, mid, hi)

find_min([1])
find_min([25, 1])
find_min([25, 1, 3])
find_min([21, 25, 33, 1, 3, 7, 13, 15])
find_min([33, 1, 3, 7, 13, 15])
find_min([21, 25, 33, 1, 3])
find_min([21, 25, 33, 1])

find_min(range(35))

