import os
import sys
import logging

'''
levelname   ==  what level of log
module      ==  if running template.py ; then it will log that module name
message     ==  what is the message that is to be in that log

fileHandler is to generate log file
StreamHandler to print in the terminal
'''

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # a standard way to log

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("cnnClassifierLogger")