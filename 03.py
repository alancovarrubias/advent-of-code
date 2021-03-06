SEPARATOR = ","
FILENAME = "files/03.txt"

def distance_traveled(intersection):
    return intersection[2] + intersection[3]

def manhattan_distance(intersection):
    return abs(intersection[0]) + abs(intersection[1])

def find_intersections(wire1, wire2):
    intersections = []
    p2 = [0, 0, 0]
    for dir1 in wire1:
        p1 = p2.copy()
        p2[0] += dir1[0]
        p2[1] += dir1[1]
        p2[2] += max(abs(dir1[0]), abs(dir1[1]))

        if p1[0] == p2[0]:
            static_index = 0
            dynamic_index = 1
        elif p1[1] == p2[1]:
            static_index = 1
            dynamic_index = 0

        q2 = [0, 0, 0]
        for dir2 in wire2:
            q1 = q2.copy()
            q2[0] += dir2[0]
            q2[1] += dir2[1]
            q2[2] += max(abs(dir2[0]), abs(dir2[1]))

            # [x, y, d1, d2]
            intersection = [0, 0, 0, 0]
            intersection[static_index] = p1[static_index]
            if ((q1[static_index] < p1[static_index] and q2[static_index] > p1[static_index]) or
                (q1[static_index] > p1[static_index] and q2[static_index] < p1[static_index])):
                intersection[dynamic_index] = q2[dynamic_index]
                if ((p1[dynamic_index] < q2[dynamic_index] and p2[dynamic_index] > q2[dynamic_index]) or
                    (p1[dynamic_index] > q2[dynamic_index] and p2[dynamic_index] < q2[dynamic_index])):
                    intersection[2] = p1[2] + abs(q2[dynamic_index] - p1[dynamic_index])
                    intersection[3] = q1[2] + abs(p2[static_index] - q1[static_index])
                    intersections.append(intersection)
        return intersections

def convert_instruction(instruction):
    magnitude = int(instruction[1:])
    direction = instruction[0]
    if direction == "R":
        return [magnitude, 0]
    elif direction == "U":
        return [0, magnitude]
    elif direction == "L":
        return [-magnitude, 0]
    elif direction == "D":
        return [0, -magnitude]

def build_wire(line):
    instruction_list = line.split(SEPARATOR)
    direction_list = list(map(convert_instruction, instruction_list))
    return direction_list

def build_wires(filename):
    with open(filename) as f:
        line1 = f.readline().rstrip()
        line2 = f.readline().rstrip()
        wire1 = build_wire(line1)
        wire2 = build_wire(line2)
        return wire1, wire2

wire1, wire2 = build_wires(FILENAME)
intersections = find_intersections(wire1, wire2)
manhattan_distances = list(map(manhattan_distance, intersections))
distances_traveled = list(map(distance_traveled, intersections))
print(manhattan_distances)
print(distances_traveled)
