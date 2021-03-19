from manim import *


def pt(x, y):
    return np.array([x, y, 0])


def com_shift(shape: VMobject):
    return -shape.get_center_of_mass()


class DecomposeRight(Scene):
    def construct(self):
        tri1 = Polygon(pt(0, 0), pt(6, 0), pt(0, 3))

        def shifty(shape, shift=com_shift(tri1)):
            return shape.shift(shift)

        self.play(ShowCreation(shifty(tri1)), run_time=1.3)
        bot_brace = Brace(tri1)
        bot_brace_text = bot_brace.get_text("6 Units")
        left_brace = Brace(tri1, direction=LEFT)
        left_brace_text = left_brace.get_text("3 Units")
        self.play(ShowCreation(bot_brace), Write(bot_brace_text), ShowCreation(left_brace), Write(left_brace_text))

        area1 = Tex(r"""\begin{align*}
                        A_i&=\frac{1}{2}b_ih \\
                        &=9\ \text{Units}^2
                    \end{align*}""")
        self.play(Write(shifty(area1, pt(4, 3))))

        tri_small = Polygon(pt(3, 0), pt(6, 0), pt(6, .01), pt(3, 1.5))
        anti_triangle = Polygon(pt(0, 0), pt(3, 0), pt(3, 1.5), pt(0, 3))
        bot_brace_small = Brace(anti_triangle)
        bot_brace_small_text = bot_brace_small.get_text("3 Units")
        shifty(bot_brace_small)
        shifty(bot_brace_small_text)
        self.play(ShowCreation(shifty(tri_small)))
        self.add(shifty(anti_triangle))
        self.remove(tri1)
        self.play(
            Rotate(tri_small, about_point=pt(3 - 2, 1.5 - 1)),
            Transform(bot_brace, bot_brace_small),
            Transform(bot_brace_text, bot_brace_small_text),
            run_time=1.4
        )
        square1 = Polygon(pt(0, 0), pt(3, 0), pt(3, 3), pt(0, 3))
        shifty(square1)
        area2 = Tex(r"""\begin{align*}
                        A_i&=\frac{1}{2}b_ih=b_fh=A_f \\
                        &=9\ \text{Units}^2 \quad\ = 9\ \text{Units}^2
                     \end{align*}""")
        shifty(area2, pt(4, 3))
        self.play(FadeOut(anti_triangle), FadeOut(tri_small), FadeIn(square1), Transform(area1, area2))
        self.wait(2)


# noinspection DuplicatedCode
class DecomposeIsosceles(Scene):
    def construct(self):
        tri = Polygon(pt(0, 0), pt(2, -2), pt(-4, -2))
        com = com_shift(tri)
        tri.shift(com)
        angle = - PI / 13
        tri_rot = tri.copy().rotate(angle)
        self.play(ShowCreation(tri_rot), run_time=1)
        lineh = Line(pt(-4, -2), pt(2, -2)).shift(com)
        hshift = pt(-.28, .03)
        linehr = lineh.copy().rotate(angle).shift(hshift)
        braceh = Brace(lineh, direction=lineh.copy().rotate(-PI / 2).get_unit_vector())
        bracehr = Brace(linehr, direction=linehr.copy().rotate(-PI / 2).get_unit_vector())
        braceh_text = braceh.get_text("9 Units")
        bracehr_text = braceh_text.copy().shift(hshift)
        linev = Line(pt(0, 0), pt(0, -2)).shift(4 * LEFT + com)
        lshift = pt(.03, .72)
        linevr = linev.copy().rotate(angle).shift(lshift)
        bracev = Brace(linev, direction=linev.copy().rotate(-PI / 2).get_unit_vector())
        bracevr = Brace(linevr, direction=linevr.copy().rotate(-PI / 2).get_unit_vector())
        bracev_text = bracev.get_text("3 Units")
        bracevr_text = bracev_text.copy().shift(lshift)
        self.play(ShowCreation(bracehr), Write(bracehr_text), ShowCreation(bracevr), Write(bracevr_text))

        area1 = Tex(r"""\begin{align*}
                        A_i&=\frac{1}{2}b_ih \\
                        &=13.5\ \text{Units}^2
                    \end{align*}""").shift(pt(4, 3))
        self.play(Write(area1))

        self.play(
            Transform(tri_rot, tri),
            Transform(bracehr, braceh),
            Transform(bracehr_text, braceh_text),
            Transform(bracevr, bracev),
            Transform(bracevr_text, bracev_text),
            run_time=1.5
        )

        tri1 = Polygon(pt(1, -1), pt(2, -2), pt(1, -2)).shift(com)
        tri2 = Polygon(pt(-4, -2), pt(-2, -1), pt(-2, -2)).shift(com)
        anti_tri = Polygon(pt(0, 0), pt(1, -1), pt(1, -2), pt(-2, -2), pt(-2, -1)).shift(com)
        self.play(ShowCreation(anti_tri))
        self.add(tri1, tri2)
        self.remove(tri_rot)

        square = Polygon(pt(1, 0), pt(1, -2), pt(-2, -2), pt(-2, 0)).shift(com)
        braceh2 = Brace(square)
        bracev2 = Brace(square, direction=LEFT)
        # noinspection PyTypeChecker
        self.play(
            Rotate(tri1, about_point=pt(1, -1) + com),
            Rotate(tri2, about_point=pt(-2, -1) + com, angle=-PI),
            Transform(bracehr, braceh2),
            Transform(bracehr_text, braceh2.get_text("4.5 Units")),
            Transform(bracevr, bracev2),
            Transform(bracevr_text, bracev2.get_text("3 Units")),
            run_time=1.4
        )

        area2 = Tex(r"""\begin{align*}
                        A_i&=\frac{1}{2}b_ih=b_fh=A_f \\
                        &=13.5\ \text{Units}^2 = 13.5\ \text{Units}^2
                    \end{align*}""").shift(pt(3, 3))

        self.play(FadeIn(square), FadeOut(anti_tri), FadeOut(tri1), FadeOut(tri2), Transform(area1, area2))

        self.wait(2)
