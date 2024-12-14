from pynput import mouse
import hashlib
import time

class Fortuna_auto():
    """
    Класс для генерации случайных чисел с использованием данных о движении мыши 
    и хеширования с алгоритмом SHA-256. Использует метод Fortuna для генерации случайных чисел.

    Атрибуты:
        coord (str): Строка для хранения координат мыши в бинарном виде.
        flag (bool): Флаг, указывающий, активен ли процесс сбора координат.
        hesh_pul (int): Переменная для хранения текущего хеша, используется для генерации чисел.
        coef (int): Коэффициент для обрезки сгенерированного числа.
        self_gen (generator): Генератор случайных чисел.

    Методы:
        on_move(x, y):
            Обрабатывает события движения мыши, собирая координаты для генерации случайных чисел.
        gen():
            Генерирует случайные числа на основе хеша координат мыши и текущего времени.
        next_num():
            Возвращает следующее случайное число от генератора.
        start_listen():
            Запускает слушатель событий мыши для получения координат.
    """
    def __init__(self):
        """
        Инициализирует объект класса Fortuna_auto.
        Создает переменные для хранения координат, флага сбора данных, хеша, коэффициента 
        и генератора случайных чисел.
        """
        self.coord = ''
        self.flag = True
        self.hesh_pul = 0
        self.coef = 8
        self.self_gen = 0
    
    def on_move(self,x,y):
        """
        Обрабатывает события движения мыши, собирает координаты и запускает генератор чисел.

        :param x: Координата по оси X.
        :param y: Координата по оси Y.
        
        Возвращает False, когда длина собранных данных достигает 256 бит, что инициирует 
        запуск генератора случайных чисел.
        """
        if self.flag == True:
            self.coord += (bin(x)[2:]+bin(y)[2:])
            if len(self.coord) >= 256:
                self.self_gen = self.gen()
                next(self.self_gen)
                return False
    
    def gen(self):
        """
        Генератор случайных чисел на основе хеширования координат и текущего времени.

        Генерирует случайные числа, используя хеш SHA-256 от координат мыши и текущего времени.
        Процесс генерирования чисел запускается после сбора достаточного объема данных.

        :yield: Следующее случайное число, обрезанное по коэффициенту `coef`, в 32-битном формате.
        """
        self.flag = False
        while True:
            new_hesh = int(hashlib.sha256(self.coord.encode('utf-8')).hexdigest(),16)
            self.hesh_pul ^= new_hesh
            self.coord = str(self.hesh_pul)
            tme = str(time.time())
            ind = tme.index('.')
            yield int(str(self.hesh_pul ^ int(tme[:ind] + tme[ind+1:]))[:self.coef],32)

    def next_num(self):
        """
        Возвращает следующее случайное число от генератора.

        :return: Следующее случайное число, генерируемое методом `gen()`.
        """
        return next(self.self_gen)
    
    def start_listen(self):
        """
        Запускает слушатель событий мыши.

        Инициализирует слушателя движения мыши и запускает его в отдельном потоке.
        Ожидает завершения работы слушателя.
        """
        mouse_listener = mouse.Listener(on_move=self.on_move)
        mouse_listener.start()
        mouse_listener.join()

def fortuna():
    """
    Запускает генератор случайных чисел, используя объект Fortuna_auto.

    Создает экземпляр Fortuna_auto, начинает слушать события мыши и генерирует случайные числа.

    :yield: Следующее случайное число, генерируемое объектом Fortuna_auto.
    """
    fart = Fortuna_auto()
    fart.start_listen()
    while True:
        yield fart.next_num()