class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        if min_value > max_value:
            raise ValueError("min_value не може бути більшим за max_value")
        if not (min_value <= current <= max_value):
            raise ValueError("Початкове значення поза межами [min_value, max_value]")
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("current поза дозволеним діапазоном")
        self.current = start

    def set_max(self,max_max):
        if max_max < self.min_value:
            raise ValueError("max_value не може бути меншим за min_value")
        if self.current > max_max:
            raise ValueError("Поточне значення перевищує новий максимум")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("min_value не може бути більшим за max_value")
        if self.current < min_min:
            raise ValueError("Поточне значення менше нового мінімуму")
        self.min_value = min_min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимуму")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімуму")

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'