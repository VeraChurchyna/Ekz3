# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:
    def_states = {'nothing':0,'first state':1, 'second state':2, 'last state':3}

    def __init__(self, _index, _state=def_states['nothing']):
        self._index = _index
        self._state = _state

    # def info(self):
    #     print(f'State of tomato is: {self._state} ')

    def grow(self):
        print('Tomato is growing')
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            print('It is last state of tomato')
            return True
        else:
            print('It is NOT last state of tomato')



# tomat = Tomato(0)
# tomat.info()
# tomat.grow()
# tomat.info()
# tomat.is_ripe()

# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов
# на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая

class TomatoBush:
    def __init__(self, number):
        self.number = number
        self.tomatoes = [Tomato(i) for i in range(number)]
        # for i in range(self.number):
        #     tomato = Tomato(i)
        #     self.tomatoes.append(tomato)

    def grow_all(self):
        # print('All tomatoes are growing')
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])


    def give_away_all(self):
        self.tomatoes = []
        print('Томатов нет')

# tomatoes=TomatoBush(5)
# tomatoes.grow_all()
# tomatoes.all_are_ripe()
# tomatoes.grow_all()
# tomatoes.all_are_ripe()
# # tomatoes.grow_all()
# # tomatoes.all_are_ripe()
#
# tomatoes.give_away_all()


# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и
# 2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели.
# Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f'Gardener {self.name} starts working')
        self._plant.grow_all()
        print(f'Gardener {self.name} stops working')


    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('урожай собран!')
        else:
            print('Еще рано собирать! Поухаживайте еще!')
    @staticmethod
    def knowlege_base():
        print('Справка по садоводству:')
#
# # 1. Вызовите справку по садоводству
# # 2. Создайте объекты классов TomatoBush и Gardener
# # 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# # 4. Попробуйте собрать урожай
# # 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# # 6. Соберите урожай
#
Gardener.knowlege_base()
tomatoes = TomatoBush(5)
gardener = Gardener('Alex',tomatoes)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
