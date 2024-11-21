"""Define a Person Class
"""


class Person:
    def __init__(self, name, age):
        """Person class initializer

        Args:
            name (str): name
            age (int): age
        """
        self._name = name
        self._age = age

    def __str__(self):
        """String representation of object

        Returns:
            str: Person's information
        """
        return f"Person's info, name[{self._name}], age[{self._age}]"

    def __eq__(self, other):
        """Comparison Operator

        Args:
            other (Person): Object to compare to

        Raises:
            TypeError: Incorrect Type

        Returns:
            Boolean: True if objects have same age, False otherwise
        """
        if not isinstance(other, Person):  # check if other is type Person
            raise TypeError('Unsupported operand type == for these objects')
        return self._age == other._age  # True or False


def main():
    pass


if __name__ == '__main__':
    # Call main function
    main()
