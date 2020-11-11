from drunk import NormalDrunk
from field import Field
from coordinate import Coordinate

def walking(field, drunker, steps):
    src = field.get_coordinate(drunker)

    for _ in range(steps):
        field.move_drunker(drunker)

    return src.distance(field.get_coordinate(drunker))

def simulate_random_path(steps, attemps, drunk_kind):
    drunker = drunk_kind(name='V')

    src = Coordinate(0, 0)
    distances = []

    for _ in range(attemps):
        field = Field()
        field.add_drunker(drunker, src)
        simulate_walking = walking(field, drunker, steps)
        distances.append(round(simulate_walking, 1))

    return distances

def main(distance_to_walk, attemps, drunk_kind):

    for steps in distance_to_walk:
        distance = simulate_random_path(steps, attemps, drunk_kind)
        avg = round(sum(distance) / len(distance), 4)
        max_distance = max(distance)
        min_distance = min(distance)
        print(f'{drunk_kind.__name__} has made {steps} steps')
        print(f'The avg distance is {avg} and the max distance is {max_distance} the min distance is {min_distance}')


if __name__ == '__main__':

    distance_to_walk = [10, 100, 1000, 10000]
    attemps = 100

    main(distance_to_walk, attemps, NormalDrunk)
