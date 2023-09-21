from random import randint
from time import perf_counter
import tracemalloc
from tkinter import *

class MultiTask():
    def __init__(self):
        
        self.tasks_condition = {1: '\n#Задача 1\nCоставить программу обмена значениями трех переменных а, b, c:\nтак, чтобы b присвоилось значение c, с присвоить значение а,\na присвоить значение b. Затратить на это минимум строк\n', 2.1: '\n#Задача 2.1\nКонсольная программа.\nПользователь вводит 2 числа. Проверьте, что это именно числа,\nесли это не так, то выведите пользователю ошибку и попросите ввести число снова.\nКогда пользователь ввел числа, выведите сумму этих чисел.\n', 2.2: '\n#Задача 2.2\nДоработайте задачу так, чтобы пользователь мог вводить n разных чисел.\nПредоставьте возможность ввести n самому пользователю.\n', 3.1: '\n#Задача 3.1\nДано число x, которое принимает значение от 0 до 100. Вычислите чему будет равно x^5\n', 3.2: '\n#Задача 3.2\nИзмените задачу так, чтобы для вычисления степени использовалось только умножение.\n\n+0.5 балла: посмотрите сколько времени и памяти занимают оба метода.\nЧто можно сделать для оптимизации данной задачи?\n', 4: '\n#Задача 4\nПользователь может вводить число от 0 до 250.\nПроверьте, принадлежит ли введенное число числам Фибоначчи.\n', 5: '\n#Задача 5\nРеализуйте программу двумя способами на определение времени года\nв зависимости от введенного месяца года.\n', 6: '\n#Задача 6\nПосчитайте сумму, количество четных и нечетных чисел от 1 до N. N вводит пользователь.\n', 7: '\n#Задача 7\nДля каждого из чисел от 1 до N, где N меньше 250 выведите количество делителей.N вводит пользователь.\nВыведите число и через пробел количество его делителей. Делителем может быть 1.\n\n+0.5 балла: сколько памяти и времени занимает программа,\nчто можно сделать для оптимизации затрачиваемых ресурсов?\n', 8: '\n#Задача 8\nНайти все различные пифагоровы тройки из интервала от N до М.\n', 9: '\n#Задача 9\nНайти все целые числа из интервала от N до M, которые делятся на каждую из своих цифр.\n', 10: '\n#Задача 10\nНатуральное число называется совершенным, если оно равно сумме всех своих делителей, \nвключая единицу. Вывести первые N (N<5) совершенных чисел на экран.\n', 11: '\n#Задача 11\nЗадайте одномерный массив в коде и выведите в консоль\nпоследний элемент данного массива тремя способами.\n\n+0.5 балла: сравните их по времени выполнения.\n', 12: '\n#Задача 12\nЗадайте одномерный массив в коде и выведите в консоль массив в обратном порядке.\n', 13: '\n#Задача 13\nРеализуйте нахождение суммы элементов массива через рекурсию.\nМассив можно задать в коде.\n', 14.1: '\n#Задача 14.1\nРеализуйте оконное приложение-конвертер рублей в доллары.\nСоздайте окно ввода для суммы в рублях.\n', 14.2: '\n#Задача 14.2\nДоработайте приложение так, чтобы можно было переводить доллары в рубли.\n', 15: '\n#Задача 15\nРеализуйте вывод таблицы умножения в консоль размером n на m\nкоторые вводит пользователь, но при этом они не могут быть больше 20 и меньше 5.\n', 16: '\n#Задача 16\nРеализуйте вывод в консоль поле для морского боя с выставленными кораблями.\nДанные о кораблях, можно подгружать из файла или генерировать самостоятельно.'}
        
        print('\nВведите номер задания (при необходимости через точку): ', end = '')
        while True:
            try:
                self.task = float(input())
            except ValueError:
                print('\nВведён неверный номер задачи, попробуйте ещё раз: ', end = '')
            else:
                if self.task not in self.tasks_condition.keys():
                    print('\nВведён неверный номер задачи, попробуйте ещё раз: ', end = '')
                    continue
                self.task_choser()
                break
        
    def task_choser(self):
        print(self.tasks_condition[self.task])
        if self.task == 1:
            self.task_1()
        elif self.task == 2.1:
            self.task_2_1()
        elif self.task == 2.2:
            self.task_2_2()
        elif self.task == 3.1:
            self.task_3_1()
        elif self.task == 3.2:
            self.task_3_2()
        elif self.task == 4:
            self.task_4()
        elif self.task == 5:
            self.task_5()
        elif self.task == 6:
            self.task_6()
        elif self.task == 7:
            self.task_7()
        elif self.task == 8:
            self.task_8()
        elif self.task == 9:
            self.task_9()
        elif self.task == 10:
            self.task_10()
        elif self.task == 11:
            self.task_11()
        elif self.task == 12:
            self.task_12()
        elif self.task == 13:
            self.task_13()
        elif self.task == 14.1:
            self.task_14_1()
        elif self.task == 14.2:
            self.task_14_2()
        elif self.task == 15:
            self.task_15()
        elif self.task == 16:
            self.task_16()
            
    def task_1(self):
        a, b, c = 1, 2, 3
        print('a = ', a, 'b = ', b, 'c = ', c)
        a, b, c = b, c, a
        print('\na = ', a, 'b = ', b, 'c = ', c)
        
    def task_2_1(self):
        while True:
            try:
                num1 = float(input('Первое число: '))
                num2 = float(input('Второе число: '))
                print('Сумма: ', num1 + num2)
                break
            except ValueError:
                print('Введены не числа, попробуйте ввести снова:')
        
    def task_2_2(self):
        while True:
            sum = 0
            try:
                for _ in range(int(input('Введите n: '))):
                    num = float(input('Введите число: '))
                    sum += num
                print('Сумма: ', sum)
                break
            except ValueError:
                print('Введены не числа, попробуйте ввести снова:')
                
    def task_3_1(self):
        x = randint(0, 100)
        print('x = ', x, ', x^5 = ', x ** 5)

    def task_3_2(self):
        x = randint(0, 100)
        
        def prog_1():
            return x ** 5
        
        def prog_2():
            return x * x * x * x * x
            
        time_start = perf_counter()
        tracemalloc.start()
        prog_1()
        memory_1 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time_1 = perf_counter() - time_start 
        
        time_start = perf_counter()
        tracemalloc.stop()
        tracemalloc.start()
        prog_2()
        memory_2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time_2 = perf_counter() - time_start
        
        print('x = ', x, ', x^5 = ', x * x * x * x * x)
        print('Как мы видим в кортежах ниже (введите номер задания >1 раз), занимаемая память не меняется,\nно затрачиваемое время в способе, при возведении в степень, увеличивается в 3, 4, а то и в 5 раз\nв отличие от способа с последовательным умножением.\nДля оптимизации данной задачи я не нашёл ничего особенного и реально оптимизирующего,\nтак как степень всего лишь 5, а число не такое большое, просто следует\nперемножать число само на себя 4 раза.')
        print(memory_1, time_1 * 100000)
        print(memory_2, time_2 * 100000)
    
    def task_4(self):
        num = int(input('Введите число: '))
        if 0 <= num <= 250 and num in [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]:
            print('Число Фибоначчи')
        else:
            print('Не число Фибоначчи')
    
    def task_5(self):
        month = int(input('Введите месяц числом: '))
        month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
        for key, value in month_dict.items():
            if month in value:
                print('Это', key)
    
    def task_6(self):
        total_sum, even_num, odd_num = 0, 0, 0
        for i in range(1, int(input('Введите N: ')) + 1):
            total_sum += i
            if i % 2 == 0:
                even_num += 1
            else:
                odd_num += 1

        print('Сумма чисел:', total_sum, '\nКоличество четных чисел:', even_num, '\nКоличество нечетных чисел:', odd_num)
    
    def task_7(self):
        def div_finder():
            for num in range(1, int(input('Введите N: ')) + 1):
                div_sum = 0
                for div in range(1, num + 1):
                    if num % div == 0:
                        div_sum += 1
                print(num, 'Кол-во делителей:', div_sum)
                
        time_start = perf_counter()
        tracemalloc.start()
        div_finder()
        memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time = perf_counter() - time_start 
        
        print(memory, time)
        print('Выше показаны затрачиваемая память и время. Для оптимизации, например, можно вместо\nперебора всех делителей num от 1 до num, брать диапазон от 1 до num//2 + 1,\nчтобы не брать числа, которые при умножении на 2 точно больше num.')
            
    def task_8(self):
        N, M = int(input('Введите N: ')), int(input('Введите M: '))
        for a in range(N, M + 1):
            for b in range(a, M + 1):
                for c in range(b, M + 1):
                    if a ** 2 + b ** 2 == c ** 2:
                        print(a, b, c)
    
    def task_9(self):
        N, M = int(input('Введите N: ')), int(input('Введите M: '))
        for num in range(N, M + 1):
            for sym in str(num):
                if int(sym) == 0 or num % int(sym) != 0:
                    flag = False
                    break
                flag = True
            if flag:
                print(num)
    
    def task_10(self):
        N, total, num = int(input('Введите N: ')), 0, 1
        while total != N:
            sum = 0
            for div in range(1, num//2 + 1):
                if num % div == 0:
                    sum += div
            if num == sum:
                print(num)
                total += 1
            num += 1
    
    def task_11(self):
        def met_1():
            print(mas[-1])
        
        def met_2():
            new_mas = mas[-1:]
            print(*new_mas)
        
        def met_3():
            print(mas.pop())
        
        mas = [1, 2, 3, 4, 5]
        
        time_start = perf_counter()
        met_1()
        time_1 = perf_counter() - time_start
        
        time_start = perf_counter()
        met_2()
        time_2 = perf_counter() - time_start
        
        time_start = perf_counter()
        met_3()
        time_3 = perf_counter() - time_start
        
        print(time_1 * 1000, time_2 * 1000, time_3 * 1000, sep = '\n')
        print('Сколько ни запускай это задание, всегда показывает разное время выполнения всех способов\nи каждый из них имеет разное место по скорости, поэтому не могу их нормально сравнивать,\nвсе примерно одинаковы.')
    
    def task_12(self):
        mas = [1, 2, 3, 4, 5]
        print(mas[::-1])
    
    def task_13(self):
        def mas_sum(ind, total):
            if ind == -1:
                return total
            else:
                total += mas[-ind]
                return mas_sum(ind - 1, total)
        
        mas = [1, 2, 3, 4, 5]
        total = 0
        print('Массив:', mas,'\nСумма элементов массива:', mas_sum(len(mas) - 1, total))
    
    def task_14_1(self):
        def to_dol():
            rub_sum = round(int(amount_rub.get()) / 96.62, 2)
            conv_to_dol['text'] = str(rub_sum) + ' $'
        
        window = Tk()
        window.attributes('-topmost', True)
        window.title('Приложение-конвертер')
        window.geometry('400x180')
        text_rub = Label(window, text = 'Введите рубли')
        text_rub.grid(column = 0, row = 0)
        amount_rub = Entry(window, width = 12)
        amount_rub.grid(column = 1, row = 0, padx = 10)
        conv_b_1 = Button(window, text = 'Конвертировать', command = to_dol)
        conv_b_1.grid(column = 2, row = 0)
        conv_to_dol = Label(window)
        conv_to_dol.grid(column = 3, row = 0, padx = 10)
        
        window.mainloop()
    
    def task_14_2(self):
        def to_dol():
            rub_sum = round(int(amount_rub.get()) / 96.62, 2)
            conv_to_dol['text'] = str(rub_sum) + ' $'
        
        def to_rub():
            dol_sum = round(int(amount_dol.get()) * 96.62)
            conv_to_rub['text'] = str(dol_sum) + ' ₽'
        
        window = Tk()
        window.attributes('-topmost', True)
        window.title('Приложение-конвертер')
        window.geometry('400x180')
        
        text_rub = Label(window, text = 'Введите рубли')
        text_rub.grid(column = 0, row = 0)
        amount_rub = Entry(window, width = 12)
        amount_rub.grid(column = 1, row = 0, padx = 10)
        conv_b_1 = Button(window, text = 'Конвертировать', command = to_dol)
        conv_b_1.grid(column = 2, row = 0)
        conv_to_dol = Label(window)
        conv_to_dol.grid(column = 3, row = 0, padx = 10)
        
        text_dol = Label(window, text = 'Введите баксы')
        text_dol.grid(column = 0, row = 1)
        amount_dol = Entry(window, width = 12)
        amount_dol.grid(column = 1, row = 1, padx = 10)
        conv_b_2 = Button(window, text = 'Конвертировать', command = to_rub)
        conv_b_2.grid(column = 2, row = 1)
        conv_to_rub = Label(window)
        conv_to_rub.grid(column = 3, row = 1, padx = 10)
        
        window.mainloop()
        
    def task_15(self):
        while True:
            n, m = int(input('Введите n (ряд): ')), int(input('Введите m (столбец): '))
            if (n < 5 or n > 20) or (m < 5 or m > 20):
                print('Значения не входят в диапазон, попробуйте снова:')
            else:
                break
            
        for row in range(1, n + 1):
            if row != 2:
                print('')
            else:
                print('\n')
            for col in range(1, m + 1):
                if col == 2:
                    print('  ',sep = '', end = '')
                if row * m <= 9:
                    print(row * col, ' ' * 4, sep = '', end = '')
                elif row * m <= 99:
                    print(row * col, ' ' * (5 - len(str(row * col))), sep = '', end = '')
                else:
                    print(row * col, ' ' * (5 - len(str(row * col))), sep = '', end = '')

    def task_16(self):
        map = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        
        for row in range(10):
            start = randint(0, 17)
            size = randint(1, 4)
            for part in range(0, size):
                if row == 0 or map[row - 1][start + part] == map[row][start + part]:
                    map[row][start + part] = '='

        for row in range(10):
            print()
            for col in range(20):
                print (map[row][col], end = '')
                
        print('\nПоле генерируется самостоятельно')


while True:
    MultiTask()