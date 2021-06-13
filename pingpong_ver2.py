from tkinter import *
import time


root=Tk()
WIDTH=400
HEIGHT=700
PAD_WIDTH=150
PAD_HEIGHT=10
PAD_X1=200
PAD_Y1=600

ball_x=WIDTH / 2
ball_y=HEIGHT / 2
PAD_X2=200
PAD_Y2=100

ball_x1=ball_x-10
ball_y1=ball_y-10
ball_x2=ball_x+10
ball_y2=ball_y+10
x1=0
x2=0

c=Canvas(width=WIDTH,
         height=HEIGHT,
         bg='red')
c.pack()







def fx_1(s):
    global x1
    if s =='+':
        x1=5
    else:
        x1=-5


def fx_2(s):
    global x2
    if s=='+':
        x2=5
    else:
        x2=-5


def drawing():
 c.delete('all')
pad = c.create_rectangle(PAD_X1 - PAD_WIDTH / 2,
                          PAD_Y1 - PAD_HEIGHT / 2,
                          PAD_X1 + PAD_WIDTH / 2,
                          PAD_Y1 + PAD_HEIGHT / 2,
                          fill='black')

pad2=c.create_rectangle(PAD_X2-PAD_WIDTH/2,
                                   PAD_Y2-PAD_HEIGHT/2,
                                   PAD_X2+PAD_WIDTH/2,
                                   PAD_Y2+PAD_HEIGHT/2,
                                   fill='black')

ball=c.create_oval(ball_x1,ball_y1,
                   ball_x2,ball_y2,
                   fill='cyan')




root.bind("<Left>",lambda e :fx_1('-'))
root.bind("<Right>",lambda e :fx_1('+'))
root.bind("<A>",lambda e :fx_2('-'))
root.bind("<D>",lambda e :fx_2('+'))


ball_x_speed=2
ball_y_speed=1

while True:


     c.move(ball,ball_x_speed,
            ball_y_speed)
     c.move(pad,x1,0)
     c.move(pad2, x2, 0)
     if ball_x2>=WIDTH:
         ball_x_speed=-ball_x_speed


     root.update()
     time.sleep(0.1)


