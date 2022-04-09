from window import Window


class TrafficLight:

    def __init__(self):
        self.__color = 'красный'

    # я хотел сделать по заданию, но всё пошло не по плану)
    # сильно не пинайте, я почти не спал и мне кажется, что это шедевр)))
    def running(self):
        window = Window()
        window.run()


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
