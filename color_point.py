from point import Point
import random

class ColorPoint(Point):
    def __init__(self, x,y,color):
        # raise an exception if we try to have not a number
        if not isinstance(x,(int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError ("y must be a number")

        super().__init__(x,y) #this replaces self.x and self.y
        self.color = color


    def __str__(self):
        return f"<{self.color}:{self.x}, {self.y}>"

p = ColorPoint(1,2,"red")
print(p.distance_orig())
print(p)
# colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "periwinkle", "burgundy"]
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10,10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
#
# print(color_points)
# color_points.sort()
# print(color_points)
