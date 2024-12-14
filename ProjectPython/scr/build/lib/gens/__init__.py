"""
Модуль объединяет основные генераторы случайных чисел, предоставляемые пакетом gens.

Экспортируемые генераторы:
- linear_congruential_generator: Линейный конгруэнтный генератор.
- lagged_fibonacci_generator: Генератор на основе лагового ряда Фибоначчи.
- bbs_generator: Генератор Блюм-Блюм-Шуба.
- isaac_generator: Генератор ISAAC.
- maclaren_marsaliya_generator: Генератор Макларена-Марсальи.
- fortuna: Генератор Fortuna.
"""
from gens.AlgBBS_PRNG import bbs_generator
from gens.Fibon_PRNG import lagged_fibonacci_generator
from gens.Fortuna_auto import fortuna
from gens.ISAAC import isaac_generator
from gens.LCM import linear_congruential_generator
from gens.MM_PRNG import maclaren_marsaliya_generator

__all__ = [
    "linear_congruential_generator",
    "lagged_fibonacci_generator",
    "bbs_generator",
    "isaac_generator",
    "maclaren_marsaliya_generator",
    "fortuna"
]