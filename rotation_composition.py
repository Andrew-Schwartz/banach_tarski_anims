import functools

import numpy.linalg as LA
from manim import *
from numpy import tan, arctan


def pt(x, y, z):
    return np.array([x, y, z])


def unit(array: np.ndarray) -> np.ndarray:
    norm = LA.norm(array)
    return array / norm


class Rotato(ThreeDScene):
    def rotatoes(self, rotation_vectors):
        prism = Prism()
        individual = prism.copy()
        self.play(ShowCreation(individual))
        for rotation in rotation_vectors:
            norm = LA.norm(rotation)
            rotation = rotation / norm
            self.play(Rotate(individual, angle=norm, axis=rotation), run_time=1.2)
        self.wait(0.5)

        # a and b are `angle * unit_vector` - see
        # https://wikimedia.org/api/rest_v1/media/math/render/svg/6beebd8e0b921524bd82b4675d58dc984250fdc0
        def compose(a: np.ndarray, b: np.ndarray) -> np.ndarray:
            alpha, beta = LA.norm(a), LA.norm(b)
            a, b = a / alpha, b / beta
            numerator = tan(beta / 2) * b + tan(alpha / 2) * a + tan(beta / 2) * tan(alpha / 2) * np.cross(b, a)
            denominator = 1 - tan(beta / 2) * tan(alpha / 2) * np.dot(b, a)
            rhs = numerator / denominator
            angle = 2 * arctan(LA.norm(rhs))
            return angle * unit(rhs)

        final_rotation = functools.reduce(compose, rotation_vectors)
        composed = prism.copy()
        self.play(Transform(individual, individual.copy().set_opacity(0.3)), ShowCreation(composed))
        axis = Line3D(-final_rotation * 3, final_rotation * 3, thickness=0.005, color=RED)
        self.play(ShowCreation(axis))
        shift = final_rotation / max([abs(x) for x in final_rotation])
        marker1 = Sphere(radius=0.08, color=GREEN).shift(shift)
        marker2 = Sphere(radius=0.08, color=GREEN).shift(-shift)
        self.play(ShowCreation(marker1), ShowCreation(marker2))
        self.play(Rotate(composed, angle=LA.norm(final_rotation), axis=final_rotation), run_time=2)
        self.wait(1)


class ColorPrism(ThreeDVMobject):
    colors = [
        BLUE,
        TEAL,
        GREEN,
        YELLOW,
        RED,
        PURPLE
    ]

    # colors = [
    #     "#FFD500",  # Yellow
    #     "#C41E3A",  # Orange
    #     "#009E60",  # Green
    #     "#FF5800",  # Red
    #     "#0051BA",  # Blue
    #     "#FFFFFF"  # White
    # ]

    CONFIG = {
        "colors": [
            "#FFD500",  # Yellow
            "#C41E3A",  # Orange
            "#009E60",  # Green
            "#FF5800",  # Red
            "#0051BA",  # Blue
            "#FFFFFF"  # White
        ],
    }

    def __init__(self):
        ThreeDVMobject.__init__(self)


class Composition2(Rotato):
    def construct(self):
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        angle = PI / 2
        self.rotatoes([
            angle * OUT,
            angle * RIGHT
        ])


class Composition3(Rotato):
    def construct(self):
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.07)
        self.rotatoes([
            PI / 2 * RIGHT,
            PI / 2 * UP,
            PI / 5 * OUT
        ])
