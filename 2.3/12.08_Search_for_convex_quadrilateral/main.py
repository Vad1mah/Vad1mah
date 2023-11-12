from math import hypot, sqrt, sin
import sys
import numpy as np

class Point:
    def __init__(self, x, y):
        self.coordinate = (x, y)

class Quadrilateral:
    def __init__(self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y):
        self.A = (p1_x, p1_y)
        self.B = (p2_x, p2_y)
        self.C = (p3_x, p3_y)
        self.D = (p4_x, p4_y)
        d1 = hypot(self.C[0] - self.A[0], self.C[1] - self.A[1])
        d2 = hypot(self.D[0] - self.B[0], self.D[1] - self.B[1])
        d1_vector = np.array([self.C[0] - self.A[0], self.C[1] - self.A[1]])
        d2_vector = np.array([self.D[0] - self.B[0], self.D[1] - self.B[1]])
        sinus = sin(self.angle_between((d1_vector), (d2_vector)))
        try:
            self.area = d1 * d2 * sinus / 2
        except ValueError:
            self.area = 0

    def unit_vector(self, vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)

    def angle_between(self, v1, v2):
        """ Returns the angle in radians between vectors 'v1' and 'v2'. """
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
          
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
        return f'{str(self.area)} ({str(round((self.area), 3))})'

class Main:
    def __init__(self):
        self.create_coordinate_list()
        self.create_point_list()
        self.create_quadrilaterals()
        self.compare_quadrilaterals()
        self.show_result()
        
    def create_coordinate_list(self):
        with open('plist.txt', 'r') as file:
            self.coordinate_list = file.read().replace('[', '').replace(']', ',').replace(' ', '').rstrip(',').split(',')

    def create_point_list(self):
        self.point_list = []
        
        for i in range(0, len(self.coordinate_list), 2):
            self.point_list.append(Point(int(self.coordinate_list[i]), int(self.coordinate_list[i + 1])))
        
    def create_quadrilaterals(self):
        self.quadrilateral_list = []
        
        for p1 in range(len(self.point_list)):
            p1_x = self.point_list[p1].coordinate[0]
            p1_y = self.point_list[p1].coordinate[1]
            for p2 in range(p1 + 1, len(self.point_list)):
                p2_x = self.point_list[p2].coordinate[0]
                p2_y = self.point_list[p2].coordinate[1]
                for p3 in range(p2 + 1, len(self.point_list)):
                    p3_x = self.point_list[p3].coordinate[0]
                    p3_y = self.point_list[p3].coordinate[1]
                    for p4 in range(p3 + 1, len(self.point_list)):
                        p4_x = self.point_list[p4].coordinate[0]
                        p4_y = self.point_list[p4].coordinate[1]
                        self.quadrilateral_list.append(Quadrilateral(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y))
        
    def compare_quadrilaterals(self):
        self.smallest_quadrilateral = sys.maxsize
        self.biggest_quadrilateral = -1

        for quadrilateral in self.quadrilateral_list:
            if quadrilateral == self.biggest_quadrilateral:
                    continue
            elif quadrilateral > self.biggest_quadrilateral:
                    self.biggest_quadrilateral = quadrilateral
            if quadrilateral < self.smallest_quadrilateral and quadrilateral != 0:
                    self.smallest_quadrilateral = quadrilateral

    def show_result(self):
        print(f'\nНаименьшая площадь выпуклого четырёхугольника: {self.smallest_quadrilateral}\nКоординаты его точек:')
        print(f'A: {self.smallest_quadrilateral.A}\nB: {self.smallest_quadrilateral.B}\nC: {self.smallest_quadrilateral.C}\nD: {self.smallest_quadrilateral.D}')
        print(f'\nНаибольшая площадь выпуклого четырёхугольника: {self.biggest_quadrilateral}\nКоординаты его точек:')
        print(f'A: {self.biggest_quadrilateral.A}\nB: {self.biggest_quadrilateral.B}\nC: {self.biggest_quadrilateral.C}\nD: {self.biggest_quadrilateral.D}\n')

Main()