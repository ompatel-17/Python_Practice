import datetime

#Take inputs from user
entry_date = input("Enter the entry date (DD-MM-YYYY): ")
entry_time = input("Enter the entry time (HH-MM-SS): ")
break_start_time = input("Enter the break start time (HH-MM-SS): ")
break_end_time = input("Enter the break end time (HH-MM-SS): ")
out_time = input("Enter the out time (HH-MM-SS): ")


def time_difference(entry_date, entry_time, break_start_time, break_end_time, out_time):
    
    try:
        # Convert input strings to datetime objects
        entry = datetime.datetime.strptime(entry_date + " " + entry_time, "%d-%m-%Y %H-%M-%S")
        break_start = datetime.datetime.strptime(entry_date + " " + break_start_time, "%d-%m-%Y %H-%M-%S")
        break_end = datetime.datetime.strptime(entry_date + " " + break_end_time, "%d-%m-%Y %H-%M-%S")
        out = datetime.datetime.strptime(entry_date + " " + out_time, "%d-%m-%Y %H-%M-%S")

        # Calculate the difference between entry and out time
        work_duration = out - entry

        # Calculate the difference between break start and end time
        break_duration = break_end - break_start

        # Subtract the break duration from work duration to get the actual work duration
        actual_work_duration = work_duration - break_duration

        # Divide the total seconds by 3600 to get the duration in hours
        hours = actual_work_duration.total_seconds() / 3600

        return hours
    
    except ValueError:
        
        return "Error: Invalid date/time format provided. Please enter the date and time in the correct format."


# Call the time_difference function and print the result
a = time_difference(entry_date, entry_time, break_start_time, break_end_time, out_time)

# b = 12 - (a)
print("The total working hours are:", a)
