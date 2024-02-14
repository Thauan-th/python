from abc import ABC
from uuid import uuid4


class Person(ABC):

    def __init__(self: object, name: str) -> None:
        self.__name = name  # private attribute - dunder convention

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        self.__name = name


class Student(Person):

    def __init__(self: object, name: str, course: str) -> None:
        super().__init__(name)
        self.__course = course
        self.__course_id = self.__generate_course_id()

    @property
    def course(self: object) -> str:
        return self.__course

    @course.setter
    def course(self: object, course: str) -> None:
        self.__course = course

    @property
    def course_id(self: object) -> str:
        return self.__course_id

    def __generate_course_id(self: object) -> str:
        return str(uuid4()).split("-")[-1]


if __name__ == "__main__":
    person = Person("John")
    student = Student("Mary", "Computer Science")

    print(person.name)
    print(student.name)

    print(student.course)
    print(student.course_id)
