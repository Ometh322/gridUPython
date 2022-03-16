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
from typing import Dict, Union


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    input_items: Dict[str, int] = dict(items_to_set)
    for input_key, input_value in input_items.items():
        cur_value: Union[str, int] = dict_to_update.get(input_key, 'no_key')
        if cur_value == 'no_key' or cur_value < input_value:
            dict_to_update[input_key] = input_value
    return dict_to_update


set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
