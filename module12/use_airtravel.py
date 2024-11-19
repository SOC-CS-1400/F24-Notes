"""
Test use of model for aircraft flights
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    # Make aircraft
    registration = 'G-EUPT'
    model = 'Airbus A319'
    num_rows=22 
    num_seats_per_row=6
    a = Aircraft(registration, model, num_rows, num_seats_per_row)
    # Create a flight
    f = Flight('SN060', a)
    return f # return flight

def main():
    f1 = make_flight()
    # Add a passenger
    f1.allocate_seat('12A', 'Guido van Rossum') # Python
    f1.allocate_seat('12B', 'Larry Wall') # Perl
    f1.allocate_seat('15F', 'Bjarne Stroustrup') #C++
    f1.allocate_seat('1D', 'Anders Hejlsberg') # C#
    f1.allocate_seat('1A', 'Richard Hickey') # Clojure
    f1.allocate_seat('4B', 'Yukihiro Matsumoto') # Ruby
    pp(f1._seating) # TEST
    f1.relocate_passenger('12B', '12F')
    pp(f1._seating) # TEST


if __name__ == '__main__':
    # Call main function
    main()
