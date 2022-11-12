# Import the functions from the Draw 2-D library
# so that they can be used in this program.
# from curses.panel import top_panel
from ctypes import sizeof
from tkinter import Canvas
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_ground(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 200, 300, 200)
    draw_pine_tree(canvas, 650, 100, 200)
    draw_lake(canvas, 60, 60, 450, 260)
    text(canvas, 250, 150)
    draw_sun(canvas, 600, 350, 700, 450)
    draw_clouds(canvas, 100, 350, 150, 400)
    draw_clouds(canvas, 50, 400, 100, 450)
    draw_clouds(canvas, 250, 450, 300, 500)
    draw_clouds(canvas, 70, 370, 120, 430)
    draw_clouds(canvas, 650, 350, 700, 400)
    draw_clouds(canvas, 560, 420, 600, 450)
    draw_clouds(canvas, 360, 360, 420, 400)
    draw_clouds(canvas, 400, 370, 460, 420)
    # draw_grid(canvas, scene_width, scene_height, 50)
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval):
    label_y=15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    
    label_x =15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 1.5, width=0, fill="goldenrod4")

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 1.5, scene_width, scene_height, width=0, fill="deepSkyBlue")

def draw_clouds(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="white", outline="white")
        
def draw_sun(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=1, fill="goldenrod1", outline="goldenrod1")

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width= height /  10
    trunk_height= height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

    skirt_width = height/2
    skirt_left=  center_x - skirt_width /2 
    skirt_bottom= trunk_top
    peak_x= center_x
    peak_y= bottom + height
    skirt_right= center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, trunk_top, fill="forestGreen")

def draw_lake(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="steelBlue3", outline="steelBlue3")

def text(canvas,center_x, center_y):
    draw_text(canvas, center_x, center_y, "Get Outside More!", fill="black",)
# Define your functions such as
# draw_sky and draw_ground here.


# Call the main function so that
# this program will start executing.
main()