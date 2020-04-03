'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import urllib.request

def convert_to_datetime(line: str) -> datetime:
    '''TODO 1:
    Given a log line extract its timestamp and convert it to a datetime object. 
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
    datetime(2014, 7, 3, 23, 27, 51)'''
    


def time_between_shutdowns(loglines):
    '''TODO 2:
    Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
    timedelta between the first and last one. 
    Return this datetime.timedelta object.'''
    
def main() -> None:
    SHUTDOWN_EVENT = 'Shutdown initiated'

    # prep: read in the logfile
    tmp_folder = Path(Path(__file__).parent, './tmp')
    tmp_folder.mkdir(parents=True, exist_ok=True)

    logfile = Path(tmp_folder, 'log.txt')
    urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

    loglines = logfile.read_text()

    



if __name__ == "__main__":
    main()
