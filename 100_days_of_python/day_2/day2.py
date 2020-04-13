"""
Extract datetimes from log entries and calculate the time
between the first and last shutdown events
"""

import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

SHUTDOWN_EVENT = "Shutdown initiated"

tmp_folder = Path(Path(__file__).parent, "./tmp")
tmp_folder.mkdir(parents=True, exist_ok=True)

logfile = Path(tmp_folder, "log.txt")
urllib.request.urlretrieve("http://bit.ly/2AKSIbf", logfile)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line: str) -> datetime:
    datetime_in_line = line.split()[1]
    return datetime.strptime(datetime_in_line, "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines: list) -> timedelta:
    lines_with_shutdown_events = [line for line in loglines if SHUTDOWN_EVENT in line]
    timestamp_of_shutdowns = [
        convert_to_datetime(line) for line in lines_with_shutdown_events
    ]
    return max(timestamp_of_shutdowns) - min(timestamp_of_shutdowns)


def main() -> None:
    print(time_between_shutdowns(loglines))


if __name__ == "__main__":
    main()
