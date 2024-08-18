import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        # Check if the input string contains " to ", raise ValueError if not found
        if " to " not in s:
            raise ValueError("Input format is incorrect, missing ' to '")

        # Attempt to match the input string to the expected time format using regex
        if match := re.match(
            r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s):
            # Check if a match was found
            if match:
                # Extract the matched groups (hours, minutes, periods)
                start_hour, start_minute, start_time, end_hour, end_minute, end_time = match.groups()

                # Default minutes to '00' if they are None
                start_minute = start_minute or '00'
                end_minute = end_minute or '00'
                # Convert all captured time components to integers
                start_hour, start_minute, end_hour, end_minute = map(int, [start_hour, start_minute, end_hour, end_minute])

                # Convert start hour to 24-hour format
                if start_time == "PM" and start_hour != 12:
                    start_hour += 12
                elif start_time == "AM" and start_hour == 12:
                    start_hour = 0
                # Convert end hour to 24-hour format
                if end_time == "PM" and end_hour != 12:
                    end_hour += 12
                elif end_time == "AM" and end_hour == 12:
                    end_hour = 0
                 # Validate the time components to ensure they are within valid ranges
                if (
                    not 0 <= start_hour <= 23
                    or not 0 <= start_minute <= 59
                    or not 0 <= end_hour <= 23
                    or not 0 <= end_minute <= 59
                ):
                    raise ValueError# Raise ValueError if any component is invalid
                # Return the converted time range in "HH:MM to HH:MM" format
                return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"
        raise ValueError # Raise ValueError if the regex match fails (input is in an unexpected format)






if __name__ == "__main__":
    main()
