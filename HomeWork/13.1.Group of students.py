class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender{self.gender}, age{self.age}, first_name{self.first_name}, last_name{self.last_name}"

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!