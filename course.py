'''William Martell P3: Linked List Recursive'''

class Course():
    '''Creates a course with default empty values and has callable functions to receive the 
    information'''
    def __init__(self, _number = 0,_name = "", _credit_hr=0.0, _grade=0.0):
        if not isinstance(_number, int):
            raise ValueError("You must enter a course number.")
        if _number < 0:
            raise ValueError("Course number must be positive.")
        self._number = _number

        if not isinstance(_name, str):
            raise ValueError("You must enter a course number.")
        self._name = _name

        if not isinstance(_credit_hr, float)and not isinstance(_credit_hr,int):
            raise ValueError("Invalid amount of credit hours.")
        if _credit_hr < 0:
            raise ValueError("Credit hours must be positive.")
        self._credit_hr = _credit_hr

        if not isinstance(_grade, float) and not isinstance(_grade, int):
            raise ValueError("Invalid Grade entered.")
        if _grade < 0:
            raise ValueError("Grade point average must be a positive number.")
        self._grade = _grade
        self.next = None

    def name(self):
        '''returns the name of the class'''
        return self._name

    def number(self):
        '''returns the class number'''
        return int(self._number)

    def credit_hr(self):
        '''returns the number of credit hours the course contains'''
        return float(self._credit_hr)

    def grade(self):
        '''returns the grade of the course'''
        return self._grade

    def __str__(self):
        '''prints the course and all of the information that the course contains'''
        return f'cs{str(self.number())} {self.name()} Grade:{str(self.grade())} Credit Hours: {str(self.credit_hr())}'
        
