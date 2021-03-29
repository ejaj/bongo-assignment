def print_depth(d, depth=0):
    """
    passed nested dictionary, print all keys with their depth.
    :param d:
    :param start:
    :return:
    """
    for key, value in d.items():
        print(key, depth + 1)
        if isinstance(value, dict):
            print_depth(value, depth=depth + 1)


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a)
