
import time
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        log_message = f"""
        print("-" * 20)
        print("LOG")
        print("-" * 20)
        print(f"Timestamp: {timestamp}")
        print(f"Function: {func.__name__}")
        print(f"Time Taken: {time_taken} seconds")
        print(f"inputs: args = {args}, kwargs = {kwargs}")
        print(f"Results = {result}")
        print("-" * 20)
        return result
    return wrapper
"""

        with open ("log.txt","a") as file:
            file.write(log_message)

    return wrapper


    