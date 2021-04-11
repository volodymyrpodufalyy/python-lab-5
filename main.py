import re
import os


def main():
    with open(os.path.join(os.path.dirname(__file__), 'access_log_Jul95.txt'), 'r') as file:
        REGEX_GIF_REQUEST = re.compile(
            r'([a-zA-Z0-9._-]+)'
            r'( - - )'
            r'(\[01/Jul/1995:(03:(?:39|4\d|5\d):\d{2}) -\d{4}\])'
            r' \"([a-zA-Z0-9. _/-]+)'
            r'.gif'
            r' ([a-zA-Z0-9._/-]+)\"'
            r' (200 \d+)')

        REGEX_STOP = re.compile(r'(01/Jul/1995:(03:55:00))')

        matches = []
        count = 0
        for line in file:
            match = REGEX_GIF_REQUEST.search(line)
            stop_match = REGEX_STOP.search(line)
            if match:
                matches.append(match)
                count += 1
            if stop_match:
                break

        for match in matches:
            print(match.group())
    print(count)

if __name__ == '__main__':
    main()