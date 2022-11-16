"""
Brandon Treu
dictionary_test_example.py

this is just for unit testing
"""

def in_dict(fun_dict, search):
    try:
        return search in fun_dict
    except Exception:
        raise




if __name__ == '__main__':
    d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    print(in_dict(d, 'A'))