from swampy.World import World

world = World()

canvas = world.ca(width=1000, height=1000, background='white')
bbox = [[-150, -100], [150, 100]]

canvas.rectangle(bbox, outline='black', width=2, fill='green4')


class Rectangle(object):
    """Represents a rectangle."""


box = Rectangle()
box.color = 'blue'
box.bbox = [[-100, -80], [100, 80]]


class Canvas(object):
    """Represents a canvas.
    attributes: width, height, and background color"""


canvas = Canvas()
canvas.width = 250
canvas.height = 300


class Point(object):
    """Represents a point in space."""


p = Point()
p.x = 100
p.y = 50


class Circle(object):
    """Represents a circle.
    attributes: center point, radius"""


c = Circle()
c.radius = 25
c.center = Point()
c.center.x = 40
c.center.y = 40


def draw_rectangle(canvas, rectangle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)


def draw_point(canvas, point):
    bbox = [[point.x, point.y], [point.x, point.y]]
    drawn_canvas = world.ca((canvas.width, canvas.height))
    drawn_canvas.rectangle(bbox, fill="black")


def draw_circles(canvas, circle):
    drawn_canvas = world.ca(canvas.width, canvas.hieght)
    drawn_canvas.circle([circle.center.x, circle.center.y], circle.radius)


world.mainloop()
