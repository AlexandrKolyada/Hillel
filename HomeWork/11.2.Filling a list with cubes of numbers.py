def generate_cube_numbers(end):

    # i = 2
    for i in range(2, end + 1):
        cube = i ** 3
        if cube >= end:
            return
        else:
            yield cube

from  inspect import isgenerator

gen = generate_cube_numbers(10)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], '10 у кубі це 1000'
print('OK')
