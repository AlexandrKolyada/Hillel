class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender{self.gender}, age{self.age}, first_name{self.first_name}, last_name{self.last_name}"

from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        base = super().__str__()
        return f"{base}, record_book{self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

class GroupFullError(Exception):
    pass

from exceptions import GroupFullError

class Group:
    CAPACITY = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.CAPACITY:
            raise GroupFullError(f"Група {self.number} вже заповнена (ліміт {self.CAPACITY} студентів)")
        self.group.add(student)

    def delete_student(self, last_name):
        s = self.find_student(last_name)
        if s is not None:
            self.group.remove(s)
        return s

    def find_student(self, last_name):
        for s in self.group:
            if s.last_name == last_name:
                return s
        return None

    def __str__(self):
        if not self.group:
            all_student = "(empty)"
        else:
            all_student = "\n".join(str(s) for s in self.group)
        return f"Number:{self.number}\n{all_student}"

from Student import Student
from group import Group
from exceptions import GroupFullError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)


assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None


gr.delete_student('Taylor')
print(gr)


more = [
    Student('M', 20, f'Name{i}', f'Last{i}', f'RB{i:03}') for i in range(3, 12)
]
for s in more[:8]:
    gr.add_student(s)

try:
    gr.add_student(more[8])
except GroupFullError as e:
    print(f"Не вдалося додати 11-го студента: {e}")
