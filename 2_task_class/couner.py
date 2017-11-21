"""
1. Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в
 заданном диапазоне.
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Счетчик имеет два метода: увеличения и уменьшения,
— и свойство, позволяющее получить его текущее состояние.
Написать программу, демонстрирующую все возможности класса.
"""


class Counter:
    """
    Счетчик может ходит вниз и забираться вверх.
    position - текущая позиция в счетчике.
    """

    @staticmethod
    def decrease():
        return 'decrease'

    @staticmethod
    def increase():
        return 'increase'

    def __init__(self,first=0,last=10,enter=0):
        """
        Инифицализация
        :param first: Начала границы счетчика
        :param last: Окончание границы счетчика
        :param enter: Позиция входа в счетчик
        """
        self.begin, self.end, self.position = first, last, enter
        self.MODE = 'increase'

    def __next__(self):
        if self.MODE == 'increase':
            if self.position == self.end:
                self.position = self.begin
            else:
                self.position += 1
            return self.position
        if self.MODE == 'decrease':
            if self.position == self.begin:
                self.position = self.end
            else:
                self.position -= 1
            return self.position


print("Демонстрация возможностей класса:\n")
print("Инициализируем счетчик по умолчанию: \ncount = Counter()")
count = Counter()
print("Проверяем начальную позицию счетчика: {}".format(count.position))
# Запоминаем позицию, для расчета отклонения.
diff = count.position
up = 4
print("Вызываем последовательно next(count) {} раза.".format(up))
for _ in range(up):
    next(count)
print("После выхова next(count), ожидаем позицию счетчика {1}, а она: {0}".format(count.position, diff + up))
print("Меняем режим счетчика на уменьшение: \ncount.MODE = Counter.decrease()")
count.MODE = Counter.decrease()
down = 17
# Запоминаем позицию, для расчета отклонения.
diff = count.position
print("Вызываем последовательно next(count) {} раза. В режиме уменьшения".format(down))
for _ in range(down):
    next(count)
print("После выхова next(count), ожидаем позицию счетчика {1}, а она: {0}, правильно, границы {2}:{3} и счетчик считает по кругу".format(count.position, diff - down, count.begin, count.end))
print("\n")
start_counter, end_couter, position_counter = 5, 200, 67
print("Инициализируем счетчик по значениям: \ncount = Counter({}, {}, {})".format(start_counter, end_couter, position_counter))
count = Counter(start_counter, end_couter, position_counter)
print("Проверяем начальную позицию счетчика: {}".format(count.position))
# Запоминаем позицию, для расчета отклонения.
diff = count.position
up = 27
print("Вызываем последовательно next(count) {} раза.".format(up))
for _ in range(up):
    next(count)
print("После вызова next(count), ожидаем позицию счетчика {1}, а она: {0}".format(count.position, diff + up))
print("Меняем режим счетчика на уменьшение: \ncount.MODE = Counter.decrease()")
count.MODE = Counter.decrease()
down = 92
# Запоминаем позицию, для расчета отклонения.
diff = count.position
print("Вызываем последовательно next(count) {} раза. В режиме уменьшения".format(down))
for _ in range(down):
    next(count)
print("После вызова next(count), ожидаем позицию счетчика {1}, а она: {0}, правильно, границы {2}:{3} и счетчик считает по кругу".format(count.position, diff - down, count.begin, count.end))