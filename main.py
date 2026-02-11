import os
import sys
import logging
import google.cloud.logging
import time

client = google.cloud.logging.Client(project=os.getenv("PROJECT_ID"))
client.setup_logging()

if __name__ == "__main__":
    # check env provided
    start_time = time.perf_counter()
    logging.info(f"Test Run start at {start_time}")
    
    if len(sys.argv) > 1:
        logging.info(f"Received input parameter: {sys.argv[1]}")
    else:
        logging.info("No input parameter provided.")

    time.sleep(10)  # wait for logging to flush
    