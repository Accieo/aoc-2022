from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Beacon:
    x: int
    y: int

@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon
    distance: int = 0

def find_blocked(sensors: list[Sensor], y: int) -> int:
    """Finds the blocked spots at a given height y."""

    blocked_ranges = list()
    near_target = list()
    for sensor in sensors:
        up = sensor.y - sensor.distance
        down = sensor.y + sensor.distance
        if up <= y <=  down:
            near_target.append(sensor)

    for sensor in near_target:
        dist_to_target = y - abs(sensor.y)
        width = sensor.distance - abs(dist_to_target)
        blocked_ranges.append((sensor.x - width, sensor.x + width))

    min_x = min([x for x, _ in blocked_ranges])
    max_x = max([x for _, x in blocked_ranges])
    total = abs(min_x - max_x)
        
    return total

def common():
    with open('input/day15.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))

        sensors = list()
        for line in data:
            sensor, beacon = line.split(':')
            sx, sy = sensor.split('=')[1:3]
            sx = sx.replace(', y', '')
            bx, by = beacon.split('=')[1:3]
            bx = bx.replace(', y', '')
            beacon = Beacon(x=int(bx), y=int(by))
            sensor = Sensor(x=int(sx), y=int(sy), beacon=beacon)
            sensor.distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
            sensors.append(sensor)

    return sensors

def part_one():
    sensors = common()

    blocked = find_blocked(sensors=sensors, y=2_000_000)

    return blocked

def part_two():
    return

if __name__ == '__main__':
    print(part_one())
    print(part_two())
