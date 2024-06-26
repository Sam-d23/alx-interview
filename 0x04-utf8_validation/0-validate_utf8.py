#!/usr/bin/python3


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing the data set
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    # Masks to check the first byte
    masks = [0b10000000, 0b11000000, 0b11100000, 0b11110000, 0b11111000]

    # Masks to check bytes that follow the first byte in multi-byte character
    follow_byte_mask = 0b11000000
    follow_byte_value = 0b10000000

    for byte in data:
        byte = byte & 0xFF  # Only consider the last 8 bits

        if num_bytes == 0:
            for i in range(5):
                if (byte & masks[i]) == masks[i - 1]:
                    num_bytes = i
                    break
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if (byte & follow_byte_mask) != follow_byte_value:
                return False

        num_bytes -= 1

    return num_bytes == 0
