import logging
import os
from datetime import datetime
def setup_logger():
    """Sets up the logger for ETL process."""
    log_filename = f"logs/etl_log_{datetime.now().strftime('%Y_%m_%d')}.txt"
    file_path=os.path.join(os.path.dirname(__file__), '..', log_filename)
    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Also show logs in console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))
    logging.getLogger().addHandler(console)
    logging.info("Logger initialized")
    return logging