import time
import itertools


class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [7, 31]], ['green', [7, 31]], ['yellow', [7, 31]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[0][1])


tl1 = TrafficLight()
tl1.running()
