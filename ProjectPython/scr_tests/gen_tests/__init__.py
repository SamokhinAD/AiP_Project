"""
Этот модуль объединяет тестовые функции для проверки генераторов случайных чисел.
Экспортируемые функции:
- diehard_tests: Тесты Diehard.
- nist_tests: Тесты NIST.
"""
from gen_tests.testingDiehard import diehard_tests
from gen_tests.testingNIST import nist_tests

__all__ = [
    "diehard_tests",
    "nist_tests",
]