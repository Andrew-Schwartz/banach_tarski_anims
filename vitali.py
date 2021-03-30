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
