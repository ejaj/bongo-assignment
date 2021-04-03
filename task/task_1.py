def print_depth(data, depth=1):
    """
    Take a nested dictionary, print all keys with their depth.
    :param data:
    :param depth:
    :return:
    """
    for key in data:
        print(key, depth)
        if isinstance(data[key], dict):
            print_depth(data[key], depth + 1)
