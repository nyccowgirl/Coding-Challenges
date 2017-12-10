"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    count = 0

    i = 0

    while i < (len(branches) - 1):
        if len(branches) > 2:
            if branches[i + 2] == 0:
                count += 1
                i = i + 2
            else:
                count += 1
                i = i + 1
        else:
            count += 1
            break

    return count


# def  lemur(branches):
#     """Return number of jumps needed."""

#     assert branches[0] == 0, "First branch must be alive"
#     assert branches[-1] == 0, "Last branch must be alive"

#     # START SOLUTION

#     at = 0
#     n_jumps = 0

#     while at < len(branches) - 1:
#         at += 2
#         if at >= len(branches) or branches[at] == 1:
#             # We can jump this far, so only jump 1
#             at -= 1
#         n_jumps += 1

#     return n_jumps


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"