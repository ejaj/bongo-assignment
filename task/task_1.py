def print_depth(data, depth=0):
    """
    Take a nested dictionary, print all keys with their depth.
    :param data:
    :param depth:
    :return:
    """
    for key, value in data.items():
        print(key, depth + 1)
        if isinstance(value, dict):
            print_depth(value, depth=depth + 1)
