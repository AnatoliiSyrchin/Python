class Road:
    # вес одного квадратного метра асфальта толщиной 1 см
    one_m2_weight = 25
    # и толщина слоя в см
    height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculating_weight(self):
        # вес одного слоя в кг
        one_layer_weight = self._length * self._width * self.one_m2_weight
        # возвращаем вес всех слоев в тоннах
        return one_layer_weight * self.height * 10 ** -3


if __name__ == '__main__':
    road_length = 20
    road_width = 5000
    my_road = Road(road_length, road_width)
    print(f'Масса асфальта, необходимого для покрытия всей дороги :'
          f'{my_road.calculating_weight():0.2f} тонн')
