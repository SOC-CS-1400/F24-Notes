"""
Test use of model for aircraft flights
"""
from airtravel import Flight, Aircraft, AirbusA319, Boeing777
from pprint import pprint as pp


def make_flight():
    # Make aircraft
    registration = 'G-EUPT'
    model = 'Airbus A319'
    num_rows = 22
    num_seats_per_row = 6
    a = Aircraft(registration, model, num_rows, num_seats_per_row)
    # Create a flight
    f1 = Flight('SN060', a)
    # Add a passenger
    f1.allocate_seat('12A', 'Guido van Rossum')  # Python
    f1.allocate_seat('12B', 'Larry Wall')  # Perl
    f1.allocate_seat('15F', 'Bjarne Stroustrup')  # C++
    f1.allocate_seat('1D', 'Anders Hejlsberg')  # C#
    f1.allocate_seat('1A', 'Richard Hickey')  # Clojure
    f1.allocate_seat('4B', 'Yukihiro Matsumoto')  # Ruby
    pp(f1._seating)  # TEST
    f1.relocate_passenger('12B', '12F')
    pp(f1._seating)  # TEST
    return f1  # return flight


def make_many_flights():
    a1 = AirbusA319('G-EUPT')
    f1 = Flight('BA758', a1)
    f1.allocate_seat('12A', 'Guido van Rossum')  # Python

    f2 = Flight('AF782', Boeing777('F-GSPS'))
    f2.allocate_seat('4B', 'Yukihiro Matsumoto')  # Ruby

    return f1, f2


def main():
    # f1 = make_flight()
    f1, f2 = make_many_flights()
    print(f'f1 model {f1.aircraft_model()}')
    print(f'f2 model {f2.aircraft_model()}')


if __name__ == '__main__':
    # Call main function
    main()
