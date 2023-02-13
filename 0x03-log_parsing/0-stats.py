#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    count = 0
    for line in sys.stdin:
        count += 1
        elements = line.split()
        if len(elements) != 9:
            continue
        try:
            size = int(elements[-1])
            status = int(elements[-2])
            total_size += size
            if status in status_codes:
                status_codes[status] += 1
        except ValueError:
            continue
        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for status in sorted(status_codes.keys()):
                if status_codes[status] > 0:
                    print("{}: {}".format(status, status_codes[status]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))
