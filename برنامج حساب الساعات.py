def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

input_seconds = int(input("Enter the number of seconds: "))
hours, minutes, seconds = convert_seconds_to_hms(input_seconds)
print(f"{input_seconds} seconds is equal to: {hours} hours, {minutes} minutes, {seconds} seconds")
