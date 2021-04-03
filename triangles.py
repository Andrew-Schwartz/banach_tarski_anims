from manim import *


def pt(x, y):
    return np.array([x, y, 0])


def triangle(x, shr=0):
    maxy = 3.9
    pt1, pt2, pt3 = pt(0, 0), pt(8, 0), pt(x, maxy)
    tri = Polygon(
        pt1, pt2, pt3,
        fill_color='#7890CD',
        fill_opacity=1,
        stroke_color='#D9D9D9',
        stroke_width=2,
    )
    shift = pt(-7 + 1 + shr, -maxy + 1)
    tri.shift(shift)
    brace_b = Brace(Line(pt1, pt2).shift(shift), direction=DOWN)
    text_b = brace_b.get_tex("b")
    line_c = Line(pt2, pt3)
    brace_c = Brace(line_c.shift(shift), direction=line_c.copy().rotate(-PI / 2).get_unit_vector())
    text_c = brace_c.get_tex("c")
    line_a = Line(pt3, pt1)
    brace_a = Brace(line_a.shift(shift), direction=line_a.copy().rotate(-PI / 2).get_unit_vector())
    text_a = brace_a.get_tex("a")
    return tri, brace_b, text_b, brace_c, text_c, brace_a, text_a


# -7 to 7 x
# -3.9 to 3.9 y

class Right(Scene):
    def construct(self):
        tri, bb, bt, bc, tc, _, _ = triangle(0, shr=1)
        b2 = Brace(tri, direction=LEFT)
        t2 = b2.get_tex("h=a")
        self.add(tri, bb, bt, b2, t2, bc, tc)


class Middle(Scene):
    def construct(self):
        self.add(*triangle(6))


class Obtuse(Scene):
    def construct(self):
        self.add(*triangle(12.8))
