from manim import *


def pt2(x, y):
    return np.array([x, y, 0])


def shifty(shape, right=-2, up=-1):
    shape.shift(RIGHT * right)
    shape.shift(UP * up)
    return shape


class DecomposeTriangle(Scene):
    def construct(self):
        tri1 = Polygon(pt2(0, 0), pt2(6, 0), pt2(0, 3))
        self.play(ShowCreation(shifty(tri1)), run_time=1.3)
        bot_brace = Brace(tri1)
        bot_brace_text = bot_brace.get_text("6 Units")
        left_brace = Brace(tri1, direction=LEFT)
        left_brace_text = left_brace.get_text("3 Units")
        self.play(FadeIn(bot_brace), FadeIn(bot_brace_text), FadeIn(left_brace), FadeIn(left_brace_text))

        area1 = Tex("$A_i=\\frac{1}{2}b_ih$")
        self.play(Write(shifty(area1, 4, 3)))

        tri_small = Polygon(pt2(3, 0), pt2(6, 0), pt2(6, .01), pt2(3, 1.5))
        anti_triangle = Polygon(pt2(0, 0), pt2(3, 0), pt2(3, 1.5), pt2(0, 3))
        bot_brace_small = Brace(anti_triangle)
        bot_brace_small_text = bot_brace_small.get_text("3 Units")
        shifty(bot_brace_small)
        shifty(bot_brace_small_text)
        self.play(ShowCreation(shifty(tri_small)))
        self.add(shifty(anti_triangle))
        self.remove(tri1)
        self.play(Rotate(tri_small, about_point=pt2(3 - 2, 1.5 - 1)), Transform(bot_brace, bot_brace_small),
                  Transform(bot_brace_text, bot_brace_small_text))
        square1 = Polygon(pt2(0, 0), pt2(3, 0), pt2(3, 3), pt2(0, 3))
        shifty(square1)
        area2 = Tex("$A_i=\\frac{1}{2}b_ih=b_fh=A_f$")
        shifty(area2, 4, 3)
        self.play(FadeOut(anti_triangle), FadeOut(tri_small), FadeIn(square1), Transform(area1, area2))
        self.wait(2)
