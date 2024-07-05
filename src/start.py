# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: SageMath 10.1.rc0
#     language: sage
#     name: sagemath
# ---

# %% [markdown]
# # About SageMath
#
# [SageMath](https://www.sagemath.org) (Sage for short) is a general purpose computational mathematics system developed by a worldwide community of hundreds of researchers, teachers and engineers. It’s based on the Python programming language and includes GAP, PARI/GP, Singular, and dozens of other specialized libraries.
#
# This live document will guide you through the first steps of using Sage, and provide pointers to explore and learn further. In the following, we will be assuming that you are reading this document as a Jupyter notebook (Jupyter is the primary user interface
# for Sage).
# $\def\NN{\mathbb{N}}\def\ZZ{\mathbb{Z}}\def\QQ{\mathbb{Q}}\def\RR{\mathbb{R}}\def\CC{\mathbb{C}}$
# <a id='index-0'></a>

# %% [markdown]
# ## A first calculation
#
# Sage can be used as a pocket calculator: you type in some expression to be calculated, Sage evaluates it, and prints the result; and repeat. This is called the *Read-Eval-Print-Loop*. In the Jupyter notebook, you type the expression in an **input cell**, or **code cell**. This is the rectangle below this paragraph containing $1+1$. Click on the cell to select it, and press shift-enter to evaluate it. You may instead click the Run button (right triangle) in the toolbar.

# %%
1 + 1


# %% [markdown]
# Sage prints out its response in an **output cell** just below the input cell (that’s 2, so Sage confirms that 1 plus 1 is 2). Click again in the cell, replace $1+1$ by $2+2$, and evaluate it. Notice how much quicker it is now. That’s because a Sage process had to be started the first time, and then stayed ready.
#
# Congratulations, you have done your first calculations with Sage.

# %% [markdown]
# ## Using the Jupyter notebook
#
# Now take some time to explore the <kbd>Help</kbd> menu. You find abundant information on Jupyter, Sage, and friends. 
# For now we just review the basics of Jupyter notebook. Use the plus button in the toolbar to create a new input cell below this paragraph (you may need to first click this paragraph to focus), then calculate any simple expression of your liking.
#
# You can move around and edit any cell by clicking in it. Go back and change your $2+2$ above to $3+3$ and evaluate it once again.
#
# You can also edit any **text cell** by double clicking on it. Try it now! The text you see is using the [Markdown](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html) markup language. Do some changes to the text, and evaluate it again to rerender it. Markdown supports a fair amount of basic formatting, such as bold, underline, basic lists, and so forth. Thanks to the LaTeX rendering engine [MathJax](https://www.mathjax.org/), you may embed mathematical formulae such as $\sin x - y^3$ just like with LaTeX. It can be fun to type in fairly complicated math, like this:
#
# $$
#     \zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=\prod_p \left(\frac{1}{1-p^{-s}}\right)
# $$
#
# If you *mess everything up*, you can use the menu <kbd>Kernel</kbd> > <kbd>Restart Kernel</kbd> to restart Sage. You can also use the menu <kbd>File</kbd> > <kbd>Save Notebook</kbd> to save notebook, and <kbd>File</kbd> > <kbd>Revert Notebook to Checkpoint</kbd> to reset to any previously saved version.

# %% [markdown]
# ## More interactions
#
# We are now done with basic interaction with Sage. Much richer interactions are possible thanks to Jupyter’s *interactive widgets*. Evaluate the next code cell, and try clicking on the sliders to illustrate multiplication below. 

# %%
@interact
def f(n=(1..15), m=(1..15)):
    print("n * m = {} = {}".format(n * m, factor(n * m)))
    P = polygon([(0, 0), (0, n), (m, n), (m, 0)])
    P.show(aspect_ratio=1, gridlines='minor', figsize=[3, 3], xmax=14, ymax=14)


# %% [markdown]
# Also, you can try changing the slider ranges to something different by editing the input cell (make sure to also change `xmax`, `ymax`).

# %% [markdown]
# ## A brief tour
#
# We start showcasing the different areas of mathematics covered by Sage.
# <a id='index-1'></a>

# %% [markdown]
# This should output a rational number. If you know Python, notice the difference; Sage knows fractions!

# %%
4/6

# %% [markdown]
# ### Math display
#
# `%display latex` turns on math typesetting using MathJax. Type `%display plain` to turn it off.

# %%
# %display latex

# %%
factor(x^10 - 1)

# %%
# %display plain
factor(x^10 - 1)

# %% [markdown]
# ### Plots

# %%
plot(sin(10*x))


# %% [markdown]
# ### Interactive widgets

# %%
@interact
def plt(n=5, f=[sin, cos, tan]):
    return plot(f(n*x))


# %% [markdown]
# ### 3D plots

# %%
plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))

# %% [markdown]
# ### Calculus

# %%
# %display latex
var('x,y')
f = (cos(pi/4 - x) - tan(x)) / (1 - sin(pi/4 + x))
limit(f, x = pi/4, dir='minus')

# %%
solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y)

# %%
plot3d(sin(pi*sqrt(x^2 + y^2)) / sqrt(x^2 + y^2), (x, -5, 5), (y, -5, 5))

# %%
contour_plot(y^2 + 1 - x^3 - x, (x,-pi,pi), (y,-pi,pi),
             contours=[-8,-4,0,4,8], colorbar=True)

# %% [markdown]
# ### Algebra

# %%
factor(x^100 - 1)

# %%
p = 54 * x^4 + 36*x^3 - 102*x^2 - 72*x - 12
p.factor()

# %%
for K in [ZZ, QQ, ComplexField(16), QQ[sqrt(2)], GF(5)]:
    print(K, ":"); print(K['x'](p).factor())

# %%
ZZ.category()

# %%
sorted( ZZ.category().axioms() )

# %% [markdown]
# ### Linear algebra

# %%
A = matrix(GF(7), 4, [5,5,4,3,0,3,3,4,0,1,5,4,6,0,6,3]); A

# %%
P = A.characteristic_polynomial(); P

# %%
P(A)  # Cayley-Hamilton

# %%
A.eigenspaces_left()

# %% [markdown]
# Computing the rank of a large sparse matrix:

# %%
M = random_matrix(GF(7), 10000, sparse=True, density=3/10000)
M.rank()

# %% [markdown]
# ### Geometry

# %%
polytopes.truncated_icosidodecahedron().plot()

# %% [markdown]
# ### Programming and plotting

# %%
n, l, x, y = 10000, 1, 0, 0
p = [[0, 0]]
for k in range(n):
    theta = (2 * pi * random()).n(digits=5)
    x, y = x + l * cos(theta), y + l * sin(theta)
    p.append([x, y])
g = line(p, thickness=.4) + line([p[n], [0, 0]], color='red', thickness=2)
g.show(aspect_ratio=1)

# %% [markdown]
# ### Interactive plots

# %%
var('x')
@interact
def g(f='x*sin(1/x)',
      c=slider(-1, 1, .01, default=-.5),
      n=(1..30),
      xinterval=range_slider(-1, 1, .1, default=(-8,8), label="x-interval"),
      yinterval=range_slider(-1, 1, .1, default=(-3,3), label="y-interval")):
    f = eval(f)
    x0 = c
    degree = n
    xmin,xmax = xinterval
    ymin,ymax = yinterval
    p   = plot(f, xmin, xmax, thickness=4)
    dot = point((x0,f(x=x0)),pointsize=80,rgbcolor=(1,0,0))
    ft = f.taylor(x,x0,degree)
    pt = plot(ft, xmin, xmax, color='red', thickness=2, fill=f)
    show(dot + p + pt, ymin=ymin, ymax=ymax, xmin=xmin, xmax=xmax)
    html(r'$f(x)\;=\;%s$' % latex(f))
    html(r'$P_{%s}(x)\;=\;%s+R_{%s}(x)$' % (degree,latex(ft),degree))


# %% [markdown]
# ### Graph Theory
#
# Coloring graphs:

# %%
g = graphs.PetersenGraph(); g
g.plot(partition=g.coloring())

# %% [markdown]
# ### Combinatorics
#
# Fast counting:

# %%
Partitions(100000).cardinality()

# %% [markdown]
# Playing poker:

# %%
Suits   = Set(["Hearts", "Diamonds", "Spades", "Clubs"])
Values  = Set([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])
Cards   = cartesian_product([Values, Suits])
Hands   = Subsets(Cards, 5)
Hands.random_element()

# %%
Hands.cardinality()

# %% [markdown]
# ### Algebraic Combinatorics
#
# Drawing an affine root systems:

# %%
L = RootSystem(["G", 2, 1]).ambient_space()
p = L.plot(affine=False, level=1)
p.show(aspect_ratio=[1, 1, 2], frame=False)

# %% [markdown]
# ### Number Theory

# %%
E = EllipticCurve('389a')
plot(E, thickness=3)

# %% [markdown]
# ### Games
#
# Sudoku solver:

# %%
S = Sudoku('5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3'); S

# %%
list(S.solve())

# %% [markdown]
# ## Help system
#
# We review the three main ways to get help in Sage:
#
# - Navigating through the documentation  
# - Tab-completion 
# - Contextual help 

# %% [markdown]
# ### Navigating through the documentation
#
# The <kbd>Help</kbd> menu gives access to the HTML documentation for Sage (and other pieces of software). This includes the Sage tutorial, the Sage thematic tutorials, and the Sage reference manual. 
#
# This documentation is also available online from Sage’s web site
# [https://doc.sagemath.org](https://doc.sagemath.org/html/en/index.html) .

# %% [markdown]
# ### Completion and contextual documentation
#
# Start typing something and press the Tab key. The interface tries to complete it with a command name. If there is more than one completion, then they are all presented to you. Remember that Sage is case sensitive, i.e., it differentiates upper case from lower case. Hence the Tab completion of
# `klein` won’t show you the `KleinFourGroup` command that builds the group $ \ZZ/2 \times \ZZ/2 $ as a permutation group. Try pressing the <kbd>Tab</kbd> key in the following cells (with cursor at the end):

# %%
klein

# %%
Klein

# %% [markdown]
# To see documentation and examples for a command, type a question mark `?` at the end of the command name and evaluate the cell.
#

# %%
KleinFourGroup?

# %% [markdown]
# #### Exercise A
#
# What is the largest prime factor of $600851475143$?

# %%
factor?

# %%

# %% [markdown]
# ### Digression: assignments and methods
#
# In the above manipulations we did not store any data for later use. This can be done in Sage with the assignment symbol as in:

# %%
a = 3
b = 2
a + b

# %% [markdown]
# This can be understood as Sage evaluating the expression to the right of the = sign and creating the appropriate object, and then associating that object with a label, given by the left-hand side. Multiple assignments can be done at once:

# %%
a, b = 2, 3
a

# %%
b

# %% [markdown]
# This allows us to swap the values of two variables directly:

# %%
a, b = 2, 3
a, b = b, a
a, b

# %% [markdown]
# We can also assign a common value to several variables simultaneously:

# %%
c = d = 1
c, d

# %%
d = 2
c, d

# %% [markdown]
# Note that when we use the word *variable* in the computer-science sense we
# mean “a label attached to some data stored by Sage”. Once an object is
# created, some *methods* apply to it. This means *functions* but instead of
# writing `f(my_object)` you write `my_object.f()`:

# %%
p = 17
p.is_prime()

# %% [markdown]
# See [Tutorial: Objects and Classes in Python and Sage](http://doc.sagemath.org/html/en/thematic_tutorials/tutorial-objects-and-classes.html#tutorial-objects-and-classes) for details.

# %% [markdown]
# ### Method discovery with tab-completion
#
# <a id='index-2'></a>

# %% [markdown]
# To know all methods of an object you can once more use <kbd>Tab</kbd>-completion. Write the name of the object followed by a dot and then press <kbd>Tab</kbd>:

# %%
a.

# %% [markdown]
# #### Exercise B
#
# Create the permutation 51324 and assign it to the variable p.

# %%
Permutation?

# %%

# %% [markdown]
# What is the inverse of p?

# %%
p.inv

# %% [markdown]
# Does $p$ have the pattern 123? What about 1234? And 312? (even if you don’t
# know what a pattern is, you should be able to find a command that does this).

# %%
p.pat

# %% [markdown]
# ### Linear algebra

# %% [markdown]
# #### Exercise C
#
# Use the matrix() command to create the following matrix.
#
# $$
# M = \left(\begin{array}{rrrr}
# 10 & 4 & 1 & 1 \\
# 4 & 6 & 5 & 1 \\
# 1 & 5 & 6 & 4 \\
# 1 & 1 & 4 & 10
# \end{array}\right)
# $$

# %%
matrix?

# %%

# %% [markdown]
# Then, using methods of the matrix,
#
# 1. Compute the determinant of the matrix.  
# 1. Compute the echelon form of the matrix.  
# 1. Compute the eigenvalues of the matrix.  
# 1. Compute the kernel of the matrix.  
# 1. Compute the LLL decomposition of the matrix (and lookup the
#    documentation for what LLL is if needed!)  

# %%

# %% [markdown]
# Now that you know how to access the different methods of matrices,
#
# 1. Create the vector $ v = (1, -1, -1, 1) $.  
# 1. Compute the two products: $ M \cdot v $ and $ v \cdot M $. What mathematical operation is Sage doing implicitly?  

# %%
vector?

# %%

# %% [markdown]
# Vectors in Sage can be used as row vectors or column vectors. A method such as eigenspaces might not
# return what you expect, so it is best to specify `eigenspaces_left` or `eigenspaces_right` instead. Same thing for kernel (`left_kernel` or `right_kernel`), and so on.

# %% [markdown]
# ### Plotting
#
# The `plot()` command allows you to draw plots of functions. Recall
# that you can access the documentation by pressing the <kbd>Tab</kbd> key
# after writing `plot?` in a cell:

# %%
plot?

# %% [markdown]
# Here is a simple example:

# %%
var('x')  # make sure x is a symbolic variable

# %%
plot(sin(x^2), (x, 0, 10))

# %% [markdown]
# Here is a more complicated plot. Try to change every single input to the plot
# command in some way, evaluating to see what happens:

# %%
P = plot(sin(x^2), (x, -2, 2), rgbcolor=(0.8, 0, 0.2), thickness=3, linestyle='--', fill='axis')
show(P, gridlines=True)

# %% [markdown]
# Above we used the `show(P)` command to show a plot after it was created. You can
# also use `P.show()` instead:

# %%
P.show(gridlines=True)

# %% [markdown]
# Try putting the cursor right after `P.show(` and pressing <kbd>Tab</kbd> key to get a list of
# the options for how you can change the values of the given inputs.

# %%
P.show(

# %% [markdown]
# Plotting multiple functions at once is as easy as adding the plots together:

# %%
P1 = plot(sin(x), (x, 0, 2*pi))
P2 = plot(cos(x), (x, 0, 2*pi), rgbcolor='red')
P1 + P2

# %% [markdown]
# ### Symbolic Expressions
#
# Here is an example of a symbolic function:

# %%
f(x) = x^4 - 8*x^2 - 3*x + 2
f(x)

# %%
f(-3)

# %% [markdown]
# This is an example of a function in the *mathematical* variable $ x $. When Sage
# starts, it defines the symbol $ x $ to be a mathematical variable. If you want
# to use other symbols for variables, you must define them first:

# %%
x^2

# %%
u + v

# %%
var('u v')

# %%
u + v

# %% [markdown]
# Still, it is possible to define symbolic functions without first
# defining their variables:

# %%
f(w) = w^2
f(3)

# %% [markdown]
# In this case those variables are defined implicitly:

# %%
w

# %% [markdown]
# #### Exercise D
#
# Define the symbolic function $ f(x) = x \sin x^2 $. Plot $ f $ on the
# domain $ [-3, 3] $ and color it red. Use the `find_root()` method to
# numerically approximate the root of $ f $ on the interval $ [1, 2] $:

# %%

# %% [markdown]
# Compute the tangent line to $ f $ at $ x = 1 $:

# %%

# %% [markdown]
# Plot $ f $ and the tangent line to $ f $ at $ x = 1 $ in one image:

# %%

# %% [markdown]
# #### Exercise E (Advanced)
#
# Solve the following equation for $y$
#
# $$
# y = 1 + x y^2
# $$
#
# There are two solutions, take the one for which $ \lim_{x\to0} y(x) = 1 $.
# (Don’t forget to create the variables $ x $ and $ y $!).

# %%

# %% [markdown]
# Expand $ y $ as a truncated Taylor series around $ 0 $ containing
# $ n = 10 $ terms.

# %%

# %% [markdown]
# Do you recognize the coefficients of the Taylor series expansion? You might want to use the [On-Line Encyclopedia of Integer Sequences](https://oeis.org/), or better yet, Sage’s class OEIS which queries the encyclopedia:

# %%
oeis?

# %%

# %% [markdown]
# Congratulations for completing your first Sage tutorial!

# %% [markdown]
# ## Exploring further

# %% [markdown]
# ### Accessing Sage
#
# - The [Sage cell service](https://sagecell.sagemath.org) lets you evaluate individual Sage commands.  
# - In general, Sage computations can be embedded in any web page using [Thebe](https://thebe.readthedocs.io/en/stable).
# - [Binder](https://mybinder.org) is a service that lets you run Jupyter online on top of an arbitrary software stack. 
#   Sessions are free, anonymous, and temporary. You can use one of the existing repositories, or create your own.  
#
# <a id='index-3'></a>

# %% [markdown]
# ### Ways to use Sage
#
# There are other ways beyond the Jupyter Notebook to use Sage: interactive command line, program scripts, etc.
# See [Sage tutorial](https://doc.sagemath.org/html/en/tutorial/introduction.html#ways-to-use-sage).

# %% [markdown]
# ### Resources
#
# - [Sage tutorial](https://doc.sagemath.org/html/en/tutorial/index.html)  
# - [Sage thematic tutorials](https://doc.sagemath.org/html/en/thematic_tutorials/index.html)  
# - [The open book *Computational Mathematics with Sage*](https://www.sagemath.org/sagebook/english.html)
# - [Sage quick reference cards](https://wiki.sagemath.org/quickref)  
# - [Sage webpage https://www.sagemath.org](https://www.sagemath.org)  
# - [Ask Sage https://ask.sagemath.org](https://ask.sagemath.org)  
# - [Sage GitHub repo](https://github.com/sagemath/sage/issues)
