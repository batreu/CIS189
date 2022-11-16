"""
Brandon Treu
topic3io.py

this program will create a .txt file and write to it, then it will get information from the .txt file, then read from
the .txt file, it will take user input and lastly update information on the file then print.
"""

# Write to a file before read from a file
def write_to_file(info_file):
    f = open('test_scores.txt', 'a')
    f.write(str(info_file))
    f.close()


def get_student_info(**scores):
    for key, value in scores.items():
        print(value)
    score = 0
    info_file = [scores]
    while score >= 0:
        try:
            score = int(input("Enter your score or enter -1 to quit: "))
        except ValueError:
            print("Entr numbers only for scores.")
        else:
            if score == -1:
                break
            else:
                info_file.append(score)
    write_to_file(info_file)

# read
def read_from_file():
    f = open('test_scores.txt', "r")
    line = f.readline()
    print(line)
    f.close()

# driver
if __name__ == '__main__':
    get_student_info(name='Robert')
    get_student_info(name='Jessica')
    get_student_info(name='Oliver')
    get_student_info(name='Noah')
    read_from_file()
