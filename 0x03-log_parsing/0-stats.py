#!/usr/bin/python3
"""
Let's Parse Logs!

Example Input:
18.129.91.37 - [2024-03-28 12:46:23.196213] "GET /projects/260 HTTP/1.1" 405 27

Example Output:
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

"""
import sys
from typing import Dict


def print_stats(file_size: int, status_codes: Dict[str, int]) -> None:
    """ Output Log Statistics """

    # Print file size
    print('File size:', file_size)

    # Print status_codes sorted by status code
    for code, stat in sorted(status_codes.items(), key=lambda c: c[0]):
        print(f'{code}: {stat}')


if __name__ == '__main__':

    # Initialize File Size
    file_size = 0

    # Initialize Status Codes dictionary and define valid codes
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    # Track read lines
    count_read = 0

    try:

        # Read through stdin
        for line in sys.stdin:

            try:
                infos = line[:-1].split()

                # Update file_size
                size = int(infos[-1])
                file_size += size

                # Update status_codes
                code = int(infos[-2])
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1

            except BaseException:
                pass

            # Increment count_read
            count_read += 1

            # Print on 10th consecutive line
            if count_read % 10 == 0:
                print_stats(file_size, status_codes)

    # Handle SIGINT
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    # Print for a last time
    print_stats(file_size, status_codes)
