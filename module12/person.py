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


def main():
    pass


if __name__ == '__main__':
    # Call main function
    main()
