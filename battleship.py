class BoardOutException(Exception):
    pass


board =[['O' for i in range(6)] for i in range(6)]
class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # -Тогда, чтобы проверить, находится ли точка в списке, достаточно просто использовать оператор in, как мы делали это с числами



def map():
    print('  | 1 | 2 | 3 | 4 | 5 | 6 |')
    for a, b in enumerate(board):
        print(f'{a+1} | {" | ".join(b)} |')
map()


class Board():
    def __init__(self):
        self.board = [['O' for i in range(6)] for i in range(6)]  #Двумерный список, в котором хранятся состояния каждой из клеток.
        self.ships = [3, 2, 2, 1, 1, 1, 1]  #Список кораблей доски.
        self.lives = sum(self.ships)  #Количество живых кораблей на доске
        self.hid = ...  #-Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).

    def add_ship(self, ship):  #-Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).
        for ship in ship.direction:
            if self.out(ship) or self.board[ship.y - 1][ship.x - 1] == '■':
                raise BoardOutException("Выбери друге место")
    def contour(self,):  #-Метод contour, который обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке кораблей (помечает соседние точки, где корабля по правилам быть не может).
        ...
    def open_hid(self):  #-Метод, который выводит доску в консоль в зависимости от параметра hid.
        ...
    def out(self):  #-Метод out, который для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит.
        ...
    def shot(self):  #Метод shot, который делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения).
        ...
a = Board
print(a.lives)

#выставление кораблей  #Буквой X помечаются подбитые корабли, буквой T — промахи.
class Ship():
    def __init__(self, x, y, length, direction):
        self.x = x  # Точка, где размещён нос корабля.
        self.y = y  # Точка, где размещён нос корабля.
        self.length = length  # Длина.
        self.direction = direction  # Направление корабля(вертикальное / горизонтальное).
        self.lives = length  # Количеством жизней(сколько точек корабля ещё не подбито).
    def dots(self):  #этот метод возвращает все точки корабля
        dots = []
        for i in range(self.length):
            dots.append(Dot(self.x + i * self.direction[0], self.y + i * self.direction[1]))
        return dots


