def move_robot(direction, sign):
    if sign == 'stop':
        print("STOPPING")
    elif sign == 'turn left' and direction != 'turn_right':
        print("TURNING LEFT")
    elif sign == 'turn right' and direction != 'turn_left':
        print("TURNING RIGHT")
    elif direction == 'forward':
        print("MOVING FORWARD")
    else:
        print("DEFAULT ACTION")
