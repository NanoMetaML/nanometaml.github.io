import itertools

def pick_items_from_dict_lists(dict_of_lists):
    # Get the keys and lists from the dictionary
    keys = list(dict_of_lists.keys())
    lists = list(dict_of_lists.values())

    # Generate the Cartesian product of all lists
    combinations = list(itertools.product(*lists))

    # Create a list of key-value pairs for each combination
    result = [{keys[i]: item[i] for i in range(len(keys))} for item in combinations]
    return result

# Example usage:
if __name__ == "__main__":
    dict_of_lists = {
        'numbers': [1, 2, 3],
        'letters': ['a', 'b'],
        'symbols': ['X', 'Y', 'Z']
    }

    result = pick_items_from_dict_lists(dict_of_lists)
    print(result)

