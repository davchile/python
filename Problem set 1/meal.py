def main():
    time = input("What time is it?:")
    print(convert(time))

def convert(time):
    hours , minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes_to_hours = float((1 * minutes) / 60)
    time = hours + minutes_to_hours
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return ""
main()