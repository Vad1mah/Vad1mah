from math import hypot, sqrt
import sys

class Point:
    def __init__(self, x, y):
        self.coordinate = (x, y)

class Triangle:
    def __init__(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
        self.A = (p1_x, p1_y)
        self.B = (p2_x, p2_y)
        self.C = (p3_x, p3_y)
        self.AB = hypot(self.B[0] - self.A[0], self.B[1] - self.A[1])
        self.AC = hypot(self.C[0] - self.A[0], self.C[1] - self.A[1])
        self.BC = hypot(self.C[0] - self.B[0], self.C[1] - self.B[1])
        p = (self.AB + self.AC + self.BC) / 2
        try:
            self.area = sqrt(p * (p - self.AB) * (p - self.AC) * (p - self.BC))
        except ValueError:
            self.area = 0
            
    def __eq__(self, other):
        return self.area == other
        
    def __ne__(self, other):
        return self.area != other
        
    def __lt__(self, other):
        return self.area < other
        
    def __le__(self, other):
        return self.area <= other
        
    def __gt__(self, other):
        return self.area > other
        
    def __ge__(self, other):
        return self.area >= other

    def __str__(self):
        return f'{str(self.area)} ({str(int(self.area))})'

class Main:
    def __init__(self):
        self.create_coordinate_list()
        self.create_point_list()
        self.create_triangles()
        self.compare_triangles()
        self.show_result()
        
    def create_coordinate_list(self):
        with open('plist.txt', 'r') as file:
            self.coordinate_list = file.read().replace('[', '').replace(']', ',').replace(' ', '').rstrip(',').split(',')

    def create_point_list(self):
        self.point_list = []
        
        for i in range(0, len(self.coordinate_list), 2):
            self.point_list.append(Point(int(self.coordinate_list[i]), int(self.coordinate_list[i + 1])))
        
    def create_triangles(self):
        self.triangles_list = []
        
        for p1 in range(len(self.point_list)):
            p1_x = self.point_list[p1].coordinate[0]
            p1_y = self.point_list[p1].coordinate[1]
            for p2 in range(p1 + 1, len(self.point_list)):
                p2_x = self.point_list[p2].coordinate[0]
                p2_y = self.point_list[p2].coordinate[1]
                for p3 in range(p2 + 1, len(self.point_list)):
                    p3_x = self.point_list[p3].coordinate[0]
                    p3_y = self.point_list[p3].coordinate[1]
                    self.triangles_list.append(Triangle(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y))
        
    def compare_triangles(self):
        self.smallest_triangle = sys.maxsize
        self.biggest_triangle = -1

        for triangle in self.triangles_list:
            if triangle > self.biggest_triangle:
                    self.biggest_triangle = triangle
            elif triangle == self.biggest_triangle:
                    continue
            elif triangle < self.smallest_triangle and triangle != 0:
                    self.smallest_triangle = triangle

    def show_result(self):
        print(f'\nНаименьшая площадь треугольника: {self.smallest_triangle}\nКоординаты его точек:')
        print(f'A: {self.smallest_triangle.A}\nB: {self.smallest_triangle.B}\nC: {self.smallest_triangle.C}')
        print(f'\nНаибольшая площадь треугольника: {self.biggest_triangle}\nКоординаты его точек:')
        print(f'A: {self.biggest_triangle.A}\nB: {self.biggest_triangle.B}\nC: {self.biggest_triangle.C}\n')

Main()