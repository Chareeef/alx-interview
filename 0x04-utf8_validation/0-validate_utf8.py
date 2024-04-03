#!/usr/bin/python3
"""UTF-8 Validation problem
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Given data set as a serie of integers (bytes),
    return whether it is a valid UTF-8 encoding or not.
    """

    def single_UTF8_byte(byte: int) -> bool:
        """Check if byte represents a single UTF-8 byte
        e.g.: 0xxxxxxx
        """
        return True if byte >> 7 == 0 else False

    def continuation_UTF8_byte(byte: int) -> bool:
        """Check if byte represents a continuation UTF-8 byte
        e.g.: 10xxxxxx
        """
        if byte >> 7 == 1 and byte >> 6 & 1 == 0:
            return True
        else:
            return False

    def two_UTF8_byte(byte: int) -> bool:
        """Check if the byte at data[idx] starts a 2-byte UTF-8 grapheme
        e.g.: 110xxxxx
        """
        if byte >> 7 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 0:
            return True
        else:
            return False

    def three_UTF8_byte(byte: int) -> bool:
        """Check if the byte at data[idx] starts a 3-byte UTF-8 grapheme
        e.g.: 1110xxxx
        """
        if byte >> 7 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 1\
                and byte >> 4 & 1 == 0:
            return True
        else:
            return False

    def four_UTF8_byte(byte: int) -> bool:
        """Check if the byte at data[idx] starts a 4-byte UTF-8 grapheme
        e.g.: 11110xxx
        """
        if byte >> 7 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 1\
                and byte >> 4 & 1 == 1 and byte >> 3 & 1 == 0:
            return True
        else:
            return False

    # Read through data
    total_bytes = len(data)
    idx = 0

    while idx < total_bytes:
        byte = data[idx]

        # Ensure it is a byte (8-bit unsigned integer)
        if byte < 0 or byte > 255:
            return False

        if single_UTF8_byte(byte):
            # Move forward by 1
            idx += 1
            continue

        elif two_UTF8_byte(byte):
            # Verify there is one continuation byte
            if idx > total_bytes - 2 or\
                    not continuation_UTF8_byte(data[idx + 1]):
                return False

            # Move forward by 2
            idx += 2
            continue

        elif three_UTF8_byte(byte):
            # Verify there is two continuation byte
            if idx > total_bytes - 3 or\
                    not continuation_UTF8_byte(data[idx + 1]) or\
                    not continuation_UTF8_byte(data[idx + 2]):
                return False

            # Move forward by 3
            idx += 3
            continue

        elif four_UTF8_byte(byte):
            # Verify there is two continuation byte
            if idx > total_bytes - 4 or\
                    not continuation_UTF8_byte(data[idx + 1]) or\
                    not continuation_UTF8_byte(data[idx + 2]) or\
                    not continuation_UTF8_byte(data[idx + 3]):
                return False

            # Move forward by 4
            idx += 4

    # If we exit the loop, it means that data is a valid UTF-8 encoding
    return True
