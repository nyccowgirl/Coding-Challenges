"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    size_a = len(a)
    size_b = len(b)
    sort_lst = []
    x = 0
    y = 0

    while True:
        if size_a == 0:
            sort_lst.extend(b[y:])
            break
        elif size_b == 0:
            sort_lst.extend(a[x:])
            break
        else:
            if a[x] <= b[y]:
                sort_lst.append(a[x])
                x += 1
                size_a -= 1
            else:
                sort_lst.append(b[y])
                y += 1
                size_b -= 1

    return sort_lst


# SOLUTION FILE:

# def sort_ab(a, b):
#     """Given already-sorted lists, `a` and `b`, return sorted list of both.

#     You may not use sorted() or .sort().
#     """

#     # START SOLUTION

#     out = []

#     ia = 0  # index into list a
#     ib = 0  # index into list b

#     while ia < len(a) and ib < len(b):
#         # Check current items in both lists:
#         #  - if a < b, add a and increase ia
#         #  - else      add b and increase ib

#         if a[ia] < b[ib]:
#             out.append(a[ia])
#             ia += 1

#         else:
#             out.append(b[ib])
#             ib += 1

#     # One list could have things remaining; add any remaining items
#     out.extend(a[ia:])
#     out.extend(b[ib:])

#     return out


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
