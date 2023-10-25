class My_list(list):
    def __init__(self, a = 0, b = 0, c = 0):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c
        self.elems_list = [self.a, self.b, self.c]
        
    def __sub__(self, other):
        temp_list = []
        for index, elem in enumerate(self.elems_list):
            elem_1 = elem
            elem_2 = other.elems_list[index]
            
            if isinstance(elem_1, int) or isinstance(elem_1, float) and isinstance(elem_2, int) or isinstance(elem_2, float):
                temp_list.append(elem_1 - elem_2)
                
            elif isinstance(elem_1, str) and isinstance(elem_2, str):
                if len(elem_1) >= len(elem_2):
                    temp_list.append(elem_1)
                else:
                    temp_list.append(elem_2)
            
            elif isinstance(elem_1, list) or isinstance(elem_1, tuple) and isinstance(elem_2, list) or isinstance(elem_2, tuple): # consists only of numbers!
                extra_list = []
                while len(elem_1) < len(elem_2):
                    elem_1.append(0)
                while len(elem_2) < len(elem_1):
                    elem_2.append(0)
                    
                for i, elem in enumerate(elem_1):
                    extra_list.append(elem_1[i] - elem_2[i])
                temp_list.append(extra_list)
                
            elif isinstance(elem_1, bool) and isinstance(elem_2, bool):
                if elem_1 == 'True' and elem_2 == 'True':
                    temp_list.append(0)
                elif elem_1 == 'True' and elem_2 == 'False':
                    temp_list.append(1)
                elif elem_1 == 'False' and elem_2 == 'True':
                    temp_list.append(-1)
                elif elem_1 == 'False' and elem_2 == 'False':
                    temp_list.append(0)
            
            else:
                temp_list.append('undefined')
            
        return My_list(temp_list[0], temp_list[1], temp_list[2])
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return My_list(self.a / other, self.b / other, self.c / other)
        else:
            return 'Деление невозможно'
        
    def __str__(self):
        return super().__str__() +  " Список элементов"

l1 = My_list(1, 2, 3)
l2 = My_list(3, 4, 5)
l3 = l2 - l1
l4 = l1 - l2
print(l1 / 5)
print(l3)
print(l4)