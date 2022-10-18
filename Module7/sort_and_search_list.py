"""
Brandon Treu
sort_and_search_list.py

This program will sort and then search a list
"""
list = [25, 20, 15, 10, 5]
#Write sort_list() to sort the list
def sort_list(list):
    try:
        list.sort()
    except ValueError:
        return #i need to retun my sorted list so it can be printed

#Write search_list()
def search_list(list, number):
    try:
        index_listing = list.index(number)
    except ValueError:
        return -1
    else:
        pass #no need to return anything since this is a copy


if __name__ == '__main__':
    sort_list(list)
    search_list(list, 1)
    print(list)
