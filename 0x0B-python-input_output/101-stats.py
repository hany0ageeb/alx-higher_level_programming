#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""


class Metrics:
    """class Metrics
    Attributes:
        total_file_size(int): (instance attribute) total file size so far
        status_codes(dict): dict with number of lines for each code
    """
    def __init__(self):
        self.total_file_size = 0
        self.status_codes = {}

    def log_line(self, line):
        """compute and update metrices"""
        if type(line) is not str:
            return
        parts = line.split(' ')
        if len(parts) >= 9:
            file_size = parts[8]
            status = parts[7]
            if file_size[len(file_size) - 1] == "\n":
                self.total_file_size += int(file_size[:-1])
            else:
                self.total_file_size += int(file_size)
            if status in self.status_codes:
                self.status_codes[status] += 1
            else:
                self.status_codes[status] = 1

    def print_metrics(self):
        """print metrices with specified format"""
        print("File size: {:d}".format(self.total_file_size))
        for key, value in sorted(self.status_codes.items()):
            print("{}: {:d}".format(key, value))


def main():
    """script entry point"""
    import sys
    line_counter = 1
    m = Metrics()
    try:
        for line in sys.stdin:
            m.log_line(line)
            line_counter += 1
            if line_counter % 10 == 0:
                m.print_metrics()
    except KeyboardInterrupt:
        m.print_metrics()
        raise


if __name__ == '__main__':
    main()
