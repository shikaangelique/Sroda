# interactive real time color change with auto mandale drawing

import turtle

# screen setup
ninja_screen = turtle.Screen()
ninja_window_height = int(ninja_screen.window_height())
ninja_window_width = int(1.5 * ninja_window_height)
ninja_screen_radius = ninja_window_height / 2
ninja_screen.setup(ninja_window_width, ninja_window_height)
# ninja_screen.tracer(0)

# global variables,default conditions
ninja_previous_state = None
ninja_color = 'black'
# ninja_color_one = True
ninja_color_two = 'black'
ninja_color_three = 'black'
change_color_one = False
change_color_two = False
change_color_three = False
ninja_colors = ["black", "dark turquoise", "aquamarine", "medium sea green", "dark grey", "cornflower blue",
                "deep sky blue", "khaki", "sienna", "firebrick", "coral", "red", "crimson", "hot pink", "dark orchid",
                "medium slate blue"]


# screen borders
def draw_border():
    border = turtle.Turtle()
    border.color('grey')
    border.speed(0)
    border.penup()
    border.goto(-ninja_window_width / 2 + 25, ninja_window_height / 2 - 25)
    border.pendown()
    border.forward(ninja_window_width - 50)
    border.right(90)
    border.forward(ninja_window_height - 50)
    border.right(90)
    border.forward(ninja_window_width - 50)
    border.right(90)
    border.forward(ninja_window_height - 50)
    border.penup()
    border.goto(-ninja_window_width / 2 + 305, ninja_window_height / 2 - 25)
    border.pendown()
    border.right(180)
    border.forward(ninja_window_height - 50)
    border.hideturtle()


class ColorButtons(turtle.Turtle):
    def __init__(self, x, y, color, click_callback=None):
        turtle.Turtle.__init__(self)
        # self.screen = ninja_screen
        self.shape('circle')
        self.speed(0)
        self.my_color = color
        self.click_callback = click_callback
        self.color(color)
        self.pu()
        self.goto(x, y)
        self.left(90)
        self.onclick(self.onclick_handler)

    def onclick_handler(self, x, y):
        if self.click_callback:
            self.click_callback(self, self.my_color)
        self.shape('turtle')


class ColorOneChangeSelect(turtle.Turtle):
    def __init__(self, x, y, name, click_callback=None):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape('circle')
        self.color('black')
        self.penup()
        self.left(90)
        self.name = name
        self.click_callback = click_callback
        self.onclick(self.onclick_handler)
        color_change_labels(x, y, self.name)

    def onclick_handler(self, x, y):
        global change_color_one
        if self.click_callback:
            # self.click_callback(self, self.color)
            change_color_one = True
            self.shape('turtle')


class ColorTwoChangeSelect(turtle.Turtle):
    def __init__(self, x, y, name, click_callback=None):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape('circle')
        self.color('black')
        self.penup()
        self.left(90)
        self.name = name
        self.click_callback = click_callback
        self.onclick(self.onclick_handler)
        color_change_labels(x, y, self.name)

    def onclick_handler(self, x, y):
        global change_color_two
        if self.click_callback:
            # self.click_callback(self, self.color)
            change_color_two = True
            self.shape('turtle')


class ColorThreeChangeSelect(turtle.Turtle):
    def __init__(self, x, y, name, click_callback=None):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape('circle')
        self.color('black')
        self.penup()
        self.left(90)
        self.name = name
        self.click_callback = click_callback
        self.onclick(self.onclick_handler)
        color_change_labels(x, y, self.name)

    def onclick_handler(self, x, y):
        global change_color_three
        if self.click_callback:
            # self.click_callback(self, self.color)
            change_color_three = True
            self.shape('turtle')


def color_change_labels(x, y, name):
    label = turtle.Turtle()
    label.penup()
    label.goto(x + 20, y - 7)
    label.write(name, font=("Arial", 12, "normal"), move=False)
    label.hideturtle()


def handle_color_click(ct, color):
    global ninja_color
    global ninja_color_two
    global ninja_color_three
    global ninja_previous_state
    ninja_previous_state.shape('circle')
    # ninja_previous_state.update()
    if change_color_one is True:
        ninja_color = color

    if change_color_two is True:
        ninja_color_two = color

    if change_color_two is True:
        ninja_color_three = color

    ninja_previous_state = ct
    return color


def handle_save(x, y):
    print('changes saved')
    setup_screen_turtle()


def setup_button(x, y, name, color, shape, handler):
    set_button = turtle.Turtle()
    set_button.speed(0)
    set_button.shape(shape)
    set_button.color(color)
    set_button.penup()
    set_button.goto(x + 18, y - 8)
    set_button.write(name, font=("Arial", 12, "normal"))
    set_button.goto(x, y)
    set_button.onclick(handler)
    set_button.showturtle()


def handle_restart(x, y):
    ninja_screen.clear()
    ninja_screen.reset()
    draw_border()
    create_ui()
    # setup_screen_turtle()
    ninja_screen.mainloop()


def create_ui():
    global ninja_previous_state
    x = -ninja_window_width / 2 + 50
    y = ninja_window_height / 2 - 50

    ci = 0
    for r in range(2):
        cx = x
        cy = y - (150 + (30 * r))
        for c in range(8):
            color = ninja_colors[ci]
            cb = ColorButtons(cx + (c * 25), cy, color, handle_color_click)
            if ci == 0:
                cb.shape('turtle')
                ninja_previous_state = cb
            ci += 1
    setup_button(x, y - 300, 'Draw', 'green', 'circle', handle_save)
    setup_button(x, y - 350, 'Restart', 'red', 'triangle', handle_restart)

    ColorOneChangeSelect(x, y - 40, 'Color One', 'black')
    ColorTwoChangeSelect(x + 150, y - 40, 'Color Two', 'black')
    ColorThreeChangeSelect(x + 75, y - 70, 'Color Three', 'black')


def setup_screen_turtle():
    mandala_main = turtle.Turtle()
    mandala_main.penup()
    mandala_main.goto(40, -30)
    mandala_main.speed(0)
    mandala_main.pendown()
    mandala_main.hideturtle()
    for times in range(36):
        mandala_main.color(ninja_color)
        mandala_main.speed(0)
        mandala_main.circle(100)
        mandala_main.color(ninja_color_two)
        mandala_main.forward(200)
        mandala_main.left(120)
        mandala_main.color(ninja_color_three)
        mandala_main.forward(100)
        mandala_main.right(120)
        mandala_main.left(170)
        mandala_main.left(20)
        mandala_main.forward(15)


if __name__ == '__main__':
    draw_border()
    create_ui()
    # setup_screen_turtle()
    ninja_screen.mainloop()
