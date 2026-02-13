import re
import csv
from collections import Counter
from pathlib import Path
from typing import List, Tuple

class LogAnalyzer:
    """
    A class to parse syslog files and analyze error patterns.
    """

    def __init__(self, log_file: str):
        self.log_file = Path(log_file)
        self.log_pattern = re.compile(
            r"(?P<timestamp>[A-Z][a-z]+ \d+ \d+:\d+:\d+) "
            r"(?P<host>[\w]+) "
            r"(?P<service>[\w\[\]=]+): "
            r"(?P<level>[A-Z]+) "
            r"(?P<message>.+)"
        )
        self.error_messages: Counter = Counter()

    def analyze(self) -> None:
        """
        Reads the log file line by line and counts specific error messages.
        Raises FileNotFoundError if the source file does not exist.
        """
        if not self.log_file.exists():
            raise FileNotFoundError(f"Log file not found at: {self.log_file}")

        with self.log_file.open('r', encoding='utf-8') as f:
            for line in f:
                match = self.log_pattern.search(line)
                if not match:
                    continue

                level = match.group("level")
                message = match.group("message").strip()

                # Filter only ERROR logs for the report
                if level == 'ERROR':
                    self.error_messages[message] += 1

    def get_top_errors(self, limit: int = 5) -> List[Tuple[str, int]]:
        """Returns the most frequent errors found in the logs."""
        return self.error_messages.most_common(limit)

    def export_to_csv(self, output_path: str) -> None:
        """
        Saves the error statistics to a CSV file.
        """
        sorted_errors = sorted(self.error_messages.items(), key=lambda x: x[1], reverse=True)
        
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Error", "Count"])
                writer.writerows(sorted_errors)
            print(f"Successfully saved report to: {output_path}")
        except IOError as e:
            print(f"Failed to write CSV file: {e}")
