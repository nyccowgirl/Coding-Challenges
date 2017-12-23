"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """

    if not astring:
        return astring
    else:
        return astring[-1] + rev_string(astring[:-1])


# SOLUTION FILE:

# def rev_string(astring):
#     """Return reverse of string using recursion.

#     You may NOT use the reversed() function!
#     """

#     # START SOLUTION

#     if len(astring) < 2:
#         return astring

#     return astring[-1] + rev_string(astring[:-1])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"
