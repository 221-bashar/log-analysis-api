from parser.log_parser import LogParser

# Initialize parser with log file
parser = LogParser("logs/auth.log")

# Parse logs
parsed_logs = parser.parse()

# Print parsed results
for entry in parsed_logs:
    print(entry)
