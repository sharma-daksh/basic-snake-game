from turtle import Turtle


STARTING_POSI=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.body_parts=[]
        self.create_snake()
        self.head=self.body_parts[0]

    def create_snake(self):
        for posi in STARTING_POSI:
            self.add_part(posi)

    def add_part(self,posi):
        new_part=Turtle("square")
        new_part.color("black")
        new_part.penup()
        new_part.goto(posi)
        self.body_parts.append(new_part)

    def extend(self):
        self.add_part(self.body_parts[-1].position())
    
    def move(self):
        for body_num in range(len(self.body_parts)-1,0,-1):
            new_x=self.body_parts[body_num-1].xcor()
            new_y=self.body_parts[body_num-1].ycor()
            self.body_parts[body_num].goto(new_x,new_y)
        self.body_parts[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
