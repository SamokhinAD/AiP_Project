"""
Этот модуль сравнивает генераторы случайных чисел с помощью тестов Diehard и NIST.
Результаты выводятся в виде таблицы.
"""
from scr.gens import *
from scr_tests.gen_tests import *

num: int = 1000

gen1 = bbs_generator()
gen2 = lagged_fibonacci_generator()
print('поводи мышкой пжпж')
gen3 = fortuna()
gen4 = isaac_generator()
m: int = 2_147_483_648
a: int = 594_156_893
c: int = 75_692
seed: int = 123_456_789
gen5 = linear_congruential_generator(m, a, c, seed)
gen6 = maclaren_marsaliya_generator()
gen_arr = [gen1,gen2,gen3,gen4,gen5,gen6]

diehard_res = []
nist_res = []

for gen in gen_arr:
    diehard_res.append(diehard_tests(gen,num))
for gen in gen_arr:
    nist_res.append(nist_tests(gen,num))

print('')
print('                                      Result Table YooHooo')
print('')
print('                ','           BBS     Fib   Fortuna  ISAAC    LCM    MacMar   ')
print('                ','diehard',' ',diehard_res[0],' ',diehard_res[1],' ',diehard_res[2],' ',diehard_res[3],' ',diehard_res[4],' ',diehard_res[5])
print('                ',' NIST  ',' ',nist_res[0],'  ',nist_res[1],' ',nist_res[2],' ',nist_res[3],' ',nist_res[4],' ',nist_res[5])
print('')