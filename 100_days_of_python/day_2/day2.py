"""
Extract datetimes from log entries and calculate the time
between the first and last shutdown events
"""

from datetime import datetime
from datetime import timedelta
from pathlib import Path
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp_folder = Path(Path(__file__).parent, "./tmp")
tmp_folder.mkdir(parents=True, exist_ok=True)

logfile = Path(tmp_folder, "log.txt")
urllib.request.urlretrieve("http://bit.ly/2AKSIbf", logfile)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line: str) -> datetime:
    """
    Given a log line extract its timestamp and convert it to a datetime object. 
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
    datetime(2014, 7, 3, 23, 27, 51)
    """

    datetime_in_line = line.split()[1]
    return datetime.strptime(datetime_in_line, "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines: list) -> timedelta:
    """
    Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
    timedelta between the first and last one. 
    Return this datetime.timedelta object."""

    lines_with_shutdown_events = [line for line in loglines if SHUTDOWN_EVENT in line]
    timestamp_of_shutdowns = [
        convert_to_datetime(line) for line in lines_with_shutdown_events
    ]
    return max(timestamp_of_shutdowns) - min(timestamp_of_shutdowns)


def main() -> None:
    print(time_between_shutdowns(loglines))


if __name__ == "__main__":
    main()
