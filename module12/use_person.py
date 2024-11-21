"""Test Person Class
"""
from person import Person

def main():
    print('Testing Person class')
    p1 = Person('Waldo Weber', 18)
    print(type(p1), p1)
    p2 = Person('Superman', 18)
    print(type(p2), p2)
    if p1 == p2:
        print('You are the same age')


if __name__ == '__main__':
    # Call main function
    main()
