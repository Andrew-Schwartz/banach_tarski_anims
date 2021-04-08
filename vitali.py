from manim import *


class Vitali(ThreeDScene):
    # noinspection PyTypeChecker
    def construct(self):
        prism = Prism()
        prismo1 = Prism(dimensions=[1, 2, 1])
        prismo2 = Prism(dimensions=[1, 2, 1])
        prismo3 = Prism(dimensions=[1, 2, 1])

        prismo1.shift([-1, 0, 0])
        prismo1.rotate(angle=PI / 2, axis=RIGHT)

        prismo2.rotate(angle=PI / 2, axis=RIGHT)

        prismo3.shift([1, 0, 0])
        prismo3.rotate(angle=PI / 2, axis=RIGHT)
        l1 = Line(RIGHT, LEFT)
        l3 = Line(LEFT, RIGHT)
        axes = ThreeDAxes()
        self.add(axes)
        l1.shift([-3, 0, 0])
        l3.shift([3, 0, 0])
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(ShowCreation(prism))
        self.play(Rotate(prism))
        self.play(Rotate(prism, angle=-1 * PI))
        self.play(Rotate(prism, angle=PI, axis=RIGHT))
        self.play(Rotate(prism, angle=PI / 2, axis=LEFT))
        self.play(ShowCreation(prismo1), ShowCreation(prismo2), ShowCreation(prismo3), FadeOut(prism))
        self.play(Rotate(prismo1, angle=2 * PI), Rotate(prismo2, angle=2 * PI), Rotate(prismo3, angle=2 * PI))
        self.play(ShowCreation(l1), ShowCreation(l3))
        self.play(MoveAlongPath(prismo1, l1), MoveAlongPath(prismo3, l3))


def NextRec(x=0.5):
    newrec = Rectangle(width=0.5, height=4)
    newrec.shift([x, 0, 0])
    return newrec


class Vitalanim(Scene):
    def construct(self):
        square = Square(4)
        square.shift([1.75, 0, 0])
        psquare = Square(4, color=PURPLE, fill_color=PURPLE, fill_opacity=1)
        rec1 = NextRec(0)
        rec2 = NextRec()
        rec3 = NextRec(1)
        rec4 = NextRec(1.5)
        rec5 = NextRec(2)
        rec6 = NextRec(2.5)
        rec7 = NextRec(3)
        rec8 = NextRec(3.5)
        liner = Line(end=np.array([0, 0, 0]), start=np.array([1.75, 0, 0]), fill_opacity=0)
        liner.set_opacity(0)
        self.play(ShowCreation(rec1))
        self.play(ShowCreation(rec2))
        self.play(ShowCreation(rec3))
        self.play(ShowCreation(rec4))
        self.play(ShowCreation(rec5))
        self.play(ShowCreation(rec6))
        self.play(ShowCreation(rec7))
        self.play(ShowCreation(rec8))
        self.play(ShowCreation(square), FadeOut(rec1), FadeOut(rec2), FadeOut(rec3), FadeOut(rec4), FadeOut(rec5),
                  FadeOut(rec6), FadeOut(rec7), FadeOut(rec8))
        self.play(ShowCreation(liner))
        self.play(MoveAlongPath(square, liner))
        self.play(ShowCreation(psquare))

        self.wait(2)


def seg(x, y):
    return np.array([x, y, 0])


class ChoiceAxiom(Scene):
    def construct(self):
        axes = Axes()
        c1 = np.array([-5, 0, 0])
        c2 = np.array([5, 0, 0])
        line1 = Line(c1, c2, color=ORANGE)
        line2 = Line(c1, c2, color=RED)
        line3 = Line(c1, c2, color=GREEN)
        line4 = Line(c1, c2, color=PURPLE)
        line5 = Line(c1, c2, color=BLUE)
        l1 = Line(seg(2 * .2, 0), seg(2 * .3, 0), color=ORANGE)
        l2 = Line(seg(0, 2.5), seg(2 * .1, 2.5), color=RED)
        l3 = Line(seg(2 * .4, -2.5), seg(2 * .5, -2.5), color=GREEN)
        l4 = Line(seg(2 * .1, 1, ), seg(2 * .2, 1), color=PURPLE)
        l5 = Line(seg(2 * .3, -1), seg(2 * .4, -1), color=BLUE)
        line1.set_opacity(0.5)
        line2.set_opacity(0.5)
        line3.set_opacity(0.5)
        line4.set_opacity(0.5)
        line5.set_opacity(0.5)
        lineu = Line(start=np.array([0, 0, 0]), end=np.array([0, 2.5, 0]), opacity=0)
        lined = Line(start=np.array([0, 0, 0]), end=np.array([0, -2.5, 0]), opacity=0)
        lineu2 = Line(start=np.array([0, 0, 0]), end=np.array([0, 1, 0]), opacity=0)
        lined2 = Line(start=np.array([0, 0, 0]), end=np.array([0, -1, 0]), opacity=0)
        lineu.set_opacity(0)
        lined.set_opacity(0)
        lineu2.set_opacity(0)
        lined2.set_opacity(0)
        self.add(axes)
        self.play(ShowCreation(line1), ShowCreation(line2), ShowCreation(line3), ShowCreation(line4),
                  ShowCreation(line5), ShowCreation(lineu), ShowCreation(lined), ShowCreation(lineu2),
                  ShowCreation(lined2))
        self.play(MoveAlongPath(line2, lineu), MoveAlongPath(line3, lined), MoveAlongPath(line4, lineu2),
                  MoveAlongPath(line5, lined2), run_time=3)
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), FadeIn(l4), FadeIn(l5), run_time=3)
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4), FadeOut(line5))

        self.wait(2)
