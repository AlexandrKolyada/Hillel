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
