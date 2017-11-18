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
    def __init__(self,first=0,last=10,enter=0):
        """
        Инифицализация
        :param first: Начала границы счетчика
        :param last: Окончание границы счетчика
        :param enter: Позиция входа в счетчик
        """
        self.begin, self.end, self.position = first, last, enter

    def __next__(self):
        if self.position == self.end:
            self.position = self.begin
        else:
            self.position += 1
        return self.position

    def prev(self):
        if self.position == self.begin:
            self.position = self.end
        else:
            self.position -= 1
        return self.position

print("Create Counter with default init.")
count = Counter()
print("Position of counter: {}".format(count.position))
up = 4
for _ in range(up):
    next(count)
print("Position of counter after increase of {1}: {0}".format(count.position,up))
down = 17
for _ in range(down):
    count.prev()
print("Position of counter after decrease of {1}: {0}\n".format(count.position, down))

s,e,p = (5,200,67)
print("Create Counter with custom params. Start in {}, End in {}, Start position is {}".format(s,e,p))
count = Counter(first=s,last=e,enter=p)
print("Position of counter: {}".format(count.position))
up = 27
for _ in range(up):
    next(count)
print("Position of counter after increase of {1}: {0}".format(count.position,up))
down = 92
for _ in range(down):
    count.prev()
print("Position of counter after decrease of {1}: {0}".format(count.position, down))