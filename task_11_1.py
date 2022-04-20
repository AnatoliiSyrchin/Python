class Date:
    def __init__(self, date_string):
        self.day, self.month, self.year = self.convert_date(date_string)
        self.validate_date(self.day, self.month, self.year)

    @classmethod
    def convert_date(cls, date):
        return map(int, date.split('-'))

    @staticmethod
    def validate_date(day, month, year):
        is_leap = True if not year % 4 and not (bool(year % 100) ^ bool(year % 400)) else False
        assert 1 <= month <= 12, ('месяц может быть от 1 до 12')
        if month == 2:
            month_days = 29 if is_leap else 28
            assert 1 <= day <= month_days, (f'число может быть от 0 до {month_days}')
        else:
            month_days = 30 + (month + (month // 8)) % 2
            assert 1 <= day <= month_days, (f'число может быть от 0 до {month_days}')

    def __str__(self):
        return f'число: {self.day}, месяц: {self.month}, год: {self.year}'


if __name__ == '__main__':
    import datetime

    current_date = datetime.datetime.now().strftime('%d-%m-%Y')
    print(current_date)
    my_date = Date(current_date)
    print(my_date)

    test_date = '30-02-22'
    print(test_date)
    my_date_2 = Date(test_date)
    print(my_date_2)
