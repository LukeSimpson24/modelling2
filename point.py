import random

class Point: #needs capital P
    def __init__(self,x,y): #definition inside a class so it is not a function it is a method
        """
        initialise a Point object.
        :param x: the x position on the axis
        :param y: the y position on the y axis
        """
        self.x = x # define x attribute via self.x
        self.y = y # and assign the value x to it


    def __str__(self):
        """
        magic method tha tis called when we try to print an instance
        :return: <x,y>
        """
        return f"point({self.x},{self.y})"

    def __repr__(self):
        return self.__str__() # use the same way of printing str

    def distance_orig(self):
        return(self.x**2 + self.y**2)**0.5 #square root of the sum of x

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance




# now we need to instantiate it!
p = Point(1,2) # p is an instance of 1 and 2
p = Point(2,3)
p4 = Point(4.4,-55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x=20
print(f"p.x={p.x} and p.y={p.y}")
print(p)

#create list of 5 random points
points =[]
for i in range(5):
    points.append(Point(random.randint(-10, 10), #x value
                        random.randint(-10,10))) # y value
print("i got these 5 random points:")
print(points)
P=Point(3,4)
print(p.distance_orig()) # expect 5 answer
p2 = Point(1,1)
print(f"i am comparing p>p2:{p>p2}") #expect to have true
print("the sorted list of points is:")
points.sort()
print(points)
