def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

time_input = "01:50:06"
seconds = convert_to_seconds(time_input)
print(f"{time_input} is equal to {seconds} seconds.")
