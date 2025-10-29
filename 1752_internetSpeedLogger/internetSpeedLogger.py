import speedtest
import datetime
import os
import time

# --- Configuration ---

# The name of the file where results will be saved.
LOG_FILE = "internet_speed_log.csv"

# How many seconds to wait between tests.
# 3600 = 1 hour
# 900 = 15 minutes
WAIT_TIME_SECONDS = 20

# --- End Configuration ---


def get_internet_speeds():
    """
    Runs a speed test and returns download and upload speeds in Mbps.
    """
    try:
        st = speedtest.Speedtest()
        
        # We can find the best server, but this adds time.
        # For logging, it's good to be consistent.
        # st.get_best_server() 
        
        print("Running download test...")
        # Get speeds in bits per second
        download_bits = st.download()
        
        print("Running upload test...")
        # Get speeds in bits per second
        upload_bits = st.upload()
        
        # Convert bits per second to megabits per second (Mbps)
        # 1,000,000 bits = 1 megabit
        download_mbps = download_bits / 1_000_000
        upload_mbps = upload_bits / 1_000_000
        
        return download_mbps, upload_mbps
        
    except speedtest.ConfigRetrievalError:
        print("Error: Could not retrieve speedtest configuration.")
        print("Please check your internet connection.")
        return None, None
    except Exception as e:
        print(f"An error occurred during the speed test: {e}")
        return None, None

def log_speeds(logfile, download, upload):
    """
    Appends the speed test results to a CSV log file.
    Creates the file and adds a header if it doesn't exist.
    """
    # Check if file exists to determine if we need a header
    file_exists = os.path.isfile(logfile)
    
    # 'a' means 'append' mode. 'newline=' is important for CSVs.
    with open(logfile, 'a', newline='') as f:
        # Get current time for the timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if not file_exists:
            # Write the header row if it's a new file
            f.write("Timestamp,Download_Mbps,Upload_Mbps\n")
        
        # Write the data row
        f.write(f"{timestamp},{download:.2f},{upload:.2f}\n")
    
    print(f"Logged: {timestamp}, {download:.2f} Mbps Down, {upload:.2f} Mbps Up")

def main():
    print("--- Internet Speed Logger ---")
    print(f"Logging to: {LOG_FILE}")
    print(f"Checking speed every {WAIT_TIME_SECONDS / 60} minutes.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            download_speed, upload_speed = get_internet_speeds()
            
            if download_speed is not None:
                log_speeds(LOG_FILE, download_speed, upload_speed)
            
            print(f"Waiting for {WAIT_TIME_SECONDS} seconds...")
            time.sleep(WAIT_TIME_SECONDS)
            
    except KeyboardInterrupt:
        print("\nLogger stopped. Exiting.")

if __name__ == "__main__":
    main()