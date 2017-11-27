"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Wesley Turner.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
window = rg.TurtleWindow()
julia = rg.SimpleTurtle()
julia.pen = rg.Pen('black', 20)
julia.speed = 5
maria = rg.SimpleTurtle("turtle")
maria.pen = rg.Pen('green', 35)
maria.speed = 5
julia.right(30)
for i in range(5):
    julia.forward(250)
    julia.right(150)
    julia.forward(250)
maria.pen_up()
maria.left(90)
maria.forward(150)
maria.right(50)
maria.forward(50)
maria.pen_down()
for i in range(12):
    maria.forward(40)
    maria.left(30)

window.close_on_mouse_click()