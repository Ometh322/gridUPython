"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {'a': 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    input_items = dict(items_to_set)
    for input_key, input_value in input_items.items():
        if len(dict_to_update.items()) > 0:
            for k, v in dict_to_update.items():
                if input_key == k and input_value > v:
                    dict_to_update[k] = input_value
        else:
            dict_to_update[input_key] = input_value
    return dict_to_update


set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
