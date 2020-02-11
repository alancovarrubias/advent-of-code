FILENAME = "files/06.txt"
CENTER_OF_MASS = "COM"
SANTA = "SAN"
YOU = "YOU"

def get_orbits(filename):
    with open(filename) as f:
        orbits = list(map(lambda x: x.rstrip().split(")"), f.readlines()))
        return orbits
        
orbits = get_orbits(FILENAME)
orbit_map = {}
for orbit in orbits:
    center = orbit[0]
    orbiter = orbit[1]
    if center in orbit_map:
        orbit_map[center].append(orbiter)
    else:
        orbit_map[center] = [orbiter]

orbit_map["total"] = 0
orbit_map["level"] = 0
def count_orbits(orbit_map, orbiters):
    next_orbiters = []
    for orbiter in orbiters:
        if orbiter in orbit_map:
            next_orbiters.extend(orbit_map[orbiter])
        orbit_map["total"] += orbit_map["level"]
    orbit_map["level"] += 1
    if next_orbiters:
        count_orbits(orbit_map, next_orbiters)

# count_orbits(orbit_map, [CENTER_OF_MASS])
# print(orbit_map["total"])

def find_path(orbit_map, orbiters, search):
    if search in orbiters:
        return [search]
    else:
        paths = []
        for orbiter in orbiters:
            if orbiter in orbit_map:
                path = find_path(orbit_map, orbit_map[orbiter], search)
                paths.append([orbiter] + path)
            else:
                paths.append([orbiter])
        search_paths = list(filter(lambda path: search in path, paths))
        if search_paths:
            return search_paths[0]
        else:
            return []

you_path = find_path(orbit_map, [CENTER_OF_MASS], YOU)
santa_path = find_path(orbit_map, [CENTER_OF_MASS], SANTA)

index = 0
while True:
    if you_path[index] != santa_path[index]:
        break
    index += 1
index += 1
min_orbit_transfers = len(you_path) - index + len(santa_path) - index
print(min_orbit_transfers)
