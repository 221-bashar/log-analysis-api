# parser/log_parser.py
import re

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.parsed_logs = []

    def parse(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                # Example: "Nov 22 12:00:01 server sshd[123]: Failed password for user root from 1.2.3.4"
                match = re.search(r'(?P<timestamp>\w+ \d+ \d+:\d+:\d+).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    self.parsed_logs.append(match.groupdict())
        return self.parsed_logs

if __name__ == "__main__":
    parser = LogParser("logs/auth.log")
    logs = parser.parse()
    print(logs)

