from student import Student
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
    Student('M', 20, f'Name{i}', f'Last{i}', f'RB{i:03}') for i in range(3, 13)
]

for s in more[:9]:
    gr.add_student(s)


try:
    gr.add_student(more[9])
except GroupFullError as e:
    print(f"Не вдалося додати 11-го студента: {e}")
