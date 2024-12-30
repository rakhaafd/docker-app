import time

LOG_FILE = "/data/log.txt"

def main():
    print("Starting application...")
    while True:
        with open(LOG_FILE, "a") as file:
            file.write(f"Timestamp: {time.ctime()}\n")
            print(f"Timestamp written: {time.ctime()}")
        time.sleep(5)  # Write every 5 seconds

if __name__ == "__main__":
    main()