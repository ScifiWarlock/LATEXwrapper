from pytex_lib import LATEXdefinitions as ld
import os

os.chdir("/Users/omkar/Desktop/PyTeX/POTW")

ld.create("TA-POTW-Sem1")
ld.clear()
ld.preamble("article", "TA Problems of the Week: Semester One", "Omkar Tasgaonkar")

ld.ong_bruh()

ld.topic_index(True)

ld.topic("Problem of the week (9/30 - 10/3): Integrals!")
ld.line("Given a function ;math('f(x)'); at ;math('x'); = 2;math(greek('pi'));, which outputs -1:", True)

ld.equation("If\ f'(x)", "-(" + ("1 - " + ld.cos() + "^" + fr"{{2}}" + "(" + ld.greek('pi') + "/2 - x)") + ")" + "^" + fr"{{1/2}}")
ld.line("Find ;math('f(x)');", True)

ld.example("Solution:")
ld.line("Assume domain restriction from 0 to ;math(greek('pi'));/2", True)

ld.equation(ld.cos() + "^" + fr"{{2}}" + "(" + ld.greek('pi') + "/2 -x)", ld.sin() + "^" + fr"{{2}}" + "(x)")
ld.equation("f'(x)", ("-(1 - " + (ld.sin() + "^" + fr"{{2}}" + "(x)")) + ")" + "^" + fr"{{1/2}}")
ld.equation(("-(1 - " + (ld.sin() + "^" + fr"{{2}}" + "(x)")) + ")" + "^" + fr"{{1/2}}", "-("+ (ld.cos() + "^" + fr"{{2}}" + "(x)") + ")" + "^" + fr"{{1/2}}")
ld.equation("-("+ (ld.cos() + "^" + fr"{{2}}" + "(x)") + ")" + "^" + fr"{{1/2}}", "-" + ld.cos() + "(x)")
ld.line(" ", True)

ld.line("Now that we have simplified the derivative to a simple cos function, we can integrate it.", True)

ld.write_integral("-" + ld.cos() + '(x)', 'x', True)
ld.equation("", ld.sin() + "(x) + C" )

ld.equation(ld.sin() + "(2" + ld.greek('pi') + ') + C', "-1")
ld.equation("C", "-2")
ld.equation("So\ f(x)", ld.sin() + "(x) - 2")


ld.gahzamn()
ld.compile()