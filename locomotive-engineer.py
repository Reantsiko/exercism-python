"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagons = []
    for arg in args:
        wagons.append(arg)
    return wagons


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    for i in range(2):
        if i == 2:
            break
        wagon = each_wagons_id.pop(0)
        each_wagons_id.append(wagon)
    missing_wagons.reverse()
    for missing_wagon in missing_wagons:
        each_wagons_id.insert(1, missing_wagon)
    return each_wagons_id


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route['stops'] = list(kwargs.values())
    return route


# TODO: define the 'extend_route_information()' function
def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    for key in more_route_information:
        route[key] = more_route_information[key]
    return route


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows: list) -> list:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    wagons = []
    for i in range(len(wagons_rows)):
        wagon_column = []
        wagon_column.append(wagons_rows[0][i])
        wagon_column.append(wagons_rows[1][i])
        wagon_column.append(wagons_rows[2][i])
        wagons.append(wagon_column)
    return wagons
