#!/usr/bin/env python
"""
Georgia Institute of Technology - CS1301
Introduction to Object Oriented Programming using Python.
"""
__author__ = "Crawford Kennedy"
""" I worked on the homework assignment alone, using only this semester's course materials. """

class Student(object):
    """ docstring of a Student object.
    Student have the following properties:
    Attributes:
        name: A string representing the student's name. (i.e. George)
        gtid: A string representing  the student's GT id. (i.e. 1234)
        major: A Major object, representing the student's major. (i.e. <CS>)
        courses: A list representing the courses a student has taken or is currently  enrolled in. A new Student may or may not come with Courses already taken. (default to empty list)
    """

    def __init__(self, name, gtid, major, courses = []):
        self.name = name
        self.gtid = gtid
        self.major = major
        self.courses = courses
        
    def get_total_credits(self):
        """ return the student's total amount of credits as an int"""
        totalCredits = 0
        for course in self.courses:
            totalCredits += course.cresits
        return totalCredits
        

    def get_missing_credits(self):
        """ return the student's missing amount of credits to graduate as as an int (hint: Missing Credits = Required by Major - Total Credits) """
        missingCredits = self.major.required_credits - self.get_total_credits()
        if missingCredits > 0:
            return missingCredits
        return 0
        

    def get_class_standing(self):
        """ return a string representation of the student's class standing. Freshman: 0-9 credits; Sophomore: 10-19; Junior: 20-29; Senior: 30-39"""
        if self.get_total_credits() < 10:
            return 'Freshman'
        if self.get_total_credits() < 20:
            return 'Sophomore'
        if self.get_total_credits() < 30:
            return 'Junior'
        if self.get_total_credits() < 40:
            return 'Senior'
        

    def register(self, course):
        """ Add a course to the student's courses. No duplicate courses are allowed. If student is registered for X course with code "ZZ 1234", it should not be allowed to registered for Y course with code "ZZ 1234". In other words, what makes a course unique is its code. (hint: implement this in the Course class; major hint: override the __eq__ method in Course). Also, in our system a student can only register for courses that belong to his/her major."""
        used = 0
        for courses in self.courses:
            if courses == course:
                used = 1
            if not(self.major == course.major):
                used = 1
        if used == 0:
            self.courses.append(course)

    def register_many(self, courses):
        """ register courses from a list of Course objects """
        for course in courses:
            used = 0
            for course2 in self.courses:
                if course == course2:
                    used = 1
                if not(self.major == course.major):
                    used = 1
            if used == 0:
                self.courses.append(course)
    
    def is_taking(self, course):
        """ Returns true if student is registered for a course """
        for courses in self.courses:
            if courses == course:
                return True
        return False
        

    def drop(self, course):
        """ Drop a course if student is registered to it. Raise a DropNotEnrolledCourseException if student is not registered for that course. (TODO: implement this simple exception yourself, helpful toturial [http://www.programiz.com/python-programming/user-defined-exception]). Pass a message of the exception, exactly this: "Not enrolled in: {0}".format(course) """
        used = 0
        try:
            for courses in self.courses:
                if courses == course:
                    used = 1
            if used == 0:
                raise DropNotEnrolledCourseException()
        except DropNotEnrolledCourseException:
            return "Not enrolled in: {0}".format(course)
        self.courses.remove(course)
            
    # ################## #
    # DON'T CHANGE THIS: #
    # ################## #
    def __str__(self):
        """ String representation of a Student object """
        return "({0}, {1}, {2})".format(self.name, self.gtid, self.get_class_standing())


class Course(object):
    """ docstring of a Course object.
    Course have the following properties:
    Attributes:
        code: A string representing the course code (i.e CS1301)
        major: A Major object, representing the major a Course belongs to. (i.e <CS>)
        credits: An integer representing the course's amount of credits (i.e 3)
        instructor: A  string representing the instructor of the course (i.e Jay Summet)
    """

    def __init__(self, code, major, cresits, instructor):
        """Initialize a Course object whose code is *code*, credits is *cresits*, and instructor is *instructor*."""
        self.code = code
        self.cresits = cresits
        self.instructor = instructor
        self.major = major

    def __eq__(self, other):
        return self.code == other.code

    # ################## #
    # DON'T CHANGE THIS: #
    # ################## #
    def __str__(self):
        """ String representation of a Course object """
        return "({0}, {1}, {2})".format(self.code, self.cresits, self.instructor)
    def __repr__(self):
        return "<Course object: ({0}, {1}, {2})>".format(self.code, self.cresits, self.instructor)

class Major(object):
    """docstring of a Major object.
    Major have the following properties:
        Attributes:
            name: A string representing the major name (i.e CS)
            required_credits: An int representing the amount of credits required to graduate (i.e 40)
    """
    def __init__(self, name, required_credits):
        """Initialize an Instructor object whose name is *name* and required_credits are *required_credits*"""
        self.name = name
        self.required_credits = required_credits


# #################################################### #
# Implemtent your DropNotEnrolledCourseException below: #
# #################################################### #
class Error(Exception):
    pass
class DropNotEnrolledCourseException(Error):
    pass

if __name__ == '__main__':
    help(Major)
