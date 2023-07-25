"""
Custom Logging Library to log errors to a file for debugging
"""
from datetime import datetime

class Logger:

    def __init__(self, logfile = 'ErrorLog.log') -> None:
        
        self.logfile = logfile

    def log(self, error):
        '''
        Log the error to a custom file
        Ensure the the file is appended
        '''
        print(error)
        with open(self.logfile, 'a') as f:
            timestamp = datetime.now()
            f.write(f'{timestamp}: {error}\n')
