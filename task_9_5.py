class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title}. Запуск отрисовки")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title}. Запуск отрисовки")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title}. Запуск отрисовки")


if __name__ == '__main__':
    my_pen = Pen('Ручка')
    my_pen.draw()

    my_pen = Pencil('Карандаш')
    my_pen.draw()

    my_pen = Handle('Маркер')
    my_pen.draw()
