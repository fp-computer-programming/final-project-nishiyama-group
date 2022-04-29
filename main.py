# Author: ATN 5/17/22

import turtle

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

window = turtle.Screen()
window.setup(1024, 768)

button_1 = turtle.Turtle()
button_1.hideturtle()
button_1.shape('square')
button_1.fillcolor('blue')
button_1.penup()
button_1.goto(-256, 0)
button_1.write('Examen', align = 'center', font=FONT)
button_1.sety(0 + CURSOR_SIZE + FONT_SIZE)
# button_1.onclick(window.bgcolor('black'))
button_1.showturtle()


window.mainloop()
