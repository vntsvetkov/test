

def seconds_to_time(secs: int) -> str:
    days = secs//86400
    hours = secs//3600 % 24
    minutes = secs//60 % 60
    seconds = secs % 60
    result = str(days//10) + str(days % 10) + ":" + \
             str(hours // 10) + str(hours % 10) + ":" + \
             str(minutes // 10) + str(minutes % 10) + ":" + \
             str(seconds // 10) + str(seconds % 10)
    return result


def main():
    secs = int(input("Введите количество секунд: "))
    current_time = seconds_to_time(secs)
    print(current_time)


if __name__ == "__main__":
    main()