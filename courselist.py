'''William Martell 
CS Project: Linked List Recursive'''


from recursioncounter import RecursionCounter
from course import Course

TOTAL_CREDITS = 0.0
TOTAL_GRADE_POINTS = 0.0

class CourseList():
    '''Creates a list of courses'''
    def __init__(self):
        '''Creates the course list with the head of None'''
        self.head = None
        self.cursor = self.head
    
    def size(self):
        '''returns the number of items in the list'''
        return self.__size_helper(self.head)

    def __size_helper(self, cursor):
        '''Helps the size function find the size'''
        RecursionCounter()
        if cursor is None:
            return 0
        return 1 + self.__size_helper(cursor.next)



    def find(self, number):
        '''Looks through the linked list to find a specific course number'''
        if self.head is None:
            return -1

        return self.__find_helper(self.head, number)

    def __find_helper(self, cursor, number):
        '''Helps the find function search for the course number in the linked list'''
        RecursionCounter()
        if cursor is None:
            return -1

        if cursor._number == number:
            return cursor

        if cursor._number is not None:
            return self.__find_helper(cursor.next, number)

        return -1



    def calculate_gpa(self):
        '''Calculates the GPA of all of the courses inside of the linked list'''
        if self.head is None:
            return 0.0
        return self.__calculate_gpa_helper(self.head,TOTAL_CREDITS,TOTAL_GRADE_POINTS)

    def __calculate_gpa_helper(self, cursor, TOTAL_CREDITS, TOTAL_GRADE_POINTS):
        '''Helps calculate the GPA of the courses'''
        RecursionCounter()
        if cursor is not None:
            TOTAL_CREDITS += cursor._credit_hr
            TOTAL_GRADE_POINTS += (cursor._grade * cursor._credit_hr)
            return self.__calculate_gpa_helper(cursor.next, TOTAL_CREDITS, TOTAL_GRADE_POINTS)

        return TOTAL_GRADE_POINTS / TOTAL_CREDITS



    def is_sorted(self):
        '''returns True if the list is sorted by the Course number, false otherwise'''
        return self.__is_sorted_helper(self.head)

    def __is_sorted_helper(self, cursor):
        '''Helps the is_sorted function determine if the list is sorted or not'''
        RecursionCounter()
        if cursor is None or cursor.next is None:
            return True
        if cursor.number() > cursor.next.number():
            return False
        return self.__is_sorted_helper(cursor.next)



    def insert(self,course):
        '''Inserts a course into the linked list'''
        #If head is equal to none
        if self.head is None:
            self.head = course

        else:
        #call recursively and find where it goes
            self.head = self.__insert_helper(self.head, course)

    def __insert_helper(self, cursor, course):
        '''Helps the insert function insert a course'''
        RecursionCounter()
        #base case
        if cursor is None:
            return course

        if course.number() < cursor.number():
            course.next = cursor
            return course

        cursor.next = self.__insert_helper(cursor.next, course)
        return cursor



    def remove(self,number):
        '''remove the first occurrence of the specified course'''
        previous = None
        current = self.head
        if self.head is None:
            return self.head

        return self.__remove_helper(self.head, number, previous, current)

    def __remove_helper(self, cursor, number, previous, current):
        '''Helps the remove function remove a specified course from the linked list'''
        RecursionCounter()
        if cursor is None:
            return self.head

        if cursor._number == number:
            previous.next = cursor.next


        if cursor._number != number:
            previous = current
            current = cursor.next
            return self.__remove_helper(cursor.next, number, previous, current)

        return self.head

    def remove_all(self, number):
        '''removes all occurrences of the specified course'''
        previous = None
        current = self.head
        while (self.head is not None and current._number == number):
            self.head = current.next
            current = self.head
        while current is not None:
            while current is not None and current._number != number:
                previous = current
                current = current.next
            if current is None:
                return self.head
            previous.next = current.next
            current = previous.next
        return self.head



    def __iter__(self):
        '''Iterate through the list.'''
        self.cursor = self.head
        return self

    def __next__(self):
        '''Goes to the next value and returns it'''
        if self.cursor is None:
            raise StopIteration
        course = self.cursor
        self.cursor = self.cursor.next
        return course

    def __str__(self):
        pass
