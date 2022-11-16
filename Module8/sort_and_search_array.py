"""
Brandon Treu
sort_and_search_array.py

this will sort and search an array and return output
"""
import array as arr

# declare my array
a = arr.array('i', [11, 22, 33, 44, 55, 66])

# function to search my array
def search_array(a,number):
    try:
        index_array = a.index(number)
        print(index_array)
        return index_array
    except ValueError:
        return -1


# there is no sort for array that I could find, so first make it a list, then sort
def sort_array(a):
    a_list = a.tolist()
    a_list.sort()
    print(a_list)





if __name__ == '__main__':
    search_array(a,55)
    sort_array(a)

