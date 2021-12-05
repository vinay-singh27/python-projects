from random import randint
import turtle
from tkinter import Canvas


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GraphicalRectangle(Rectangle):

    def draw(self, canvas):
        # go to certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GraphicalPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        # go to certain coordinate
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# create rectangle object
rectangle1 = GraphicalRectangle(Point(randint(0, 400), randint(0, 400)),
                                Point(randint(10, 400), randint(10, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle1.point1.x, ",",
      rectangle1.point1.y, "and",
      rectangle1.point2.x, ",",
      rectangle1.point2.y)

# get point & area from the user
user_point = GraphicalPoint(float(input('Enter x: ')), float(input('Enter y: ')))
user_area = float(input('Guess the area of the rectangle: '))

# Print the result
print("Your point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle1))
print("Your area estimate was off by: ", rectangle1.area() - user_area)

#draw the rectangle
my_canvas = turtle.Turtle()
rectangle1.draw(canvas=my_canvas)
user_point.draw(canvas=my_canvas)
turtle.done()
