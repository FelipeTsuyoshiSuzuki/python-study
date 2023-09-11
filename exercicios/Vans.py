def main():
    distance, speed, time = input().split(" ")
    print(loop_count(int(distance), int(speed), int(time)))


def loop_count(distance, speed, time):
    distance_traveled = (speed * 1000) * time
    return int(distance_traveled / distance)


if __name__ == "__main__":
    main()