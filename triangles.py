from manim import *


def pt(x, y):
    return np.array([x, y, 0])


def triangle(x):
    polygon = Polygon(
        pt(0, 0), pt(6, 0), pt(x, 3),
        fill_color='#7890CD',
        fill_opacity=1,
        stroke_color='#D9D9D9',
        stroke_width=2,
    )
    return polygon.shift(-polygon.get_center_of_mass())


class Right(Scene):
    def construct(self):
        self.add(triangle(0))


class Middle(Scene):
    def construct(self):
        self.add(triangle(4))


class Obtuse(Scene):
    def construct(self):
        self.add(triangle(9))
