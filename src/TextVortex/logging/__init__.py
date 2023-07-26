import os 
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
# This format will include the timestamp of the log message, 
# the log level (e.g., INFO, ERROR, WARNING), 
# the module where the log message originates from, 
# and the actual log message itself.
log_dir = "logs" 
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok = True)
 

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("TextVortextLogger")