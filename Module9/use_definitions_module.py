
"""
Brandon Treu
use_definitions_module.py

this program will import my_definitions and then run the functions within
"""
import my_definitions as my_module  # import my module

if __name__ == '__main__':
    sharks_dict = {
        'Hammerhead Sharks': 'Big',
        'Great Whites': 'Bigger',
        'Whale Sharks': 'Biggest'
    }

    mountain_ranges = (
        'Rockey Mountains',
        'Smokey Mountains',
        'Appalachian Mountains'
    )

    my_module.greeting()
    my_module.author('Deckard Cain')
    my_module.print_dict(sharks_dict)
    my_module.print_set(mountain_ranges)