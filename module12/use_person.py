"""Test Person Class
"""
from person import Person

def main():
    print('Testing Person class')
    p1 = Person('Waldo Weber', 18)
    print(type(p1), p1)
    p2 = Person('Superman', 120)
    print(type(p2), p2)


if __name__ == '__main__':
    # Call main function
    main()
