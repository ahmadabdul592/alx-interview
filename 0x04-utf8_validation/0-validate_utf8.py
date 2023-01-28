#!/usr/bin/python3
""" Defines validUTF8 method """


def validUTF8(data):
    """ Validates elements of data passed to it if
    they are valid UTF-8 encodings """
    def counts(dig):
        """ Checks the digit at the begining """
        count = 0
        for i in range(7, -1, -1):
            if dig & (1 << i):
                count += 1
            else:
                break
        return count

    count = 0
    for j in data:
        if not count:
            count = counts(j)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if counts(j) != 1:
                return False
    return count == 0
