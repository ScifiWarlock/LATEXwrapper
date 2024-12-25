import LATEXdefintions as ld

ld.create("test1")
ld.clear()
ld.preamble("article", "testing with python", "Omkar Tasgaonkar")

ld.ong_bruh()

ld.topic_index()
ld.figure_index()

ld.line("Hello whats up, ;math('welcome');", True)
ld.line("This is after a double space, now a single space", False)
ld.image(14.06, "This is a test image")
ld.line("", False)
ld.line("As you can see we have inserted a screeenshot above for the eigenvector ;math('v');", True)

#slide one
ld.line("", False)
ld.topic("Eigenvalues and eigenvectors")
ld.line("An eigenvalue is a scalar for the vector that maintains its direction after a transform, an eignevector", False)
ld.example("13.5: Find the eigenvector of the matrix M")

ld.line(ld.integral('exp(-x^2)', 'x') + " is equal to ;math(sqrt(greek('pi')));", False)

ld.gahzamn()

ld.compile()