import functools

import numpy.linalg as npla
from manim import *
from numpy import tan, arctan


def pt(x, y, z):
    return np.array([x, y, z])


def unit(array: np.ndarray) -> np.ndarray:
    norm = npla.norm(array)
    return array / norm


# noinspection PyAbstractClass
class ColorPrism(VGroup):
    colors = [
        "#FFD500",
        "#C41E3A",
        "#009E60",
        "#FF5800",
        "#0051BA",
        "#FFFFFF",
    ]

    # noinspection PyDefaultArgument
    def __init__(
            self,
            dimensions=[3, 2, 1],
            side_length=2,
            fill_opacity=0.75,
            stroke_width=0,
            **kwargs,
    ):
        self.side_length = side_length
        self.dimensions = dimensions
        super().__init__(
            *[
                Square(
                    side_length=self.side_length,
                    fill_color=color,
                    fill_opacity=fill_opacity,
                    stroke_width=stroke_width,
                ).flip().shift(self.side_length * OUT / 2).apply_matrix(z_to_vector(vec))
                for vec, color in zip([IN, OUT, LEFT, RIGHT, UP, DOWN], self.colors)
            ],
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            **kwargs
        )
        self.set_shade_in_3d(True)
        for dim, value in enumerate(self.dimensions):
            self.rescale_to_fit(value, dim, stretch=True)


class Rotato(ThreeDScene):
    def rotatoes(self, prism: ColorPrism, rotation_vectors):
        individual = prism.copy()
        self.play(ShowCreation(individual))
        for rotation in rotation_vectors:
            norm = npla.norm(rotation)
            rotation = rotation / norm
            self.play(Rotate(individual, angle=norm, axis=rotation), run_time=1.2)
        self.wait(0.5)

        # a and b vectors that encode directionality and angle, they are given by `angle * unit_vector`
        # math source: https://wikimedia.org/api/rest_v1/media/math/render/svg/6beebd8e0b921524bd82b4675d58dc984250fdc0
        def compose(a: np.ndarray, b: np.ndarray) -> np.ndarray:
            alpha, beta = npla.norm(a), npla.norm(b)
            a, b = a / alpha, b / beta
            numerator = tan(beta / 2) * b + tan(alpha / 2) * a + tan(beta / 2) * tan(alpha / 2) * np.cross(b, a)
            denominator = 1 - tan(beta / 2) * tan(alpha / 2) * np.dot(b, a)
            rhs = numerator / denominator
            angle = 2 * arctan(npla.norm(rhs))
            return angle * unit(rhs)

        final_rotation = functools.reduce(compose, rotation_vectors)
        composed = prism.copy()
        self.play(Transform(individual, individual.copy().set_opacity(0.25)), ShowCreation(composed))
        axis = Line3D(-final_rotation * 3, final_rotation * 3, thickness=0.005, color=RED)
        self.play(ShowCreation(axis))
        shift = final_rotation / max([abs(x) for x in final_rotation])
        shift2 = final_rotation / min([abs(x) for x in final_rotation])
        print(f"final_rotation = {final_rotation}")
        print(f"shift = {shift}")
        print(f"shift2 = {shift2}")
        marker1 = Sphere(radius=0.08, color=GREEN).shift(shift)
        marker2 = Sphere(radius=0.08, color=GREEN).shift(-shift)
        self.play(ShowCreation(marker1), ShowCreation(marker2))
        self.play(Rotate(composed, angle=npla.norm(final_rotation), axis=final_rotation), run_time=2)
        self.wait(1)


class Composition2(Rotato):
    def construct(self):
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.07)
        angle = PI / 2
        self.rotatoes(ColorPrism(dimensions=[2, 2, 2]), [
            angle * OUT,
            angle * DOWN,
        ])


class Composition3(Rotato):
    def construct(self):
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.07)
        self.rotatoes(ColorPrism(), [
            PI / 2 * RIGHT,
            PI / 2 * UP,
            PI / 5 * OUT
        ])
