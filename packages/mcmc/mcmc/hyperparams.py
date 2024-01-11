import itertools

def getHyperParamVector(hyperParams):
    # Get the keys and lists from the dictionary
    keys = list(hyperParams.keys())
    lists = list(hyperParams.values())

    # Generate the Cartesian product of all lists
    combinations = list(itertools.product(*lists))

    # Create a list of key-value pairs for each combination
    result = [{keys[i]: item[i] for i in range(len(keys))} for item in combinations]
    return result
