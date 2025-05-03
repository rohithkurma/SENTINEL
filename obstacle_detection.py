from gpiozero import DistanceSensor

left = DistanceSensor(echo=19, trigger=20)
right = DistanceSensor(echo=18, trigger=17)
back = DistanceSensor(echo=6, trigger=5)

def check_obstacles():
    if left.distance < 0.25:
        return 'turn_right'
    elif right.distance < 0.25:
        return 'turn_left'
    elif back.distance < 0.25:
        return 'stop'
    return 'forward'
