from classes.Car import Car
from classes.Street import Street
from classes.Intersection import Intersection
from classes.Input import Input

import os


def open_file(file_name: str) -> Input:

    base_path = os.path.dirname(os.getcwd())
    in_path = os.path.join(base_path, 'data', 'in', f'{file_name}.txt')

    cars = []
    streets = []
    traffic_lights = []
    intersections = []

    with open(in_path, mode='r', encoding='utf8', newline='\n') as in_file:
        # get all lines stripped
        lines = [line.rstrip('\n') for line in in_file]

        # first line contains infos
        first_line = lines[0].split(' ')
        sim_duration = int(first_line[0])
        nr_intersections = int(first_line[1])
        nr_streets = int(first_line[2])
        nr_cars = int(first_line[3])
        bonus_points = int(first_line[4])

        # streets
        for input_index in range(1, nr_streets+1): # the next n (number of streets) lines are streets
            street_line = lines[input_index].split(' ')

            origin_id = int(street_line[0])
            finish_id = int(street_line[1])
            street_id = street_line[2]
            length = int(street_line[3])

            street = Street(
                id=street_id,
                origin=origin_id,
                finish=finish_id,
                length=length,
            )
            streets.append(street)

        # cars
        car_index = 0
        for input_index in range(nr_streets+1, len(lines)):
            car_line = lines[input_index].split(' ')

            car_id = car_index
            car_index += 1
            num_streets_planned = len(car_line) - 1
            car_streets = []

            for street in car_line[1:]:
                street_id = street
                car_streets.append(street)

            car = Car(
                id=car_id,
                num_streets_planned=num_streets_planned,
                planned_streets=car_streets,
                current_street=car_streets[0],
                next_street=car_streets[1],
            )

            cars.append(car)

    input_data = Input(sim_duration=sim_duration,
                       cars=cars,
                       streets=streets,
                       traffic_lights=traffic_lights,
                       intersections=intersections
                       )

    # INTERSECTIONS
    for intersection_index in range(0, nr_intersections):

        incoming_streets = []
        for street in streets:
            if street.finish == intersection_index:
                incoming_streets.append(street)

        intersection = Intersection(
            id=intersection_index,
            nrIncomingStreets=len(incoming_streets),
            incomingStreets=incoming_streets
        )

        intersections.append(intersection)

    return input_data


if __name__ == '__main__':
    open_file('a')
