"""
Test use of model for aircraft flights
"""
from airtravel import Flight, Aircraft


def main():
    print(Flight)
    f1 = Flight('SN060') # use parentheses to call the constructor
    print(f'F1 Flight type {f1}')
    print(f'F1 Flight number {f1.number()}')
    
    f2 = Flight('DL123') # use parentheses to call the constructor
    print(f'F2 Flight number {f2.number()}')
    f2.set_number('DL456')
    print(f'F2 Flight number {f2.number()}')
    
    # f3 = Flight('DL12344') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('9L123') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('dl123') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('DL1A3') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    f3 = Flight('DL193') # use parentheses to call the constructor
    print(f'F3 Flight number {f3.number()}')

    registration = 'G-EUPT'
    model = 'Airbus A319'
    num_rows=22 
    num_seats_per_row=6
    a1 = Aircraft(registration, model, num_rows, num_seats_per_row)
    print(f'Aircraft type {type(a1)}')
    print(f'Aircraft registration {a1.registration()}')
    print(f'Aircraft model {a1.model()}')
    a1.set_model('Boeing 777')
    print(f'Aircraft model {a1.model()}')
    print(f'Aircraft num_rows {a1.num_rows()}')
    print(f'Aircraft num_seats_per_rows {a1.num_seats_per_row()}')


if __name__ == '__main__':
    # Call main function
    main()
