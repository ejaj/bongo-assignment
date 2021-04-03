class Person(object):
    """
    A class to represent a Person.

    ...
    Attributes
    ----------
    first_name : str
        first name of the person
    last_name : str
        last_name name of the person
    father : str
        father of the person
    """

    def __init__(self, first_name, last_name, father):
        """
        Constructs all the necessary attributes for the person object.
        :param first_name:
        :param last_name:
        :param father:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return self.first_name + " " + self.last_name


def print_depth(data, depth=1):
    """
    Take a nested dictionary and Person Object, print all keys with their depth.
    :param data:
    :param depth:
    :return:
    """
    if isinstance(data, Person):
        print_family_details(data, depth)
        if isinstance(data.father, Person):
            print_depth(data.father, depth + 1)

    elif isinstance(data, dict):
        for key in data:
            print(key, depth)
            if isinstance(data[key], object):
                print_depth(data[key], depth + 1)


def print_family_details(person, depth):
    """
    Print family details.

    :param person:
    :param depth:
    :return:
    """
    print_fields = ["first_name", "last_name", "father"]
    for field in print_fields:
        print(getattr(person, field), depth)
