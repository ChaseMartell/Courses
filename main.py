'''William Martell 
CS Project: Linked List Recursive'''

from courselist import CourseList
from course import Course

def main():
    '''Creates a Course list, reads the data.txt file for information, and prints 
    out the list of courses along with the cumulative GPA.'''
    clpractice = CourseList()
    with open("data.txt") as information:
        for i in information:
            info = i.split(',')
            clpractice.insert(Course(int(info[0]),info[1],float(info[2]),
            float(info[3].rstrip('\n'))))
    information.close()

    gpa = clpractice.calculate_gpa()
    print("Current List: ("+str(clpractice.size())+")")
    for course in clpractice:
        print(course)
    print(f'\n\n\nCumulative GPA: {str(round(gpa,3))}')



if __name__ == "__main__":
    main()
