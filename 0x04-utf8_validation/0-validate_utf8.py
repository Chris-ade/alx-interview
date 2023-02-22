def validUTF8(data):
    num_bytes = 0
    for i in data:
        # Check if the current byte is a start of a new character
        if num_bytes == 0:
            # Determine the number of bytes in the current character
            if (i >> 5) == 0b110:
                num_bytes = 1
            elif (i >> 4) == 0b1110:
                num_bytes = 2
            elif (i >> 3) == 0b11110:
                num_bytes = 3
            elif (i >> 7) == 0b0:
                num_bytes = 0
            else:
                # Current byte is a continuation byte or an invalid UTF-8 character
                return False
        else:
            # Check if the current byte is a continuation byte
            if (i >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
