import numpy.linalg as npla
from manim import *
from numpy import tan, arctan


def pt(x, y, z):
    return np.array([x, y, z])


def unit(array: np.ndarray) -> np.ndarray:
    norm = npla.norm(array)
    return array / norm


class Step1(ThreeDScene):
    def construct(self):
        # phi
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        s = Sphere()
        self.play(ShowCreation(s))
        dir = pt(1, 2, 2)
        axis = Arrow3D(-dir, dir, thickness=0.005, height=0.2, base_radius=0.1, color=RED)
        tex = Tex(r"$\qquad\phi$", color=RED).to_corner(UL)
        self.add_fixed_in_frame_mobjects(tex)
        self.play(
            ShowCreation(axis),
            Write(tex),
        )
        self.play(
            Rotate(s, axis=dir),
            run_time=2
        )

        self.wait(2)


class Step2(ThreeDScene):
    def construct(self):
        # composition
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        s = Sphere()
        self.play(ShowCreation(s))
        phi_dir = pt(1, 2, 2)
        phi_axis = Arrow3D(-phi_dir, phi_dir, thickness=0.005, height=0.2, base_radius=0.1, color=RED)
        phi_tex = Tex(r"$\phi$", color=RED).to_corner(UL)
        psi_dir = pt(2, 1, 1)
        psi_axis = Arrow3D(-psi_dir, psi_dir, thickness=0.005, height=0.2, base_radius=0.1, color=GREEN)
        psi_tex = Tex(r"$\psi$", color=GREEN).to_corner(UL).shift(DOWN)
        self.add_fixed_in_frame_mobjects(phi_tex)
        self.play(ShowCreation(phi_axis), Write(phi_tex))
        self.add_fixed_in_frame_mobjects(psi_tex)
        self.play(ShowCreation(psi_axis), Write(psi_tex))
        self.play(Indicate(phi_axis))
        self.play(
            Rotate(s, axis=phi_dir),
            run_time=2
        )
        self.play(Indicate(psi_axis))
        self.play(
            Rotate(s, axis=psi_dir),
            run_time=2
        )

        self.wait(2)


def compose(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    alpha, beta = npla.norm(a), npla.norm(b)
    a, b = a / alpha, b / beta
    numerator = tan(beta / 2) * b + tan(alpha / 2) * a + tan(beta / 2) * tan(alpha / 2) * np.cross(b, a)
    denominator = 1 - tan(beta / 2) * tan(alpha / 2) * np.dot(b, a)
    rhs = numerator / denominator
    angle = 2 * arctan(npla.norm(rhs))
    return angle * unit(rhs)


class Step3(ThreeDScene):
    def construct(self):
        # associativity
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=90 * DEGREES)
        shl = 2.25 * LEFT
        sl = Sphere().shift(shl)
        shr = 2.25 * RIGHT
        sr = Sphere().shift(shr)
        self.play(ShowCreation(sr), ShowCreation(sl))
        self.wait(1)
        phi_dir = pt(1, 2, 2)
        phi_axis = Arrow3D(-phi_dir, phi_dir, thickness=0.005, height=0.2, base_radius=0.1, color=RED)
        # phi_axis = Line3D(-phi_dir, phi_dir, thickness=0.005, color=RED)
        phi_axis_l = phi_axis.copy().shift(shl)
        phi_axis_r = phi_axis.copy().shift(shr)
        phi_tex = Tex(r"$\phi$", color=RED).to_corner(UL)
        psi_dir = pt(2, 1, 1)
        psi_axis = Arrow3D(-psi_dir, psi_dir, thickness=0.005, height=0.2, base_radius=0.1, color=GREEN)
        # psi_axis = Line3D(-psi_dir, psi_dir, thickness=0.005, color=GREEN)
        psi_axis_l = psi_axis.copy().shift(shl)
        psi_axis_r = psi_axis.copy().shift(shr)
        psi_tex = Tex(r"$\psi$", color=GREEN).to_corner(UL).shift(DOWN)
        xi_dir = pt(-2, 2, 1)
        xi_axis = Arrow3D(-xi_dir, xi_dir, thickness=0.005, height=0.2, base_radius=0.1, color=BLUE)
        # xi_axis = Line3D(-xi_dir, xi_dir, thickness=0.005, color=BLUE)
        xi_axis_l = xi_axis.copy().shift(shl)
        xi_axis_r = xi_axis.copy().shift(shr)
        xi_tex = Tex(r"$\chi$", color=BLUE).to_corner(UL).shift(DOWN * 2)
        self.add_fixed_in_frame_mobjects(phi_tex)
        self.play(
            Write(phi_tex),
            ShowCreation(phi_axis_l),
            ShowCreation(phi_axis_r),
        )
        self.add_fixed_in_frame_mobjects(psi_tex)
        self.play(
            Write(psi_tex),
            ShowCreation(psi_axis_l),
            ShowCreation(psi_axis_r),
        )
        self.add_fixed_in_frame_mobjects(xi_tex)
        self.play(
            Write(xi_tex),
            ShowCreation(xi_axis_l),
            ShowCreation(xi_axis_r),
        )
        self.play(Indicate(psi_axis_r), Indicate(xi_axis_r), Indicate(xi_axis_l))
        psi_xi_dir = compose(PI * unit(xi_dir), PI * unit(psi_dir))
        self.play(
            Rotate(sl, axis=xi_dir),
            Rotate(sr, angle=npla.norm(psi_xi_dir), axis=psi_xi_dir),
            run_time=2.4
        )
        phi_psi_dir = compose(PI * unit(psi_dir), PI * unit(phi_dir))
        self.play(Indicate(phi_axis_r), Indicate(phi_axis_l), Indicate(psi_axis_l))
        self.play(
            Rotate(sl, angle=npla.norm(phi_psi_dir), axis=phi_psi_dir),
            Rotate(sr, axis=phi_dir),
            run_time=2.4
        )

        self.wait(2)


class Step4(ThreeDScene):
    def construct(self):
        # inverse
        self.add(ThreeDAxes())
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        s = Sphere()
        self.play(ShowCreation(s))
        dir = pt(1, 2, 2)
        axis = Arrow3D(-dir, dir, thickness=0.005, height=0.2, base_radius=0.1, color=RED)
        tex = Tex(r"$\phi,\ \alpha=\pi$", color=RED).to_corner(UL)
        self.add_fixed_in_frame_mobjects(tex)
        self.play(
            Write(tex),
            ShowCreation(axis),
        )
        self.play(
            Rotate(s, axis=dir),
            run_time=2
        )
        self.remove(tex)
        tex2 = Tex(r"$\phi,\ \alpha=-\pi$", color=RED).to_corner(UL)
        self.add_fixed_in_frame_mobjects(tex)
        self.play(Transform(tex, tex2))
        # noinspection PyTypeChecker
        self.play(
            Rotate(s, axis=dir, angle=-PI),
            run_time=2
        )

        self.wait(2)
