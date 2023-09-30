def funk(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, str):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict


print(funk(name='Sergey', age=44, city='Moscow'))
