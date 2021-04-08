from manim import *


class Outro(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        s1 = Sphere()
        s1p = s1.copy().shift(1.5 * LEFT).rotate(PI, axis=UP)
        s2 = s1.copy()
        s2p = s2.copy().shift(1.5 * RIGHT).rotate(PI, axis=UP)
        self.play(ShowCreation(s1))
        self.wait(0.2)
        self.play(
            ReplacementTransform(s1, s1p),
            ReplacementTransform(s2, s2p),
            run_time=2
        )

        self.wait(2)
