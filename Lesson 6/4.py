from random import choice


class Car:
    """ Main car """
    direction = ["n", 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the police? {p}')

    def go(self):
        print(f'{self.name}: Car went')

    def stop(self):
        print(f'{self.name}: Car stopped')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}'


class TownCar(Car):
    """ City car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """ Cargo truck """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ Sports Car """


class PoliceCar(Car):
    """ Patrol car """

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


pc = PoliceCar('001', 'black', 150)
wc = WorkCar('002', 'white', 40)
sc = SportCar('777', 'red', 230)
tc = TownCar('000', 'yellow', 60)

loc = [pc, wc, sc, tc]

for i in loc:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
