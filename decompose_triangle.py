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
        area1.to_corner(UR)
        self.play(Write(area1))
        # self.play(Write(shifty(area1, pt(4, 3))))

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
        area2.to_corner(UR)
        area2.shift(pt(.5, 0))
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
                    \end{align*}""").to_corner(UR)
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
                    \end{align*}""").to_corner(UR)

        self.play(FadeIn(square), FadeOut(anti_tri), FadeOut(tri1), FadeOut(tri2), Transform(area1, area2))

        self.wait(2)


class DecomposeIsosceles2(Scene):
    def construct(self):
        l = 12.8 * 3 / 4
        angle = np.arcsin(3 / l)
        q = l * np.cos(angle)
        pt1, pt2, pt3 = pt(0, 0), pt(6, 0), pt(q, 3)
        tri = Polygon(pt1, pt2, pt3)
        com = com_shift(tri) + RIGHT
        tri.shift(com)
        self.play(ShowCreation(tri), run_time=1)
        angle = PI - angle
        line_b = Line(pt1, pt2).shift(com)
        brace_b = Brace(line_b, direction=line_b.copy().rotate(-PI / 2).get_unit_vector())
        text_b = brace_b.get_text("6 Units")
        line_h = Line(pt1, pt(0, pt3[1])).shift(com)
        brace_h = Brace(line_h, direction=line_h.copy().rotate(PI / 2).get_unit_vector())
        # this make is display so don't change the "\ 2"
        text_h = brace_h.get_text("3 Units")
        self.play(
            ShowCreation(brace_b), ShowCreation(text_b),
            ShowCreation(brace_h), ShowCreation(text_h),
        )
        self.wait(1)
        area1 = Tex(r"$A=\frac{1}{2}bh=\frac{1}{2}\cdot6\cdot3=9$").to_corner(UR)
        self.play(Write(area1))
        self.wait(2)

        self.play(
            FadeOut(area1),
            FadeOut(brace_h), FadeOut(text_h),
            FadeOut(brace_b), FadeOut(text_b),
        )

        line_new_b = Line(pt3, pt1).shift(com).shift(2 * LEFT)
        brace_new_b = Brace(line_new_b, direction=line_new_b.copy().rotate(-PI / 2).get_unit_vector())
        text_new_b = brace_new_b.get_text(f"{line_new_b.get_length().__round__(2)} Units").shift(0.2 * LEFT)

        self.play(
            Transform(tri, tri.copy().shift(2 * LEFT)),
            ShowCreation(brace_new_b),
            Write(text_new_b),
        )

        self.wait(1)

        self.play(
            Rotate(tri, angle=angle, about_point=pt(0, 0), run_time=2),
            Rotate(brace_new_b, angle=angle, about_point=pt(0, 0), run_time=2),
            Rotate(text_new_b, angle=angle, about_point=pt(0, 0), run_time=2),
        )
        # y1 == y3
        [[x1, y1, _], [x2, y2, _], [x3, _, _]] = tri.get_vertices()

        # line_new_h = Line(pt(x2, y1), pt(x2, y2)).shift(LEFT * x2 - x1)
        brace_new_h = Brace(tri, direction=LEFT)
        text_new_h = brace_new_h.get_text(f"{(y2 - y1).__round__(2)} Units")
        # noinspection PyTypeChecker
        self.play(
            Rotate(text_new_b, angle=-angle),
            ShowCreation(brace_new_h),
            Write(text_new_h),
            run_time=1.5
        )

        square = Polygon(
            pt((x2 + x3) / 2, y1),
            pt((x2 + x3) / 2, y2),
            pt((x1 + x2) / 2, y2),
            pt((x1 + x2) / 2, y1),
        )
        tri1 = Polygon(
            pt(x3, y1),
            pt((x2 + x3) / 2, (y2 + y1) / 2),
            pt((x2 + x3) / 2, y1),
        )
        tri2 = Polygon(
            pt(x1, y1),
            pt((x1 + x2) / 2, (y2 + y1) / 2),
            pt((x1 + x2) / 2, y1),
        )
        anti_tri = Polygon(
            pt((x1 + x2) / 2, y1),
            pt((x1 + x2) / 2, (y2 + y1) / 2),
            pt(x2, y2),
            pt((x2 + x3) / 2, (y2 + y1) / 2),
            pt((x2 + x3) / 2, y1),
        )

        brace1 = Brace(tri1)
        text1 = brace1.get_text(f"{((x2 + x1) / 2).__abs__().__round__(2)}")
        brace2 = Brace(tri2)
        text2 = brace2.get_text(f"{((x2 + x3) / 2).__abs__().__round__(2)}")
        brace_anti = Brace(anti_tri)
        text_anti = brace_anti.get_text(f"{((x2 + x3) / 2 - (x2 + x1) / 2).__abs__().__round__(2)}")
        self.play(
            Transform(brace_new_b, brace_new_b.copy().shift(DOWN)),
            Transform(text_new_b, text_new_b.copy().shift(DOWN)),
            ShowCreation(anti_tri),
            ShowCreation(brace1),
            Write(text1),
            ShowCreation(brace2),
            Write(text2),
            ShowCreation(brace_anti),
            Write(text_anti),
        )
        self.add(tri1, tri2)
        self.remove(tri)

        self.wait(2)

        brace_final_h = Brace(square, direction=LEFT)
        text_final_h = brace_final_h.get_text(f"{(y2 - y1).__round__(2)} Units")
        text_square_b = brace_anti.get_text(f"{((x2 + x3) / 2 - (x2 + x1) / 2).__abs__().__round__(2)} Units")

        # noinspection PyTypeChecker
        self.play(
            Rotate(tri2, about_point=pt((x1 + x2) / 2, (y2 + y1) / 2)),
            Rotate(tri1, about_point=pt((x2 + x3) / 2, (y2 + y1) / 2), angle=-PI),
            FadeOut(brace1), FadeOut(brace2), FadeOut(text1), FadeOut(text2), FadeOut(text_new_b),
            Transform(brace_new_b, brace_anti),
            Transform(text_anti, text_square_b),
            Transform(brace_new_h, brace_final_h),
            Transform(text_new_h, text_final_h),
            run_time=1.4
        )
        self.wait(0.5)

        area2 = Tex(r"$A=\frac{1}{2}bh=\frac{1}{2}\cdot4.8\cdot1.88=9$").to_corner(UR)
        self.play(
            FadeOut(tri1), FadeOut(tri2), FadeOut(anti_tri),
            FadeIn(square),
            Write(area2),
        )

        self.wait(2)
