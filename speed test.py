from speedtest import Speedtest
import time

def get_speed(test_type):
    print(f"Getting {test_type} speed...")
    speed = wifi.download() if test_type == 'download' else wifi.upload()
    speed_mbps = speed / 1024 / 1024
    print(f"{test_type}: {speed_mbps:.2f} mbps")

if __name__ == "__main__":
    wifi = Speedtest()
    
    get_speed('download')
    get_speed('upload')

    # Add a delay before exiting
    time.sleep(5)  # Adjust the time in seconds as needed
