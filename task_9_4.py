class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        turn = {
            'left': 'налево',
            'right': 'направо'
        }
        print(f'машина {self.name} повернула {turn[direction]}.')

    def show_speed(self):
        print(f'Ваша скорость: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'Ваша скорость: {self.speed}.') if self.speed <= 60 else print(
            f'Ваша скорость: {self.speed}. Вы превысили скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Ваша скорость: {self.speed}.') if self.speed <= 40 else print(
            f'Ваша скорость: {self.speed}. Вы превысили скорость!')


class PoliceCar(Car):

    def show_speed(self):
        if self.is_police:
            print(f'Вы на полицейской машине, зачем вам знать скорость?')
        else:
            print(f'Это обычная машина в полицейской окраске. За это наказывают!')


if __name__ == '__main__':

    my_new_car = WorkCar(100, 'red', 'lada')
    my_new_car.turn('left')
    my_new_car.show_speed()

    my_sport_car = SportCar(300, 'yellow', 'ra-ta-ta')
    my_sport_car.show_speed()

    my_police_car = PoliceCar(100, 'white-blue', 'police', True)
    my_police_car.show_speed()

    my_not_police_car = PoliceCar(100, 'white-blue', 'fake_police')
    my_not_police_car.show_speed()
