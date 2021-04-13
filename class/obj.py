'''stepic.org, тесты, задачи на тему ООП'''


# ------------------------------------------------------------------------------
import random


class A:
    def __init__(self, val=0):
        self.val = val

    #
    def add(self, x):
        self.val += x

    #
    def print_val(self):
        print(self.val)


#
a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)
#
a.print_val()
b.print_val()
c.print_val()


# --------------------------------------------------------------------------
class Hero():
    '''Класс создаем героя для игры'''

    def __init__(self, name, race, level, force, magic, intelligence):
        self.name = name
        self.race = race
        self.level = level
        self.force = force
        self.magic = magic
        self.intelligence = intelligence

    '''Добавляем методы'''

    def name(self):
        pass

    def race(self):
        pass

    def level(self):
        pass

    def force(self):
        pass

    def magic(self):
        pass

    def intelligence(self):
        pass


# ----------------------------------------
class Point3D():
    '''Класс для хранения координат'''
    arr_xy = []  # Для хран. координат

    def __init__(self, coordinat=None):
        self.coordinat = Point3D.arr_xy.append(coordinat)


pt = Point3D(123)
print(Point3D.arr_xy)


class Point(Point3D):
    '''Дочерний класс '''

    def __init__(self, coordinat=0):
        self.coordinat = Point3D.arr_xy.append(coordinat)


pt1 = Point('erwer')
print(Point3D.arr_xy)


# --
# ------------------------------------------------------------------------------------
class MoneyBox():
    '''Класс копилка задание stepic.org'''
    list_box = []  # список для добалнения значений

    def __init__(self, capacity):  # Конструктор. вх. значение вместительность list_box
        self.capacity = capacity
        self.count = 0

    #
    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        return False

    #
    def add(self, v):
        if self.can_add(v):
            self.count += v


#
x = MoneyBox(10)
x.add(5)
x.add(3)
x.add(0)
print(x.can_add(2))
# print(x.can_add(2))
# -
print(x.capacity)
print('*' * 20)


# -------------------------------------------------------------------------------------
class Buffer:
    '''Класс Buffer, задание stepic.org'''

    def __init__(self):
        self.list = []

    '''Метод добавления элементов. в список и вывод.'''
    '''def add(self, *a):
        for i in a: self.list.append(i)   # Добавляем в список
        #print(self.list)
        while len(self.list) >= 5:  # Пока длинна >= 5 выполняем...
            summa = 0; count = 0    # Сумма, счетчик элементов.
            for i in self.list:     # Бежим по списку.
                summa += (i); count +=1 # Подсчитываем сумму и счетчик
                if count == 5:
                    print(summa)
                    for j in self.list[:count]: # Отсекаем первую пятёрку элементов
                        self.list.remove(j)
                    i, j = 0, 0      # Обнуляем сумму, счетчики циклов.
                    #print(self.list)'''
    ''' !! Более улучшенный метод добавления и посчета'''

    def add(self, *a):
        for i in a:  # Бежим по кортежу
            self.list.append(i)  # Добавляем в список
            if len(self.list) == 5:  # если длинна списока составила 5 элем.
                print(sum(self.list))  # Выводим сумму всех элементов
                self.list.clear()  # Очищаем список из 5 елементов, и возвращ. в начало цикла

    '''Вернуть сохраненные в текущий момент элементы последовательности в порядке, 
    в котором они были добавлены'''

    def get_current_part(self):
        # if len(self.list) < 5:
        return self.list


# -
b = Buffer()
# b.add(*range(42**4))
# print(b.get_current_part())
# ------------------------------------------------------------------------------------
'''Тестируем map, lambda'''
lst = [*range(1, 1500)]


def sqr_func(iter):
    return (iter * 2) // 2 ** 5


def run():
    m = list(map(sqr_func, lst))
    return m


# print(run())
'''---------------------------'''


# ---------------------- Наследование---------------------------
class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1
        print(self.val)

    def add_many(self, x):
        for i in range(x):
            print('add_one_Base')
            self.add_one()


class Derived(Base):
    def add_one(self):
        print('add_one_Dereved')
        self.val += 10
        print(self.val)


# a = Derived()
# a.add_one()

b = Derived()
b.add_many(3)

# print(a.val)
print(b.val)


# --     --------------------------------------------
class A:
    def foo(self):
        print("A")


class B(A):
    pass


class C(A):
    def foo(self):
        print("C")


class D:
    def foo(self):
        print("D")


class E(B, D, C):
    pass


E().foo()
print('-' * 30)
# ------------- Задача stepic.org наследование классов ---------
PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/test_class'
#
def read_file(P):
    with open(P, 'r') as file:
        data = []
        for i in file.readlines():
            data.append(''.join(i.strip().replace(':', '').split()))
        return data

'''['4', 'A', 'BA', 'CA', 'DBC', '4', 'AB', 'BD', 'CD', 'DA']'''
#
dict_data = {} # словарь для добавл. предков, классов.
#p = read_file(PATH)         # список возвр. ф-ц.read_file(PATH)
#
def add_class():
    for i in range(1, int(p[0]) + 1):
        if len(p[i]) == 1:
            dict_data[p[i][0]] = ['None']
        else:
            dict_data[p[i][0]] = [','.join(p[i][1:])]
    print(dict_data)
#
#add_class()
#
def get_sum():
    d = [i for i in p[1:] if i.isdigit()]
    k = ''.join(d)
    return int(k)+1
#
def get_class(p):
    p = p[1:]
    for i in p[get_sum():]:
        print(i[0],i[1])
#
#get_class(p)
#
'''Алгоритм DFS «Depth-first search» или «Поиск в глубину»'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    #print(start, visited)
    #print(graph[start] - visited)
    for next in graph[start] - visited:
        #print(next + ' След. итерация')
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))
#
print('-'*30)
s = [[j for j in range(random.randint(2,4))] for i in range(3)]
print(s)

visit = [False]*len(s[0]+s[1]+s[2])
print(visit)
def dfs1(c):
    visit[c] = True
    print(visit)
    for i in s[c]:
        print(i)
        if not visit[i]:
            dfs1(i)
dfs1(0)
#


#----------------------------------------------------------
class Myx1:
    def __init__(self):
        self.val = 3
#
lst = list()
i = 0
while i < 10:
    #m = "{i}".format
    m = Myx1()
    lst.append(m)
    i += 1
    #print(Myx1.__str__(m), m.val, "!!")
# ---------------------------------------------------------------
print('-' * 30)
print(getattr(pt, "y", 'Такого значения нет.'))  # Возвр. значен. атрибута, а если нет, выводит текст.
print(hasattr(pt, "i"))  # Проверяет на наличии атрибута.
setattr(pt, "c", 122)  # Задает значение атрибута, если его нет, то создает его.
print(pt.__dict__)  # Выводит все атр. в экземпляре класса
print(pt.__doc__)  # выводит строку с описанием класса, если нет ()
print(Point3D.__name__)  # выводит имя класса
print(isinstance(pt, Point3D))  # проверяет принадлежность объекта к классу.
# ---------------------------------------------------------------
