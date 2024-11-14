"""
Model for aircraft flights
"""


class Flight:
    # Define initializer method or constructor
    # This is called when an object is created
    def __init__(self, number, aircraft):
        # Define instance variables
        self._number = self._validate_flight_number(number)
        self._aircraft = aircraft
        # Get rows and seats
        rows, seats = self._aircraft.seating_plan()
        # 'Waste" index 0. 
        self._seating = [None] + [{letter: None for letter in seats} 
                                  for _ in rows]
    
    def _validate_flight_number(self, number):
        # If any of the rules below fail, raise ValueError
        # Must be 5 characters long
        if len(number) != 5:
            raise ValueError(f'Invalid flight number length [{number}]')
        # First two characters (Airline Code) should be alpha
        if not number[:2].isalpha():
            raise ValueError(f'Invalid airline code [{number[:2]}]')
        # First two characters should be uppercase
        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code [{number[:2]}]')
        # Last three characters (Airline Flight Number) should be digits
        if not number[2:].isdigit():
            raise ValueError(f'Invalid flight number [{number[2:]}]')
        return number
    
    # Functions inside classes are called methods
    # This is also called a "getter" method
    # First parameter MUST be 'self' is a reference to 
    # the object that is being created
    def number(self):
        return self._number

    # This is also called a "setter" method
    def set_number(self, number):
        self._number = self._validate_flight_number(number)
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        # Validate seat letter. Ex '2B'
        letter = seat[-1]  # take last char
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')   
        # Validate the row number
        row_text = seat[:-1] # take all but last char
        try:
            row = int(row_text)  # str to int conversion
        except:
            raise ValueError(f'Invalid seat row {row_text}')   
        if row not in rows:  # valid number?
            raise ValueError(f'Invalid seat row {row_text}')   
        
        return row, letter
    
    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        # check if seat is occupied
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')
        # Otherwise is good to go
        self._seating[row][letter] = passenger
        
        
            


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    # Add setters and getters for all instance variables

    def registration(self):
        return self._registration
    
    def set_registration(self, registration):
        self._registration = registration
    
    def model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model
    
    def num_rows(self):
        return self._num_rows
    
    def set_num_rows(self, num_rows):
        self._num_rows = num_rows
        
    def num_seats_per_row(self):
        return self._num_seats_per_row
        
    def set_num_seats_per_row(self, num_seats_per_row):
        self._num_seats_per_row = num_seats_per_row
            
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK'[:self._num_seats_per_row])
            


def main():
    pass


if __name__ == '__main__':
    # Call main function
    main()
