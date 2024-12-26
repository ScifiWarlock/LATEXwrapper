Welcome to PyTeX. This is a collection of easily implementable python methods that convert parameters into LaTeX for easier, more efficient scripting.

Below are the methods:

1. greek(): no params, accesses greek letters and formats in latex
   - Alpha, beta, gamma, delta, epsilon, zeta, eta, theta, lambda, mu, pi, nabla
  
2. cos() and sin(): Work in progress, not stable

3. give_infinity(): request an infinity in latex format; can add in a line, equation, or integral command

4. create(file_name): creates a tex file with passed name

5. clear(): add this to the code each time; clears the latex file and updates it each run

6. texcurl(): no params; internal function, not for pytex use

7. preamble(type, title, author): necessary for starting a latex file; place after create()

8. figure_index() and topic_index(): no params; images and sections/subsection table of contents respectively

9. ong_bruh(): no commands, used to begin the latex file

10. line(string, bool): string is line you want to enter (for functions in a line cmd then add a ;func(); delimiter in the string, no need for concatenation). bool true means it will be double spaced line after the cmd, false means single space

11. d_partial(x, y): partial derivative of x with respect to y

12. equation(left, right): formats on latex that left = right

13. math(string): latex math formatting for a string

14. image(time, capt): adds an image centered and top caption; enter the time the screenshot was taken, add a caption for it to be added to the figure list

15. example(string): subsubsection created

16. topic(string): subsection created

17. integral(func, var, lower, upoer): integral of function with respect to a variable; upper and lower bound parameters optional, assumed None if nothing is passed

18. sqrt(string): returns a square root formatting; can be used in a line cmd

19. gahzamn(): no params, required for ending the latex doc

20. compile(): no params, needed to launch subprocess cmd to populate latex file
