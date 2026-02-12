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
    #print(f"Test Run start at {start_time}")
    logging.info(f"Test Run start at {start_time}")
    
    project=os.getenv("PROJECT_ID")
    #print(f'project_name: {project}')
    logging.info(f"project_name: {project}")
    
    bucket_name=os.getenv("BRONZE_BUCKET") 
    #print(f'bucket_name: {bucket_name}')
    logging.info(f"bucket_name: {bucket_name}")
    
    if len(sys.argv) > 1:
        #print(f"Received input parameter: {sys.argv[1]}")
        logging.info(f"Received input parameter: {sys.argv[1]}")
    else:
        #print("No input parameter provided.")
        logging.info("No input parameter provided.")

    time.sleep(10)  # wait for logging to flush
    