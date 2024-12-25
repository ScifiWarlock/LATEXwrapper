from pytex import LATEXdefinitions as ld
import os

os.chdir("/Users/omkar/Desktop/PyTeX/Multi_13/13_6")

ld.create("13.6Notes")
ld.clear()
ld.preamble("article", "Multi 13.6 Notes", "Omkar Tasgaonkar")

ld.ong_bruh()

ld.topic_index()
ld.figure_index()

ld.topic("The Directional Derivative:")
ld.line("", False)
ld.line("The directional derivative tells us the slope in a direction:", True)

ld.equation(ld.d_partial('x', 'f'), " slope\ in\ x-dir")
ld.equation(ld.d_partial('y', 'f'), " slope\ in\ y-dir")

ld.image(20.55, "A graph z = f(x, y) represents the hill")
ld.line("We want to find the slope in a certain direction, a rotation of theta in cylindrical", False)

ld.image(20.57, "Rotation of theta")
ld.line("So our direction vector ;math('u');", False)

ld.line("Therefore our directional derivative is the dot product of two vectors, now which vectors?", True)

ld.topic("The Gradient")
ld.line("", False)
ld.line("The gradient tells us the biggest derivative vector at a certain point in the graph!", False)

ld.image(21.01, "The Gradient, max growth")
ld.equation(ld.greek('nabla') + ' f(x,y)', ld.d_partial('x', 'f')+ fr"\vec{{i}}" + "+" + ld.d_partial('y', 'f') + fr"\vec{{j}}")

ld.line("So now, if we rotate this gradient by an angle theta, then we can say that the gradient is a subset of rotated gradients", False)
ld.line("Or that ;math(greek('nabla')); f(x, y) " + fr"$\in$" + " G where G is the superset", True)

ld.line("For the final step, the directional derivative must be a scalar quantity as it is a slope, so:", False)
ld.equation("Directional\ derivative", ld.greek('nabla') + ' f(x,y)' + fr"\cdot" + " u")
ld.line("Whereby ;math('u'); is the direction vector for angle ;math(greek('theta'));", True)

ld.example("Using " + ld.math(ld.greek('nabla')) + " f(x, y) to find Directional Derivative")
#ld.image(21.11, "Example surface")
ld.line("Find the directional derivative of ;math('f(x,y) = 3x^2 - 2y^2 at (-3/4, 0)'); in the direction of:", False)
ld.line(ld.math("3/4" + fr"\vec{{i}}" + "+" + fr"\vec{{j}}"), True)

ld.equation(ld.greek('nabla') + ' f(x,y)', "6x"+fr"\vec{{i}}" + "-" + "4y"+fr"\vec{{j}}")
ld.equation("u", "3/5" + fr"\vec{{i}}" + "+" + "4/5" + fr"\vec{{j}}")
ld.equation(ld.greek('nabla') + ' f(-3/4, 0)' + fr"\cdot" + " u", "-9/2" + fr"\vec{{i}}" + fr"\cdot" + "(" + "3/5" + fr"\vec{{i}}" + "+" + "4/5" + fr"\vec{{j}}" + ")")

ld.line("So the directional derivative or dot product for this question evaluates to: -27/10", True)

ld.gahzamn()
ld.compile()






