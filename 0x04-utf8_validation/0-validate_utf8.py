def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Loop through all integers in the data set
    for num in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if num >> 7 == 0b0:
                # 1-byte UTF-8 character
                num_bytes = 1
            elif num >> 5 == 0b110:
                # 2-byte UTF-8 character
                num_bytes = 2
            elif num >> 4 == 0b1110:
                # 3-byte UTF-8 character
                num_bytes = 3
            elif num >> 3 == 0b11110:
                # 4-byte UTF-8 character
                num_bytes = 4
            else:
                # Invalid UTF-8 character
                return False
        else:
            # This is a continuation byte
            if num >> 6 != 0b10:
                # Invalid continuation byte
                return False
            # Decrement the number of bytes left in the current character
            num_bytes -= 1
    # If there are no more continuation bytes expected, then the data set is valid
    return num_bytes == 0
