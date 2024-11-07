from multiprocessing import Process
from datetime import datetime
import time
import random

def wait_and_print(process_id):
    # Wait for a random time between 0 and 1 second
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    # Print the process ID and the current time
    print(f"Current time: {datetime.now()}")

# Create and start three processes
if __name__ == "__main__":
    processes = [Process(target=wait_and_print, args=(i,)) for i in range(3)]
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()