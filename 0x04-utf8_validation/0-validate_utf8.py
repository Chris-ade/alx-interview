#!/usr/bin/python3
"""
UTF-8 Valdation Module
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8", errors="strict")
        return True
    except UnicodeDecodeError:
        return False
