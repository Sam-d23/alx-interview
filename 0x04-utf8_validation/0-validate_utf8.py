#!/usr/bin/python3


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 encoding."""
    skip = 0
    n = len(data)

    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        byte = data[i]

        if byte < 0 or byte > 0xFF:
            return False

        if byte <= 0x7F:
            skip = 0
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
        else:
            return False

        if n - i < span:
            return False

        for j in range(1, span):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False

        skip = span - 1


    return True
