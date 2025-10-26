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
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"gender{self.gender}, age{self.age}, first_name{self.first_name}, last_name{self.last_name}, record_book{self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError(f"Група {self.number} вже заповнена (ліміт 10 студентів)")
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
        all_student = ''
        if not self.group:
            all_student = "(empty)"
        else:
            all_student = "\n".join(str(s) for s in self.group)
        return f"Number:{self.number}\n{all_student}"


class GroupFullError(Exception):
    pass

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 21, 'Jon', 'A', 'AN150')
st4 = Student('Male', 19, 'Bob', 'B', 'AN144')
st5 = Student('Male', 20, 'Claudia', 'C', 'AN148')
st6 = Student('Male', 23, 'Denzel', 'D', 'AN149')
st7 = Student('Male', 20, 'Erick', 'E', 'AN141')
st8 = Student('Male', 19, 'Bill', 'F', 'AN143')
st9 = Student('Male', 23, 'Sara', 'G', 'AN146')
st10 = Student('Male', 24, 'Tris', 'H', 'AN147')
st11 = Student('Male', 22, 'Monika', 'I', 'AN140')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except GroupFullError as e:
    print(f"Не вдалося додати студента: {e}")

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!