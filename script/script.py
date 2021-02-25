from utility import in_reader, out_writer
from classes import Input
from classes.Schedule import Schedule
from classes.Submission import Submission


def main():

    file_names = ['a', 'b', 'c', 'd', 'e', 'f']

    # ALL THE FILES
    for file_name in file_names:

        # read in the input
        input: Input = in_reader.open_file(file_name=file_name)

        # create all schedules
        schedules = []

        # Create master list of planned streets from cars
        all_planned_streets = []
        for car in input.cars:
            # Iterate through all streets to be able to assign individual street name and not whole list
            for planned_street in car.planned_streets.id:
                all_planned_streets.append(planned_street)

        # get list with individual street names
        all_planned_streets_unique_set = set(all_planned_streets)
        all_planned_streets_unique = list(all_planned_streets_unique_set)

        # create dictionary
        dict = {}
        for street in all_planned_streets_unique:
            dict[street] = all_planned_streets.count(street)

        # look for intersection streets in dictionary
        for intersection in input.intersections:
            dict_intersection = {}
            for street_name in intersection.incomingStreets:
                count = dict[street_name.id]
                dict_intersection[street_name.id] = count
            # sort dictionary
            dict_intersection = dict_intersection(sorted(x.items(), key=lambda item: item[1]))

            # create dictionary to hold street name and time
            street_time = []  # String array
            for street in dict_intersection:
                time = str(2)  # tbd
                street_time.append(street + ' ' + time)  # as a String
            # create new schedule object
            new_schedule = Schedule(intersection.id,
                                    intersection.nrIncomingStreets,
                                    street_time)
            # add new schedule object to schedule array
            schedules.append(new_schedule)

        # create submission object
        num_intersections = len(input.intersections)
        submission = Submission(num_intersections, schedules)

        # write the output file in /data
        out_writer.write_file(file_name=file_name, input=submission)


if __name__ == '__main__':
    main()
