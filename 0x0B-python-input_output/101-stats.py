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
        self.is_printed = False

    def log_line(self, line):
        """compute and update metrices"""
        status, file_size = Metrics.parse_line(line)
        self.total_file_size += file_size
        if status in ('200', '301', '400', '401', '403', '404', '405', '500'):
            self.status_codes[status] = self.status_codes.get(status, 0) + 1
        self.is_printed = False

    @staticmethod
    def parse_line(line: str):
        """parse line"""
        if type(line) is not str or line == "":
            return ('', 0)
        if line[len(line) - 1] == '\n':
            start = len(line) - 2
        else:
            start = len(line) - 1
        current = start
        file_size = 0
        status_code = ''
        while current >= 0:
            while current >= 0 and line[current] != ' ':
                current -= 1
            try:
                if current > 0:
                    file_size = int(line[current + 1:start + 1])
                else:
                    file_size = int(line[current:start + 1])
            except ValueError:
                file_size = 0
            start = current - 1
            current -= 1
            while current >= 0 and line[current] != ' ':
                current -= 1
            if current < 0:
                return ('', file_size)
            elif current == 0:
                status_code = line[current:start + 1]
            else:
                status_code = line[current + 1:start + 1]
            return (status_code, file_size)

    def print_metrics(self):
        """print metrices with specified format"""
        if self.is_printed:
            return
        msg = "File size: {:d}\n".format(self.total_file_size)
        for key, value in sorted(self.status_codes.items()):
            msg += "{}: {:d}\n".format(key, value)
        print(msg, end='')
        self.is_printed = True


def main():
    """script entry point"""
    import sys
    line_counter = 0
    m = Metrics()
    try:
        for line in sys.stdin:
            m.log_line(line)
            line_counter += 1
            if line_counter % 10 == 0:
                m.print_metrics()
        m.print_metrics()
    except KeyboardInterrupt as e:
        m.print_metrics()
        raise


if __name__ == '__main__':
    main()
