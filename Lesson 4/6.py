from itertools import count, cycle
my_count = count(7)
my_cycle = cycle('ABC')

for i in range(5):
    print('(my_count, my_cycle) = ({},{})'.format(next(my_count), next(my_cycle)))
