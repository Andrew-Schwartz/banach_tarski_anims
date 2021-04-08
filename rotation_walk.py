from manim import *


def pt(x, y, z):
    return np.array([x, y, z])


class Walk(ThreeDScene):
    def construct(self):
        angle = np.arccos(1 / 3) / 3
        self.bigboi = Sphere(radius=3)
        points = []

        def walk(axes):
            self.remove(self.bigboi)
            self.bigboi = Sphere(radius=3)
            sphere = Sphere(radius=0.05).shift(pt(3, 0, 0))
            self.add(sphere)
            for axis in axes:
                self.play(
                    Rotate(sphere, angle=angle, about_point=ORIGIN, axis=axis),
                    Rotate(self.bigboi, angle=angle, about_point=ORIGIN, axis=axis),
                    # have to draw each point to get it to render above the surface
                    *[Rotate(point) for point in points]
                )
            points.append(sphere)
            # sphere.shift(pt(1, 0, 0))
            self.wait(0.5)

        self.set_camera_orientation(phi=90 * DEGREES, theta=0)
        self.play(ShowCreation(self.bigboi))

        walk([OUT, DOWN, IN])
        walk([UP, OUT, UP, IN])
        walk([DOWN])
        walk([IN, IN, UP, UP, OUT])
        walk([IN, IN, UP, UP, OUT, OUT, DOWN, DOWN])

        self.remove(self.bigboi)
        # noinspection PyAttributeOutsideInit
        self.bigboi = Sphere(radius=3)
        self.add(self.bigboi)

        self.wait(2)
