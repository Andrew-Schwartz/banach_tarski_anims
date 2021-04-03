from manim import *


def pt(x, y):
    return np.array([x, y, 0])


def triangle(x):
    maxy = 3.9
    polygon = Polygon(
        pt(0, 0), pt(8, 0), pt(x, maxy),
        fill_color='#7890CD',
        fill_opacity=1,
        stroke_color='#D9D9D9',
        stroke_width=2,
    )
    return polygon.shift(pt(-7, -maxy))


# -7 to 7 x
# -3.9 to 3.9 y

class Right(Scene):
    def construct(self):
        self.add(triangle(0))


class Middle(Scene):
    def construct(self):
        self.add(triangle(6))


class Obtuse(Scene):
    def construct(self):
        self.add(triangle(14))
