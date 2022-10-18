"""
Brandon Treu
function_keyword_and_arbitrary_arguments.py

this program will accept key word arguments, then iterate through them and produce an average number to output
"""


def average_scores(*args, **kwargs):
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name')
    major = kwargs.get('major')
    # Use *args for average calculation
    var_count = 0
    total = 0
    for i in args:
        var_count += 1
        total += i
    gpa = str(total / var_count)
    print('Result: Name ' + str(first_name) + ' ' + str(last_name) + ' ' + 'course = ' + str(
        major) + ' ' + 'with current average ' + gpa)
# no need to return anting here since im printing it out on the last iteration


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
