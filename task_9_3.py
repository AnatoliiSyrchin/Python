class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._Worker__income['wage'] + self._Worker__income['bonus']


if __name__ == '__main__':
    worker_name = 'Ivan'
    worker_surname = 'Ivanov'
    worker_position = 'worker'
    worker_wage = 15000
    worker_bonus = 20000
    new_worker = Position(worker_name, worker_surname, worker_position, worker_wage, worker_bonus)
    print(f'У сотрудника {new_worker.get_full_name()} общий доход {new_worker.get_total_income()}')
