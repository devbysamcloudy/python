import time
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Create the log message as a string (not inside a misplaced docstring)
        log_message = f"""
{'-' * 20}
LOG
{'-' * 20}
Timestamp: {timestamp}
Function: {func.__name__}
Time Taken: {time_taken:.4f} seconds
Inputs: args = {args}, kwargs = {kwargs}
Results = {result}
{'-' * 20}

"""
        
        # Write to log file
        with open("log.txt", "a") as file:
            file.write(log_message)
            
        return result
    return wrapper