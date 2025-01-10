from pytex_lib import LATEXdefinitions as ld
import os
os.chdir("/Users/omkar/Desktop/PyTeX/Multi_13/13_7")

ld.create("13.7Notes")
ld.clear()
ld.preamble("article", "Multi 13.7 Notes", "Omkar Tasgaonkar")

ld.ong_bruh()

ld.topic_index(False)
ld.figure_index()

ld.topic("Finding the equation of a plane")
ld.line("To find the equation of a plane, you need a normal vector and a point on the plane", True)
ld.equation("a(x - x0) + b(y - y0) + c(z-z0)", "0")
ld.line("The normal vector is ;greek('nabla'); F(x0, y0, z0), which is the gradient", False)
ld.line("To find the equation of a line, you need a direction vector and point on the line. The normal vector is the gradient as well, and you can write a parametric equation", True)
ld.equation("x", "x0 + at")
ld.equation("y", "y0 + bt")
ld.equation("z", "z0 + ct")

ld.topic("Tangent plane and normal line to a surface")
ld.line("If given z = f(x, y), then rewrite as: ", False)
ld.equation("F(x, y, z)", "f(x, y) - z")

ld.example("Writing a surface equation")
ld.line("For F(x, y, z), if ;greek('nabla'); F(x, y, z)" + fr" \cdot " + "r(t) where r(t) is the tangent vector", False)
ld.line("This dotproduct is equal to zero, so the gradient and tangent vector are orthogonal; refer to the example surface below", False)
ld.image(8.22, "There are infinitely many tangent vectors orthogonal to the gradient, which is the normal vector, perpendicular to the plane")
ld.line("The gradient is also the direction vector of the normal line, so you can write the equation of the normal line as well given a point on that line", True)

ld.example("Finding the equation of a tangent plane")
ld.line("Given ;math('z^2 - 2x^2 - 2y^2'); = 12, find a tangent plane at point (1, -1, 4)", False)
ld.equation("F(x, y, z)", "z^2 - 2x^2 - 2y^2 - 12 = 0")
ld.equation(ld.d_partial("x", "F"), "-4x")
ld.equation(ld.d_partial("y", "F"), "-4y")
ld.equation(ld.d_partial("z", "F"), "2z")
ld.equation("-4(x-1) + 4(y+1) +8(z-4)", "0")

ld.shazamn(
    """t Whats up this is test topic
    e Whats up this a test example
    hello 2x^2 = 2x^2 True"""
)

ld.gahzamn()
ld.compile()
